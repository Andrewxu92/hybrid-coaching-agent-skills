# Integration Guide

## Recommended repository relationship

Use two repositories:

```text
skill-for-hirox
└── mature training engine

hybrid-coaching-agent-skills
└── athlete intelligence + Hybrid/HYROX decision layer
```

This keeps the new decision layer portable and prevents accidental duplication of the upstream training engine.

## Overlay install

```bash
./integration/install-overlay.sh /path/to/skill-for-hirox
```

The overlay:

1. Adds the seven core intelligence skills.
2. Applies the four HYROX boundary patches.
3. Leaves upstream training and nutrition skills intact.
4. Creates one-time backups for the patched HYROX skill files (`*.pre-v0.1.1.bak`).
5. Exits if `hyrox-skills/{hyrox-coach,hyrox-needs-profile,hyrox-week-template,hyrox-plan-audit}` is missing.

Review the generated backup files before committing the integration to the upstream repository.

## Discovery

The canonical distributable root is `skills/`. A compatible client can copy or symlink these directories into its configured skill discovery directory (for example `.agents/skills/`).

## Integration invariants

- Explicitly named atomic skills win over compound routers.
- Known method targets bypass unnecessary diagnosis.
- HYROX demand questions stay in the demand layer.
- Capability-vs-demand comparison belongs to `capability-gap-analysis`.
- Immediate race-state decisions belong to `state-based-pacing`.
