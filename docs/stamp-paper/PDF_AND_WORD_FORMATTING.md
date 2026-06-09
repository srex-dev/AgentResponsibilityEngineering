# PDF And Word Formatting

## Known Limits

The slim paper is authored in Markdown, converted to Word, and exported to PDF.
That path is not LaTeX. It does not automatically provide IEEE/ACM typography,
floating figures, or equation numbering.

For a venue-grade PDF, plan one of these paths:

- hand-polish the Word export once
- port the manuscript to LaTeX as a separate work item

## Converter Coverage

The private converter path handles:

- Markdown headings
- bold body text
- Markdown tables
- embedded PNG figures
- bullets and numbered lists

It does not reliably fix very large paragraphs from legacy Word extracts. Break
those manually in Markdown if the PDF renders dense blocks.

## Figures

The public manuscript references figures under:

[`../../assets/stamp-paper/`](../../assets/stamp-paper/)

Current figure files:

- [`fig_golden_path.png`](../../assets/stamp-paper/fig_golden_path.png)
- [`eq_ordering.png`](../../assets/stamp-paper/eq_ordering.png)
- [`eq_allow_ledger.png`](../../assets/stamp-paper/eq_allow_ledger.png)

## Public Sync

After regenerating artifacts in the private implementation repo, sync the public
PDF, Markdown, DOCX, and figure files to this repository and run:

```bash
python tools/check_public_repo.py
```
