---
name: adaptation-target-selector
description: >-
  Select the smallest useful desired training adaptation from a capability gap and, when available, a performance-limitation hypothesis. Use when the user asks "下一步提高什么/训练目标是什么". Hand off to existing strength, endurance, speed, periodization, or session skills for detailed programming.
metadata:
  version: "0.1.1"
  layer: "decision"
---
# Adaptation Target Selector

## Purpose
Choose what should change before deciding how to train it.

## Decision map
- Strength gap → basic strength / specific strength / metabolic-hybrid strength as supported by evidence.
- Speed gap → technical efficiency / MAS-related capacity / hybrid speed as supported by evidence.
- Endurance gap → aerobic base / threshold capacity / high-intensity or hybrid endurance as supported by evidence.
- Unknown mechanism → choose a conservative target and recommend the minimum useful assessment.

## Procedure
1. Read ranked capability gaps.
2. Read limitation screen when available.
3. Choose one primary adaptation target.
4. Add at most one secondary target if required for transfer or risk control.
5. Hand off to the existing mature method selector.

## Output
```yaml
primary_target: string
secondary_target: string | null
rationale: string
method_handoff: strength|endurance|speed|planning
```

## Boundary
This skill selects an adaptation target. It does not generate the detailed exercise prescription when an existing method skill can do it better.
