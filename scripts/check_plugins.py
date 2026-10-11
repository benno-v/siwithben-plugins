#!/usr/bin/env python3
"""Lightweight checks: JSON manifests parse, names match, versions are semver, skills have frontmatter."""
import json, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
errors = []
m = json.loads((root / ".claude-plugin/marketplace.json").read_text())
for e in m["plugins"]:
    d = root / e["source"]
    pj = d / ".claude-plugin/plugin.json"
    if not pj.exists():
        errors.append(f"{e['name']}: missing {pj}"); continue
    p = json.loads(pj.read_text())
    if p.get("name") != e["name"]:
        errors.append(f"{e['name']}: name differs from plugin.json ({p.get('name')})")
    if not re.fullmatch(r"\d+\.\d+\.\d+", p.get("version", "")):
        errors.append(f"{e['name']}: version is not semver")
    for f in ["README.md", "LICENSE"]:
        if not (d / f).exists(): errors.append(f"{e['name']}: missing {f}")
    skills = list((d / "skills").glob("*/SKILL.md"))
    if not skills: errors.append(f"{e['name']}: no skills")
    for s in skills:
        t = s.read_text()
        fm = re.match(r"---\n(.*?)\n---\n", t, re.S)
        if not fm or "name:" not in fm.group(1) or "description:" not in fm.group(1):
            errors.append(f"{s}: missing name/description frontmatter")
        elif not re.search(rf"^name:\s*{s.parent.name}\s*$", fm.group(1), re.M):
            errors.append(f"{s}: frontmatter name should be '{s.parent.name}'")
print("\n".join(errors) or "All plugin checks passed")
sys.exit(1 if errors else 0)
