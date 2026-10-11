"""Tests for the task-tracker scripts. Run: python3 -m unittest discover -s plugins/task-tracker/tests -v"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SAMPLE = ROOT / "tests" / "sample-data"
sys.path.insert(0, str(SCRIPTS))

import apply_changes as ac  # noqa: E402
import render_dashboard as rd  # noqa: E402
import tasks_md as tm  # noqa: E402

TODAY = "2026-10-12"
NOW = "2026-10-12 09:00"


def fenced(data):
    return "Here are my changes:\n```task-tracker-changes\n" + json.dumps(data) + "\n```\nThanks"


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.tasks = self.dir / "TASKS.md"
        shutil.copy(SAMPLE / "TASKS.md", self.tasks)
        self.rev = tm.revision(tm.load(self.tasks))

    def tearDown(self):
        self.tmp.cleanup()

    def doc(self):
        return tm.load(self.tasks)

    def apply(self, ops, **kw):
        data = {"base_revision": kw.pop("base", self.rev), "generated": "2026-10-12T09:00:00Z", "ops": ops}
        data.update(kw.pop("extra", {}))
        return ac.run(self.tasks, json.dumps(data), today=TODAY, now=NOW, **kw)


class TasksMdTest(Base):
    def test_round_trip_is_byte_stable(self):
        for path in (SAMPLE / "TASKS.md", ROOT / "templates" / "TASKS.md"):
            text = path.read_text(encoding="utf-8")
            self.assertEqual(tm.serialise(tm.parse(text)), text, path.name)

    def test_template_matches_script(self):
        self.assertEqual((ROOT / "templates" / "TASKS.md").read_text(encoding="utf-8"), tm.TEMPLATE)

    def test_parse_sections(self):
        doc = self.doc()
        self.assertEqual(len(doc.rows("open")), 6)
        self.assertEqual([r["id"] for r in doc.rows("proposed")], ["T-007"])
        self.assertEqual([r["id"] for r in doc.rows("done")], ["T-008"])
        self.assertEqual(doc.last_sweep, "2026-10-05 08:00")
        self.assertEqual(doc.next_id(), "T-009")
        self.assertEqual(tm.validate(doc), ([], []))

    def test_pipe_escaping_round_trip(self):
        doc = self.doc()
        doc.rows("open")[0]["action"] = "Choose A | B option"
        doc.rows("open")[0]["notes"] = "line one\nline two"
        again = tm.parse(tm.serialise(doc))
        self.assertEqual(again.rows("open")[0]["action"], "Choose A | B option")
        self.assertEqual(again.rows("open")[0]["notes"], "line one line two")
        self.assertIn("Choose A \\| B option", tm.serialise(doc))

    def test_revision_stable_and_sensitive(self):
        text = self.tasks.read_text(encoding="utf-8")
        self.assertEqual(tm.revision(tm.parse(text)), tm.revision(tm.parse(text)))
        self.assertRegex(self.rev, r"^[0-9a-f]{12}$")
        messy = text.replace("| T-002 | Book", "|T-002|   Book").replace("\n", "\r\n")
        self.assertEqual(tm.revision(tm.parse(messy)), self.rev)
        self.assertNotEqual(tm.revision(tm.parse(text.replace("2026-10-14", "2026-10-15"))), self.rev)

    def test_validate_catches_problems(self):
        text = self.tasks.read_text(encoding="utf-8")
        text = text.replace("| T-002 |", "| T-001 |").replace("| Waiting |", "| Someday |")
        text = text.replace("2026-10-23", "2026-02-30")
        errors, _ = tm.validate(tm.parse(text))
        joined = "\n".join(errors)
        self.assertIn("duplicate ID", joined)
        self.assertIn("'Someday' is not allowed", joined)
        self.assertIn("2026-02-30", joined)

    def test_wrong_columns_rejected(self):
        text = self.tasks.read_text(encoding="utf-8").replace("| ID | Action | Owner |", "| ID | Task | Owner |", 1)
        with self.assertRaises(tm.ParseError):
            tm.parse(text)

    def test_init_never_overwrites(self):
        path = self.dir / "new" / "TASKS.md"
        subprocess.run([sys.executable, str(SCRIPTS / "tasks_md.py"), "init", "--tasks", str(path)], check=True,
                       capture_output=True)
        self.assertEqual(path.read_text(encoding="utf-8"), tm.TEMPLATE)
        path.write_text("mine", encoding="utf-8")
        out = subprocess.run([sys.executable, str(SCRIPTS / "tasks_md.py"), "init", "--tasks", str(path)],
                             capture_output=True, text=True)
        self.assertFalse(json.loads(out.stdout)["created"])
        self.assertEqual(path.read_text(encoding="utf-8"), "mine")


class RenderTest(Base):
    def render(self):
        out = self.dir / "dashboard.html"
        subprocess.run([sys.executable, str(SCRIPTS / "render_dashboard.py"), "--tasks", str(self.tasks),
                        "--out", str(out), "--today", TODAY], check=True, capture_output=True)
        return out.read_text(encoding="utf-8")

    def test_tick_boxes_only_for_open_tasks(self):
        page = self.render()
        boxes = re.findall(r'<input type="checkbox" class="tick" data-id="(T-\d+)"', page)
        self.assertEqual(set(boxes), {r["id"] for r in self.doc().rows("open")})
        self.assertEqual(page.count('type="checkbox"'), len(boxes))
        proposed = re.search(r'<section id="panel-proposed".*?</section>', page, re.S).group(0)
        self.assertNotIn("checkbox", proposed)
        self.assertIn('data-act="approve" data-id="T-007"', proposed)
        self.assertIn('data-act="reject" data-id="T-007"', proposed)
        done = re.search(r'<section id="panel-done".*?</section>', page, re.S).group(0)
        self.assertIn("T-008", done)
        self.assertNotIn("checkbox", done)

    def test_self_contained_and_storage_rules(self):
        page = self.render()
        self.assertNotRegex(page, r'<(script|img|iframe)[^>]*\ssrc=')
        self.assertNotRegex(page, r"<link\b")
        self.assertNotRegex(page, r"@import|url\(")
        self.assertNotRegex(page, r"\bfetch\(|XMLHttpRequest")
        for url in re.findall(r"https?://[^\s\"'<]+", page):
            self.assertIn(f'href="{url}"', page, "only task source links may contain URLs")
        self.assertNotIn("localStorage", page)
        self.assertIn("window.storage", page)

    def test_revision_and_kpis_embedded(self):
        page = self.render()
        self.assertIn(f'<meta name="task-tracker-revision" content="{self.rev}">', page)
        data = json.loads(re.search(r'<script type="application/json" id="tt-data">(.*?)</script>', page, re.S).group(1))
        self.assertEqual(data["revision"], self.rev)
        _, _, counts = rd.build(self.doc(), rd.d(TODAY))
        self.assertEqual(counts, {"open": 6, "due_today": 1, "overdue": 1, "due_this_week": 4, "proposed": 1,
                                  "done_this_week": 0})
        self.assertIn("task-tracker-changes", page)
        self.assertIn("tasks-changes.json", page)


class ApplyTest(Base):
    def test_complete(self):
        code, s = self.apply([{"op": "complete", "id": "T-003"}])
        self.assertEqual((code, s["status"]), (0, "applied"))
        kind, _, row = self.doc().find("T-003")
        self.assertEqual((kind, row["status"]), ("done", "Done"))
        self.assertIn("done 2026-10-12", row["notes"])
        self.assertIn("- 2026-10-12 09:00 dashboard: complete T-003", self.tasks.read_text(encoding="utf-8"))
        self.assertEqual(s["new_revision"], tm.revision(self.doc()))

    def test_update(self):
        code, s = self.apply([{"op": "update", "id": "T-002", "fields": {"due": "2026-10-20", "owner": "Priya Nair",
                                                                           "status": "In progress"}}])
        self.assertEqual(code, 0)
        _, _, row = self.doc().find("T-002")
        self.assertEqual((row["due"], row["owner"], row["status"]), ("2026-10-20", "Priya Nair", "In progress"))

    def test_approve(self):
        code, s = self.apply([{"op": "approve", "id": "T-007", "fields": {"owner": "Sam Taylor"}}])
        self.assertEqual(len(s["applied"]), 1)
        kind, _, row = self.doc().find("T-007")
        self.assertEqual((kind, row["status"], row["owner"]), ("open", "Open", "Sam Taylor"))

    def test_reject(self):
        code, s = self.apply([{"op": "reject", "id": "T-007", "reason": "not needed"}])
        self.assertEqual(code, 0)
        self.assertEqual(self.doc().find("T-007")[0], None)
        text = self.tasks.read_text(encoding="utf-8")
        self.assertIn("dashboard: reject T-007 (Organise a team lunch after go-live; not needed)", text)
        self.assertEqual(self.doc().next_id(), "T-009", "a rejected ID is never reused")

    def test_add(self):
        code, s = self.apply([{"op": "add", "fields": {"action": "Order launch cake", "owner": "Sam Taylor",
                                                       "due": "2026-10-30"}},
                              {"op": "add", "fields": {"action": "Check venue", "status": "Proposed"}}])
        self.assertEqual([a["id"] for a in s["applied"]], ["T-009", "T-010"])
        kind, _, row = self.doc().find("T-009")
        self.assertEqual((kind, row["status"], row["raised"]), ("open", "Open", TODAY))
        self.assertEqual(row["source"], "dashboard: added (2026-10-12)")
        self.assertEqual(self.doc().find("T-010")[0], "proposed")

    def test_invalid_ops_skipped(self):
        code, s = self.apply([
            {"op": "complete", "id": "T-999"},
            {"op": "update", "id": "T-002", "fields": {"due": "2026-13-01"}},
            {"op": "update", "id": "T-002", "fields": {"status": "Done"}},
            {"op": "update", "id": "T-002", "fields": {"colour": "red"}},
            {"op": "complete", "id": "T-007"},
            {"op": "complete", "id": "T-008"},
            {"op": "explode", "id": "T-002"},
            {"op": "add", "fields": {"action": "Send revised returns policy wording to legal", "owner": "Priya Nair"}},
            {"op": "complete", "id": "T-004"},
        ])
        self.assertEqual(code, 0)
        self.assertEqual([a["id"] for a in s["applied"]], ["T-004"])
        reasons = [k["reason"] for k in s["skipped"]]
        self.assertEqual(len(reasons), 8)
        for fragment in ("unknown id", "not a real", "use the complete op", "unknown field", "approve it first",
                         "already done", "unknown op", "duplicate of T-001"):
            self.assertTrue(any(fragment in r for r in reasons), fragment)

    def test_revision_mismatch_skips_changed_rows(self):
        before = self.tasks.read_text(encoding="utf-8")
        ops = [{"op": "complete", "id": "T-002", "before": {"section": "open", "due": "2026-10-01"}}]
        for force in (False, True):
            code, s = self.apply(ops, base="0123456789ab", force=force)
            self.assertEqual((code, s["status"]), (0, "nothing to apply"))
            self.assertIn("due changed since the block was made", s["skipped"][0]["reason"])
            self.assertIn("due: '2026-10-01' -> '2026-10-14'", s["changed_since"][0]["change"])
        self.assertEqual(self.tasks.read_text(encoding="utf-8"), before)
        self.assertFalse((self.dir / tm.BACKUP_DIR).exists())

    def test_revision_mismatch_without_snapshot_needs_force(self):
        before = self.tasks.read_text(encoding="utf-8")
        ops = [{"op": "complete", "id": "T-002"}]
        code, s = self.apply(ops, base="0123456789ab")
        self.assertEqual((code, s["status"], s["unguarded_ops"]), (2, "refused", [0]))
        self.assertEqual(self.tasks.read_text(encoding="utf-8"), before)
        code, s = self.apply(ops, base="0123456789ab", force=True)
        self.assertEqual((code, s["status"]), (0, "applied"))
        self.assertEqual(self.doc().find("T-002")[0], "done")

    def test_idempotent(self):
        data = {"base_revision": self.rev, "generated": "x", "ops": [{"op": "complete", "id": "T-003"}]}
        code, _ = ac.run(self.tasks, fenced(data), today=TODAY, now=NOW)
        self.assertEqual(code, 0)
        after = self.tasks.read_text(encoding="utf-8")
        code, s = ac.run(self.tasks, fenced(data), today=TODAY, now=NOW)
        self.assertEqual((code, s["status"]), (2, "refused"))
        self.assertIn("already applied", s["messages"][0])
        code, s = ac.run(self.tasks, fenced(data), force=True, today=TODAY, now=NOW)
        self.assertEqual(code, 2, "--force never re-applies a block that is already in the change log")
        self.assertEqual(self.tasks.read_text(encoding="utf-8"), after)

    def test_backup_and_dry_run(self):
        original = self.tasks.read_text(encoding="utf-8")
        code, s = self.apply([{"op": "complete", "id": "T-003"}], dry_run=True)
        self.assertEqual((s["status"], len(s["would_apply"])), ("dry-run", 1))
        self.assertEqual(self.tasks.read_text(encoding="utf-8"), original)
        code, s = self.apply([{"op": "complete", "id": "T-003"}])
        self.assertEqual(Path(s["backup"]).read_text(encoding="utf-8"), original)
        self.assertEqual(Path(s["backup"]).parent, self.dir / tm.BACKUP_DIR)
        self.assertFalse((self.dir / "TASKS.md.bak").exists())

    def test_fenced_block_from_stdin(self):
        data = {"base_revision": self.rev, "generated": "x", "ops": [{"op": "complete", "id": "T-003"}]}
        out = subprocess.run([sys.executable, str(SCRIPTS / "apply_changes.py"), "--tasks", str(self.tasks),
                              "--changes", "-", "--today", TODAY, "--now", NOW],
                             input=fenced(data), capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stdout + out.stderr)
        self.assertEqual(json.loads(out.stdout)["applied"][0]["id"], "T-003")
        bad = subprocess.run([sys.executable, str(SCRIPTS / "apply_changes.py"), "--tasks", str(self.tasks),
                              "--changes", "-"], input="no block here", capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)

    def test_proposed_only_mode(self):
        code, s = self.apply([{"op": "add", "fields": {"action": "Book auditor", "status": "Open"}},
                              {"op": "complete", "id": "T-003"}],
                             proposed_only=True, extra={"source": "sweep", "last_sweep": "2026-10-12 12:30"})
        self.assertEqual(code, 0)
        doc = self.doc()
        self.assertEqual(doc.find("T-009")[0], "proposed")
        self.assertEqual(doc.find("T-003")[0], "open")
        self.assertEqual(doc.last_sweep, "2026-10-12 12:30")
        self.assertIn("proposed-only", s["skipped"][0]["reason"])
        self.assertIn("sweep: add T-009", self.tasks.read_text(encoding="utf-8"))

    def test_sample_sweep_block(self):
        code, s = ac.run(self.tasks, (SAMPLE / "sweep-changes.json").read_text(encoding="utf-8"), today=TODAY, now=NOW)
        self.assertEqual((code, len(s["applied"]), s["skipped"]), (0, 9, []))
        doc = self.doc()
        self.assertEqual([r["id"] for r in doc.rows("proposed")], ["T-007", "T-013", "T-014"])
        self.assertEqual(doc.find("T-001")[0], "done")
        self.assertEqual(doc.find("T-005")[2]["due"], "2026-10-21")
        self.assertEqual(tm.validate(doc)[0], [])


def page_data(page):
    return json.loads(re.search(r'<script type="application/json" id="tt-data">(.*?)</script>', page, re.S).group(1))


class ReviewFixesTest(Base):
    """One or more tests per finding from the security and robustness review."""

    def set_row(self, tid, **fields):
        doc = self.doc()
        doc.find(tid)[2].update(fields)
        self.tasks.write_text(tm.serialise(doc), encoding="utf-8")

    def snap(self, tid):
        kind, _, row = self.doc().find(tid)
        return {"section": kind, **{f: row[f] for f in tm.FIELDS[1:]}}

    # 1. placeholders inside task text are never expanded
    def test_placeholders_in_task_text_not_expanded(self):
        self.set_row("T-002", action="{{DATA}} <img src=x onerror=alert(1)>", notes="{{JS}} {{CSS}}")
        page, _, _ = rd.build(self.doc(), rd.d(TODAY))
        self.assertNotIn("<img", page)
        self.assertIn("{{DATA}} &lt;img src=x onerror=alert(1)&gt;", page)
        self.assertEqual(page.count("'use strict'"), 1)
        self.assertEqual(page.count(":root{"), 1)
        self.assertEqual(page.count("<script"), 2)
        self.assertEqual(page_data(page)["tasks"]["T-002"]["notes"], "{{JS}} {{CSS}}")

    # 2. the inline JSON cannot end or derail its <script> element
    def test_inline_json_escapes_html_characters(self):
        self.set_row("T-002", action="<!--<script> a & b </script>", notes="line\u2028sep\u2029x")
        page, _, _ = rd.build(self.doc(), rd.d(TODAY))
        raw = re.search(r'id="tt-data">(.*?)</script>', page, re.S).group(1)
        for ch in "<>&\u2028\u2029":
            self.assertNotIn(ch, raw)
        self.assertIn("\\u003c!--\\u003cscript\\u003e a \\u0026 b", raw)
        data = page_data(page)
        self.assertEqual(data["tasks"]["T-002"]["action"], "<!--<script> a & b </script>")
        self.assertEqual(data["tasks"]["T-002"]["notes"], "line\u2028sep\u2029x")

    # 3. the editor only sends fields the user changed
    @unittest.skipUnless(shutil.which("node"), "node is not installed")
    def test_editor_keeps_non_date_due_and_unknown_status(self):
        script = rd.EDIT_DIFF_JS + r"""
var orig = {action: 'Book room', owner: 'TBC', due: 'Fri', status: 'Someday'};
var input = function (o) { var base = {action: 'Book room', owner: '', due: '', dueTouched: false, status: 'Someday'};
  for (var k in o) base[k] = o[k]; return base; };
console.log(JSON.stringify({
  ownerOnly: ttEditDiff(orig, 'Fri', input({owner: 'Sam'})),
  nothing: ttEditDiff(orig, 'Fri', input({})),
  pickedDate: ttEditDiff(orig, 'Fri', input({due: '2026-10-20', dueTouched: true})),
  clearedDate: ttEditDiff(orig, 'Fri', input({dueTouched: true})),
  keepPending: ttEditDiff(orig, '2026-10-21', input({})),
  proposed: ttEditDiff(orig, 'Fri', {action: 'Book room', owner: '', due: '', dueTouched: false})
}));
"""
        out = subprocess.run(["node", "-e", script], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(out.stdout), {
            "ownerOnly": {"owner": "Sam"}, "nothing": None, "pickedDate": {"due": "2026-10-20"},
            "clearedDate": {"due": ""}, "keepPending": {"due": "2026-10-21"}, "proposed": None})
        page, _, _ = rd.build(self.doc(), rd.d(TODAY))
        js = self.dir / "page.js"
        js.write_text(re.search(r"<script>(.*?)</script>", page, re.S).group(1), encoding="utf-8")
        subprocess.run(["node", "--check", str(js)], check=True, capture_output=True)
        self.assertIn("' (keep)'", page)

    # 4. the revision covers the task rows only
    def test_revision_ignores_last_sweep_log_and_prose(self):
        doc = self.doc()
        doc.last_sweep = "2026-10-12 12:30"
        doc.log("2026-10-12 12:30 sweep: nothing new")
        doc.preamble.append("Some new prose.")
        self.assertEqual(tm.revision(doc), self.rev)
        doc.rows("open")[0]["notes"] = "changed"
        self.assertNotEqual(tm.revision(doc), self.rev)

    def test_sweep_does_not_invalidate_dashboard_block(self):
        dashboard = [{"op": "complete", "id": "T-003", "before": self.snap("T-003")},
                     {"op": "update", "id": "T-002", "fields": {"owner": "Priya Nair"}, "before": self.snap("T-002")},
                     {"op": "add", "fields": {"action": "Order launch cake"}}]
        code, s = self.apply([], proposed_only=True, extra={"source": "sweep", "last_sweep": "2026-10-12 12:30"})
        self.assertEqual((code, s["status"], s["new_revision"]), (0, "applied", self.rev))
        code, s = self.apply([{"op": "add", "fields": {"action": "Book auditor"}}], proposed_only=True,
                             extra={"source": "sweep", "last_sweep": "2026-10-12 16:30"})
        self.assertNotEqual(s["new_revision"], self.rev)
        code, s = self.apply(dashboard)
        self.assertEqual((code, s["status"], s["skipped"]), (0, "applied", []))
        self.assertEqual([a["op"] for a in s["applied"]], ["complete", "update", "add"])
        self.assertEqual(self.doc().find("T-003")[0], "done")

    def test_update_then_complete_same_row_in_one_block(self):
        ops = [{"op": "update", "id": "T-003", "fields": {"owner": "Sam Taylor"}, "before": self.snap("T-003")},
               {"op": "complete", "id": "T-003", "before": self.snap("T-003")}]
        code, s = self.apply(ops)
        self.assertEqual((len(s["applied"]), s["skipped"]), (2, []))
        self.assertEqual(self.doc().find("T-003")[2]["owner"], "Sam Taylor")

    # 5. a newer edit to a field is never overwritten, even with --force
    def test_update_skips_fields_changed_since(self):
        before = self.snap("T-002")
        self.set_row("T-002", owner="Jordan Lee")
        op = {"op": "update", "id": "T-002", "fields": {"owner": "Priya Nair", "due": "2026-10-20"}, "before": before}
        edited = self.tasks.read_text(encoding="utf-8")
        for force in (False, True):
            self.tasks.write_text(edited, encoding="utf-8")
            code, s = self.apply([op], base="0123456789ab", force=force)
            self.assertEqual(code, 0)
            self.assertEqual([(k.get("field"), "owner changed" in k["reason"]) for k in s["skipped"]], [("owner", True)])
            _, _, row = self.doc().find("T-002")
            self.assertEqual((row["owner"], row["due"]), ("Jordan Lee", "2026-10-20"))

    # 6. the last 5 versions are kept, with timestamps
    def test_backups_rotate_and_keep_five(self):
        versions = []
        for n in range(7):
            versions.append(self.tasks.read_text(encoding="utf-8"))
            tm.write_atomic(self.tasks, versions[-1].replace("Reference date", f"Ref {n}", 1))
        backups = sorted((self.dir / tm.BACKUP_DIR).glob("TASKS.md.*.bak"))
        self.assertEqual(len(backups), tm.BACKUPS_KEPT)
        self.assertEqual([b.read_text(encoding="utf-8") for b in backups], versions[-5:])
        self.assertRegex(backups[0].name, r"^TASKS\.md\.\d{8}-\d{6}-\d{6}\.bak$")

    def test_last_sweep_only_makes_no_backup(self):
        code, s = self.apply([], extra={"source": "sweep", "last_sweep": "2026-10-12 12:30"})
        self.assertEqual((s["status"], s["backup"]), ("applied", None))

    # 7. symlinks, permissions and fsync
    def test_write_follows_symlink_and_keeps_mode(self):
        real_dir = self.dir / "synced"
        real_dir.mkdir()
        real = real_dir / "TASKS.md"
        shutil.move(self.tasks, real)
        real.chmod(0o640)
        self.tasks.symlink_to(real)
        code, s = self.apply([{"op": "complete", "id": "T-003"}])
        self.assertEqual((code, s["status"]), (0, "applied"))
        self.assertTrue(self.tasks.is_symlink())
        self.assertEqual(tm.load(real).find("T-003")[0], "done")
        self.assertEqual(real.stat().st_mode & 0o777, 0o640)
        self.assertEqual(list(real_dir.glob(".*.tmp")), [])

    # 8. edits made while applying are not lost
    def test_edit_during_apply_is_not_overwritten(self):
        real_apply = ac.apply_ops

        def apply_and_edit(*args, **kwargs):
            result = real_apply(*args, **kwargs)
            self.tasks.write_text(self.tasks.read_text(encoding="utf-8") + "\nhand edit\n", encoding="utf-8")
            return result

        with mock.patch.object(ac, "apply_ops", apply_and_edit):
            code, s = self.apply([{"op": "complete", "id": "T-003"}])
        self.assertEqual((code, s["status"]), (2, "refused"))
        self.assertIn("changed while", s["messages"][-1])
        self.assertTrue(self.tasks.read_text(encoding="utf-8").endswith("hand edit\n"))
        self.assertEqual(self.doc().find("T-003")[0], "open")

    # 9. rows the parser cannot see are reported
    def test_validate_warns_about_unparsed_rows(self):
        text = self.tasks.read_text(encoding="utf-8")
        text = text.replace("| T-006 |", "\n| T-006 |")
        text = text.replace("## Done\n", "T-020 | Loose row | Sam |  | 2026-10-01 |  | Open |  |\n\n## Done ✅\n")
        doc = tm.parse(text)
        self.assertIsNone(doc.find("T-006")[0])
        out = subprocess.run([sys.executable, str(SCRIPTS / "tasks_md.py"), "validate", "--tasks",
                              str(self._write(text))], capture_output=True, text=True)
        warnings = "\n".join(json.loads(out.stdout)["warnings"])
        self.assertEqual(warnings.count("looks like a table row but is not parsed"), 2)
        self.assertIn("'## Done ✅' is not a section the tracker reads", warnings)

    def _write(self, text):
        path = self.dir / "other.md"
        path.write_text(text, encoding="utf-8")
        return path

    # 10. sweeps do not bring back done or rejected tasks
    def test_sweep_dedup_checks_done_rejected_and_unassigned(self):
        self.apply([{"op": "reject", "id": "T-007", "reason": "not needed"}])
        rev = tm.revision(self.doc())
        adds = [{"op": "add", "fields": {"action": "Send kick-off deck to the steering group", "owner": "Alex Morgan"}},
                {"op": "add", "fields": {"action": "Organise a team lunch after go-live", "owner": ""}},
                {"op": "add", "fields": {"action": "Draft FAQ for the help centre", "owner": "Fatima Khan"}}]
        code, s = self.apply(adds, base=rev, proposed_only=True, extra={"source": "sweep"})
        reasons = [k["reason"] for k in s["skipped"]]
        self.assertEqual(s["applied"], [])
        self.assertIn("already done as T-008", reasons[0])
        self.assertIn("T-007, which was rejected", reasons[1])
        self.assertIn("duplicate of T-005", reasons[2])
        self.set_row("T-002", owner="TBC")
        code, s = self.apply([{"op": "add", "fields": {"action": "Book training room for the customer service session"}}],
                             base=tm.revision(self.doc()), extra={"source": "sweep"})
        self.assertIn("duplicate of T-002", s["skipped"][0]["reason"])
        code, s = self.apply([{"op": "add", "fields": {"action": "Send kick-off deck to the steering group",
                                                       "owner": "Alex Morgan"}}], base=tm.revision(self.doc()))
        self.assertEqual(len(s["applied"]), 1, "a dashboard add may repeat a done task on purpose")

    # 11. bad input is reported, never a traceback
    def test_bad_input_reported_in_summary(self):
        code, s = self.apply([{"op": "add", "fields": ["ab"]}, {"op": "add", "fields": "x"},
                              {"op": "complete", "id": "T-003", "date": 123},
                              {"op": "approve", "id": "T-007", "fields": ["owner"]},
                              {"op": "update", "id": "T-002", "fields": {"owner": 5}},
                              {"op": "complete", "id": "T-004", "before": "x"}])
        self.assertEqual((code, s["status"], s["applied"]), (0, "nothing to apply", []))
        reasons = [k["reason"] for k in s["skipped"]]
        self.assertEqual(reasons[:2], ["add needs fields as a JSON object"] * 2)
        self.assertIn("date '123'", reasons[2])
        self.assertEqual(reasons[3], "fields must be a JSON object")
        self.assertEqual(reasons[4], "owner must be text")
        self.assertIn("'before' must be a JSON object", reasons[5])
        block = json.dumps({"base_revision": self.rev, "ops": []})
        self.assertEqual(ac.run(self.tasks, block, today="2026-02-30", now=NOW)[0], 1)
        self.assertEqual(ac.run(self.tasks, block, today=TODAY, now="later")[1]["status"], "error")
        for cmd in ([sys.executable, str(SCRIPTS / "render_dashboard.py"), "--tasks", str(self.tasks), "--today", "soon"],
                    [sys.executable, str(SCRIPTS / "apply_changes.py"), "--tasks", str(self.tasks),
                     "--changes", str(self.dir / "missing.json")]):
            out = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(out.returncode, 1)
            self.assertNotIn("Traceback", out.stderr)
            self.assertIsInstance(json.loads(out.stdout), dict)

    # 12. duplicate IDs block writes and dashboard controls
    def test_duplicate_ids_refused(self):
        text = self.tasks.read_text(encoding="utf-8").replace("| T-007 |", "| T-002 |")
        self.tasks.write_text(text, encoding="utf-8")
        code, s = self.apply([{"op": "complete", "id": "T-003"}], base=tm.revision(self.doc()))
        self.assertEqual((code, s["status"]), (1, "error"))
        self.assertIn("duplicate IDs (T-002)", s["messages"][0])
        self.assertEqual(self.tasks.read_text(encoding="utf-8"), text)
        page, _, _ = rd.build(self.doc(), rd.d(TODAY))
        self.assertNotIn("T-002", page_data(page)["tasks"])
        self.assertNotIn('data-id="T-002" aria-label', page)
        self.assertNotIn('data-act="edit" data-id="T-002"', page)
        self.assertIn("Duplicate ID: fix it in TASKS.md", page)


if __name__ == "__main__":
    unittest.main()


class CoreFieldSnapshotTest(unittest.TestCase):
    def test_tick_survives_source_merge(self):
        import tempfile, shutil, subprocess, json, os
        here = os.path.dirname(os.path.abspath(__file__))
        d = tempfile.mkdtemp()
        try:
            src = os.path.join(here, "sample-data", "TASKS.md"); dst = os.path.join(d, "TASKS.md")
            shutil.copy(src, dst)
            sys.path.insert(0, os.path.join(here, "..", "scripts"))
            import tasks_md as tm
            doc = tm.parse(open(dst, encoding="utf-8").read())
            rev = tm.revision(doc)
            row = doc.find("T-003")[1] if isinstance(doc.find("T-003"), tuple) else doc.find("T-003")
            text = open(dst, encoding="utf-8").read().replace("(2026-10-02) | 2026-10-02 | 2026-10-12", "(2026-10-02); Gmail: extra (2026-10-06) | 2026-10-02 | 2026-10-12", 1)
            open(dst, "w", encoding="utf-8").write(text)
            block = {"base_revision": rev, "ops": [{"op": "complete", "id": "T-003", "before": {"section": "open", "action": "Send updated Q4 budget forecast to finance", "owner": "Alex Morgan", "due": "2026-10-12", "status": "Open", "source": 'Gmail: "Q4 budget forecast" from Mei Chen (2026-10-02)'}}]}
            cf = os.path.join(d, "c.json"); json.dump(block, open(cf, "w"))
            out = subprocess.run([sys.executable, os.path.join(here, "..", "scripts", "apply_changes.py"), "--tasks", dst, "--changes", cf, "--today", "2026-10-12"], capture_output=True, text=True)
            res = json.loads(out.stdout)
            self.assertEqual([a["id"] for a in res["applied"]], ["T-003"], out.stdout)
        finally:
            shutil.rmtree(d)
