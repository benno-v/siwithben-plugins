"""Tests for init_pm_project.py. Run: python3 -m unittest discover -s plugins/claude-setup-kit/tests"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "pm-project-init" / "scripts" / "init_pm_project.py"

FOLDERS = [
    "01-initiation", "02-planning", "03-execution", "04-monitoring-and-control",
    "05-closure", "context", "inputs", "outputs", "archive",
]
FILES = [
    "CLAUDE.md", "context/project-brief.md", "context/stakeholders.md",
    "context/glossary.md", "context/decisions-log.md", "inputs/README.md", "outputs/README.md",
]


def run(root, *extra):
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root), "--json", *extra],
        capture_output=True, text=True,
    )
    return result.returncode, json.loads(result.stdout)


def snapshot(path):
    return sorted(str(p.relative_to(path)) for p in Path(path).rglob("*"))


class InitPmProjectTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_structure(self):
        code, report = run(self.root, "--name", "Website Relaunch 2027", "--sponsor", "Chief Digital Officer",
                           "--stakeholders", "Ana Lopez (Finance lead); IT steering group")
        self.assertEqual(code, 0)
        project = self.root / "website-relaunch-2027"
        self.assertEqual(report["project_dir"], str(project.resolve()))
        for folder in FOLDERS:
            self.assertTrue((project / folder).is_dir(), folder)
        for rel in FILES:
            self.assertTrue((project / rel).is_file(), rel)
            self.assertIn(rel, report["created"])
        self.assertEqual(report["skipped"], [])
        claude_md = (project / "CLAUDE.md").read_text()
        self.assertIn("# Website Relaunch 2027", claude_md)
        self.assertIn("Sponsor: Chief Digital Officer", claude_md)
        self.assertIn("End date", (project / "context/project-brief.md").read_text())
        self.assertIn("[to confirm]", claude_md)
        self.assertNotIn("Where this goes", claude_md)
        self.assertIn("| Ana Lopez | Finance lead |", (project / "context/stakeholders.md").read_text())

    def test_idempotent(self):
        run(self.root, "--name", "Alpha")
        before = snapshot(self.root)
        code, report = run(self.root, "--name", "Alpha")
        self.assertEqual(code, 0)
        self.assertEqual(report["created"], [])
        self.assertEqual(sorted(report["skipped"]), sorted(FILES))
        self.assertEqual(len(report["reused"]), len(FOLDERS) + 1)
        self.assertEqual(snapshot(self.root), before)

    def test_no_overwrite(self):
        project = self.root / "alpha"
        project.mkdir()
        custom = "# My own CLAUDE.md\nKeep this.\n"
        (project / "CLAUDE.md").write_text(custom)
        code, report = run(self.root, "--name", "Alpha", "--sponsor", "Someone")
        self.assertEqual(code, 0)
        self.assertEqual((project / "CLAUDE.md").read_text(), custom)
        self.assertIn("CLAUDE.md", report["skipped"])
        self.assertNotIn("CLAUDE.md", report["created"])
        self.assertIn("alpha/", report["reused"])

    def test_dry_run_writes_nothing(self):
        code, report = run(self.root, "--name", "Alpha", "--dry-run")
        self.assertEqual(code, 0)
        self.assertTrue(report["dry_run"])
        self.assertIn("CLAUDE.md", report["created"])
        self.assertEqual(snapshot(self.root), [])

    def test_rejects_unsafe_names(self):
        for name in ["../escape", "a/b", "..", "!!!", "   "]:
            code, report = run(self.root, "--name", name)
            self.assertNotEqual(code, 0, name)
            self.assertIn("error", report)
        self.assertEqual(snapshot(self.root), [])
        self.assertFalse((self.root.parent / "escape").exists())


if __name__ == "__main__":
    unittest.main()
