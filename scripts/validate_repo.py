#!/usr/bin/env python3
from pathlib import Path
import json, re, sys, unicodedata, xml.etree.ElementTree as ET

root=Path(__file__).resolve().parents[1]
errors=[]
semver=re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
name_re=re.compile(r"^[A-Za-z0-9_-]{1,64}$")

def load(path):
    try:
        value=json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value,dict): raise ValueError("top level must be object")
        return value
    except Exception as exc:
        errors.append(f"{path.relative_to(root)}: {exc}"); return {}

portable=load(root/"plugin.json")
compat=load(root/".codex-plugin"/"plugin.json")

for label,data in (("plugin.json",portable),(".codex-plugin/plugin.json",compat)):
    if not isinstance(data.get("name"),str) or not name_re.fullmatch(data["name"]): errors.append(f"{label}: invalid name")
    if not isinstance(data.get("version"),str) or not semver.fullmatch(data["version"]): errors.append(f"{label}: invalid semver")
    if not isinstance(data.get("description"),str) or not data["description"] or len(data["description"])>1024: errors.append(f"{label}: invalid description")
    if not isinstance(data.get("author"),dict) or not isinstance(data["author"].get("name"),str) or not data["author"]["name"].strip(): errors.append(f"{label}: author.name required")

if portable.get("name")!=compat.get("name"): errors.append("manifest names disagree")
if portable.get("version")!=compat.get("version"): errors.append("manifest versions disagree")
if compat.get("skills")!="./skills/": errors.append("compat skills must be ./skills/")

interface=(((portable.get("extensions") or {}).get("com") or {}).get("openai") or {}).get("interface")
compat_interface=compat.get("interface")
if not isinstance(interface,dict): errors.append("portable OpenAI interface missing"); interface={}
if not isinstance(compat_interface,dict): errors.append("compat interface missing"); compat_interface={}
for field,limit in (("displayName",30),("shortDescription",30),("longDescription",4000),("developerName",80)):
    value=interface.get(field)
    if not isinstance(value,str) or not value.strip(): errors.append(f"interface.{field} required")
    elif len(value)>limit: errors.append(f"interface.{field} too long")
for field in ("displayName","shortDescription","longDescription","developerName","category","capabilities","defaultPrompt","brandColor","composerIcon","logo"):
    if interface.get(field)!=compat_interface.get(field): errors.append(f"manifest interface mismatch: {field}")
caps=interface.get("capabilities")
if not isinstance(caps,list) or not 1<=len(caps)<=20: errors.append("capabilities must contain 1..20 items")
elif any(not isinstance(x,str) or not x.strip() or len(x)>120 or "\n" in x for x in caps): errors.append("invalid capability")
prompts=interface.get("defaultPrompt")
if not isinstance(prompts,list) or not 1<=len(prompts)<=3: errors.append("defaultPrompt must contain 1..3 prompts")
elif any(not isinstance(x,str) or not x.strip() or len(x)>128 or "\n" in x for x in prompts): errors.append("invalid defaultPrompt")
elif len({" ".join(x.split()).casefold() for x in prompts})!=len(prompts): errors.append("defaultPrompt values must be unique")
if interface.get("category")!="Developer Tools": errors.append("unexpected category")
if not re.fullmatch(r"#[0-9A-Fa-f]{6}",str(interface.get("brandColor",""))): errors.append("invalid brandColor")

codex=root/".codex-plugin"
if not codex.is_dir(): errors.append("missing .codex-plugin")
elif sorted(p.name for p in codex.iterdir())!=["plugin.json"]: errors.append(".codex-plugin must contain only plugin.json")

names=set()
skills=root/"skills"
if not skills.is_dir(): errors.append("skills directory missing")
else:
    for d in sorted(skills.iterdir()):
        if not d.is_dir(): errors.append(f"skills direct child is not directory: {d.name}"); continue
        f=d/"SKILL.md"
        if not f.is_file(): errors.append(f"missing {f.relative_to(root)}"); continue
        text=f.read_text(encoding="utf-8")
        m=re.match(r"^---\n(.*?)\n---\n(.+)$",text,re.S)
        if not m: errors.append(f"invalid frontmatter/body: {d.name}"); continue
        nm=re.search(r"^name:\s*(\S+)\s*$",m.group(1),re.M)
        ds=re.search(r"^description:\s*(.+)$",m.group(1),re.M)
        if not nm or not ds: errors.append(f"missing name/description: {d.name}"); continue
        skill_name=nm.group(1).strip()
        if skill_name in names: errors.append(f"duplicate skill name: {skill_name}")
        names.add(skill_name)
        if len(f"{portable.get('name','')}:{skill_name}")>64: errors.append(f"combined identity too long: {skill_name}")
if len(names)!=11: errors.append(f"expected 11 skills, found {len(names)}")
for required in ("host-workspace-operator","sandbox-python-executor","seeker-project"):
    if required not in names: errors.append(f"required skill missing: {required}")

for field in ("logo","composerIcon"):
    value=interface.get(field)
    if not isinstance(value,str) or not value.startswith("./assets/") or ".." in value.split("/"): errors.append(f"unsafe {field} path")
    elif not (root/value[2:]).is_file(): errors.append(f"missing {field}")

for svg in ("assets/logo-light.svg","assets/logo-dark.svg","assets/icon.svg"):
    try:
        parsed=ET.fromstring((root/svg).read_text(encoding="utf-8"))
        if parsed.tag.split("}")[-1]!="svg": errors.append(f"invalid SVG root: {svg}")
        box=parsed.attrib.get("viewBox","").split()
        if len(box)!=4 or box[2]!=box[3]: errors.append(f"SVG not square: {svg}")
    except Exception as exc: errors.append(f"{svg}: {exc}")

seen={}
for p in root.rglob("*"):
    rel=p.relative_to(root).as_posix()
    key=unicodedata.normalize("NFC",rel).casefold()
    if key in seen and seen[key]!=rel: errors.append(f"path collision: {seen[key]} vs {rel}")
    seen[key]=rel
    if p.is_symlink(): errors.append(f"symlink not allowed: {rel}")
    if p.is_file() and (p.name in {".env","credentials.json","secrets.json",".DS_Store","Thumbs.db"} or p.suffix in {".pyc",".pyo"}): errors.append(f"forbidden file: {rel}")
    if p.is_file() and p.stat().st_size>100*1024*1024: errors.append(f"file too large: {rel}")

print(f"version={portable.get('version')}")
print(f"skills={len(names)}")
if errors:
    for e in errors: print(f"ERROR: {e}")
    sys.exit(1)
print("validation=PASS")
