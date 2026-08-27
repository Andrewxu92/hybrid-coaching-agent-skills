# Agent Instructions

This repository contains Agent Skills intended for Hybrid / HYROX coaching.

## Source of truth

- `skills/` is the canonical distributable Skill content.
- `docs/` explains architecture and methodology for humans and maintainers.
- `sources/user-methodology/` preserves owner-provided source material.
- `tests/` defines routing and contract expectations.

## Rules for changes

1. Keep each Skill narrow and triggerable.
2. Do not duplicate logic already owned by the upstream `skill-for-hirox` training engine.
3. Do not turn a source inference into a hard coaching rule without explicit evidence.
4. Prefer `unknown` / `unclear` over invented precision.
5. Keep `SKILL.md` concise; move detailed rules into `references/`.
6. Every Skill must state what it does and when it should trigger.
7. Preserve the distinction between performance screening and medical diagnosis.
8. When routing changes, update the routing matrix and scenario tests.
9. Run `python scripts/validate_skills.py` before considering a Skill release-ready.
10. Update `CHANGELOG.md` for user-visible architecture or routing changes.

## Naming

Skill directory names and `SKILL.md` `name` fields must match and use lowercase letters, numbers, and single hyphens only.
