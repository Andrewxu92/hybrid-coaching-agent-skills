# Release 0.1.1

## Recommended GitHub repository name

`hybrid-coaching-agent-skills`

## Repository purpose

A portable collection of Agent Skills that adds an athlete-intelligence and Hybrid/HYROX decision layer without duplicating the existing `skill-for-hirox` training engine.

## What to upload

Upload the entire repository contents. The canonical distributable directory is `skills/`.

## First checks after upload

```bash
bash scripts/run_validation.sh
```

## Suggested GitHub repository settings

Keep `main` as the default branch. Enable Dependabot alerts, secret scanning/push protection, and code scanning as appropriate for the repository; GitHub recommends these baseline security features for public repositories.

## License decision

This package intentionally does not choose an open-source license on behalf of the owner. GitHub defaults to copyright protection when no license is supplied. Add the intended license before inviting reuse or contributions.
