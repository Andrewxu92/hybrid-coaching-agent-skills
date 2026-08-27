---
name: capability-gap-analysis
description: >-
  Compare an athlete's Strength, Speed, and Endurance profile with a known sport or HYROX demand profile and rank simple capability gaps. Use when the user asks "我最缺什么/短板是什么/距离目标差多少". Use `Gap = Demand - Athlete`; do not add weighting unless explicitly provided.
metadata:
  version: "0.1.1"
  layer: "athlete-intelligence"
---
# Capability Gap Analysis

## Purpose
Identify the simplest useful difference between current athlete capacity and required demand.

## Procedure
1. Obtain or route to the project demand profile.
2. Obtain the athlete capability profile.
3. For each available core dimension calculate `gap = demand - athlete`.
4. Rank positive gaps from largest to smallest.
5. Treat near-zero gaps as currently sufficient and negative gaps as non-priority capacity.
6. Do not add weighting factors unless the user or demand profile explicitly provides them.

## Output
```yaml
gaps:
  strength: number | unknown
  speed: number | unknown
  endurance: number | unknown
priority_order: []
confidence: low|medium|high
next_step: limitation_screen|adaptation_target|insufficient_data
```

## Decision gate
Use `performance-limitation-screen` when the gap is meaningful but the limiting mechanism is unclear and identifying it would change the intervention. Otherwise continue directly to `adaptation-target-selector`.

## Boundaries
- Gap is not a diagnosis.
- Gap is not an instruction to maximize the lowest score.
- Do not substitute generic population norms for the explicit demand profile.
