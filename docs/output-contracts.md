# Output Contracts v0.1.0

## Capability
```yaml
strength: 0-100 | unknown
speed: 0-100 | unknown
endurance: 0-100 | unknown
confidence: low|medium|high
```

## Gap
```yaml
gaps:
  strength: number|unknown
  speed: number|unknown
  endurance: number|unknown
priority_order: []
next_step: limitation_screen|adaptation_target|insufficient_data
```

## Limitation
```yaml
limitation:
  type: central|peripheral|threshold_metabolic|fatigue|unclear
  confidence: low|medium|high
```

## Adaptation
```yaml
primary_target: string
secondary_target: string|null
method_handoff: strength|endurance|speed|planning
```

## Transfer
```yaml
current_level: general|specific|hybrid|performance
next_transfer_step: string
hybrid_evidence: []
```

## Pacing
```yaml
action: accelerate|maintain|reduce|recover
reason: string
next_check: string
station_rule_used: string|null
```
