#!/usr/bin/env python3
"""Checks for non-Claude kits: README/LICENSE present, zip in sync, ChatGPT GPT limits respected."""
import pathlib, re, sys, zipfile
root = pathlib.Path(__file__).resolve().parent.parent / "kits"
errors = []
for kit in sorted(p for p in root.iterdir() if p.is_dir()):
    for f in ["README.md", "LICENSE"]:
        if not (kit / f).exists(): errors.append(f"{kit.name}: missing {f}")
    z = root / f"{kit.name}.zip"
    if not z.exists():
        errors.append(f"{kit.name}: missing zip (run scripts/build_kit_zips.py)")
    else:
        zf = zipfile.ZipFile(z)
        for f in kit.rglob("*"):
            if f.is_file() and "evidence" not in f.relative_to(kit).parts and f.name != "preview.png":
                arc = str(f.relative_to(root))
                if arc not in zf.namelist() or zf.read(arc) != f.read_bytes():
                    errors.append(f"{kit.name}: zip out of date for {arc} (run scripts/build_kit_zips.py)")
    ins = kit / "gpt/instructions.md"
    if ins.exists():
        n = len(ins.read_text(encoding="utf-8"))
        if n >= 8000: errors.append(f"{kit.name}: GPT instructions are {n} chars (limit 8,000)")
        d = kit / "gpt/description.txt"
        if d.exists() and len(d.read_text(encoding="utf-8").strip()) > 300:
            errors.append(f"{kit.name}: GPT description over 300 chars")
        s = kit / "gpt/conversation-starters.txt"
        if s.exists() and len([l for l in s.read_text().splitlines() if l.strip()]) > 4:
            errors.append(f"{kit.name}: more than 4 conversation starters")
    for sk in sorted(kit.glob("skills/*/SKILL.md")):
        t = sk.read_text(encoding="utf-8")
        fm = re.match(r"---\n(.*?)\n---\n", t, re.S)
        if not fm:
            errors.append(f"{sk}: missing YAML frontmatter"); continue
        keys = dict(re.findall(r"^(\w+):\s*(.+)$", fm.group(1), re.M))
        if keys.get("name", "").strip() != sk.parent.name:
            errors.append(f"{sk}: frontmatter name should be '{sk.parent.name}'")
        if not keys.get("description", "").strip():
            errors.append(f"{sk}: missing description")
        elif not keys["description"].lower().startswith(("use when", "use this", "when ")):
            errors.append(f"{sk}: description should say WHEN to use the skill")
        body = t[fm.end():].lower()
        if "approv" not in body:
            errors.append(f"{sk}: no approval boundary in the body")
print("\n".join(errors) or "All kit checks passed")
sys.exit(1 if errors else 0)
