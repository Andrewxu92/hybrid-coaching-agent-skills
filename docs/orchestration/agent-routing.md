# Agent Routing v0.4

## Precedence

1. Explicitly requested named skill wins.
2. Specific assessment/diagnostic intent beats generic planning.
3. HYROX-specific demand questions use `hyrox-needs-profile`.
4. Planning is downstream from a sufficiently clear training target.
5. Existing atomic skills remain preferred over umbrella skills when a single atomic intent is explicit.

## Core route

```text
athlete-capability-profile
        ↓
capability-gap-analysis
        ↓
performance-limitation-screen (only when decision-relevant)
        ↓
adaptation-target-selector
        ↓
existing method / periodization / planning skills
        ↓
hybrid-transfer-selector (when transfer matters)
        ↓
HYROX execution / state-based-pacing
        ↓
monitor / audit / adjust
```

## HYROX compound entry

`hyrox-coach` may remain the compound entry point, but it should delegate rather than answer capability or diagnostic questions itself.

## Do not chain everything automatically

A request for a single clear answer should activate only the minimum relevant skill. Full-chain routing is for compound coaching requests or when downstream information is actually required.
