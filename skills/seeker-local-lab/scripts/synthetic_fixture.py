#!/usr/bin/env python3
"""Send synthetic Seeker handler data to localhost only."""
from __future__ import annotations
import argparse
import json
from urllib import parse, request

ALLOWED = {"127.0.0.1", "localhost", "::1"}

def post(url: str, data: dict[str, str]) -> int:
    encoded = parse.urlencode(data).encode("utf-8")
    req = request.Request(url, data=encoded, method="POST")
    with request.urlopen(req, timeout=5) as resp:
        resp.read()
        return int(resp.status)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8080)
    args = ap.parse_args()
    if not (1 <= args.port <= 65535):
        raise SystemExit("port must be 1..65535")
    base = f"http://127.0.0.1:{args.port}"
    parsed = parse.urlparse(base)
    if parsed.hostname not in ALLOWED:
        raise SystemExit("refusing non-local target")

    info = {
        "Ptf": "SyntheticLab", "Brw": "Synthetic/1.0", "Cc": "4", "Ram": "8",
        "Ven": "SyntheticVendor", "Ren": "SyntheticGPU", "Ht": "844", "Wd": "390",
        "Os": "SyntheticOS",
    }
    result = {
        "Status": "success", "Lat": "0.0000 deg", "Lon": "0.0000 deg",
        "Acc": "9999 m", "Alt": "Not Available", "Dir": "Not Available",
        "Spd": "Not Available",
    }
    statuses = {
        "info_handler.php": post(base + "/info_handler.php", info),
        "result_handler.php": post(base + "/result_handler.php", result),
    }
    print(json.dumps({"ok": all(v == 200 for v in statuses.values()), "synthetic": True, "statuses": statuses}, indent=2))
    return 0 if all(v == 200 for v in statuses.values()) else 1

if __name__ == "__main__":
    raise SystemExit(main())
