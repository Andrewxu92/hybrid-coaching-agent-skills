# Contributing

## Before editing a Skill

Read:

- `docs/ARCHITECTURE.md`
- `docs/METHODOLOGY.md`
- the target `skills/<name>/SKILL.md`
- `docs/SOURCE-PROVENANCE.md`

## Adding a Skill

Create a directory under `skills/` with a `SKILL.md` containing valid Agent Skills frontmatter. Keep the description specific enough for an agent to decide when the skill applies.

Prefer a small Skill with focused references over a large Skill containing every rule.

## Validation

Run:

Requires Python 3.9+ and PyYAML (`python3 -m pip install pyyaml`).

```bash
bash scripts/run_validation.sh
```

## Routing changes

Any change to trigger or dispatch behavior must update:

- `docs/orchestration/routing-matrix.md`
- `docs/orchestration/agent-routing.md`
- `docs/ARCHITECTURE.md` when the layer map changes
- `tests/scenarios/routing.json`
- `tests/expected/routing-expected.json`
- `tests/scenarios/router-fixtures.json`

The principle is intent specificity: explicit single-purpose requests should route to the narrowest skill available.
