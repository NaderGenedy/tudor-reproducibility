---
name: manuscript-qc
description: >-
  Pre-submission quality control for a research manuscript or revision — numerical-claim
  verification, internal consistency, citation integrity, reporting-guideline compliance,
  and reviewer-response checking. Use when the user wants to QC a paper before submission,
  check that every number is consistent across abstract/text/tables/figures, verify
  citations are real and uncorrected, confirm guideline compliance (TRIPOD/STROBE etc.),
  or audit a response-to-reviewers. This is the TUDOR-aligned `tudor-qc`/`manuscript-qc` gate.
---

# Manuscript QC

A deterministic pre-submission gate: catch wrong numbers, broken citations, internal
contradictions, guideline gaps, and unsupported claims **before** an editor or reviewer does.
British English; ASCII-safe output (Windows cp1252-safe), matching the TUDOR house style.

## 1. Numerical-claim verification (the headline gate)
- Extract **every** quantitative claim (Ns, percentages, AUCs, ORs/HRs with CIs, p-values,
  counts of subgroups won, "+190 additional FH patients", etc.).
- For each, locate its **source of truth** and confirm it matches:
  - TUDOR headline numbers → `verified_numbers_locked.json` (do not restate from memory or a slide).
  - Derived numbers → re-derive from the script/data path (`TUDOR_MASTER.py` outputs) where feasible.
- Flag any claim with no traceable source, or any mismatch, with the exact location.

## 2. Internal consistency
- Cross-check the **same number across abstract ↔ body ↔ tables ↔ figures ↔ response letter**.
  Discrepancies are the most common reviewer catch — list every one.
- Check arithmetic: subgroup counts sum to totals; percentages match numerators/denominators;
  CI bounds bracket point estimates; "25/25 subgroups" ⇄ "75/75 pairwise" type relationships hold.
- Check denominators are stated and stable (e.g. 506,506 adults) and used consistently.

## 3. Citation integrity
- Every reference must be **real and retrievable** (verify via PubMed/Scite/CrossRef).
- **Check retractions/corrections** (`Scite` editorialNotices) — never cite a retracted paper.
- Confirm in-text citations resolve to the reference list and vice versa (no orphans/dupes).
- Confirm cited papers actually support the claim made (no citation drift).

## 4. Reporting-guideline compliance
- Pick the guideline by design (defer detail to `critical-appraisal`): **TRIPOD + PROBAST** for
  TUDOR (diagnostic/prediction model), STROBE for observational components. Walk the checklist;
  list missing/under-reported items (e.g. calibration reported? external validation described?
  handling of treatment adjustment justified? family-level dedup stated?).

## 5. Claim–evidence audit (spin check)
- Does each conclusion stay within what the data support? Flag overreach, causal language on
  associational findings, and secondary/subgroup results framed as primary.
- Confirm the two TUDOR non-negotiables are stated and defended: **family-level dedup** and the
  **NoAgeLDL sensitivity variant**.

## 6. Response-to-reviewers audit (for revisions)
- Map each reviewer point → response → the actual manuscript change (with line/section).
- Flag any "addressed" claim with no corresponding edit, and any new number introduced in the
  response that isn't in the manuscript or the locked source.

## 7. Mechanics
- British spelling throughout; ASCII-only output. Consistent units, decimal places, and
  abbreviation definitions (defined at first use). Figure/table callouts all resolve.

## Output
A pass/fail QC report, **blocking issues first** (wrong/untraceable numbers, retracted cites,
internal contradictions, guideline gaps that affect validity), then non-blocking polish. Each
finding: what, where (file/section/line), why it matters, and the fix. End with a go / no-go
recommendation for submission.

> Be exact, not vague — "AUC stated 0.83 in abstract vs 0.81 in Table 2" beats "check the AUCs".
> Pairs with `biostatistics` (stat correctness) and `critical-appraisal` (validity).
