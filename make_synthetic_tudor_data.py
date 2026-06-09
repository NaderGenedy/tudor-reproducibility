#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_synthetic_tudor_data.py
============================================================================
Generate SYNTHETIC, NON-REAL, shareable stand-ins for the two governed
TUDOR cohorts, so the full pipeline (TUDOR_MASTER.py) can run end-to-end in
any sandbox -- including Claude Code on the web -- WITHOUT any UK Biobank or
NHS / All-Wales registry data.

  *** THIS FILE CONTAINS NO REAL PATIENT DATA. ***
  Every row is drawn from random number generators with a planted FH signal.
  Column NAMES mirror the real extracts so the analysis code path is identical;
  the VALUES are fictional. Numbers produced from these files are meaningless
  clinically and must never be quoted -- they exist only to prove the code runs.

Outputs (into ./synthetic_data/):
  wales_synthetic.csv   -- Dragon-3 / All-Wales-shaped lipid-clinic cohort
  ukb_synthetic.csv     -- UK-Biobank-shaped population cohort

Reproducible: fixed SEED. British spelling retained in comments.
Author: Dr Nader Genedy (CALON-FH programme).
"""
import os, argparse
import numpy as np
import pandas as pd

SEED = 20260608
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "synthetic_data")

# Class-level fractional LDL reductions (mirrors the real treatment-adjustment table)
STATIN_REDUCTION = {"none": 0.00, "simva": 0.32, "atorva": 0.45, "rosuva": 0.50, "prava": 0.24}
EZE_ADD, PCSK9_ADD, CAP = 0.20, 0.60, 0.85


def _planted_fh_signal(rng, n, base_ldl, fh):
    """FH carriers: higher untreated LDL, LOWER triglycerides at matched LDL
    (the Brown-Goldstein selectivity the whole paper turns on), more stigmata."""
    ldl_ut = base_ldl + fh * rng.normal(3.2, 0.8, n)            # carriers ~+3 mmol/L
    tg = np.exp(rng.normal(0.45, 0.45, n)) - fh * rng.normal(0.35, 0.15, n)  # carriers lower TG
    tg = np.clip(tg, 0.4, 12.0)
    return np.clip(ldl_ut, 1.0, 14.0), tg


def make_wales(n=3099, fh_prevalence=0.18, seed=SEED):
    rng = np.random.default_rng(seed)
    fh = (rng.random(n) < fh_prevalence).astype(int)
    age = np.clip(rng.normal(52, 14, n), 18, 90)
    male = (rng.random(n) < 0.46).astype(int)
    base_ldl = rng.normal(4.3, 1.1, n)
    ldl_ut, tg = _planted_fh_signal(rng, n, base_ldl, fh)

    # Treatment: severe (high untreated LDL) more likely treated -> the masking paradox
    p_tx = 1 / (1 + np.exp(-(ldl_ut - 4.5)))
    on_tx = (rng.random(n) < 0.55 + 0.25 * p_tx).astype(int)
    statin = np.where(on_tx == 1,
                      rng.choice(list(STATIN_REDUCTION)[1:], n), "none")
    eze = ((on_tx == 1) & (rng.random(n) < 0.25)).astype(int)
    pcsk9 = ((on_tx == 1) & (rng.random(n) < 0.05)).astype(int)
    red = np.array([STATIN_REDUCTION[s] for s in statin]) + eze * EZE_ADD + pcsk9 * PCSK9_ADD
    red = np.clip(red, 0, CAP)
    ldl_meas = ldl_ut * (1 - red)                                # what the clinic actually sees

    hdl = np.clip(rng.normal(1.3, 0.3, n) - fh * 0.02, 0.5, 3.0)
    tc = ldl_meas + hdl + 0.45 * tg + rng.normal(0, 0.3, n)
    apob = np.clip(0.65 + 0.22 * ldl_ut / 3.0 + rng.normal(0, 0.1, n), 0.4, 2.2)
    apoa1 = np.clip(1.4 + 0.3 * hdl + rng.normal(0, 0.1, n), 0.8, 2.5)

    # Ascertainment: index probands vs cascade-screened relatives (the Proband Effect)
    is_index = (rng.random(n) < 0.62).astype(int)
    typ = np.where(is_index == 1, "Index", "Relative")
    # Families: relatives share a FamilyNumber with an index (drives family-level dedup)
    fam = rng.integers(1, int(n * 0.7), n)

    stig = ((fh == 1) & (rng.random(n) < 0.18) & (age < 60)).astype(int)
    arcus = ((rng.random(n) < 0.10 + 0.15 * fh)).astype(int)
    t2dm = (rng.random(n) < 0.10 + 0.18 * (age > 55)).astype(int)
    smoke = (rng.random(n) < 0.18).astype(int)
    sbp = np.clip(rng.normal(132, 16, n), 95, 210)
    onbp = (rng.random(n) < 0.30).astype(int)
    lpa = np.clip(rng.exponential(40, n), 1, 400)

    # Outcome: ASCVD rises with untreated LDL burden, age, FH, smoking
    lin = -5.2 + 0.30 * ldl_ut + 0.045 * (age - 50) + 0.35 * fh + 0.4 * smoke + 0.3 * male
    ascvd = (rng.random(n) < 1 / (1 + np.exp(-lin))).astype(int)

    df = pd.DataFrame({
        "FamilyNumber": fam, "DatabaseNumber": np.arange(1, n + 1),
        "TypeofPatient": typ, "Ageattest": age.round(1), "Gender": np.where(male == 1, "M", "F"),
        "Positive1": np.where(fh == 1, "Y", "N"),       # genetically confirmed FH status
        "LDL_1": ldl_meas.round(2), "TC_1": tc.round(2), "HDL_1": hdl.round(2), "TRG_1": tg.round(2),
        "ApoB": apob.round(2), "ApoA1": apoa1.round(2), "Lpaunitsmgl": lpa.round(0),
        "OnTreatment": np.where(on_tx == 1, "Y", "N"), "Statin": statin,
        "Ezetimibe": np.where(eze == 1, "Y", "N"), "PCSK9i": np.where(pcsk9 == 1, "Y", "N"),
        "TendonXanthomata": np.where(stig == 1, "Y", "N"), "CornealArcus": np.where(arcus == 1, "Y", "N"),
        "Diabetes_binary": t2dm, "Smoking_binary": smoke,
        "BloodPressureSystolic": sbp.round(0), "onBPtreat": onbp,
        "ASCVD_combined": ascvd,
        "_true_untreated_LDL": ldl_ut.round(2),         # ground truth (never available in real data)
    })
    return df


def make_ukb(n=60000, carrier_prevalence=0.007, seed=SEED + 1):
    rng = np.random.default_rng(seed)
    fh = (rng.random(n) < carrier_prevalence).astype(int)
    gene = np.where(fh == 1, rng.choice(["LDLR", "APOB"], n, p=[0.8, 0.2]), "none")
    age = np.clip(rng.normal(56, 8, n), 40, 70)         # UKB is a late-life biobank
    male = (rng.random(n) < 0.45).astype(int)
    base_ldl = rng.normal(3.6, 0.9, n)
    ldl_ut, tg = _planted_fh_signal(rng, n, base_ldl, fh)
    p_tx = 1 / (1 + np.exp(-(ldl_ut - 4.0)))
    on_tx = (rng.random(n) < 0.30 + 0.45 * p_tx).astype(int)  # ~81% of severe are treated
    red = on_tx * rng.choice([0.32, 0.45, 0.50], n)
    ldl_meas = ldl_ut * (1 - red)
    hdl = np.clip(rng.normal(1.4, 0.35, n), 0.5, 3.0)
    apob = np.clip(0.7 + 0.2 * ldl_ut / 3 + rng.normal(0, 0.1, n), 0.4, 2.2)
    bmi = np.clip(rng.normal(27.4, 4.6, n), 16, 55)
    t2dm = (rng.random(n) < 0.06 + 0.0015 * (bmi - 25) * 10).astype(int)
    fhx = (rng.random(n) < 0.12 + 0.3 * fh).astype(int)
    lin = -5.0 + 0.28 * ldl_ut + 0.05 * (age - 55) + 0.4 * fh + 0.3 * male
    ascvd = (rng.random(n) < 1 / (1 + np.exp(-lin))).astype(int)

    return pd.DataFrame({
        "eid": np.arange(1_000_000, 1_000_000 + n),
        "age": age.round(1), "sex": male, "fh_carrier": fh, "gene": gene,
        "ldl_direct": ldl_meas.round(2), "tc": (ldl_meas + hdl + 0.45 * tg).round(2),
        "hdl": hdl.round(2), "tg": tg.round(2), "apob": apob.round(2),
        "on_statin": on_tx, "bmi": bmi.round(1), "t2dm": t2dm,
        "family_history": fhx, "ascvd": ascvd,
        "_true_untreated_LDL": ldl_ut.round(2),
    })


def main():
    ap = argparse.ArgumentParser(description="Generate synthetic TUDOR cohorts (no real data).")
    ap.add_argument("--wales_n", type=int, default=3099)
    ap.add_argument("--ukb_n", type=int, default=60000)
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    w = make_wales(a.wales_n); u = make_ukb(a.ukb_n)
    wp = os.path.join(a.out, "wales_synthetic.csv"); up = os.path.join(a.out, "ukb_synthetic.csv")
    w.to_csv(wp, index=False); u.to_csv(up, index=False)
    print("[SYNTHETIC DATA WRITTEN - NOT REAL PATIENTS]")
    print(f"  Wales: {wp}  rows={len(w)}  FH+={int((w.Positive1=='Y').sum())}  families={w.FamilyNumber.nunique()}")
    print(f"  UKB  : {up}  rows={len(u)}  carriers={int(u.fh_carrier.sum())}")
    print("  -> now run:  python TUDOR_MASTER.py --synthetic --all")


if __name__ == "__main__":
    main()
