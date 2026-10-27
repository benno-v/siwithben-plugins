"""Structure and content checks for the grok-bot-personal-assistant kit. Standard library only."""
import pathlib
import re
import unittest

KIT = pathlib.Path(__file__).resolve().parent.parent
SUB_BOTS = ["fitness-coach", "food-bot", "money-bot", "inbox-bot", "research-bot", "personal-shopper"]
JOB_TITLES = [
    "Workout planning", "Session logging", "Daily session plan", "Weekly grocery basket",
    "Budget check-in", "Morning and weekend summaries", "Calendar and reminders",
    "Inbox triage and draft replies", "Research", "Content ideas and trends",
    "Meeting notes to actions", "Personal shopper",
]
PUBLIC_FILES = [p for p in KIT.rglob("*.md") if "evidence" not in p.relative_to(KIT).parts]


def text(rel):
    return (KIT / rel).read_text(encoding="utf-8")


def code_blocks(s):
    return re.findall(r"```\n(.*?)```", s, re.S)


class TestStructure(unittest.TestCase):
    def test_required_files(self):
        for rel in ["README.md", "LICENSE", "preview.png", "prompts/00-primary-bot-setup.md",
                    "prompts/12-jobs.md", "prompts/sub-bots/README.md",
                    "routines/routine-templates.md", "templates/approval-rules.md",
                    "checklists/connector-setup-checklist.md"]:
            self.assertTrue((KIT / rel).exists(), rel)

    def test_six_sub_bots_each_with_a_prompt(self):
        for name in SUB_BOTS:
            body = text(f"prompts/sub-bots/{name}.md")
            self.assertTrue(code_blocks(body), f"{name}: no paste-ready block")
            self.assertIn("Report to my primary assistant", body, name)
            self.assertIn("Before you start, ask me", body, name)

    def test_twelve_jobs_each_with_a_prompt(self):
        body = text("prompts/12-jobs.md")
        headings = re.findall(r"^## (\d+)\. (.+)$", body, re.M)
        self.assertEqual([int(n) for n, _ in headings], list(range(1, 13)))
        self.assertEqual([t for _, t in headings], JOB_TITLES)
        sections = re.split(r"^## \d+\. ", body, flags=re.M)[1:]
        for title, sec in zip(JOB_TITLES, sections):
            self.assertEqual(len(code_blocks(sec)), 1, f"{title}: expected one prompt block")

    def test_routine_templates(self):
        body = text("routines/routine-templates.md")
        routines = re.findall(r"^### (R\d+)\. ", body, re.M)
        self.assertGreaterEqual(len(routines), 11)
        sections = re.split(r"^### R\d+\. ", body, flags=re.M)[1:]
        for sec in sections[:11]:
            title = sec.splitlines()[0]
            m = re.search(r"Cron: `([^`]+)`", sec)
            self.assertTrue(m, f"{title}: no cron line")
            fields = m.group(1).split()
            self.assertEqual(len(fields), 5, f"{title}: cron must have 5 fields")
            block = code_blocks(sec)
            self.assertEqual(len(block), 1, title)
            self.assertIn("next run time", block[0], title)
            self.assertIn("time zone", block[0], title)
            self.assertRegex(block[0], r"(?i)\b(never|don't|do not)\b", f"{title}: no boundary")

    def test_approval_template(self):
        body = text("templates/approval-rules.md")
        for level in ["Runs alone", "Draft first", "Needs my yes", "Never"]:
            self.assertIn(level, body)
        self.assertIn("decide your own approval rules", body)
        self.assertTrue(code_blocks(body))

    def test_checklist_covers_connectors(self):
        body = text("checklists/connector-setup-checklist.md")
        for heading in ["Gmail", "Google Calendar", "Google Drive", "Notion", "Budgeting app", "own computer"]:
            self.assertIn(heading, body)
        self.assertGreaterEqual(body.count("- [ ]"), 25)


class TestContent(unittest.TestCase):
    def test_every_prompt_file_has_an_approval_boundary(self):
        for rel in ["prompts/00-primary-bot-setup.md", "prompts/12-jobs.md",
                    "routines/routine-templates.md", "templates/approval-rules.md"] + \
                   [f"prompts/sub-bots/{n}.md" for n in SUB_BOTS]:
            self.assertIn("approv", text(rel).lower(), rel + " mentions no approval boundary")

    def test_nothing_private(self):
        patterns = {
            "email address": r"[\w.+-]+@[\w-]+\.[\w.-]+",
            "phone number": r"\+?\d[\d\s().-]{8,}\d",
            "API key or token": r"(sk-[A-Za-z0-9]{10,}|gh[pous]_[A-Za-z0-9]{10,}|xai-[A-Za-z0-9]{10,})",
            "IBAN-like": r"\b[A-Z]{2}\d{2}[A-Z0-9]{10,}\b",
        }
        for p in PUBLIC_FILES:
            body = p.read_text(encoding="utf-8")
            for label, pat in patterns.items():
                self.assertIsNone(re.search(pat, body), f"{p.relative_to(KIT)}: looks like a {label}")

    def test_si_branding(self):
        for p in PUBLIC_FILES:
            body = p.read_text(encoding="utf-8")
            self.assertIsNone(re.search(r"\bAI\b", body), f"{p.relative_to(KIT)}: use SI, not AI")

    def test_no_substack_or_unverified_links(self):
        for p in PUBLIC_FILES:
            self.assertNotIn("substack", p.read_text(encoding="utf-8").lower(), p.name)

    def test_video_links_use_the_right_id_and_timestamps_match_labels(self):
        for p in PUBLIC_FILES:
            body = p.read_text(encoding="utf-8")
            self.assertNotIn("youtube.com/watch?v=O5bHcw", body)
            for m in re.finditer(r"\[(\d\d):(\d\d)\]\(https://youtu\.be/UBX3qXaFlgw\?t=(\d+)\)", body):
                self.assertEqual(int(m[1]) * 60 + int(m[2]), int(m[3]), f"{p.name}: {m[0]}")

    def test_relative_links_resolve(self):
        for p in PUBLIC_FILES:
            body = p.read_text(encoding="utf-8")
            for target in re.findall(r"\]\((?!https?://|#|mailto:)([^)\s#]+)", body):
                resolved = (p.parent / target).resolve()
                if resolved.name.endswith(".zip"):
                    continue  # built by scripts/build_kit_zips.py
                self.assertTrue(resolved.exists(), f"{p.relative_to(KIT)}: broken link {target}")


if __name__ == "__main__":
    unittest.main()
