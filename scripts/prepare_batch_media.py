#!/usr/bin/env python3
r"""Prépare les MP3 de toutes les productions non Candidats/Désir.

Le script lit `catalog/productions.json`, copie et nettoie les MP3 dans un
dossier de staging avec un nom stable `<id>.mp3`, et écrit un plan de
publication pour Archive.org.

Usage :
    python scripts/prepare_batch_media.py
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

from sanitize_media import sanitize_mp3

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog" / "productions.json"
EXPORTS_ROOT = Path(r"C:\Users\admin\Music\exports ableton")
OUTPUT = Path(r"C:\Users\admin\Music\archive_clean\ableton-productions")
EXCLUDED_ALBUMS = {"Candidats 2027", "Désir"}


def resolve(value: str) -> Path:
    normalized = value.replace("\\", "/")
    if normalized.startswith("exports ableton/"):
        return EXPORTS_ROOT / normalized[len("exports ableton/") :]
    return Path(value)


def main() -> None:
    rows = json.loads(CATALOG.read_text(encoding="utf-8"))
    selected = [
        row
        for row in rows
        if row.get("mp3") and row.get("album") not in EXCLUDED_ALBUMS
    ]
    if not selected:
        raise SystemExit("Aucun MP3 à préparer.")

    mp3_dir = OUTPUT / "mp3"
    if mp3_dir.exists():
        shutil.rmtree(mp3_dir)
    mp3_dir.mkdir(parents=True, exist_ok=True)

    plan = []
    for row in selected:
        source = resolve(row["mp3"])
        if not source.is_file():
            print(f"⚠ source absente : {source}")
            continue
        remote = f"{row['id']}.mp3"
        destination = mp3_dir / remote
        sanitize_mp3(source, destination, "Scenaristeur", row["album"])
        plan.append(
            {
                "id": row["id"],
                "title": row["title"],
                "album": row["album"],
                "source": str(source),
                "remote": remote,
                "bytes": destination.stat().st_size,
            }
        )

    (OUTPUT / "publication-plan.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"✓ {len(plan)} MP3 préparés dans {OUTPUT}")
    print(f"  plan : {OUTPUT / 'publication-plan.json'}")


if __name__ == "__main__":
    main()
