#!/usr/bin/env python3
from pathlib import Path
import json, re, sys, xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
errors = []

for manifest_path in [root/"plugin.json", root/".codex-plugin"/"plugin.json"]:
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{manifest_path.relative_to(root)}: {exc}")
        continue
    for key in ("name", "version", "description"):
        if not data.get(key):
            errors.append(f"{manifest_path.relative_to(root)} missing {key}")

skills = root/"skills"
names = set()
for d in sorted(p for p in skills.iterdir() if p.is_dir()):
    f = d/"SKILL.md"
    if not f.is_file():
        errors.append(f"missing {f.relative_to(root)}")
        continue
    text = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"invalid frontmatter: {f.relative_to(root)}")
        continue
    nm = re.search(r"^name:\s*(.+)$", m.group(1), re.M)
    ds = re.search(r"^description:\s*(.+)$", m.group(1), re.M)
    if not nm or not ds:
        errors.append(f"missing name/description: {f.relative_to(root)}")
        continue
    name = nm.group(1).strip()
    if name in names:
        errors.append(f"duplicate skill name: {name}")
    names.add(name)

for svg in [root/"assets"/"logo-light.svg", root/"assets"/"logo-dark.svg", root/"assets"/"icon.svg"]:
    try:
        parsed = ET.fromstring(svg.read_text(encoding="utf-8"))
        if parsed.tag.split("}")[-1] != "svg":
            errors.append(f"invalid svg root: {svg.relative_to(root)}")
    except Exception as exc:
        errors.append(f"{svg.relative_to(root)}: {exc}")

for p in root.rglob("*"):
    if p.is_file() and p.name in {".env", "credentials.json", "secrets.json"}:
        errors.append(f"secret-shaped file present: {p.relative_to(root)}")

print(f"skills={len(names)}")
if errors:
    for e in errors:
        print(f"ERROR: {e}")
    sys.exit(1)
print("validation=PASS")
