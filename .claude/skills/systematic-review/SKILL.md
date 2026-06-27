---
name: systematic-review
description: >-
  End-to-end systematic review and meta-analysis workflow following PRISMA 2020 and
  PROSPERO. Use when the user wants to plan or run a systematic review, register a
  protocol, build search strategies, screen records, extract data, assess risk of bias
  across studies, pool effects in a meta-analysis, assess heterogeneity/publication
  bias, or produce a PRISMA flow diagram and report. Reproducible and auditable end to end.
---

# Systematic review & meta-analysis

Run a transparent, reproducible review to PRISMA 2020 / Cochrane standards. Every decision is
recorded so the whole thing can be re-run and audited. British English.

## 0. Protocol first (PROSPERO)
- Write and **register the protocol before screening** (PROSPERO). Pre-specify: question (PICO),
  eligibility criteria, databases, search dates, screening process, data items, risk-of-bias
  tool, planned synthesis, and subgroup/sensitivity analyses. Deviations are logged, not hidden.

## 1. Search strategy
- Build a sensitive, reproducible strategy per database (PubMed/MEDLINE, Embase, Cochrane
  CENTRAL, plus trial registries via `Clinical_Trials` / `Scite__search_clinical_trials` and
  preprints). Combine MeSH + free-text with Boolean logic; document every line.
- Record database, interface, date searched, and hit count for each — needed for the PRISMA diagram.
- Add grey literature, citation chasing (forward via `Scite`, backward via reference lists).

## 2. Screening (dual, independent)
- De-duplicate. Title/abstract screen against criteria, then full-text screen.
- Two reviewers independently; record reasons for **every full-text exclusion**; resolve
  conflicts (third reviewer). Report agreement (κ) if asked.

## 3. Data extraction
- Pre-piloted form. Extract: study/design, population, intervention/exposure, comparator,
  outcomes, effect estimates + variance, follow-up, funding/conflicts. Dual extraction for
  numerics. Keep the raw extraction table as the audit record.

## 4. Risk of bias (study level)
- Choose the tool by design (hand off to `critical-appraisal`): RoB 2 (RCTs), ROBINS-I
  (non-randomised), QUADAS-2 (diagnostic), PROBAST (prediction models). Assess per outcome
  where relevant; tabulate domains.

## 5. Synthesis / meta-analysis
- **Decide poolability first** — clinical & methodological homogeneity, not just statistics.
  If too heterogeneous, synthesise narratively (SWiM) rather than forcing a pooled estimate.
- Pool with the right model (random-effects by default for clinical data); pick the effect
  measure (RR/OR/MD/SMD/HR). Hand the statistics to `biostatistics`.
- **Heterogeneity:** I², τ², prediction interval — interpret, don't just report. Explore via
  pre-specified subgroups / meta-regression (not data-dredged).
- **Small-study/publication bias:** funnel plot + Egger's (if ≥10 studies); note limitations.
- **Sensitivity analyses:** leave-one-out, by risk of bias, by model choice.

## 6. Certainty & reporting
- **GRADE** the certainty per outcome (Summary of Findings table).
- Produce the **PRISMA 2020 flow diagram** (identified → screened → eligible → included with
  exclusion counts/reasons) and complete the PRISMA checklist.
- Report to PRISMA: structured abstract, methods matching the protocol, results with forest
  plots, limitations, and a clear bottom line tied to certainty.

## Output
A protocol-aligned review package: search strategies (verbatim), PRISMA diagram + counts,
included-studies table, risk-of-bias summary, forest/funnel plots (where applicable), GRADE
SoF table, and a synthesis that states certainty honestly. Flag any post-hoc deviation.

> Never fabricate records, counts, or effect sizes — every number traces to a retrieved study.
> Pairs with `academic-research` (searching), `critical-appraisal` (RoB) and `biostatistics`
> (pooling). For an autonomous run, drive it via `autoresearch`.
