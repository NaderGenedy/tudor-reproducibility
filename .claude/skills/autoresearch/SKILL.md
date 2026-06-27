---
name: autoresearch
description: >-
  Autonomous end-to-end research loop: take a research question and drive it from
  search → read → appraise → reason → synthesise → verify, iterating until the question
  is answered with cited, fact-checked evidence. Use when the user wants a deep,
  multi-source research report, a literature/evidence brief, an "investigate this and
  come back with an answer" task, or a comprehensive review with minimal hand-holding.
  Orchestrates the academic-research, critical-appraisal, biostatistics,
  research-reasoning and loop-thinking skills.
---

# Autoresearch

A self-driving research pipeline. You decompose the question, gather and vet evidence across
sources, reason over it, and iterate until saturated — then deliver a cited, verified report.
This is the orchestrator; it leans on the other research skills for each stage.

## Pipeline (loop until the stopping criterion is met)
1. **Scope.** Restate the question; define what a complete answer contains and the explicit
   **stopping criterion** (e.g. "key claims triangulated across ≥2 independent sources and
   two consecutive search rounds add nothing new"). Decompose into 3–6 sub-questions.
2. **Plan the sweep.** For each sub-question, list diverse queries and the right source:
   PubMed/Consensus (primary literature), Scite (citation context & disputes),
   Clinical_Trials (trial landscape), web search (recent/grey literature).
3. **Gather** (`academic-research`). Run the searches; collect candidates with metadata. Be
   multi-modal — search by concept, by entity, by author, by trial — angles miss different things.
4. **Appraise** (`critical-appraisal`). Triage by evidence level and risk of bias; check
   retractions. Drop the weak; flag the contested. For stats-heavy claims, vet with
   `biostatistics`.
5. **Read deeply.** Extract the actual effect sizes, CIs, populations, and stated limitations
   from the surviving sources (full text where available).
6. **Reason** (`research-reasoning`). Synthesise across sources: where do they agree, conflict,
   and leave gaps? Build the causal/mechanistic picture; weigh competing explanations.
7. **Verify adversarially.** For each headline claim, try to *refute* it: find the
   counter-evidence, confirm the citation is real and uncorrected, check numbers are quoted
   not paraphrased. Default to "unverified" until a source backs it.
8. **Critic pass** (`loop-thinking`). Ask "what's missing — a source not read, a claim not
   checked, an angle not searched?" Whatever it finds becomes the next loop. Stop when the
   criterion is met or two rounds add nothing material.

## Discipline
- **Never fabricate** a citation, DOI, or statistic. Every claim traces to a retrieved source.
- **No silent gaps:** if a sub-question stayed unanswered or a search was capped, say so.
- **Show the audit trail:** queries run, sources kept/dropped, and why.
- Respect governance: this repo's real patient data never leaves its governed location — research
  the *literature and methods*, not individual-level records.

## Deliverable
A structured brief: executive answer → findings by sub-question (claim → evidence → strength →
dissent → gap) → numbered reference list (titles linked to `https://doi.org/{doi}`) → a
**limitations & open-questions** section → the search/verification audit. Calibrated confidence
throughout — flag what is solid vs tentative.

> For a heavier, parallelised fan-out, this pairs with the built-in `deep-research` skill;
> use `autoresearch` for the disciplined single-thread loop and as the orchestration recipe.
