# Medical & Scientific Research — Tooling Radar

> Curated, ranked watch-list of GitHub repos, **MCP servers**, **Claude skills/plugins**,
> and **top influencers** relevant to medical / clinical / biomedical research.
> Built for the TUDOR project (Dr Nader Genedy).
>
> **Ranking signal:** GitHub stars ("likes") and adoption/downloads.
> **Last refreshed:** 2026-06-27 · **Cadence:** weekly (see [§6 Auto-update](#6-auto-update)).
> Star counts are approximate snapshots and re-verified on each weekly refresh.

---

## 1. GitHub repositories — core medical / biomedical research tools

Ranked by GitHub stars (descending).

| # | Repo | ⭐ Stars | What it is |
|---|------|--------:|------------|
| 1 | [google-deepmind/alphafold](https://github.com/google-deepmind/alphafold) | ~13k | Protein-structure prediction — landmark structural-biology model. |
| 2 | [deepchem/deepchem](https://github.com/deepchem/deepchem) | ~6.8k | Deep learning for drug discovery, quantum chemistry, materials & biology. |
| 3 | [biopython/biopython](https://github.com/biopython/biopython) | ~4.2k | Core Python toolkit for computational molecular biology / genomics. |
| 4 | [broadinstitute/gatk](https://github.com/broadinstitute/gatk) | ~1.9k | Genome Analysis Toolkit — variant calling, the genomics workhorse. |
| 5 | [galaxyproject/galaxy](https://github.com/galaxyproject/galaxy) | ~1.8k | Web platform for accessible, reproducible biomedical analysis. |
| 6 | [bioconda/bioconda-recipes](https://github.com/bioconda/bioconda-recipes) | ~1.8k | Conda channel for thousands of bioinformatics packages. |
| 7 | [google/nucleus](https://github.com/google/nucleus) | — | C++/Python library for reading & writing genomics data. |
| 8 | [nroduit/Weasis](https://github.com/nroduit/Weasis) | — | Clinical-grade DICOM medical-imaging viewer. |

### Curated "awesome" lists worth subscribing to
| Repo | ⭐ Stars | Focus |
|------|--------:|-------|
| [medtorch/awesome-healthcare-ai](https://github.com/medtorch/awesome-healthcare-ai) | ~333 | Open-source healthcare tools, algorithms, datasets, papers. |
| [danielecook/Awesome-Bioinformatics](https://github.com/danielecook/Awesome-Bioinformatics) | — | Curated bioinformatics libraries & software. |
| [isaacmg/healthcare_ml](https://github.com/isaacmg/healthcare_ml) | — | ML/NLP resources by clinical application area. |
| [baeseongsu/awesome-machine-learning-for-healthcare](https://github.com/baeseongsu/awesome-machine-learning-for-healthcare) | — | ML × healthcare research collection. |
| [servierhub/top-life-sciences](https://github.com/servierhub/top-life-sciences) | — | Ranked list of top life-sciences OSS. |

---

## 2. Claude Skills & plugins for science / medicine

Ranked by stars / adoption.

| # | Repo | ⭐ Stars | Why it matters for TUDOR |
|---|------|--------:|--------------------------|
| 1 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | ~29.5k | 147 science skills + 100+ databases (PubChem, ChEMBL, UniProt, COSMIC, ClinicalTrials.gov). Used by 160k+ scientists. Covers clinical research, precision medicine, statistics. |
| 2 | [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | ~13.8k | The broad index of Claude skills/plugins — good discovery hub. |
| 3 | [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) | — | 169 skills across 13 categories incl. *Scientific & Research* and *Health & Life Sciences*. |
| 4 | [Aperivue/medsci-skills](https://github.com/Aperivue/medsci-skills) | ~167 | **Most TUDOR-aligned.** 45 skills for clinical manuscripts: PubMed/CrossRef-verified literature search, reference-integrity audit, EQUATOR (STROBE/STARD/PRISMA + 36 guidelines), sample-size/IRB, survival & meta-analysis code, forest/ROC figures, journal & cover-letter tooling. Built by a physician-researcher. |
| 5 | [Microck/ordinary-claude-skills](https://github.com/Microck/ordinary-claude-skills) | — | Includes `claude-scientific-skills` (sequence analysis, scRNA-seq, variant annotation, phylogenetics, computational pathology). |

> **Recommendation:** for TUDOR's manuscript / reproducibility workflow, install
> **medsci-skills** (clinical-publication fit) and pull statistical/figure skills from
> **K-Dense scientific-skills**. Both complement the in-repo `manuscript-qc` / `tudor-qc` skills.

---

## 3. MCP servers — biomedical data access

Model Context Protocol servers that wire Claude directly to medical databases.
(Several of these overlap with MCP servers already connected to this session:
PubMed, Clinical_Trials, Consensus, Scite, Hugging Face.)

| # | Repo | ⭐ Stars | Data sources exposed |
|---|------|--------:|----------------------|
| 1 | [Cicatriiz/healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public) | ~117 | FDA drugs, PubMed, ClinicalTrials.gov, medRxiv, ICD-10, NCBI Bookshelf, DICOM, medical calculator. |
| 2 | [cyanheads/pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server) | ~115 | PubMed / Europe PMC search, full text (PMC/EPMC/Unpaywall), citations, MeSH. STDIO + HTTP. |
| 3 | [arijitnist/Biomedical-MCP-Servers](https://github.com/arijitnist/Biomedical-MCP-Servers) | — | Collection: PubMed, bioRxiv, clinical trials, DrugBank, OpenTargets. |
| 4 | [openpharma-org/pubmed-mcp](https://github.com/openpharma-org/pubmed-mcp) | — | 35M+ PubMed citations, advanced filters, MeSH, PMC PDF access. |
| 5 | [pascalwhoop/medical-mcps](https://github.com/pascalwhoop/medical-mcps) | — | PubMed/PubTator3, OpenFDA, genetic-variant annotation, NCI cancer-trials API. |
| 6 | [Augmented-Nature/PubMed-MCP-Server](https://github.com/Augmented-Nature/PubMed-MCP-Server) | — | Full NCBI E-utilities + PubMed Central via 16 tools. |
| 7 | [JackKuo666/PubMed-MCP-Server](https://github.com/JackKuo666/PubMed-MCP-Server) | — | Lightweight PubMed search/analyze interface. |

---

## 4. Top influencers to track (for the weekly web-search sweep)

These accounts seed the weekly search so new tools surface from credible voices.

**Clinical / Health AI**
- **Nigam Shah** — Chief Data Scientist, Stanford Health Care (health data + AI).
- **Dr. Sara Murray** — Chief Health AI Officer, UCSF Health (ethical AI deployment).
- **Dr. Eric Poon** — CHIO, Duke Health; biostatistics & bioinformatics.

**Bioinformatics / Genomics**
- **Daniel MacArthur** ([@dgmacarthur](https://x.com/dgmacarthur)) — Co-Director, Medical & Population Genetics, Broad Institute.
- **Lior Pachter** — computational biology reviews & commentary.
- **Jason Moore** ([@moorejh](https://x.com/moorejh)) — Director, Institute for Biomedical Informatics, UPenn.

**Discovery sources (lists refreshed each run)**
- [HealthTech Magazine — Healthcare IT influencers](https://healthtechmagazine.net/article/2025/06/30-healthcare-it-influencers-worth-follow-2025)
- [Feedspot — Top Biotech influencers](https://x.feedspot.com/biotech_twitter_influencers/)
- [Feedspot — Bioinformatics blogs](https://bloggers.feedspot.com/bioinformatics_blogs/)

---

## 5. TUDOR-specific shortlist (start here)

1. **medsci-skills** — closest fit to the JCL manuscript / reproducibility pipeline.
2. **healthcare-mcp-public** or **cyanheads/pubmed-mcp-server** — already mirrored by the
   PubMed + Clinical_Trials MCPs connected to this session.
3. **K-Dense scientific-skills** — statistics, survival analysis, publication figures.
4. **DeepChem / Biopython** — only if the project expands into molecular/variant modelling.

---

## 6. Auto-update

This radar is refreshed **weekly** by a scheduled prompt that:
1. Re-runs the web searches in [`.claude/refresh_medical_tools_prompt.md`](.claude/refresh_medical_tools_prompt.md).
2. Re-verifies star counts and pulls newly-trending repos / MCPs / skills.
3. Scans the listed influencers + discovery lists for new releases.
4. Updates this file's tables and the **Last refreshed** date, then commits to
   `claude/github-medical-research-repos-hsia7p`.

> ⚠️ **How the schedule actually runs:** the in-session scheduler (CronCreate) only fires
> while a Claude Code session is active and auto-expires after 7 days, and this web
> environment is ephemeral. For a *truly autonomous* weekly run, trigger the refresh prompt
> via a scheduled **Claude Code on the web** session or a GitHub Actions cron — see the
> refresh prompt file for the exact instructions to paste.

---

*Sources: GitHub topic pages & repos, awesome-lists, HealthTech Magazine, Feedspot,
Anthropic skills marketplace. Star counts ≈ June 2026.*
