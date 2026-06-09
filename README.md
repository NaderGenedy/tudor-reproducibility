# TUDOR — Reproducibility Package

**TUDOR** = a **T**reatment-adjusted, ascertainment-aware **D**iagnostic algorithm for
**familial hypercholesterolaemia (FH)**, developed in the All-Wales FH Registry and
validated bidirectionally across Wales and UK Biobank — **506,506 adults**.

> **Author:** Dr Nader Genedy, University Hospital of Wales / Cardiff University
> **UK Biobank application:** 1002450 · **Target journal:** Journal of Clinical Lipidology
> **This folder:** everything needed to understand, re-run, and verify the TUDOR analysis —
> on your own machine *or* on Claude Code on the web.

---

## 0. TL;DR — run it in 3 commands

```bash
python -m pip install -r requirements.txt
python make_synthetic_tudor_data.py          # writes synthetic_data/ (NO real patients)
python TUDOR_MASTER.py --synthetic --all      # full method, end-to-end
```

That reproduces the **method** (treatment adjustment → 3-pillar features → Elastic Net →
bidirectional validation → head-to-head → NRI) on shareable synthetic data.
The **clinical numbers** live in `verified_numbers_locked.json` and can only be
regenerated where the governed data physically resides (see §4).

---

## 1. The one-paragraph science

The diagnostic criteria we use for FH — DLCN (2000), Simon Broome (1991), MEDPED (1993) —
were calibrated on **untreated, metabolically lean index cases**. Today ~80% of patients
arrive **already on a statin** and ~27% have type 2 diabetes, so the measured LDL is a
*pharmacological residue*, not the inherited phenotype. TUDOR fixes three things in one
interpretable equation: (1) **Lipid Age** — back-calculates untreated LDL from the
prescription record; (2) **Triglyceride Shield** — reads LDL in its triglyceride context,
exploiting the Brown–Goldstein selectivity that FH carriers have *lower* triglycerides at
matched LDL; (3) **Proband Effect** — separates index referrals from cascade-screened
relatives. Result: **25/25 pre-specified subgroups won** (75/75 pairwise vs three
comparators), and **+190 additional FH patients** identified where DLCN fails.

Headline numbers: `verified_numbers_locked.json`.

---

## 2. What's in this folder

| File | Purpose |
|---|---|
| `TUDOR_MASTER.py` | **The full pipeline.** Stages 0–8; runs on real or synthetic data. |
| `make_synthetic_tudor_data.py` | Generates web-safe synthetic Wales + UKB cohorts (no real data). |
| `verified_numbers_locked.json` | Ground-truth headline numbers (the reproducer's assertion targets). |
| `requirements.txt` | Pinned Python 3.12 dependencies. |
| `REPRODUCE_ON_CLAUDE_WEB.md` | Step-by-step for Claude Code **on the web** (the governance-aware path). |
| `DATA_INVENTORY.md` | Every dataset used — governed + derived — with sizes, fields, access status. |
| `run_all.sh` | One-shot convenience wrapper. |
| `output/` | Created on run: cohort, coefficients, scored head-to-head, subgroups. |
| `synthetic_data/` | Created on run: `wales_synthetic.csv`, `ukb_synthetic.csv`. |

---

## 3. Pipeline stages (what `TUDOR_MASTER.py` does)

| Stage | Name | Enforces |
|---|---|---|
| 0 | Preflight | env + data inventory; aborts `--real` if governed data absent |
| 1 | Cohort build | **family-level deduplication** (one event per `FamilyNumber`) |
| 2 | Treatment adjustment | untreated LDL = measured ÷ (1 − Σ drug reductions), capped 0.85 |
| 3 | Feature engineering | 3 pillars → **11 locked variables** |
| 4 | Fit TUDOR | Elastic Net logistic + 5-fold CV + **NoAgeLDL sensitivity** |
| 5/6 | Head-to-head | TUDOR vs DLCN / MEDPED / Simon Broome + **bidirectional** Wales split |
| 7 | Subgroups + NRI | young, on-statin, mixed dyslipidaemia, T2DM, cascade relative |
| 8 | Reproduce | print locked targets from `verified_numbers_locked.json` |

Two of Dr Genedy's standing non-negotiables are baked into the code: **family-level dedup**
(Stage 1) and the **NoAgeLDL sensitivity variant** (Stage 4).

---

## 4. Real vs synthetic — the governance line

```
LOCAL workstation / UK Biobank RAP            ANYWHERE ELSE (incl. Claude web)
  governed data present                          governed data ABSENT (correctly)
  python TUDOR_MASTER.py --real --all             python TUDOR_MASTER.py --synthetic --all
  -> reproduces the CLINICAL NUMBERS              -> reproduces the METHOD / code path only
```

**Do not upload UK Biobank or All-Wales registry individual-level data to any third-party
cloud.** It breaches the UKB Material Transfer Agreement and NHS information-governance.
`TUDOR_MASTER.py --real` will refuse to run unless all three governed files are physically
present, precisely so the real path can only execute where it is lawful.

Real governed inputs (present only on the author's machine):
- `C:/Users/nader/Downloads/FH_Dragon3 (1).csv` — Dragon-3 / All-Wales lipid clinic (424 rows, 202 cols)
- `D:/Projects/CALON_AlphaFold_Rebuild/data/pass_FULL_MASTER.csv` — All-Wales PASS master (2.8 MB)
- `D:/Projects/CALON_AlphaFold_Rebuild/data/ukb_FULL_MASTER.csv` — UK Biobank master (332 MB, 501,936 rows)

Full manifest: `DATA_INVENTORY.md`.

---

## 5. Where the rest of the project lives (outside this folder)

| Artefact | Location |
|---|---|
| Submission package (manuscript, response, cover letter, figures) | `D:/TUDOR_SUBMISSION/` (`01`–`07`) |
| R4 build scripts + tracked redlines + change ledgers | `D:/TUDOR_R4_submission/` |
| Analysis scripts (head-to-head, subgroups, NMR, FAMCAT) | `D:/Projects/CALON_AlphaFold_Rebuild/scripts/` |
| Live Wales sensitivity analysis (self-contained) | `C:/Users/nader/Downloads/calon_ukb_pipeline/CALON_rich_wales.py` |
| Figures (R source + PDF + PNG) | `D:/TUDOR_SUBMISSION/Rcode_Figure_*.R`, `Figure_*.pdf/png` |
| Award talk (15-min script) | `C:/Users/nader/Downloads/TUDOR_Talk_Script_15min_v2.{md,docx}` |
| Slide deck | `C:/Users/nader/Downloads/TUDOR_F  -  AutoRecovered (1).pptx` |

---

## 6. Outputs you'll see

After `--synthetic --all`, check `output/`:
- `cohort_wales.csv` — harmonised, family-deduplicated cohort
- `tudor_coefficients.csv` — the 11 standardised Elastic Net coefficients
- `headtohead_scored.csv` — every patient scored by TUDOR + 3 comparators
- console — AUCs, NoAgeLDL sensitivity, per-subgroup deltas, NRI

Synthetic AUCs run high (~0.97) by design — the planted signal is deliberately clean.
They demonstrate the **ordering and method** (TUDOR > DLCN > MEDPED > Simon Broome; TUDOR
wins every subgroup), not the real effect sizes.

---

## 7. Provenance & integrity

- Every headline number in `verified_numbers_locked.json` was read directly off the rendered
  award deck (Slides 7, 12, 13) and cross-checked against the JCL manuscript abstract.
- Numerical-claim QC for the manuscript itself: see `D:/TUDOR_SUBMISSION/03_Response_to_Reviewers`
  and the `manuscript-qc` / `tudor-qc` skill outputs.
- British English throughout; ASCII-only stdout (Windows cp1252-safe).
