#!/usr/bin/env python3
"""Prépare les URLs Archive.org pour les productions d'un album.

Contrairement à `prepare_media.py`, ce script travaille par identifiant de
production (et non par numéro de piste), ce qui permet de gérer plusieurs
albums.

Usage :
    python scripts/prepare_production_media.py `
      --album "Désir" `
      --item desir-maquettes `
      --verify

Écrit `site/media_productions.json`, qui sera lu par
`scripts/build_productions.py`.
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
CATALOG = ROOT / "catalog" / "productions.json"
OUTPUT = ROOT / "site" / "media_productions.json"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=CATALOG)
    parser.add_argument("--album", required=True)
    parser.add_argument("--item", required=True)
    parser.add_argument("--base-url", default="")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if not args.catalog.is_file():
        raise SystemExit(f"Catalogue introuvable : {args.catalog}")
    productions = json.loads(args.catalog.read_text(encoding="utf-8"))
    selected = [
        item
        for item in productions
        if item.get("album") == args.album and item.get("kind") == "source"
    ]
    if not selected:
        raise SystemExit(f"Aucune production source pour l'album {args.album!r}")

    base_url = (args.base_url or f"https://archive.org/download/{args.item}").rstrip("/")
    node_base = item_node_base(args.item) if args.verify else None
    manifest = {}
    if OUTPUT.is_file():
        try:
            existing = json.loads(OUTPUT.read_text(encoding="utf-8"))
            value = existing.get("files", {})
            # Compatibilité avec une ancienne version qui imbriquait le manifeste.
            if isinstance(value, dict) and isinstance(value.get("files"), dict):
                value = value["files"]
            if isinstance(value, dict):
                manifest = value
        except (OSError, json.JSONDecodeError):
            manifest = {}

    verified = 0
    total = 0
    for item in selected:
        entry: dict[str, object] = {}
        for kind in ("mp3", "wav", "midi"):
            local = item.get(kind)
            if not local:
                continue
            filename = Path(local).name
            canonical = f"{base_url}/{quote(filename, safe='')}"
            info: dict[str, object] = {
                "file": filename,
                "url": canonical,
                "canonicalUrl": canonical,
                "verified": False,
                "bytes": None,
                "http": None,
                "via": "canonical",
            }
            if args.verify:
                total += 1
                probed = probe(canonical)
                if not probed["verified"] and node_base:
                    node_url = f"{node_base}/{quote(filename, safe='')}"
                    node_probe = probe(node_url)
                    if node_probe["verified"]:
                        info["url"] = node_url
                        info["via"] = "storage-node"
                        probed = node_probe
                info.update(probed)
                if probed["verified"]:
                    verified += 1
            entry[kind] = info
        if entry:
            manifest[item["id"]] = entry

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(
            {
                "_comment": (
                    "URLs Archive.org par identifiant de production. Généré par "
                    "scripts/prepare_production_media.py."
                ),
                "checkedAt": datetime.now(timezone.utc).isoformat(timespec="seconds")
                if args.verify
                else None,
                "albums": {args.album: {"item": args.item, "baseUrl": base_url}},
                "files": manifest,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"✓ {OUTPUT.relative_to(ROOT)}")
    print(f"  album {args.album} · {len(selected)} productions")
    if args.verify:
        print(f"  {verified}/{total} URLs vérifiées")


if __name__ == "__main__":
    main()
