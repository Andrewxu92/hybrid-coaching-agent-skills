#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
INSTALLER = ROOT / "integration/install-overlay.sh"
CORE_SKILLS = [
    "hybrid-coach",
    "athlete-capability-profile",
    "capability-gap-analysis",
    "performance-limitation-screen",
    "adaptation-target-selector",
    "hybrid-transfer-selector",
    "state-based-pacing",
]
PATCH_SKILLS = [
    "hyrox-coach",
    "hyrox-needs-profile",
    "hyrox-week-template",
    "hyrox-plan-audit",
]


def write_skill(path, name, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\nname: {0}\ndescription: original\n---\n{1}\n".format(name, body),
        encoding="utf-8",
    )


def main():
    with tempfile.TemporaryDirectory() as td:
        missing = Path(td) / "not-upstream"
        missing.mkdir()
        fail = subprocess.run(
            [str(INSTALLER), str(missing)],
            capture_output=True,
            text=True,
        )
        assert fail.returncode != 0, "installer should reject a tree without hyrox-skills/"

        base = Path(td) / "skill-for-hirox"
        (base / "atomic-skills/example").mkdir(parents=True)
        originals = {}
        for name in PATCH_SKILLS:
            original = "ORIGINAL-{0}".format(name)
            originals[name] = original
            write_skill(base / "hyrox-skills" / name / "SKILL.md", name, original)
        training = "ORIGINAL-TRAINING-SKILL"
        (base / "atomic-skills/example/SKILL.md").write_text(training, encoding="utf-8")

        completed = subprocess.run(
            [str(INSTALLER), str(base)],
            check=True,
            capture_output=True,
            text=True,
        )
        assert "v0.1.1" in completed.stdout

        for name in CORE_SKILLS:
            assert (base / "hybrid-core-skills" / name / "SKILL.md").exists()
        for name in PATCH_SKILLS:
            patched = (base / "hyrox-skills" / name / "SKILL.md").read_text(encoding="utf-8")
            backup = (base / "hyrox-skills" / name / "SKILL.md.pre-v0.1.1.bak").read_text(
                encoding="utf-8"
            )
            assert originals[name] not in patched
            assert originals[name] in backup
        assert (base / "atomic-skills/example/SKILL.md").read_text(encoding="utf-8") == training

    print("Install smoke test: PASS")


if __name__ == "__main__":
    main()
