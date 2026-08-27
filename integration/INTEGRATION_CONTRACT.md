# Integration Contract v0.1.0

This repository is a portable intelligence-layer package for the existing `skill-for-hirox` training engine.

## Canonical skills

All seven new skills live directly under `skills/`. Each directory contains `SKILL.md` and optional progressive-disclosure references.

## Upstream patches

The four files under `integration/patch/` are replacement/boundary patches for the upstream HYROX umbrella skills:

- `hyrox-coach`
- `hyrox-needs-profile`
- `hyrox-week-template`
- `hyrox-plan-audit`

Do not keep both original and patched copies at the same destination path.

## Routing contract

1. Explicit named skill wins.
2. A clear single-purpose request beats a compound router.
3. HYROX demand questions stay in the demand layer.
4. Athlete-vs-demand comparison uses `capability-gap-analysis`.
5. Known training targets go directly to the existing method selector.
6. Compound preparation can enter `hyrox-coach`, which delegates to the narrowest useful skill.
7. Immediate race-state decisions use `state-based-pacing`.

## Scope

The repository does not clone the upstream training engine. It supplies the missing athlete-intelligence and Hybrid/HYROX decision layer.
