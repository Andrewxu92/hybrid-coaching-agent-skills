---
name: hyrox-coach
description: >-
  HYROX composite training controller. Use only for ambiguous or compound HYROX requests such as complete preparation systems. Delegate explicit capability assessment, capability-gap, limitation screening, adaptation selection, Hybrid transfer, pacing, weekly planning, and plan-audit requests to specific skills.
---
# HYROX Coach — Composite Router

## Dispatch

| Intent | Route |
|---|---|
| Current Strength / Speed / Endurance | `athlete-capability-profile` |
| Athlete vs HYROX demand | `capability-gap-analysis` |
| Why performance is limited | `performance-limitation-screen` |
| What adaptation to target | `adaptation-target-selector` |
| What counts as Hybrid / how to transfer | `hybrid-transfer-selector` |
| Race-state pacing | `state-based-pacing` |
| HYROX demand profile | `hyrox-needs-profile` |
| Weekly HYROX schedule | `hyrox-week-template` |
| Plan audit | `hyrox-plan-audit` |
| Full planning | `periodization-planner` → relevant weekly/session skills |

## Rule
Do not execute downstream skill logic inside this router. It only identifies and sequences the needed skills.
