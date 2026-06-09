# STAMP / ARE Paper Pipeline

This is the public pipeline hub for the STAMP/ARE paper package.

The original build scripts live in the private ARE implementation repo. This
public repository contains the synced paper artifacts, figures, STPA mirror, and
public evidence summary.

## What To Read

| Question | File |
|---|---|
| What is the paper PDF? | [`../../STAMP_ARE_Paper.pdf`](../../STAMP_ARE_Paper.pdf) |
| Where is the Markdown source? | [`../../paper/STAMP_ARE_Paper_arxiv_ready.md`](../../paper/STAMP_ARE_Paper_arxiv_ready.md) |
| What does "arXiv-ready" mean? | [`ARXIV_AND_EVIDENCE_REALITY.md`](ARXIV_AND_EVIDENCE_REALITY.md) |
| Why is the full evidence bundle not public? | [`EVIDENCE_PUBLIC_SUMMARY.md`](EVIDENCE_PUBLIC_SUMMARY.md) |
| What validation tier supports each claim? | [`../validation-tiers.md`](../validation-tiers.md) |
| Where is public STPA? | [`../../research/stpa/`](../../research/stpa/) |
| How should Word/PDF issues be handled? | [`PDF_AND_WORD_FORMATTING.md`](PDF_AND_WORD_FORMATTING.md) |

## Private Build Order

The private implementation repo uses the following shape when regenerating
paper artifacts:

```bash
python tools/paper/render_paper_assets.py
python tools/paper/build_stamp_arxiv_reconciled.py
python tools/paper/build_reference_docx.py
python tools/paper/md_to_arxiv_docx.py
python tools/paper/build_stamp_arxiv_pdf.py
python tools/paper/sync_public_discipline_repo.py
```

This public repo does not include those private build scripts. It is the public
mirror of the resulting artifacts and public-safe research package.

## Sync Rule

When refreshing the public mirror:

1. Rebuild paper artifacts in the private implementation repo.
2. Sync the PDF, Markdown, DOCX, figures, and public STPA files.
3. Update [`../../research/stpa/MIRROR_SYNC.txt`](../../research/stpa/MIRROR_SYNC.txt).
4. Run `python tools/check_public_repo.py`.
5. Confirm no private evidence, credentials, raw payloads, or protected material
   were copied into this public repo.
