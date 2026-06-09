# Reproducing TUDOR from scratch on **Claude Code on the web**

This is the governance-aware, copy-paste guide for re-running the TUDOR method in the
**web** version of Claude Code (claude.ai/code → "Cloud" / web sessions), which executes
in an **ephemeral cloud Linux sandbox** — not on your D:/C:/E: drives.

---

## ⚠️ Read first: what the web sandbox can and cannot do

| | Local workstation / UKB RAP | **Claude Code on the web** |
|---|---|---|
| Sees your D:/C:/ drives | ✅ | ❌ (fresh Ubuntu container) |
| Has the governed UKB / Wales data | ✅ | ❌ — and it **must stay that way** |
| Can reproduce the **clinical numbers** | ✅ | ❌ |
| Can reproduce the **method / code path** | ✅ | ✅ (on synthetic data) |
| Internet / `pip install` | ✅ | ✅ |

> **Never paste or upload UK Biobank or All-Wales registry individual-level data into a web
> session.** It breaches the UKB Material Transfer Agreement and NHS information-governance.
> The synthetic generator exists precisely so you never have to. The real numbers regenerate
> only on your own machine / UKB RAP.

So the web goal is: **prove the pipeline is correct and runnable end-to-end**, then carry the
verified code home to run on the governed data.

---

## Option A — point Claude Code on the web at your GitHub repo (recommended)

1. **Push this `REPRODUCIBILITY/` folder to a (private) GitHub repo**, e.g.
   `NaderGenedy/tudor-reproducibility`. It contains **no patient data** — only code,
   pinned deps, the synthetic generator, and aggregated headline JSON. Safe to host.
   ```bash
   # run locally, once
   cd D:/TUDOR_SUBMISSION/REPRODUCIBILITY
   git init && git add . && git commit -m "TUDOR reproducibility package"
   gh repo create NaderGenedy/tudor-reproducibility --private --source=. --push
   ```
2. **Open Claude Code on the web** → start a session on that repo.
3. **Paste this prompt:**
   > Set up Python 3.12, `pip install -r requirements.txt`, then run
   > `python make_synthetic_tudor_data.py` and `python TUDOR_MASTER.py --synthetic --all`.
   > Show me the console output and the contents of `output/`. Then read `TUDOR_MASTER.py`
   > and confirm the family-level dedup (Stage 1) and NoAgeLDL sensitivity (Stage 4) are correct.
4. Claude runs it in the sandbox and shows you AUCs, coefficients, subgroup deltas, and NRI —
   the full method, on synthetic data.

## Option B — no repo: hand Claude the three files

In a web session, upload only these **shareable** files:
`TUDOR_MASTER.py`, `make_synthetic_tudor_data.py`, `requirements.txt`, `verified_numbers_locked.json`.
Then paste the same prompt as step 3 above. (Never upload anything from `DATA_INVENTORY.md` §1–3.)

## Option C — rebuild the package from nothing

If you have *only* this markdown file, ask Claude on the web:
> Recreate the TUDOR reproducibility package from `README.md` + `DATA_INVENTORY.md`:
> write `make_synthetic_tudor_data.py` (synthetic Wales + UKB cohorts with a planted FH signal,
> column names per DATA_INVENTORY §2–3) and `TUDOR_MASTER.py` (stages 0–8: cohort build with
> family-level dedup, treatment back-calculation, 3-pillar features → 11 vars, Elastic Net +
> NoAgeLDL sensitivity, head-to-head vs DLCN/MEDPED/Simon Broome, subgroups + NRI). Then run it.

---

## Exact commands (any option, inside the web sandbox)

```bash
python --version                       # expect 3.12.x
python -m pip install -r requirements.txt
python make_synthetic_tudor_data.py    # -> synthetic_data/ (NO real patients)
python TUDOR_MASTER.py --check         # inventory: governed data will read [ABSENT] — correct
python TUDOR_MASTER.py --synthetic --all
python TUDOR_MASTER.py --reproduce     # print the locked clinical targets for reference
```

Expected: a clean Stage 0→8 run ending in `PIPELINE COMPLETE`, with synthetic AUCs ~0.95–0.97
(TUDOR > DLCN > MEDPED > Simon Broome) and TUDOR winning every subgroup — the **shape** of the
real result. `--check` correctly reports the governed files as `[ABSENT]` in the sandbox.

---

## Then: get the REAL numbers (on your machine, not the web)

1. Clone the same repo onto your **local** workstation (where the governed data lives), or
   into the **UK Biobank RAP** environment.
2. Confirm the three governed files are present (paths in `DATA_INVENTORY.md` §1) — or edit the
   `REAL_PATHS` dict at the top of `TUDOR_MASTER.py` to match your environment / RAP mount.
3. Run:
   ```bash
   python TUDOR_MASTER.py --real --all
   ```
   This refuses to start unless all governed inputs are physically present (a deliberate
   guard so the real path only runs where it is lawful). It writes the real cohort,
   coefficients, head-to-head, and subgroup tables to `output/`.
4. Cross-check the console against `verified_numbers_locked.json`. For the *full* published
   figures (UKB transport 0.756, NMR asymmetry, FAMCAT, 25/25 subgroup panel), also run the
   dedicated scripts in `D:/Projects/CALON_AlphaFold_Rebuild/scripts/` and
   `C:/Users/nader/Downloads/calon_ukb_pipeline/CALON_rich_wales.py`.

---

## Rebuilding the *deliverables* (manuscript / figures / slides) on the web

These don't need governed data — only the derived/aggregated artefacts — so they're web-friendly:

| Deliverable | How |
|---|---|
| Manuscript docx from md | `python md2docx_v4.py` (in `calon_ukb_pipeline/manuscript/`) or the `md2docx` skill |
| Figures | `Rscript Rcode_Figure_LDL_equation.R` and `Rcode_Figure_NMR_3panel.R` (needs R 4.5 + ggplot2/patchwork) |
| 15-min talk script | already built: `TUDOR_Talk_Script_15min_v2.{md,docx}` |
| Headline-number QC | `python TUDOR_MASTER.py --reproduce` + the `manuscript-qc` skill |

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `pyarrow` / install fails | ensure Python **3.12** (not 3.14); `pip install -r requirements.txt` |
| `[FATAL] --real requested but governed data not present` | you're not on the workstation/RAP — use `--synthetic` |
| Unicode/cp1252 crash | already handled (`stdout.reconfigure`); keep stdout ASCII |
| Different sklearn version warnings | harmless; pins are in `requirements.txt` if you need exact parity |
| Synthetic AUCs look "too good" | by design — the planted signal is clean; method-demo only |
