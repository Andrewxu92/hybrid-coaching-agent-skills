---
name: athlete-capability-profile
description: >-
  Build a lightweight athlete profile across Strength, Speed, and Endurance using validated scores or assessment evidence. Use when the user asks "我的力量/速度/耐力怎么样", needs a current capability summary, or wants an input for gap analysis or HYROX planning. Do not invent precise scores from vague self-description.
metadata:
  version: "0.1.0"
  layer: "athlete-intelligence"
---
# Athlete Capability Profile

## Purpose
Create the smallest reliable representation of current athlete capacity.

## Use when
- Current Strength / Speed / Endurance needs to be summarized.
- Existing assessment results need to be normalized into the coaching model.
- Another skill needs an athlete capability input.

## Inputs
- Validated capability scores or assessment results.
- Performance evidence.
- Optional sub-capability evidence.

## Procedure
1. Prefer previously validated data.
2. Produce three continuous 0–100 core scores when evidence supports them.
3. Treat 60 / 80 / 100 as benchmark anchors, not hard population labels.
4. Add Basic / Specific / Hybrid detail only when evidence exists.
5. Mark missing data `unknown`; do not infer precise scores.

## Output
```yaml
strength: 0-100 | unknown
speed: 0-100 | unknown
endurance: 0-100 | unknown
confidence: low|medium|high
optional_detail: {}
```

## Handoff
- Usually → `capability-gap-analysis`
- If a known weakness has conflicting response evidence → `performance-limitation-screen`

## Boundaries
- Does not diagnose medical conditions.
- Does not create scores from narrative impressions alone.
