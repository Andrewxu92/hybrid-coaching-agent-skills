---
name: hyrox-week-template
description: >-
  Arrange already-selected HYROX training priorities into a weekly structure. Use when the athlete's primary training targets are already known and the request is specifically about weekly organization rather than diagnosis or target selection.
---
# HYROX Weekly Template

## Input contract
Require or infer only what is already available:
- primary training priority
- available training frequency
- major recovery constraints
- competition phase when known

## Procedure
1. Preserve the selected training priority.
2. Apply existing fatigue-order and periodization rules.
3. Apply existing HYROX weekly constraints.
4. Return a weekly arrangement, not a new diagnosis.

## Boundary
Do not independently decide the athlete's main limitation when `capability-gap-analysis` can do so upstream.
