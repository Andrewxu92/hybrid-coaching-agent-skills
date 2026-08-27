# Hybrid Coaching Agent Skills

A lightweight Agent Skills repository for Hybrid / HYROX coaching intelligence.

This repository packages the **decision layer** extracted from a Hybrid coaching methodology and keeps it intentionally separate from the training-engine skills in the existing [`skill-for-hirox`](https://github.com/Andrewxu92/skill-for-hirox) repository.

The goal is simple:

> Turn expert coaching methodology into small, triggerable, composable Agent Skills instead of a single summary document.

## What this repo contains

### Core intelligence skills

| Skill | Responsibility |
|---|---|
| `hybrid-coach` | Compound-request router and clarification gate |
| `athlete-capability-profile` | Build the three-dimensional athlete capability profile |
| `capability-gap-analysis` | Compare athlete capacity with sport/HYROX demand |
| `performance-limitation-screen` | Screen performance-limitation hypotheses without medical diagnosis |
| `adaptation-target-selector` | Select the desired adaptation before choosing a method |
| `hybrid-transfer-selector` | Judge General → Specific → Hybrid → Performance transfer |
| `state-based-pacing` | Make immediate race/simulation pacing decisions from current state |

### Integration layer

The repo also contains boundary patches for the existing `skill-for-hirox` HYROX umbrella skills. These patches are designed to add the intelligence layer without replacing the existing training engine.

### Source and provenance

The original user-provided Markdown and supporting mind-map images are preserved under `sources/user-methodology/`. Derived rules are separated from external research and implementation inferences.

## Coaching model

```text
Athlete
  ↓
Strength / Speed / Endurance
  ↓
Capability Gap
  ↓
Performance Limitation (only when decision-relevant)
  ↓
Adaptation Target
  ↓
Existing Training Engine
  ↓
Hybrid Transfer
  ↓
HYROX Execution / Pacing
  ↓
Monitoring / Adjustment
```

### Locked simplifications

- `Strength`, `Speed`, and `Endurance` are the first-level athlete capability dimensions.
- `Hybrid` is not a fourth capability. It is a state-coupled expression of multiple meaningful demands/capabilities.
- Core capability scores are continuous `0–100` values.
- `60 / 80 / 100` are benchmark anchors, not hard population labels.
- Capability gap is `Demand - Athlete`.
- `Basic / Specific / Hybrid` are development/transfer layers; they do not all need independent scores.

## Repository layout

```text
skills/                         # Agent Skills source of truth
  <skill-name>/SKILL.md
  <skill-name>/references/...   # Optional progressive-disclosure references

docs/                           # Human-facing methodology and architecture docs
integration/                    # Overlay installer + upstream boundary patches
sources/user-methodology/        # Preserved source material supplied by the owner
tests/                          # Routing, contract and scenario tests
scripts/                        # Repository validation helpers
.github/workflows/              # CI validation
```

The `skills/` layout follows the Agent Skills format: each skill is a directory with a required `SKILL.md`; `name` and `description` are required frontmatter fields, names are lowercase kebab-case, and longer detail belongs in `references/` or other optional resources. See the current specification for exact constraints. 

## Install as a portable skill collection

Copy or symlink the contents of `skills/` into the skill discovery directory used by your agent client. For clients that use `.agents/skills/`, the resulting structure is:

```text
.agents/skills/
  athlete-capability-profile/
    SKILL.md
  capability-gap-analysis/
    SKILL.md
  ...
```

The exact discovery path is client-specific.

## Integrate with `skill-for-hirox`

This repo is intentionally an overlay rather than a frozen mirror of the upstream training engine:

```bash
./integration/install-overlay.sh /path/to/skill-for-hirox
```

The installer adds the six intelligence skills plus the `hybrid-coach` router, patches the four HYROX boundary skills, and preserves the upstream training and nutrition skills.

## Validate locally

```bash
python scripts/validate_skills.py
python tests/scripts/router-regression.py
python tests/scripts/semantic-acceptance.py
python tests/scripts/install-smoke.py
```

The local checks are deterministic structure/contract checks. They do not pretend to be a substitute for evaluating the skills inside a real Skills-compatible agent client.

## Methodology vs inference

This repository intentionally distinguishes:

- `user-methodology` — directly derived from supplied coaching material.
- `external-research` — outside evidence used to qualify, not overwrite, the methodology.
- `inference` — implementation choices required to make the methodology callable.
- `composition` — behavior produced by combining existing skills.

Do not silently turn an inference into a coaching doctrine.

## Safety / scope

These skills are for performance coaching and training decision support. They are not a medical, rehabilitation, or diagnostic system. `performance-limitation-screen` explicitly produces hypotheses about performance patterns and must not infer disease or pathology.

## Upstream relationship

The existing `skill-for-hirox` repository remains the mature training engine. This repository adds a small intelligence layer on top instead of cloning it.

## License

No open-source license is asserted in this repository. Add the intended license before distributing the project publicly.
