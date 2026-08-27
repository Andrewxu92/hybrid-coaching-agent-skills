# Architecture

## Design goal

The system separates **athlete intelligence** from the existing **training engine**.

```text
ATHLETE
  ↓
Athlete Capability Profile
  ↓
Capability Gap
  ↓
Performance Limitation Screen (only when useful)
  ↓
Adaptation Target
  ↓
Existing Training Method / Periodization Skills
  ↓
Hybrid Transfer
  ↓
HYROX Execution / State-Based Pacing
  ↓
Monitoring / Adjustment
```

## Layer responsibilities

| Layer | Question | Owner |
|---|---|---|
| Athlete | What is the athlete's current capability? | `athlete-capability-profile` |
| Demand | What does the sport/event require? | upstream `hyrox-needs-profile` |
| Gap | What is missing relative to demand? | `capability-gap-analysis` |
| Limitation | What performance pattern may explain the gap? | `performance-limitation-screen` |
| Adaptation | What should change? | `adaptation-target-selector` |
| Method | How should it be trained? | upstream method selectors |
| Planning | When/how should it be organized? | upstream periodization/planning skills |
| Transfer | How specific/hybrid is the training stimulus? | `hybrid-transfer-selector` |
| Race state | What should happen now? | `state-based-pacing` |
| Compound routing | Which path is required? | `hybrid-coach` / upstream `hyrox-coach` |

## Capability ontology

The first-level athlete capability model is intentionally small:

```text
Strength
Speed
Endurance
```

Each can be understood through a development/transfer ladder without requiring independent scores for every node:

```text
Basic → Specific → Hybrid
```

`Hybrid` is not a fourth pillar. It is a state-coupled expression of multiple meaningful demands/capabilities.

## Score model

Core capability scores are continuous `0–100`. The project uses `60 / 80 / 100` as benchmark anchors rather than hard population bands.

Capability gap uses the simple first-version rule:

```text
gap = demand - athlete
```

No hidden weighting is introduced by the intelligence layer.

## Routing principle

Use the narrowest correct skill:

1. Explicitly named skill.
2. Explicit single-purpose intent.
3. Assessment/diagnostic intent.
4. Compound planning only when necessary.

Do not run the entire coaching chain for a question that needs one answer.

## Upstream integration

This repository does not clone the upstream `skill-for-hirox` training engine. The integration overlay adds the intelligence layer and proposes boundary patches for the upstream HYROX umbrella skills.
