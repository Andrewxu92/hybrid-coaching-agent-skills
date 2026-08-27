---
name: hyrox-needs-profile
description: >-
  Describe the demands of HYROX and classify station requirements. Use when the user asks what HYROX requires, which abilities a station emphasizes, or how to build a sport-demand profile. Do not use this skill to diagnose an individual athlete.
---
# HYROX Demand Profile

## Scope
Describe the sport-side demand model. The official singles rulebook specifies eight repetitions of 1 km run + one workout station in sequence. 

## Output
- Event structure
- Station/task demands
- Dominant capability demands
- Relevant transition demands

## Boundary
This skill does not calculate athlete gaps. When athlete data exist, hand off to `athlete-capability-profile` and `capability-gap-analysis`.
