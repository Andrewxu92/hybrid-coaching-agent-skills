# Source Provenance

The repository distinguishes four provenance classes.

## `user-methodology`

Directly derived from the owner-provided coaching Markdown and supporting mind-map images in `sources/user-methodology/`.

## `external-research`

External research used to qualify general implementation choices. These sources do not overwrite or silently replace the owner-provided coaching methodology.

## `inference`

Implementation decisions made to transform prose methodology into callable Agent Skills. Examples include schema shape, output envelopes, routing precedence, and preserving `unknown`/`unclear`.

## `composition`

Behavior that emerges from combining existing skills, such as:

```text
capability-gap-analysis
→ adaptation-target-selector
→ endurance-method-selector
```

## Review rule

When source material does not support a claim, do not present the claim as owner methodology. Keep it labeled as inference or research, or mark it unknown.
