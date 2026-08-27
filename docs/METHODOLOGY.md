# Methodology

## What was extracted

The methodology is represented as a chain of:

```text
Capability
  ↓
Mechanism
  ↓
Training Stimulus
  ↓
Adaptation
  ↓
Transfer
  ↓
Performance
```

The source material also contains HYROX-specific state-management rules:

```text
Current state
+ target
+ next demand
→ pacing / transition action
```

## Three capability pillars

### Strength

```text
Basic Strength
Specific Strength
Metabolic / Hybrid Strength
```

### Speed

```text
Technical Speed
MAS-related capacity
Hybrid Speed
```

### Endurance

```text
Basic Endurance
Threshold Endurance
Hybrid Endurance
```

These are model layers. The athlete-facing profile remains three-dimensional unless deeper assessment evidence is available.

## General → Specific → Hybrid → Performance

A stimulus becomes more transfer-specific when task constraints, sport demands and state carry-over increasingly shape the next action.

The project uses a conservative Hybrid definition:

> Multiple meaningful demands/tasks are combined with limited or continuous recovery, and the earlier demand materially changes the subsequent performance state.

This prevents “two exercises in one session” from being treated as Hybrid automatically.

## Performance limitation screen

The supplied methodology suggests useful observable patterns such as:

- high HR with limited pace;
- breathing not highly stressed while the legs cannot express pace;
- performance degradation after accumulated work.

These are treated as **performance hypotheses**, not medical diagnoses.

## HYROX state-management principles

The supplied coaching material emphasizes:

- protecting threshold capacity early rather than chasing short-term speed;
- adjusting entry intensity when HR is already high before demanding stations;
- progressive starts on aerobic-machine stations;
- station-specific execution and post-station running transitions;
- pacing by current state rather than by a fixed pace target alone.

Detailed station rules are kept inside the `state-based-pacing` reference so they are loaded only when required.

## What is deliberately not hard-coded

Where the source does not provide a universal threshold, load, volume, recovery time, or population cutoff, the system leaves the value open rather than inventing precision.
