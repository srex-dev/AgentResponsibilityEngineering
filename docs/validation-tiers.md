# Validation Tiers

ARE evidence should name the validation tier behind each claim. This keeps the
public paper, STPA mirror, and implementation evidence honest about what was
proved and where.

## Tier Summary

| Tier | Name | What It Supports | What It Does Not Prove |
|---|---|---|---|
| T0 | Static argument | diagrams, STPA closure records, design claims, paper reasoning | runtime behavior |
| T1 | Local compose | bounded local integration behavior on one machine | staging or production behavior |
| T2 | Synthetic/staging | repeatable gateway/runtime behavior against a staging candidate | customer production safety |
| T3 | Production candidate | externally run readiness gate against a named candidate | universal safety or legal certification |

## Claim Rule

A claim must not speak above its tier.

Examples:

- A local Docker run can support "the local check-only path held this boundary."
- It cannot support "the production platform is safe."
- A bounded STPA closure can support "the hazards in this execution boundary
  have named dispositions."
- It cannot support "all autonomous-agent hazards are eliminated."

## Evidence Boundary

Public evidence may include:

- paper arguments
- STPA files
- public-safe summaries
- commit IDs
- aggregate test outcomes
- hashes or proof references

Public evidence must not include:

- raw payloads
- tokens or credentials
- raw headers
- signatures or private keys
- protected evidence bodies
- private proof packets
- client confidential material

## Reviewer Language

Use these phrases:

- "bounded safety case"
- "public-safe evidence summary"
- "local compose validation"
- "staging readiness gate"
- "full packet available by request or supplementary material"

Avoid these phrases unless separate evidence exists:

- "certified"
- "production safe"
- "complete proof of AI safety"
- "all hazards eliminated"
- "validated in production"
