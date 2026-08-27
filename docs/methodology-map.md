# Hybrid Coaching Methodology Map v0.4

## Locked architecture

- Strength / Speed / Endurance are the three first-level athlete capability dimensions.
- Each capability may be understood through Basic → Specific → Hybrid expression, but these are not required to be separate scored fields.
- Hybrid is not a fourth pillar. It is the expression of multiple demands/capabilities under a shared or carried-over fatigue state.
- Core scores are continuous 0–100; 60 / 80 / 100 are benchmark anchors.
- Capability gap is `Demand - Athlete` in v0.4.

## Minimal coaching loop

```text
Athlete data
  ↓
Athlete capability profile
  ↓
Demand profile
  ↓
Capability gap
  ↓
Limitation screen (only when needed)
  ↓
Adaptation target
  ↓
Existing training-method skill
  ↓
Periodization / planning
  ↓
Hybrid transfer
  ↓
HYROX execution / pacing
  ↓
Monitoring / adjustment
```

## Separation of concerns

| Layer | Primary question | Preferred component |
|---|---|---|
| Athlete | What is the athlete's current state? | `athlete-capability-profile` |
| Demand | What does HYROX require? | `hyrox-needs-profile` |
| Gap | What is missing? | `capability-gap-analysis` |
| Limitation | Why may performance be limited? | `performance-limitation-screen` |
| Adaptation | What should change physiologically/performance-wise? | `adaptation-target-selector` |
| Method | How should that adaptation be trained? | Existing strength/endurance/speed skills |
| Planning | When/how should it be organized? | Existing planning skills |
| Transfer | Has the stimulus become specific/hybrid enough? | `hybrid-transfer-selector` |
| Race state | What should happen now? | `state-based-pacing` |
| QA | Does the plan violate constraints? | `hyrox-plan-audit` |

## Source boundaries

Source-derived rules are separated from inferred operational rules. Inferred rules are implementation defaults and should not be treated as immutable coaching doctrine until validated by observed cases.
