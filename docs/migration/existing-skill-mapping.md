# Existing Skill Mapping v0.4

The existing repository already provides the training engine: demand/individualization, capability periodization, method selection for strength/endurance/speed, load and ordering tools, planning, taper and audit. Its index explicitly states that the 16 atomic skills remain available while four umbrella skills are preferred for routine composite use. The new layer should therefore add intelligence rather than duplicate training mechanics.

## Keep as-is conceptually

- `needs-analysis-individualization` — project demand + individualization.
- `capability-periodization` — coordinates multiple capability curves.
- `strength-method-selector` / `strength-coach` — how to train strength after the target is selected.
- `endurance-method-selector` / `endurance-coach` — how to train endurance after the target is selected.
- `speed-agility-method-selector` / `speed-agility-coach` — how to train speed after the target is selected.
- `periodization-planner`, `microcycle-builder`, `session-plan-builder`, `taper-peak-optimizer` — planning/execution.
- `training-load-order`, `training-variables-load-index`, `training-principles-audit`, `supercompensation-timing` — control/QA.

## New layer

- `athlete-capability-profile` — current athlete state.
- `capability-gap-analysis` — athlete vs demand.
- `performance-limitation-screen` — performance bottleneck hypothesis.
- `adaptation-target-selector` — desired change before method selection.
- `hybrid-transfer-selector` — general → specific → hybrid transfer.
- `state-based-pacing` — dynamic race-state control.

## HYROX layer

- `hyrox-needs-profile` = demand truth.
- `hyrox-week-template` = weekly arrangement.
- `hyrox-plan-audit` = plan quality gate.
- `hyrox-coach` = compound routing only.
