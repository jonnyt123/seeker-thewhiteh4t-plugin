from __future__ import annotations
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PluginQualityTests(unittest.TestCase):
    def run_script(self, relative, *args):
        return subprocess.run([sys.executable, str(ROOT/relative), *map(str,args)], cwd=ROOT, text=True, capture_output=True)

    def test_validator_passes(self):
        p=self.run_script("scripts/validate_repo.py")
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
        self.assertIn("skills=11",p.stdout)

    def test_validator_ignores_untracked_bytecode_cache(self):
        cache=ROOT/"tests"/"__pycache__"
        cache.mkdir(exist_ok=True)
        marker=cache/"quality-regression.pyc"
        marker.write_bytes(b"generated-test-cache")
        try:
            p=self.run_script("scripts/validate_repo.py")
            self.assertEqual(p.returncode,0,p.stdout+p.stderr)
        finally:
            marker.unlink(missing_ok=True)

    def test_manifests_agree(self):
        root=json.loads((ROOT/"plugin.json").read_text())
        compat=json.loads((ROOT/".codex-plugin/plugin.json").read_text())
        self.assertEqual(root["name"],compat["name"])
        self.assertEqual(root["version"],compat["version"])
        self.assertEqual(root["extensions"]["com"]["openai"]["interface"],compat["interface"])

    def test_fixture_is_loopback_only(self):
        text=(ROOT/"skills/seeker-local-lab/scripts/synthetic_fixture.py").read_text()
        self.assertIn("127.0.0.1",text)
        self.assertNotIn("0.0.0.0",text)

    def test_redactor_masks_sensitive_values(self):
        with tempfile.TemporaryDirectory() as td:
            r=Path(td); (r/"logs").mkdir(); (r/"db").mkdir()
            (r/"logs/info.txt").write_text(json.dumps({"ip":"203.0.113.8","browser":"Test"}))
            (r/"logs/result.txt").write_text(json.dumps({"status":"success","lat":"44.5","lon":"-80.9","alt":"200"}))
            p=self.run_script("skills/seeker-artifact-review/scripts/redact_seeker_data.py",r)
            self.assertEqual(p.returncode,0,p.stderr)
            for secret in ("203.0.113.8","44.5","-80.9","200"):
                self.assertNotIn(secret,p.stdout)
            self.assertIn("[REDACTED]",p.stdout)

    def test_static_audit_rejects_non_seeker(self):
        with tempfile.TemporaryDirectory() as td:
            p=self.run_script("skills/seeker-dataflow-audit/scripts/static_audit.py",td)
            self.assertEqual(p.returncode,2)
            self.assertFalse(json.loads(p.stdout)["looks_like_seeker"])

if __name__ == "__main__":
    unittest.main()
