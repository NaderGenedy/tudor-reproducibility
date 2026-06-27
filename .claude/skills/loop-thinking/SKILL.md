---
name: loop-thinking
description: >-
  Iterative, self-correcting reasoning loops for hard problems. Use when a question is
  too hard or open-ended for one pass, when a first answer should be drafted then
  attacked and refined, when the user wants you to "think harder / iterate / be
  thorough / don't stop at the first answer", or when work should continue until a
  clear stopping criterion is met rather than after a single attempt.
---

# Loop thinking

Treat hard problems as a loop, not a single shot: draft → critique → revise → repeat until a
stopping criterion is met. Quality comes from iteration and self-disconfirmation.

## The loop
1. **Define done.** State the stopping criterion *before* you start — e.g. "all sub-claims
   verified", "two consecutive rounds surface nothing new", "estimate stable within tolerance",
   "every reviewer concern addressed". Without it, looping never converges or never ends.
2. **Draft.** Produce the best first attempt quickly. Mark its weakest, least-supported parts.
3. **Critique adversarially.** Switch hats and attack your own draft: What is wrong? What is
   unsupported? What did I assume? What would a sharp reviewer / `critical-appraisal` flag?
   What did I not check?
4. **Revise.** Fix the highest-impact problems first. Re-derive numbers; re-verify claims.
5. **Re-evaluate against the criterion.** Converged? Stop. Otherwise loop — but each round
   must add real value (new evidence, a fixed flaw, a tightened estimate), not reword.
6. **Detect diminishing returns.** If two rounds add nothing material, stop and say so. Track
   what each round changed so progress is visible.

## Guards against bad loops
- **No spinning:** if you keep circling the same point, name the blocker explicitly and either
  resolve it, gather new input, or escalate to the user — don't loop in place.
- **No drift:** re-anchor to the original question every round; resist scope creep.
- **Keep state:** maintain a short running list of open questions / resolved / changed-this-round.
- **Vary the angle:** if a round stalls, change tactic (new search, new method, new assumption
  to test) rather than repeating the last move.

## Output
- The converged answer **plus** the trail: what each round changed and why you stopped.
- Any residual uncertainty the loop could not resolve, stated honestly.

> Composes with everything: loop `academic-research` until the evidence is saturated, loop
> `biostatistics`/`research-reasoning` until the argument survives critique. For fully
> autonomous multi-step loops, use `autoresearch`.
