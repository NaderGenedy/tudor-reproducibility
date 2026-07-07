# TUDOR (JCLINLIPID-D-25-01142R2) — Figure reconciliation & Supplementary plan

**Status:** accepted, pre-proof · **Journal:** Journal of Clinical Lipidology (Elsevier)
**Purpose:** reconcile the 8 uploaded figure files against the 5 accepted main-figure legends, and
reinstate the reviewer-seen extras as online Supplementary figures the academically defensible way.

> **What this document is:** an execute-ready plan (legends, main-text callouts, editor note) plus a
> clearly-marked list of the parts only the author can do (regenerate data-bound figures; locate the
> correct main-figure images; confirm the existing Supplement's numbering). It does **not** claim the
> figures themselves are fixed — several are data-bound and must be regenerated in the secure environment.

---

## 1. The situation in one paragraph

The accepted manuscript defines **5 main figures**. The submission embeds **8 image files**, only one of
which (`fig3_headtohead.png` = Figure 3) matches an accepted legend. The other seven are figures from an
**earlier, reviewer-seen version** (trimmed when the main text was cut to five) plus the companion paper's
NMR analysis. The author confirms (a) these were in a reviewed version, (b) the paper is pre-proof, and
(c) he wishes to reinstate the relevant ones as Supplementary figures. Because the revision already
"moved statistical minutiae to the Supplement", reinstating reviewer-seen detail there is consistent with
the paper's own revision approach — provided each figure is (i) cited once in the main text, (ii) internally
consistent with the accepted cohorts, and (iii) for the NMR figure, cross-cited to the companion paper.

---

## 2. Main figures — action

| Accepted legend | Correct file | Action |
|---|---|---|
| **Figure 1** — TUDOR clinical decision pathway (workflow) | ❌ not in upload | **Re-upload** correct workflow image (`D:/TUDOR_SUBMISSION/`) |
| **Figure 2** — Validation ladder & transport states | ❌ not in upload | **Re-upload** correct AUC-ladder image |
| **Figure 3** — Head-to-head comparator performance | ✅ `fig3_headtohead.png` | **Keep** — correct as uploaded |
| **Figure 4** — Operating-point trade-offs | ❌ not in upload | **Re-upload** correct trade-off image |
| **Figure 5** — Intended-use & calibration boundary | ❌ not in upload | **Re-upload** correct calibration image |

The uploaded `FH_PATHOGENESIS`, `NMR`, `fig7_nmr_smd`, `Figure_ROC_5models_2cohorts`,
`Figure10_separation_density`, `Figure9_subgroup_forest` are **not** main figures — see §3.

---

## 3. Supplementary figures — proposed disposition

Assign S-numbers that **continue your existing Supplement's sequence** (the paper already ships a separate
supplement; I don't have its current numbering — placeholders `S[a]…S[f]` below).

| File | Proposed slot | Supports (main-text hook) | Readiness |
|---|---|---|---|
| `Figure_S3_LDL_equation_impact.png` | Suppl. Fig **S[a]** | Methods — untreated-LDL reconstruction / LDL-C equation choice | ✅ closest to ready (verify n) |
| `Figure9_subgroup_forest.png` | Suppl. Fig **S[b]** | Results — subgroup robustness | ⚠️ **regenerate** (cohort mismatch) |
| `Figure_ROC_5models_2cohorts.png` | Suppl. Fig **S[c]** | Results — head-to-head discrimination | ⚠️ **regenerate** (cohort mismatch) |
| `Figure10_separation_density.png` | Suppl. Fig **S[d]** (optional) | Results — carrier/non-carrier separation | ⚠️ regenerate; also partly redundant with S[c] |
| `FH_PATHOGENESIS.png` | **Graphical abstract** (preferred) or Suppl. Fig **S[e]** | Introduction — conceptual | ✅ ready (conceptual, no data) |
| `NMR.png` **or** `fig7_nmr_smd.png` (pick one) | Suppl. Fig **S[f]** | Discussion — Triglyceride-Shield mechanism | ⚠️ overlap-managed (see §6) |

**Two objective blockers (author only):**

1. **Cohort mismatch.** `ROC`, `density`, and `subgroup` figures display **All-Wales N=5,613 (1,965 carriers)**
   and **UKB lipid-clinic N=58,021 (729 carriers)** — numbers that appear **nowhere** in the accepted paper
   (whose cohorts are n=1,274 / 4,570 / 49,427 / 501,936). As-is they read as a *different* analysis and will
   invite scrutiny. **Regenerate on the accepted cohorts** (or add an explicit cohort-definition note).
2. **`NMR.png` and `fig7_nmr_smd.png` are near-duplicates** — submit only **one**.

---

## 4. Draft Supplementary legends (copy-paste; fill n where noted)

**S[a] — LDL-C estimating equation.** Effect of the LDL-C estimating equation on threshold-based recognition
of treated LDLR carriers (UK Biobank LDLR carriers, n=3,093). (a) Lin concordance correlation coefficients for
Friedewald, Sampson-NIH and Martin-Hopkins LDL-C against the directly measured assay. (b) Mean bias
(calculated minus direct LDL-C) by triglyceride band, showing progressively greater Friedewald under-estimation
as triglycerides rise. (c) Sensitivity for a true LDL-C ≥4.9 mmol/L at the referral threshold, by triglyceride
band and equation. (d) Discordance direction by dyslipidaemia pattern, and TUDOR AUC by equation (range 0.004).
Because TUDOR reconstructs untreated LDL-C and carries triglycerides as an explicit feature, the equation choice
contributes one of eleven inputs rather than determining the decision. Aggregate outputs only; no participant-level data.

**S[b] — Subgroup discrimination.** Subgroup discrimination (AUC, DeLong 95% CI) for TUDOR versus comparators
(eDLCN, FAMCAT, Simon Broome, MEDPED) across prespecified subgroups — sex, age band, statin status, LDL-C band,
triglyceride band and type 2 diabetes — in the All-Wales registry and the UK Biobank lipid-clinic-eligible cohort.
TUDOR coefficients frozen (locked model scored, not re-estimated); dashed line = chance. *[Insert n and carrier
counts per cohort, consistent with the main-text cohorts.]*

**S[c] — ROC discrimination.** Receiver-operating-characteristic curves for discrimination of LDLR variant carriers
by TUDOR and comparators in the All-Wales registry and the UK Biobank lipid-clinic-eligible cohort, with DeLong 95%
confidence intervals. TUDOR (bold) scored with frozen coefficients; FAMCAT input-limited per cohort. *[Insert n and
carrier counts per cohort, consistent with the main-text cohorts.]*

**S[d] — Score separation (optional).** Distribution of standardised model scores among LDLR variant carriers versus
non-carriers, by model and cohort. Vertical lines mark group medians; d = Cohen's d. TUDOR shows the largest
carrier/non-carrier separation. *[Insert n per cohort.]*

**S[e] — FH mechanism (if not used as graphical abstract).** Molecular basis of LDLR-mediated familial
hypercholesterolaemia and treatment masking. Pathogenic LDLR variants impair hepatic LDL-particle clearance through
class-specific mechanisms (Classes 2–5); lipid-lowering therapy amplifies residual receptor activity and lowers
measured LDL-C, obscuring the untreated phenotype assumed by conventional criteria. TUDOR reconstructs the
pre-treatment phenotype from routine variables. Conceptual illustration; no participant-level data.

**S[f] — NMR lipoprotein signature.** Receptor-selective lipoprotein signature of LDLR carriers on NMR metabolomics
(UK Biobank, n=486,866). At matched LDL-C, LDLR carriers show lower triglycerides with unchanged VLDL-C and HDL-C,
consistent with a selective LDL-receptor-clearance lesion. **This analysis is reported in full in the companion study
[cite companion]; it is reproduced here only to document the biological basis of TUDOR's triglyceride-based
("Triglyceride Shield") feature.** Aggregate outputs only.

---

## 5. Main-text callouts to insert (every SI figure MUST be cited once)

The accepted text currently contains **no** numbered SI-figure callouts, so each reinstated figure needs one
sentence. Because this lightly edits the accepted main text, clear it with the editor (§7).

- **Methods** (untreated-LDL reconstruction): *"The choice of LDL-C estimating equation had minimal influence on TUDOR (Supplementary Figure S[a])."*
- **Results** (subgroups): *"Discrimination across prespecified subgroups is shown in Supplementary Figure S[b]."*
- **Results** (head-to-head): *"Receiver-operating-characteristic curves for all models in both cohorts are provided in Supplementary Figure S[c] (score distributions, Supplementary Figure S[d])."*
- **Introduction** (only if S[e] is an SI figure, not the graphical abstract): *"The molecular basis of LDLR-mediated FH and treatment masking is summarised in Supplementary Figure S[e]."*
- **Discussion** (Triglyceride Shield): *"TUDOR's triglyceride-based feature reflects a receptor-selective lipoprotein signature demonstrated in our companion analysis [cite] and summarised in Supplementary Figure S[f]."*

---

## 6. NMR figure — how to keep it in TUDOR without a redundant-publication problem

You chose to include NMR in TUDOR's Supplement as well as the companion paper. That is defensible **only** with
all three safeguards (the cleaner alternative — companion-only, cited from TUDOR — is noted first):

- **Preferred:** let the NMR analysis live in the companion paper and have TUDOR **cite** it (no duplicate figure).
- **If duplicated (your choice), do all of:**
  1. **Cross-cite both ways** — TUDOR's S[f] legend cites the companion; the companion cites TUDOR.
  2. **Disclose the overlap** — one line in the cover/editor note that the NMR figure also appears in the companion
     manuscript from the same dataset, reproduced to support a *different* claim (here: a model feature, not the
     paper's primary result).
  3. **Do not present it as new** — frame S[f] as supporting the Triglyceride-Shield feature, not as a TUDOR finding.
  4. **Copyright** — JCL/Elsevier is not open-access by default; if the companion publishes first elsewhere, you may
     need permission/attribution to reuse the identical figure. Using your own not-yet-published figure in both is
     fine if disclosed; reusing a *published* one needs a permission line.

*(The running deep-research report will attach the exact COPE/ICMJE/Elsevier citations for these points; this section
will be updated with them.)*

---

## 7. Draft note to the editor (pre-proof)

> Dear [Editor],
>
> Thank you for flagging the figure files for JCLINLIPID-D-25-01142R2. Two corrections before proofs:
>
> **Main figures.** Figure 3 (head-to-head, `fig3_headtohead.png`) is correct as uploaded. The files currently
> attached for Figures 1, 2, 4 and 5 are from an earlier version; I am re-uploading the correct images that match
> the accepted legends.
>
> **Supplementary figures.** I would like to reinstate [N] figures that were part of the earlier reviewed version and
> were trimmed from the main text during revision, as online Supplementary Figures S[..]–S[..]. Each has a legend and a
> single main-text callout (appended). No new claims are introduced; the additions are consistent with the accepted
> analyses. One figure (NMR lipoprotein signature) also appears in our companion manuscript from the same dataset [ref];
> it is cross-cited and disclosed as shared, and is included only to document a model feature.
>
> Please advise whether you would prefer these handled at proof stage or via a brief revised manuscript/supplement file.
>
> Kind regards,
> Dr Nader Genedy

---

## 8. Author action checklist

- [ ] Re-upload correct images for **Figures 1, 2, 4, 5** (match accepted legends).
- [ ] **Regenerate** ROC / density / subgroup figures on the **accepted cohorts** (or add a cohort-definition note).
- [ ] **Dedupe** the two NMR files — submit one.
- [ ] Decide **FH pathogenesis** = graphical abstract (preferred) vs Supplementary figure.
- [ ] Confirm the **existing Supplement's numbering**; assign final S-numbers; insert the §5 callouts.
- [ ] Add a **reciprocal cross-citation** to the NMR figure in the companion paper.
- [ ] Send the §7 note to the editor (pre-proof window).
