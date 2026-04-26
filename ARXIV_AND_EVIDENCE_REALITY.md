# arXiv, figures, and evidence — what this repo actually ships

This note is for **authors and reviewers**: it separates **marketing language** (“arxiv-ready”) from **venue mechanics** (what arXiv and journals expect) and states **where evidence bundles live**.

---

## 1. What “arXiv-ready” means *here*

| Meaning in this project | Meaning on arXiv.org (typical `cs.*`) |
|-------------------------|----------------------------------------|
| Narrative is **scoped**, **STPA-closed within a stated boundary**, and **aligned to a frozen evidence packet** (§13 of the slim paper). | Many submissions use **LaTeX** (`article`/`IEEEtran`/etc.) with **BibTeX**, vector figures, and numbered equations. |
| The **canonical authoring path** is **Markdown** → optional **Word** (`tools/paper/md_to_arxiv_docx.py`) → optional **PDF** (Word or `docx2pdf`). | arXiv accepts **PDF** for some categories and paths; **LaTeX** is still the default expectation for long-form CS papers. **Always read** [arXiv help for your subject class](https://info.arxiv.org/help/submit/index.html) before final upload. |
| **No LaTeX manuscript** is maintained in-tree yet; there is **no** automatic TikZ / PNG figure pipeline from the slim Markdown. | Camera-ready PDFs usually come from a **TeX** build, not from Word, if you want consistent fonts/margins/refs. |

**Bottom line:** The slim manuscript is **submission-*shaped*** (abstract, sections, appendices, hazard table, text figure): good for **review** and **ancillary** material. It is **not** a claim that the PDF already matches every arXiv PDF-only checklist item. If you need **true** arXiv LaTeX, plan a **pandoc or hand port** to `.tex` + a figure directory.

---

## 2. Tables, charts, graphs, formulas

| Artifact | In slim `STAMP_ARE_ARXIV_READY` today | Where else |
|----------|--------------------------------------|------------|
| **Tables** | **Appendix A** (roles), **Appendix B** (hazard closure at a glance, synced from `STPA_RESOLUTION.md` §1). §4 references the full hazard table in the normative doc. | Full UCA/assumption tables: `research/stpa/STPA_RESOLUTION.md`, `UCA_ENUMERATION.md`. |
| **Charts / graphs** | **Not** in the slim Markdown build (no matplotlib, no PNG pipeline). | Long-form `STAMP_ARE_FULL.md` may describe diagrams; export figures manually if a venue requires them. |
| **Vector architecture figures** | **Not** auto-generated. **Appendix C** is a **text figure** (golden execution chain) so reviewers get *something* printable without a draw tool. | `docs/` architecture markdown can inform hand-drawn figures for LaTeX. |
| **Formulas** | No displayed LaTeX math in the slim paper. | Ordering obligations: `formal/tla/are_execution_boundary.tla` (proof **target**, not TLAPS-checked). |

---

## 3. Where the **evidence bundles** are

**Canonical location (this repository, not the public discipline repo):**

```text
research/evidence-bundles/2026-04-26-stamp-safety-reviewer-packet-submission/
```

That directory is a **frozen snapshot**: copied `STPA_RESOLUTION.md`, `STPA_PACKAGE.md`, `claims_ledger.md`, `interposition_audit.md`, `SAFETY_CASE.md`, paper pointers, **`FILES.sha256`**, `GIT_HEAD.txt`, pytest + internal-gate logs, and `MANIFEST.md`. Integrity:

```bash
cd research/evidence-bundles/2026-04-26-stamp-safety-reviewer-packet-submission
sha256sum -c FILES.sha256
```

**Why bundles are not on [AgentResponsibilityEngineering](https://github.com/srex-dev/AgentResponsibilityEngineering):** That repo is **public narrative + PDFs**. Full logs and internal paths are **IP / hygiene** sensitive and **large**. Reviewers who need the bundle should receive it as **confidential supplementary** or you attach a **zip** as arXiv **Ancillary files** / journal supplementary — produced by:

```bash
python tools/paper/assemble_submission_package.py
```

Output: `paper/submission-package/_dist/STAMP_ARE_submission_<bundle>_<UTC>/` (see `paper/submission-package/README.md`).

---

## 4. Minimal “complete submission system” checklist

1. **Manuscript:** `paper/STAMP_ARE_ARXIV_READY.md` (+ optional `.docx` / PDF).  
2. **This reality note:** `paper/ARXIV_AND_EVIDENCE_REALITY.md` (for PC / reviewers / yourself).  
3. **Normative closure:** `research/stpa/STPA_RESOLUTION.md` (in repo + copied in bundle).  
4. **Frozen bundle:** directory above + verified `FILES.sha256`.  
5. **Optional LaTeX port** when you want arXiv-default typography — **separate work item**.

---

*Version: aligned to submission-package layout and `build_stamp_arxiv_reconciled.py` appendices B–C.*
