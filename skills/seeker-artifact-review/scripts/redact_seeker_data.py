#!/usr/bin/env python3
"""Summarize Seeker artifacts without echoing precise location/IP data."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return None

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", nargs="?", default=".")
    args = ap.parse_args()
    root = Path(args.repo).resolve()
    info = load_json(root/"logs"/"info.txt")
    result = load_json(root/"logs"/"result.txt")

    out = {"repo": str(root), "info_present": bool(info), "result_present": bool(result)}
    if isinstance(info, dict):
        out["device"] = {
            "os": info.get("os"),
            "platform": info.get("platform"),
            "browser": info.get("browser"),
            "resolution": f'{info.get("wd","?")}x{info.get("ht","?")}',
            "public_ip": "[REDACTED]" if info.get("ip") else None,
            "gpu": "[PRESENT]" if info.get("render") else None,
        }
    if isinstance(result, dict):
        out["location"] = {
            "status": result.get("status"),
            "latitude": "[REDACTED]" if result.get("lat") else None,
            "longitude": "[REDACTED]" if result.get("lon") else None,
            "accuracy": result.get("acc"),
            "altitude": "[REDACTED]" if result.get("alt") and result.get("alt") != "Not Available" else result.get("alt"),
            "direction": result.get("dir"),
            "speed": result.get("spd"),
            "error": result.get("error"),
        }

    out["results_csv_present"] = (root/"db"/"results.csv").is_file()
    out["kml_files"] = len(list(root.glob("*.kml")))
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
