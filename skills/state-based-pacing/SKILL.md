---
name: state-based-pacing
description: >-
  Select an immediate HYROX pacing action from current HR, pace, breathing, fatigue, target pace, current station, and next demand. Use during racing or race simulations when a static target pace is insufficient, especially when HR is already high before a demanding station.
metadata:
  version: "0.1.0"
  layer: "execution"
---
# State-Based Pacing

## Inputs
- Current HR / HR state
- Current pace / target pace
- Breathing state
- Fatigue / leg state
- Current station
- Next station or demand

## Decision rules
1. If current intensity is approaching/exceeding threshold and later demands remain, prioritize threshold protection.
2. If HR is already high before a demanding station, reduce entry intensity and restore breathing/state before adding intensity.
3. Ski: conservative start → stabilize → progressive pace.
4. Row: slightly conservative start → progressive pace → later adjust by perceived effort.
5. Strength-station exits: use the station-specific short-stride/high-cadence recovery pattern when supported by the station rule.
6. Never convert a single observation into a fixed pace prescription for all athletes.

## Output
```yaml
action: accelerate|maintain|reduce|recover
reason: string
next_check: string
station_rule_used: string | null
```

## Boundary
This is a state-management skill, not a full race-plan generator.
