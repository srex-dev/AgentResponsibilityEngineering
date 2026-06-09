# Evidence Public Summary

This file gives reviewers and readers a public-safe view of the evidence model
behind the STAMP/ARE paper.

It is not a substitute for the full frozen Level 3 packet when a reviewer needs
to inspect raw gate logs, transcripts, and file hashes.

## Claim Tiering

Strong claims in the manuscript should map to a validation tier. See
[`../validation-tiers.md`](../validation-tiers.md).

Do not treat local Docker-only runs as proof of staging or production behavior
without separate evidence.

## Normative STPA

The public STPA mirror is available in:

[`../../research/stpa/`](../../research/stpa/)

Important files:

| File | Purpose |
|---|---|
| [`STPA_RESOLUTION.md`](../../research/stpa/STPA_RESOLUTION.md) | Closure record |
| [`STPA_PACKAGE.md`](../../research/stpa/STPA_PACKAGE.md) | Main package |
| [`UCA_ENUMERATION.md`](../../research/stpa/UCA_ENUMERATION.md) | Unsafe control action enumeration |
| [`HAZARD_UCA_CONSTRAINT_TEST_CLOSURE.md`](../../research/stpa/HAZARD_UCA_CONSTRAINT_TEST_CLOSURE.md) | Hazard, constraint, and test closure |

## Frozen Packet Identity

| Field | Value |
|---|---|
| Bundle directory | `research/evidence-bundles/2026-04-26-stamp-safety-reviewer-packet-submission/` |
| Git commit at freeze | `653d455346e57f6a0ba37eecb4132138d923a36d` |
| Meaning of frozen | Normative STPA docs, paper pointers, full test/gate logs, and hashes copied at freeze time |

The full frozen packet is not stored in this public repo. That is intentional:
it may include raw logs and implementation evidence that should be shared only
through a controlled reviewer or supplementary-material channel.

## Recorded Outcomes

From the frozen packet manifest at the time of freeze:

- `python -m pytest tests/ -q`: STAMP harness, 10 passed
- `python tools/testing/run-all-internal-gates.py`: internal gate matrix, 48
  components, all pass

Re-freeze updates these numbers. If the paper claim changes, this summary should
be updated in the same commit.

## Public-Safety Rule

Public evidence may include IDs, decisions, aggregate counts, commit hashes,
source references, and public-safe summaries.

Public evidence must not include raw payloads, tokens, credentials, raw headers,
signatures, private keys, protected evidence bodies, private proof packets, or
client confidential material.
