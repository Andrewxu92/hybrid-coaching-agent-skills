---
name: performance-limitation-screen
description: >-
  Screen observable performance-limitation patterns using HR, pace, breathing, fatigue, RPE, and task response. Use when a meaningful capability gap exists but the useful training target depends on understanding whether the pattern is central, peripheral, threshold/metabolic, fatigue-related, or unclear. This is a performance hypothesis, not a medical diagnosis.
metadata:
  version: "0.1.1"
  layer: "diagnostic-screen"
---
# Performance Limitation Screen

## Purpose
Provide a cautious performance hypothesis, not a medical diagnosis.

## Patterns
| Observed pattern | Working hypothesis |
|---|---|
| HR high + pace limited | central limitation suspected |
| Breathing not highly stressed + legs cannot express pace | peripheral limitation suspected |
| Intensity reaches threshold early / pace becomes unsustainable | threshold or metabolic limitation suspected |
| Response degrades primarily after accumulated work | fatigue-related limitation suspected |
| Conflicting or insufficient evidence | unclear |

## Procedure
1. Compare HR, pace, breathing, RPE and task outcome together.
2. Use pattern matching only as a hypothesis.
3. Record the evidence supporting and contradicting the hypothesis.
4. If evidence is insufficient, return `unclear`.
5. Recommend the smallest next assessment that could change the training decision.

## Output
```yaml
limitation:
  type: central|peripheral|threshold_metabolic|fatigue|unclear
  confidence: low|medium|high
evidence_for: []
evidence_against: []
next_assessment: string | null
```

## Boundaries
- Not medical diagnosis.
- Do not infer disease, organ dysfunction, or pathology.
