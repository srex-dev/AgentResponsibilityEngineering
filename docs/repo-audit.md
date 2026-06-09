# Public Repo Audit

Run the public repo audit before publishing major updates:

```bash
python tools/check_public_repo.py
```

The audit checks:

- required community and citation files exist
- local Markdown links resolve
- obvious secret-shaped strings are absent from text files

It is intentionally lightweight. It does not replace human review of claims,
paper quality, or evidence tiering.

## CI

GitHub Actions runs the same audit on pull requests and pushes to `main` via:

```text
.github/workflows/public-repo-audit.yml
```

If a legitimate text example trips the scanner, rewrite it as a placeholder such
as `Bearer <token>` rather than embedding a realistic secret-shaped value.
