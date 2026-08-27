from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
installer = ROOT / "integration/install-overlay.sh"
with tempfile.TemporaryDirectory() as td:
    base = Path(td) / "skill-for-hirox"
    (base / "hyrox-skills/hyrox-coach").mkdir(parents=True)
    (base / "atomic-skills/example").mkdir(parents=True)
    original_training = "ORIGINAL-TRAINING-SKILL"
    (base / "atomic-skills/example/SKILL.md").write_text(original_training, encoding="utf-8")
    original = "---\nname: hyrox-coach\ndescription: original\n---\nORIGINAL\n"
    (base / "hyrox-skills/hyrox-coach/SKILL.md").write_text(original, encoding="utf-8")
    subprocess.run([str(installer), str(base)], check=True, capture_output=True, text=True)
    assert (base / "hybrid-core-skills/hybrid-coach/SKILL.md").exists()
    assert (base / "hybrid-core-skills/athlete-capability-profile/SKILL.md").exists()
    assert (base / "hyrox-skills/hyrox-coach/SKILL.md").read_text(encoding="utf-8") != original
    assert (base / "hyrox-skills/hyrox-coach/SKILL.md.pre-v0.1.0.bak").read_text(encoding="utf-8") == original
    assert (base / "atomic-skills/example/SKILL.md").read_text(encoding="utf-8") == original_training
print("Install smoke test: PASS")
