#!/usr/bin/env python3
"""Rebuild kits/<kit>.zip from kits/<kit>/ (excludes tests/evidence and preview.png). Deterministic timestamps."""
import os, pathlib, zipfile
root = pathlib.Path(__file__).resolve().parent.parent / "kits"
for kit in sorted(p for p in root.iterdir() if p.is_dir()):
    files = sorted(f for f in kit.rglob("*") if f.is_file()
                   and "evidence" not in f.relative_to(kit).parts and f.name != "preview.png")
    with zipfile.ZipFile(root / f"{kit.name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            info = zipfile.ZipInfo(str(f.relative_to(root)), (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, f.read_bytes())
    print(f"built kits/{kit.name}.zip ({len(files)} files)")
