# Integration Overlay v0.1.1

This package is an overlay for the existing `skill-for-hirox` repository. It intentionally does not replace the existing training engine.

Apply the new core skills and routing rules, then patch the HYROX umbrella skills so compound requests can delegate to the new intelligence layer.

The external repository is not bundled here; patch files are proposed replacements.

## Required upstream layout

The installer expects this `skill-for-hirox` tree:

```text
hyrox-skills/hyrox-coach/SKILL.md
hyrox-skills/hyrox-needs-profile/SKILL.md
hyrox-skills/hyrox-week-template/SKILL.md
hyrox-skills/hyrox-plan-audit/SKILL.md
```

It copies `skills/` into `hybrid-core-skills/` and replaces only those four boundary files. Training, periodization, and nutrition skills stay untouched. The installer exits if the upstream directories are missing.
