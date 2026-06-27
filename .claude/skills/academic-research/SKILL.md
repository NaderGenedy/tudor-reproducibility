---
name: academic-research
description: >-
  Rigorous academic literature search, retrieval and synthesis for medical/clinical
  research. Use when the user asks to find papers, review the evidence, build a
  background/related-work section, do a (mini) systematic search, locate primary
  sources, or check what is known about a clinical/biomedical question. Verifies
  every citation against a real source — never fabricates references.
---

# Academic research

Find, verify, and synthesise the scholarly evidence on a question. British English.

## Non-negotiables
- **Never invent a citation.** Every reference must come from a tool result (PubMed, Consensus,
  Scite, Clinical_Trials, Europe PMC). If you cannot retrieve it, say so — do not guess a DOI,
  author list, or year.
- **Check for retractions/corrections** before relying on a paper (Scite `editorialNotices`).
- **Distinguish evidence levels:** RCT/meta-analysis > cohort > case-control > case series >
  expert opinion. State the design when you cite.
- **Quote, don't paraphrase, for key claims** — capture the actual sentence supporting a number.

## Workflow
1. **Frame the question.** Convert to PICO (Population, Intervention/exposure, Comparator,
   Outcome) where applicable. List the concepts and synonyms/MeSH terms.
2. **Search broadly, then narrow.** Run 3–5 diverse queries across the available tools:
   - `mcp__PubMed__search_articles` / `mcp__Consensus__search` for primary literature.
   - `mcp__Scite__search_literature` for Smart Citation context (who agrees/disputes a claim).
   - `mcp__Clinical_Trials__search_trials` for the trial landscape.
   Use Boolean operators and exact phrases; record the queries you ran.
3. **Triage.** Keep the highest-evidence, most-cited, most-recent, and most-contradictory hits.
   Note disagreement explicitly — a contested finding is a finding.
4. **Read deeply** (use `get_full_text_article` / Scite section reads): pull the methods, the
   effect size with CI, the population, and the limitation the authors admit.
5. **Synthesise**, don't list. Group by theme/claim. For each claim give: the evidence,
   the strength, the dissent, and the gap.
6. **Cite properly.** Inline numbered refs `[1]`; reference list with title hyperlinked to
   `https://doi.org/{doi}`. Flag any paper you could not fully verify.

## Output
- A short synthesis (claims → evidence → strength → gaps), then a numbered reference list.
- A one-line **search audit** (queries + databases used) so the search is reproducible.
- If evidence is thin or conflicting, say that plainly rather than over-claiming.

> TUDOR context: the manuscript targets the *Journal of Clinical Lipidology*. Favour FH /
> lipidology / cardiovascular-risk sources; cross-check headline numbers against
> `verified_numbers_locked.json` claims rather than restating them from memory.
