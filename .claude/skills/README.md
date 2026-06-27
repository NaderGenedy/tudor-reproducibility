# Research skills (Claude Code Agent Skills)

Custom skills for academic / clinical research, tailored to the TUDOR project.
Each folder holds a `SKILL.md`; Claude auto-invokes one when a request matches its
`description`, or you can call it explicitly (e.g. `/autoresearch`).

| Skill | Use it for |
|-------|------------|
| [`academic-research`](academic-research/SKILL.md) | Find, verify & synthesise literature (PubMed / Consensus / Scite / trials). Never fabricates citations. |
| [`biostatistics`](biostatistics/SKILL.md) | Choose tests/models, interpret CIs & effect sizes, evaluate prediction models (AUC, calibration, NRI), power/sample size. |
| [`research-reasoning`](research-reasoning/SKILL.md) | First-principles, mechanistic & causal reasoning; surface assumptions; cause vs correlation. |
| [`critical-appraisal`](critical-appraisal/SKILL.md) | Risk-of-bias & quality appraisal — TRIPOD/PROBAST, QUADAS, GRADE, STROBE/PRISMA/CONSORT. |
| [`loop-thinking`](loop-thinking/SKILL.md) | Iterative draft → critique → revise loops with explicit stopping criteria. |
| [`systematic-review`](systematic-review/SKILL.md) | Full PRISMA 2020 / PROSPERO review & meta-analysis — protocol, search, screening, extraction, pooling, GRADE, PRISMA diagram. |
| [`manuscript-qc`](manuscript-qc/SKILL.md) | Pre-submission gate — numerical-claim verification, internal consistency, citation integrity, TRIPOD compliance, reviewer-response audit (the TUDOR `tudor-qc` gate). |
| [`autoresearch`](autoresearch/SKILL.md) | Autonomous end-to-end research loop that orchestrates all of the above. |

**How they compose:** `autoresearch` drives the pipeline → `academic-research` gathers →
`critical-appraisal` + `biostatistics` vet → `research-reasoning` synthesises →
`loop-thinking` iterates to convergence.

These are project-scoped skills (committed to the repo), so they travel with TUDOR and work in
Claude Code on the web. They complement the built-in `deep-research` and `code-review` skills.
