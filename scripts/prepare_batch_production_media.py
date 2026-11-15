#!/usr/bin/env python3
r"""Met à jour site/media_productions.json pour un lot Archive.org.

Lit le plan produit par `prepare_batch_media.py` et vérifie les URLs de l'item
Archive.org. Fusionne les entrées avec le manifeste existant (Désir, etc.).

Usage :
    python scripts/prepare_batch_production_media.py `
      --plan "C:\Users\admin\Music\archive_clean\ableton-productions\publication-plan.json" `
      --item ableton-productions `
      --verify
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

from prepare_media import item_node_base, probe

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "site" / "media_productions.json"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--item", required=True)
    parser.add_argument("--base-url", default="")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    base_url = (args.base_url or f"https://archive.org/download/{args.item}").rstrip("/")
    node_base = item_node_base(args.item) if args.verify else None

    manifest = {}
    albums = {}
    if OUTPUT.is_file():
        try:
            existing = json.loads(OUTPUT.read_text(encoding="utf-8"))
            value = existing.get("files", {})
            if isinstance(value, dict) and isinstance(value.get("files"), dict):
                value = value["files"]
            if isinstance(value, dict):
                manifest = value
            if isinstance(existing.get("albums"), dict):
                albums = existing["albums"]
        except (OSError, json.JSONDecodeError):
            manifest = {}

    verified = 0
    for item in plan:
        remote = item["remote"]
        canonical = f"{base_url}/{quote(remote, safe='')}"
        info = {
            "file": remote,
            "url": canonical,
            "canonicalUrl": canonical,
            "verified": False,
            "bytes": item.get("bytes"),
            "http": None,
            "via": "canonical",
        }
        if args.verify:
            probed = probe(canonical)
            if not probed["verified"] and node_base:
                node_url = f"{node_base}/{quote(remote, safe='')}"
                node_probe = probe(node_url)
                if node_probe["verified"]:
                    info["url"] = node_url
                    info["via"] = "storage-node"
                    probed = node_probe
            info.update(probed)
            if probed["verified"]:
                verified += 1
        manifest[item["id"]] = {"mp3": info}
        albums[item["album"]] = {"item": args.item, "baseUrl": base_url}

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(
            {
                "_comment": (
                    "URLs Archive.org par identifiant de production. Généré par "
                    "prepare_production_media.py et prepare_batch_production_media.py."
                ),
                "checkedAt": datetime.now(timezone.utc).isoformat(timespec="seconds")
                if args.verify
                else None,
                "albums": albums,
                "files": manifest,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"✓ {OUTPUT.relative_to(ROOT)} · {len(plan)} productions")
    if args.verify:
        print(f"  {verified}/{len(plan)} URLs vérifiées")


if __name__ == "__main__":
    main()
