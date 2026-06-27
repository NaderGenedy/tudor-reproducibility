# Weekly refresh — Medical & Scientific Research Tooling Radar

Paste this prompt into a Claude Code session (web or local) to refresh
`MEDICAL_RESEARCH_TOOLS.md`. It is also the prompt fired by the in-session weekly cron.

---

**Task:** Refresh `MEDICAL_RESEARCH_TOOLS.md` in this repo.

1. Run web searches for newly trending / updated items in these buckets:
   - GitHub repos for medical / biomedical / clinical research tools (sort by stars).
   - MCP servers for biomedical data (PubMed, ClinicalTrials.gov, FDA, genomics).
   - Claude skills / plugins for science & medicine.
   - New releases or tools highlighted by the influencers listed in §4 of the file.
   Suggested queries:
   - "trending github medical research bioinformatics repositories this week"
   - "new MCP server biomedical PubMed clinical trials github 2026"
   - "new Claude skills medical research clinical manuscript 2026"
   - Per-influencer: "<name> new tool / repo / release 2026"

2. Re-verify GitHub star counts for every repo already listed (WebFetch each repo page).

3. Update `MEDICAL_RESEARCH_TOOLS.md`:
   - Re-sort each table by stars (descending).
   - Add any new high-signal repos/MCPs/skills; remove dead/archived ones.
   - Note notable rank changes since last week.
   - Update the **Last refreshed** date at the top.

4. Commit to branch `claude/github-medical-research-repos-hsia7p` with message
   `chore: weekly refresh of medical research tooling radar (<date>)` and push.

Keep it concise — tables + one-line descriptions. British English.

---

## Making the weekly schedule autonomous

The in-session cron (CronCreate) only fires while a session is live and expires after
7 days, and the web sandbox is ephemeral. For a hands-off weekly run, use **one** of:

- **Claude Code on the web — scheduled session:** create a recurring trigger that opens a
  session on this repo and pastes the task above. See
  https://code.claude.com/docs/en/claude-code-on-the-web
- **GitHub Actions cron:** a weekly workflow (`on: schedule: - cron: "13 8 * * 1"`) that
  runs Claude Code headless against this repo with the task above. Requires an API key
  secret and network egress to web search.
