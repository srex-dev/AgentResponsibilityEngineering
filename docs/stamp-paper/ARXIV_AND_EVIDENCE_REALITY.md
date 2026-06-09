# arXiv And Evidence Reality

## What "arXiv-ready" Means Here

In this repository, "arXiv-ready" means the argument is structured for
submission: abstract, bounded STPA closure, appendices, figures, and evidence
tiering.

It does not mean the repository ships a default LaTeX build. The current public
source path is Markdown -> Word -> PDF.

## Evidence Is Tiered

Evidence is not binary.

| Tier | Public artifact |
|---|---|
| Level 1 | Paper and discipline framing |
| Level 2 | Public evidence summary and STPA mirror |
| Level 3 | Full frozen hashed packet by request or supplementary material |

The public PDF omits raw logs on purpose. See:

- [`EVIDENCE_PUBLIC_SUMMARY.md`](EVIDENCE_PUBLIC_SUMMARY.md)
- [`../validation-tiers.md`](../validation-tiers.md)

## Formatting And Figures

The paper source lives at:

[`../../paper/STAMP_ARE_Paper_arxiv_ready.md`](../../paper/STAMP_ARE_Paper_arxiv_ready.md)

Figures live at:

[`../../assets/stamp-paper/`](../../assets/stamp-paper/)

For venue-grade typography, either hand-polish the Word/PDF export or port the
paper to LaTeX as a separate work item.
