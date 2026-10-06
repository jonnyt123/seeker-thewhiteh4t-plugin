#!/usr/bin/env python3
"""Read-only static summary for a thewhiteh4t/seeker checkout."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", nargs="?", default=".")
    args = ap.parse_args()
    root = Path(args.repo).resolve()
    seeker = read(root/"seeker.py")
    templates_raw = read(root/"template"/"templates.json")
    js = read(root/"js"/"location.js")
    php_info = read(root/"php"/"info.php")
    php_result = read(root/"php"/"result.php")

    version = None
    m = re.search(r"^VERSION\s*=\s*['\"]([^'\"]+)['\"]", seeker, re.M)
    if m: version = m.group(1)
    templates = []
    try:
        templates = [x.get("name") for x in json.loads(templates_raw).get("templates", [])]
    except Exception:
        pass

    report = {
        "repo": str(root),
        "looks_like_seeker": all((root/p).exists() for p in ["seeker.py","metadata.json","template/templates.json","js/location.js"]),
        "version": version,
        "templates": templates,
        "server_bind_all_interfaces": "0.0.0.0" in seeker,
        "public_ip_recon": "ipwhois.app" in seeker,
        "telegram_forwarding": "send_telegram" in seeker,
        "webhook_forwarding": "send_webhook" in seeker,
        "browser_geolocation": "navigator.geolocation" in js,
        "device_info_handler": "logs/info.txt" in seeker and "info.txt" in php_info,
        "location_result_handler": "logs/result.txt" in seeker and "result.txt" in php_result,
        "csv_retention": "results.csv" in seeker,
        "kml_export": "kmlout" in seeker,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["looks_like_seeker"] else 2

if __name__ == "__main__":
    raise SystemExit(main())
