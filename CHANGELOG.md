# Changelog

## 0.1.1 — Package hygiene

- Removed the stale nested `integration/patch/patch/` copy of the HYROX boundary patches.
- Normalized leftover `v0.4` labels to the current package version.
- Made local validation run on Python 3.9+ and check skill files instead of only matching fixture keywords.
- Tightened the overlay installer so it requires the upstream `hyrox-skills/` layout used by `skill-for-hirox`.
- Documented that monitoring/adjustment is deferred rather than implied as a missing skill.

## 0.1.0 — Initial standalone package

- Packaged the Hybrid coaching intelligence layer as a standalone GitHub repository.
- Added seven canonical Agent Skills under `skills/`.
- Preserved source methodology and supporting diagrams for provenance.
- Added the upstream `skill-for-hirox` integration overlay and four HYROX boundary patches.
- Added routing, handoff, Hybrid-transfer, pacing, installation, and static validation tests.
- Added GitHub Actions validation.
