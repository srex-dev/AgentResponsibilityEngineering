# STAMP / ARE paper — one place to start

If anything felt **scattered**, use this file as the hub.

## What to read

| Question | File |
|----------|------|
| **What is “arXiv-ready” vs LaTeX?** | `paper/ARXIV_AND_EVIDENCE_REALITY.md` (short) |
| **Read STPA without ARE access** | Public mirror: [AgentResponsibilityEngineering `research/stpa/`](https://github.com/srex-dev/AgentResponsibilityEngineering/tree/main/research/stpa) |
| **Why isn’t the full evidence bundle inside the public PDF?** | `paper/STAMP_ARE_ARXIV_READY.md` §13 + `paper/EVIDENCE_PUBLIC_SUMMARY.md` |
| **Word/PDF looks wrong — how do I fix formatting?** | `paper/PDF_AND_WORD_FORMATTING.md` |
| **Claims cheat sheet** | `paper/STAMP_ARE_FINAL.md` |

## Build order (slim paper → Word → PDF)

```bash
# 1) Figures / equation PNGs (matplotlib)
python tools/paper/render_paper_assets.py

# 2) Assemble Markdown (docx extract + STPA inserts + §13 + appendices)
python tools/paper/build_stamp_arxiv_reconciled.py

# 3) Word (embeds tables + images from paper/assets/)
python tools/paper/md_to_arxiv_docx.py paper/STAMP_ARE_ARXIV_READY.docx paper/STAMP_ARE_ARXIV_READY.md

# 4) PDF — Word “Save As PDF”, or docx2pdf, or your desktop path
```

## Submission zip (manuscript + full bundle)

```bash
python tools/paper/assemble_submission_package.py
```

Output under `paper/submission-package/_dist/` (gitignored).
