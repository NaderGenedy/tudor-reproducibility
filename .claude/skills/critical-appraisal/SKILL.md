---
name: critical-appraisal
description: >-
  Structured critical appraisal of a research paper, preprint, protocol, or evidence
  claim. Use when the user asks "is this study any good?", to assess risk of bias,
  validity, or quality, to apply CASP / GRADE / ROBINS / Cochrane RoB / QUADAS, to
  check reporting-guideline compliance (CONSORT, STROBE, STARD, PRISMA, TRIPOD), or to
  decide how much to trust a finding before acting on it.
---

# Critical appraisal

Judge whether a study's conclusions are warranted by its design, conduct, and reporting.
Appraise the *method*, not the topic — a result you like can still be poorly supported.

## Pick the right lens (by design)
- **Diagnostic / prediction model** → QUADAS-2 (diagnostic accuracy), **TRIPOD** + PROBAST
  (prediction-model reporting & risk of bias). *Most relevant to TUDOR.*
- **RCT** → Cochrane RoB 2 + CONSORT.
- **Cohort / case-control / cross-sectional** → ROBINS-I / Newcastle–Ottawa + **STROBE**.
- **Systematic review / meta-analysis** → AMSTAR-2 + PRISMA.
- **Overall certainty of evidence** → **GRADE** (downgrade for risk of bias, inconsistency,
  indirectness, imprecision, publication bias).

## What to interrogate every time
1. **Validity (internal):** randomisation/allocation, confounding control, blinding, missing
   data handling, selective outcome reporting. For prediction models: data leakage, optimism,
   calibration reported?, validated externally?
2. **Bias hunt:** selection, measurement, attrition, immortal-time, **ascertainment/spectrum**,
   funding/conflict. Name the bias and its likely *direction and magnitude*, not just its
   presence.
3. **Statistics:** appropriate method? assumptions checked? effect size + CI (not just p)?
   multiplicity handled? sample size adequate? (Hand off specifics to `biostatistics`.)
4. **Generalisability (external):** does the population/setting match the claim and your use
   case? Was the comparator fair and current?
5. **Reporting integrity:** are the numbers internally consistent (text vs tables vs abstract)?
   any guideline items missing? citations real and uncorrected (check retractions)?
6. **Spin check:** do the conclusions exceed what the data support? Is a secondary/subgroup
   result framed as primary?

## Output
- **Verdict** with calibrated confidence (high / moderate / low / very low certainty).
- **Strengths** (brief) and **threats to validity** ranked by how much they could change the
  conclusion — biggest first, with direction of effect.
- **Bottom line:** how much to trust it and what would need to be true to rely on it.
- For manuscripts under revision, frame findings as actionable fixes (what to add/redo).

> Be fair, not contrarian: distinguish fatal flaws from minor limitations. Reserve "fatal"
> for things that actually invalidate the conclusion.
