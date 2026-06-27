---
name: biostatistics
description: >-
  Biostatistical reasoning and reproducible analysis for clinical/epidemiological
  data. Use when the user needs to choose a statistical test or model, interpret a
  p-value / CI / effect size, design an analysis, compute power/sample size, handle
  confounding or missing data, evaluate a diagnostic/prediction model (AUC, calibration,
  NRI, decision curves), or sanity-check a statistical claim. Prioritises correctness,
  assumptions, and honest uncertainty over a fast answer.
---

# Biostatistics

Pick the right method, state its assumptions, quantify uncertainty, and make it reproducible.

## Core principles
- **Question → estimand → method**, in that order. Name what you are trying to estimate before
  choosing a test. Descriptive ≠ associational ≠ causal — say which you are doing.
- **Effect size + CI over p-values.** Report magnitude and uncertainty; a p-value alone is not
  a result. Avoid "significant/non-significant" dichotomies.
- **State and check assumptions** (distribution, independence, linearity, proportional hazards,
  homoscedasticity). If violated, name the robust/alternative method.
- **Confounding & bias first.** Before modelling, list plausible confounders, selection bias,
  immortal-time bias, and ascertainment/measurement bias. (TUDOR is explicitly
  ascertainment-aware — keep that lens.)
- **Multiplicity & overfitting:** pre-specify; correct for multiple testing; use CV / external
  validation for prediction; never tune on the test set.

## Test/model selection (quick map)
- Two groups, continuous outcome → t-test (or Mann–Whitney if non-normal/ordinal).
- ≥3 groups → ANOVA / Kruskal–Wallis (+ planned contrasts, not just omnibus).
- Binary outcome, covariates → **logistic regression**; report ORs with CIs.
- Time-to-event → Kaplan–Meier + **Cox PH** (check proportionality); report HRs.
- Counts/rates → Poisson / negative-binomial (check overdispersion).
- Clustered/repeated (e.g. family-level data) → mixed models / GEE. **TUDOR dedups at
  `FamilyNumber`; respect that clustering — don't treat relatives as independent.**
- High-dimensional / regularisation → Elastic Net / LASSO (TUDOR's fitter); report the
  penalty, the CV scheme, and a sensitivity variant.

## Diagnostic / prediction-model evaluation
- **Discrimination:** AUC/C-statistic with CI. **Calibration:** calibration plot + slope/
  intercept (discrimination without calibration is incomplete).
- **Reclassification:** NRI / IDI — report continuous *and* categorical, and the comparator.
- **Clinical utility:** decision-curve analysis / net benefit beats accuracy alone.
- **Validation:** internal (bootstrap/CV) then **external/bidirectional** (TUDOR: Wales ↔ UKB).
- Watch optimism, class imbalance, and leakage (treatment info leaking into "untreated" features).

## Power & sample size
- Specify effect size, alpha, power, allocation, and the test before computing n. State the
  assumptions driving the number; give a sensitivity range, not a single figure.

## Reproducibility
- Pin versions, set seeds, show the code, and report exactly what was excluded and why.
- Re-derive numbers from data/scripts; don't restate figures from memory or a slide.

## Output
Method chosen + why, assumptions (checked/violated), the estimate with CI, the caveats, and —
when analysis is requested — runnable, commented code (match the repo's Python 3.12 / scikit
stack). For prediction models, always pair discrimination with calibration and utility.
