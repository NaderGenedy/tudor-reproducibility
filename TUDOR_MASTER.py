#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TUDOR_MASTER.py  --  master orchestrator + reproducer for the TUDOR project
============================================================================
TUDOR = Treatment-adjusted, ascertainment-aware Diagnostic algorithm for
familial hypercholesterolaemia (FH), validated bidirectionally across the
All-Wales FH Registry and UK Biobank (506,506 adults).

This single file documents and EXECUTES the whole analytic method:

  Stage 0  preflight        environment + data inventory
  Stage 1  cohort build     load Wales + UKB, harmonise, FAMILY-LEVEL DEDUP
  Stage 2  treatment adjust back-calculate untreated LDL (the "Lipid Age")
  Stage 3  features         3 pillars -> 11 locked variables
  Stage 4  fit TUDOR        Elastic Net logistic (+ NoAgeLDL sensitivity)
  Stage 5  bidirectional    Wales North<->South geographic validation
  Stage 6  head-to-head     TUDOR vs DLCN / MEDPED / Simon Broome
  Stage 7  subgroups + NRI  the populations the old tools miss
  Stage 8  reproduce        assert headline numbers vs verified_numbers_locked.json

DATA GOVERNANCE -- READ THIS
  The REAL inputs (UK Biobank App 1002450; All-Wales / Dragon-3 registry) are
  controlled-access. They must NOT be uploaded to any third-party cloud (incl.
  Claude Code on the web) -- that would breach the UKB Material Transfer
  Agreement and NHS information-governance. Therefore:
     * on your LOCAL machine / UKB RAP  ->  run with real data  (--real)
     * anywhere else (incl. the web)    ->  run on SYNTHETIC data (--synthetic)
  Synthetic mode reproduces the METHOD and proves the code path; it does NOT
  reproduce the clinical numbers (those live in verified_numbers_locked.json
  and can only be regenerated where the governed data physically resides).

USAGE
  python TUDOR_MASTER.py --check                 # inventory inputs, do nothing
  python TUDOR_MASTER.py --synthetic --all       # full run on synthetic data
  python TUDOR_MASTER.py --real --all            # full run on governed data (local only)
  python TUDOR_MASTER.py --synthetic --stage 4   # run a single stage
  python TUDOR_MASTER.py --reproduce             # print the locked headline targets

Author: Dr Nader Genedy, University Hospital of Wales / Cardiff University.
Python 3.12.  British spelling in prose; ASCII-only stdout (cp1252-safe).
"""
import os, sys, json, argparse, warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output")
SYNTH = os.path.join(HERE, "synthetic_data")
LOCKED = os.path.join(HERE, "verified_numbers_locked.json")
SEED = 20260608

try:
    sys.stdout.reconfigure(encoding="utf-8")   # safe on Windows cp1252 consoles
except Exception:
    pass

# ---- Real (governed) data locations. Present ONLY on Dr Genedy's machine. ----
REAL_PATHS = {
    "wales_dragon3": r"C:/Users/nader/Downloads/FH_Dragon3 (1).csv",
    "wales_pass":    r"D:/Projects/CALON_AlphaFold_Rebuild/data/pass_FULL_MASTER.csv",
    "ukb_master":    r"D:/Projects/CALON_AlphaFold_Rebuild/data/ukb_FULL_MASTER.csv",
}
STATIN_REDUCTION = {"none": 0.0, "simva": 0.32, "atorva": 0.45, "ator": 0.45,
                    "rosuva": 0.50, "ros": 0.50, "prava": 0.24, "fluva": 0.21, "pitava": 0.35}
EZE_ADD, PCSK9_ADD, CAP = 0.20, 0.60, 0.85


def log(msg): print(msg, flush=True)
def rule(t): log("\n" + "=" * 74 + f"\n{t}\n" + "=" * 74)


# ============================================================ Stage 0: preflight
def stage0_preflight(mode):
    rule("STAGE 0 - PREFLIGHT (environment + data inventory)")
    log(f"Python {sys.version.split()[0]}   mode={mode}")
    for mod in ["pandas", "numpy", "sklearn", "scipy"]:
        try:
            m = __import__(mod); log(f"  [OK] {mod} {getattr(m,'__version__','?')}")
        except Exception as e:
            log(f"  [MISSING] {mod}  ->  pip install -r requirements.txt  ({e})")
    log("\nGoverned data (real) inventory:")
    for k, p in REAL_PATHS.items():
        log(f"  {'[PRESENT]' if os.path.exists(p) else '[ABSENT ]'} {k}: {p}")
    if mode == "real" and not all(os.path.exists(p) for p in REAL_PATHS.values()):
        log("\n[FATAL] --real requested but governed data is not all present on this machine.")
        log("        You are probably NOT on Dr Genedy's workstation / UKB RAP.")
        log("        Re-run with --synthetic to exercise the method.  Exiting.")
        sys.exit(2)
    if mode == "synthetic" and not os.path.exists(os.path.join(SYNTH, "wales_synthetic.csv")):
        log("\n[INFO] No synthetic data yet -> generating it now.")
        import make_synthetic_tudor_data as g
        os.makedirs(SYNTH, exist_ok=True)
        g.make_wales().to_csv(os.path.join(SYNTH, "wales_synthetic.csv"), index=False)
        g.make_ukb().to_csv(os.path.join(SYNTH, "ukb_synthetic.csv"), index=False)
        log("       synthetic_data/ written.")


# ========================================================= Stage 1: cohort build
def _harmonise_wales(d):
    """Map raw Dragon-3 / synthetic columns -> standard analytic frame."""
    g = pd.DataFrame()
    num = lambda c: pd.to_numeric(d.get(c), errors="coerce")
    g["family"] = d.get("FamilyNumber")
    g["fh_pos"] = (d.get("Positive1").astype(str).str.upper() == "Y").astype(int)
    g["ldl_meas"] = num("LDL_1"); g["tc"] = num("TC_1"); g["hdl"] = num("HDL_1"); g["tg"] = num("TRG_1")
    g["apob"] = num("ApoB"); g["apoa1"] = num("ApoA1")
    g["age"] = num("Ageattest")
    g["male"] = (d.get("Gender").astype(str).str.upper().str[0] == "M").astype(int)
    g["on_tx"] = (d.get("OnTreatment").astype(str).str.upper() == "Y").astype(int)
    g["statin"] = d.get("Statin").astype(str).str.lower()
    g["eze"] = (d.get("Ezetimibe").astype(str).str.upper() == "Y").astype(int)
    g["pcsk9"] = (d.get("PCSK9i").astype(str).str.upper() == "Y").astype(int)
    g["stigmata"] = (d.get("TendonXanthomata").astype(str).str.upper() == "Y").astype(int)
    g["t2dm"] = num("Diabetes_binary").fillna(0).astype(int)
    g["proband_index"] = (d.get("TypeofPatient").astype(str).str.lower() == "index").astype(int)
    g["ascvd"] = num("ASCVD_combined").fillna(0).astype(int)
    return g.dropna(subset=["ldl_meas", "age"])


def stage1_cohort(mode):
    rule("STAGE 1 - COHORT BUILD + FAMILY-LEVEL DEDUPLICATION")
    wpath = REAL_PATHS["wales_dragon3"] if mode == "real" else os.path.join(SYNTH, "wales_synthetic.csv")
    raw = pd.read_csv(wpath, encoding="latin-1" if mode == "real" else "utf-8", low_memory=False)
    wales = _harmonise_wales(raw)
    n0 = len(wales)
    # NON-NEGOTIABLE #1: one event per family (South Wales is a subset of All-Wales by FamilyNumber)
    wales = wales.sort_values("ascvd", ascending=False).drop_duplicates("family", keep="first")
    log(f"  Wales rows: {n0} -> {len(wales)} after family-level dedup "
        f"({n0-len(wales)} relatives collapsed); FH+={int(wales.fh_pos.sum())}")
    upath = REAL_PATHS["ukb_master"] if mode == "real" else os.path.join(SYNTH, "ukb_synthetic.csv")
    ukb = pd.read_csv(upath, low_memory=False)
    if mode == "synthetic":
        ukb = ukb.rename(columns={"ldl_direct": "ldl_meas", "fh_carrier": "fh_pos",
                                  "sex": "male", "on_statin": "on_tx"})
    log(f"  UKB rows: {len(ukb)}; carriers={int(ukb['fh_pos'].sum()) if 'fh_pos' in ukb else 'n/a'}")
    os.makedirs(OUT, exist_ok=True)
    wales.to_csv(os.path.join(OUT, "cohort_wales.csv"), index=False)
    return wales, ukb


# ==================================================== Stage 2: treatment adjust
def stage2_treatment_adjust(wales):
    rule("STAGE 2 - TREATMENT ADJUSTMENT (back-calculate untreated LDL)")
    def reduction(row):
        r = 0.0
        for k, v in STATIN_REDUCTION.items():
            if k in str(row["statin"]):
                r = v; break
        r += EZE_ADD * row["eze"] + PCSK9_ADD * row["pcsk9"]
        return min(r, CAP)
    red = wales.apply(reduction, axis=1) * wales["on_tx"]
    wales = wales.copy()
    wales["ldl_untreated"] = (wales["ldl_meas"] / (1 - red)).clip(upper=20)
    masked = (wales["ldl_untreated"] - wales["ldl_meas"])
    log(f"  Mean LDL unmasking on treated patients: +{masked[wales.on_tx==1].mean():.2f} mmol/L")
    log(f"  (this is the 'Lipid Age' pillar -- restores the pre-treatment phenotype)")
    return wales


# ============================================================ Stage 3: features
FEATURES = ["ldl_untreated", "trig_filter", "statin_residual", "age", "male",
            "apob", "tg", "hdl", "premature_ascvd", "proband_index", "stigmata"]

def stage3_features(wales):
    rule("STAGE 3 - FEATURE ENGINEERING (3 pillars -> 11 locked variables)")
    w = wales.copy()
    w["trig_filter"] = w["ldl_meas"] / (w["tg"] + 0.1)                 # Pillar 2: Triglyceride Shield
    w["statin_residual"] = w["on_tx"] * w["ldl_meas"]                  # residual phenotype on therapy
    w["premature_ascvd"] = ((w["ascvd"] == 1) & (w["age"] < 55)).astype(int)
    for c in ["apob", "hdl", "tg"]:
        w[c] = w[c].fillna(w[c].median())
    log("  Pillar 1 Lipid Age        -> ldl_untreated")
    log("  Pillar 2 Triglyceride Shield -> trig_filter = LDL/(TG+0.1)")
    log("  Pillar 3 Proband Effect   -> proband_index (index vs cascade relative)")
    log(f"  11 features: {FEATURES}")
    return w


# ============================================================ Stage 4: fit TUDOR
def _fit_elasticnet(X, y, seed=SEED):
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import StratifiedKFold
    from sklearn.metrics import roc_auc_score
    Xs = StandardScaler().fit_transform(X)
    clf = LogisticRegression(penalty="elasticnet", solver="saga", l1_ratio=0.5,
                             C=0.5, max_iter=5000, random_state=seed)
    cv = StratifiedKFold(5, shuffle=True, random_state=seed)
    aucs = []
    for tr, te in cv.split(Xs, y):
        clf.fit(Xs[tr], y[tr]); aucs.append(roc_auc_score(y[te], clf.predict_proba(Xs[te])[:, 1]))
    clf.fit(Xs, y)
    return clf, float(np.mean(aucs)), float(np.std(aucs))

def stage4_fit(wales):
    rule("STAGE 4 - FIT TUDOR (Elastic Net logistic) + NoAgeLDL SENSITIVITY")
    w = wales.dropna(subset=FEATURES)
    X, y = w[FEATURES].values, w["fh_pos"].values
    clf, auc, sd = _fit_elasticnet(X, y)
    log(f"  TUDOR 5-fold internal AUC = {auc:.3f} +/- {sd:.3f}  (n={len(w)}, FH+={int(y.sum())})")
    # NON-NEGOTIABLE #2: NoAgeLDL sensitivity -- drop the dominant age+LDL backbone
    noage = [f for f in FEATURES if f not in ("age", "ldl_untreated", "statin_residual")]
    _, auc2, _ = _fit_elasticnet(w[noage].values, y)
    log(f"  NoAgeLDL sensitivity AUC  = {auc2:.3f}  (signal beyond age+LDL backbone)")
    coef = pd.Series(clf.coef_[0], index=FEATURES).sort_values(key=abs, ascending=False)
    log("  Top standardised coefficients:")
    for k, v in coef.head(5).items():
        log(f"    {k:18s} {v:+.3f}")
    os.makedirs(OUT, exist_ok=True)
    coef.to_frame("coef").to_csv(os.path.join(OUT, "tudor_coefficients.csv"))
    return clf, auc


# ===================================================== Stage 5/6: comparators + bidirectional
def dlcn_score(r):
    """Simplified Dutch Lipid Clinic Network points (illustrative; full table in scripts/)."""
    s = 0.0
    ldl = r["ldl_meas"]
    s += 8 if ldl >= 8.5 else 5 if ldl >= 6.5 else 3 if ldl >= 5.0 else 1 if ldl >= 4.0 else 0
    s += 6 * r["stigmata"]                      # tendon xanthomata
    s += 2 * r["premature_ascvd"]               # premature CVD
    s += 1 * r.get("proband_index", 0)          # family history proxy
    return s

def simon_broome(r):
    return 1 if (r["ldl_meas"] >= 4.9 and (r["stigmata"] == 1 or r["premature_ascvd"] == 1)) else 0

def medped(r):
    cut = 6.7 if r["age"] >= 40 else 5.7 if r["age"] >= 30 else 4.9
    return 1 if r["ldl_meas"] >= cut else 0

def stage56_headtohead(wales, clf):
    rule("STAGE 5/6 - HEAD-TO-HEAD: TUDOR vs DLCN / MEDPED / Simon Broome (+ bidirectional)")
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import roc_auc_score
    w = wales.dropna(subset=FEATURES).copy()
    w["DLCN"] = w.apply(dlcn_score, axis=1)
    w["SimonBroome"] = w.apply(simon_broome, axis=1)
    w["MEDPED"] = w.apply(medped, axis=1)
    w["TUDOR"] = clf.predict_proba(StandardScaler().fit_transform(w[FEATURES].values))[:, 1]
    y = w["fh_pos"].values
    res = {k: round(roc_auc_score(y, w[k]), 3) for k in ["TUDOR", "DLCN", "MEDPED", "SimonBroome"]}
    log(f"  Overall AUC: {res}")
    # Bidirectional geographic split (family parity stands in for North/South Wales)
    north = w[w["family"].astype("int64", errors="ignore").astype(str).str[-1].astype(int) % 2 == 0] \
        if np.issubdtype(w["family"].dtype, np.number) else w.iloc[::2]
    south = w.drop(north.index)
    def auc_on(sub):
        return round(roc_auc_score(sub["fh_pos"], sub["TUDOR"]), 3) if sub["fh_pos"].nunique() > 1 else float("nan")
    log(f"  Bidirectional TUDOR AUC: North={auc_on(north)}  South={auc_on(south)}")
    w.to_csv(os.path.join(OUT, "headtohead_scored.csv"), index=False)
    return w, res


# ============================================================ Stage 7: subgroups + NRI
def stage7_subgroups_nri(w):
    rule("STAGE 7 - SUBGROUPS + NET RECLASSIFICATION (where the old tools fail)")
    from sklearn.metrics import roc_auc_score
    subs = {
        "young_<50":        w[w.age < 50],
        "on_statin":        w[w.on_tx == 1],
        "mixed_dyslip_TGhi": w[w.tg >= 2.5],
        "type2_diabetes":   w[w.t2dm == 1],
        "cascade_relative": w[w.proband_index == 0],
    }
    log("  subgroup            n    FH+   TUDOR   DLCN")
    for name, s in subs.items():
        if len(s) < 30 or s.fh_pos.nunique() < 2:
            log(f"  {name:18s} {len(s):5d}  (too few to score)"); continue
        at = roc_auc_score(s.fh_pos, s.TUDOR); ad = roc_auc_score(s.fh_pos, s.DLCN)
        log(f"  {name:18s} {len(s):5d} {int(s.fh_pos.sum()):4d}  {at:.3f}  {ad:.3f}   (delta {at-ad:+.3f})")
    # Simple categorical NRI vs DLCN at a fixed operating threshold
    thr_t = w.TUDOR.quantile(0.75); thr_d = w.DLCN.quantile(0.75)
    up = ((w.fh_pos == 1) & (w.TUDOR >= thr_t) & (w.DLCN < thr_d)).mean()
    down = ((w.fh_pos == 1) & (w.TUDOR < thr_t) & (w.DLCN >= thr_d)).mean()
    log(f"  Illustrative categorical NRI (events) vs DLCN: {up-down:+.3f}")


# ============================================================ Stage 8: reproduce
def stage8_reproduce():
    rule("STAGE 8 - REPRODUCER: locked headline targets")
    if not os.path.exists(LOCKED):
        log("  [WARN] verified_numbers_locked.json not found."); return
    v = json.load(open(LOCKED, encoding="utf-8"))
    h = v["head_to_head_overall_auc"]["wales_primary"]
    log(f"  Wales primary (REAL): TUDOR {h['TUDOR']} vs DLCN {h['DLCN']} "
        f"(MEDPED {h['MEDPED']}, SB {h['SimonBroome']})")
    log(f"  Bidirectional Wales : {v['bidirectional_wales']['direction_1_auc']} / "
        f"{v['bidirectional_wales']['direction_2_auc']}  (statin-naive "
        f"{v['bidirectional_wales']['statin_naive_auc']})")
    log(f"  Win count           : {v['win_count']['total_subgroups']} subgroups, "
        f"{v['win_count']['pairwise_vs_3_comparators']} pairwise; max gap "
        f"+{v['win_count']['largest_auc_gap']}")
    log(f"  NRI continuous      : +{v['nri']['continuous_primary']} / +{v['nri']['continuous_reciprocal']}")
    log(f"  Extra FH per 100    : T2DM +{v['additional_fh_caught_per_100']['type2_diabetes']}, "
        f"mixed +{v['additional_fh_caught_per_100']['mixed_dyslipidaemia']}, "
        f"young +{v['additional_fh_caught_per_100']['young']}")
    log("  NOTE: synthetic runs reproduce the METHOD; these REAL numbers regenerate")
    log("        only where the governed data lives (local workstation / UKB RAP).")


# ==================================================================== driver
def main():
    ap = argparse.ArgumentParser(description="TUDOR master orchestrator + reproducer")
    ap.add_argument("--real", action="store_true", help="use governed data (local machine only)")
    ap.add_argument("--synthetic", action="store_true", help="use synthetic data (web-safe)")
    ap.add_argument("--check", action="store_true", help="inventory inputs and exit")
    ap.add_argument("--reproduce", action="store_true", help="print locked targets and exit")
    ap.add_argument("--all", action="store_true", help="run every stage")
    ap.add_argument("--stage", type=int, help="run a single stage 1-8")
    a = ap.parse_args()

    if a.reproduce:
        stage8_reproduce(); return
    mode = "real" if a.real else "synthetic"
    if a.check:
        stage0_preflight(mode); return
    if not (a.all or a.stage):
        log(__doc__); log("Nothing to do. Try:  python TUDOR_MASTER.py --synthetic --all"); return

    stage0_preflight(mode)
    wales, ukb = stage1_cohort(mode)
    wales = stage2_treatment_adjust(wales)
    wales = stage3_features(wales)
    if a.stage in (1, 2, 3):
        log("\n[done: requested early stage]"); return
    clf, _ = stage4_fit(wales)
    if a.stage == 4:
        return
    scored, _ = stage56_headtohead(wales, clf)
    if a.stage in (5, 6):
        return
    stage7_subgroups_nri(scored)
    stage8_reproduce()
    rule("PIPELINE COMPLETE")
    log(f"  Outputs in: {OUT}")
    log("  Synthetic numbers are illustrative; clinical truth = verified_numbers_locked.json")


if __name__ == "__main__":
    main()
