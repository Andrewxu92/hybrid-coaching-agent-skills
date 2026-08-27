---
name: hybrid-transfer-selector
description: >-
  Judge whether a training stimulus is general, specific, hybrid, or performance-oriented based on meaningful task interaction and state carry-over, then choose the next transfer step. Use for questions such as "这个训练算 Hybrid 吗/什么时候加入专项混合训练". Hybrid is not a fourth scored capability and not simply two exercises combined.
metadata:
  version: "0.1.0"
  layer: "transfer"
---
# Hybrid Transfer Selector

## Core definition
A Hybrid task combines multiple meaningful demands with limited or continuous recovery such that the earlier demand changes the subsequent performance state.

## Transfer ladder
`GENERAL → SPECIFIC → HYBRID → PERFORMANCE`

## Procedure
1. Identify the primary adaptation being trained.
2. Identify the sport-relevant task or constraint.
3. Check whether a prior task materially carries fatigue/state into the next task.
4. If no carry-over exists, keep the session general or specific rather than labeling it Hybrid.
5. If carry-over exists, identify the minimum additional complexity needed for transfer.

## Output
```yaml
current_level: general|specific|hybrid|performance
transfer_gap: string
next_transfer_step: string
hybrid_evidence: []
```

## Boundary
Hybrid is a transfer context, not a fourth scored capability and not a synonym for "two exercises in one workout."
