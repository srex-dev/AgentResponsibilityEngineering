# Contributing

Thank you for helping shape Agent Responsibility Engineering.

This repository is public-facing research and discipline material, so the bar is
different from a private implementation repo: clarity, attribution, and public
safety matter more than volume.

## Good Contributions

Useful contributions include:

- clearer terminology
- better diagrams
- STPA/STAMP corrections
- public-safe examples
- citation improvements
- typo/link fixes
- evidence-boundary clarification
- questions that sharpen the discipline

## Out Of Scope

Please do not submit:

- private ARE platform source code
- Command Center, visual RAG, BYOPolicy, or governance-strata internals
- private proof packets or raw gate logs
- customer or employer confidential material
- raw payloads, credentials, signatures, tokens, or headers
- legal or certification claims that are not supported by the evidence model

## Public-Safety Rule

If a contribution would require a reviewer to inspect sensitive material to
understand it, it probably belongs in a private review packet, not this repo.

## Local Checks

Before opening a pull request, run:

```bash
python tools/check_public_repo.py
```

The check verifies required public files, local Markdown links, and obvious
secret-shaped strings.

## Pull Requests

Keep pull requests focused. Explain:

- what changed
- why it matters
- whether it changes the public/commercial boundary
- whether evidence or citation claims changed

## Code Of Conduct

Participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
