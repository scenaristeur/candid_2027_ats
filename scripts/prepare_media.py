#!/usr/bin/env python3
"""Prépare les exports MP3 / MIDI hébergés sur Internet Archive.

Le script lit le dossier local des exports (lecture seule), construit les URLs
de l'item Archive.org et écrit `site/media.json`. Avec `--verify`, il vérifie
que chaque URL répond bien en HTTP avant de marquer le fichier comme publiable.

Usage :
    python scripts/prepare_media.py --item candidats-2027-exports
    python scripts/prepare_media.py --item candidats-2027-exports --verify

Le dossier des exports peut être changé avec --exports ou CANDIDAT_EXPORTS.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
MEDIA_FILE = ROOT / "site" / "media.json"

DEFAULT_EXPORTS = Path(
    os.environ.get(
        "CANDIDAT_EXPORTS",
        r"C:\Users\admin\Music\exports ableton\Candid_2027_ats",
    )
)

KINDS = {".mp3": "mp3", ".mid": "midi", ".midi": "midi"}


def human_size(num: int | None) -> str:
    if not num:
        return "taille inconnue"
    if num >= 1024 * 1024:
        return f"{num / (1024 * 1024):.1f} Mo"
    return f"{num / 1024:.0f} Ko"


def scan(exports: Path) -> tuple[dict[int, dict[str, Path]], list[str]]:
    warnings: list[str] = []
    found: dict[int, dict[str, Path]] = {}
    seen_names: dict[str, Path] = {}

    if not exports.is_dir():
        raise SystemExit(f"Dossier d'exports introuvable : {exports}")

    for path in sorted(exports.rglob("*")):
        if not path.is_file():
            continue
        kind = KINDS.get(path.suffix.lower())
        if not kind:
            continue
        match = re.match(r"^(\d{2})\s*-", path.name)
        if not match:
            warnings.append(f"ignoré (pas de préfixe NN -) : {path.name}")
            continue
        number = int(match.group(1))
        previous = found.setdefault(number, {}).get(kind)
        if previous:
            keep = path if path.stat().st_mtime > previous.stat().st_mtime else previous
            warnings.append(
                f"doublon {kind} pour le titre {number:02d} : "
                f"{previous.name} / {path.name} → {keep.name}"
            )
            found[number][kind] = keep
        else:
            found[number][kind] = path

        if path.name in seen_names:
            warnings.append(
                f"nom de fichier en double, l'upload Archive.org risque de fusionner : {path.name}"
            )
        seen_names[path.name] = path

    return found, warnings


def probe(url: str) -> dict:
    """Vérifie une URL : HEAD puis, si besoin, GET avec Range."""
    result = {"verified": False, "bytes": None, "contentType": None, "http": None}
    headers = {"User-Agent": "Candidats2027-site/1.0"}

    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method, headers=headers)
        if method == "GET":
            request.add_header("Range", "bytes=0-0")
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                result["http"] = response.status
                result["verified"] = 200 <= response.status < 300
                length = response.headers.get("Content-Length")
                if length and length.isdigit() and int(length) > 1:
                    result["bytes"] = int(length)
                result["contentType"] = response.headers.get("Content-Type")
                return result
        except urllib.error.HTTPError as error:
            result["http"] = error.code
            if method == "HEAD" and error.code in (403, 405, 501):
                continue
            return result
        except (urllib.error.URLError, TimeoutError, OSError):
            if method == "HEAD":
                continue
            return result
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exports", type=Path, default=DEFAULT_EXPORTS)
    parser.add_argument("--item", default="candidats-2027-exports")
    parser.add_argument("--base-url", default="")
    parser.add_argument(
        "--verify",
        action="store_true",
        help="vérifie chaque URL sur Internet Archive (HTTP 200)",
    )
    args = parser.parse_args()

    item = args.item.strip()
    if not item:
        raise SystemExit("Identifiant Internet Archive vide.")
    base_url = (args.base_url or f"https://archive.org/download/{item}").rstrip("/")

    found, warnings = scan(args.exports)
    if not found:
        raise SystemExit(f"Aucun MP3/MIDI trouvé dans {args.exports}")

    files: dict[str, dict] = {}
    checked = 0
    verified = 0
    total_bytes = 0
    upload_paths: list[Path] = []

    for number in sorted(found):
        entry: dict[str, object] = {}
        for kind in ("mp3", "midi"):
            path = found[number].get(kind)
            if not path:
                continue
            url = f"{base_url}/{quote(path.name, safe='')}"
            info: dict[str, object] = {
                "file": path.name,
                "url": url,
                "bytes": path.stat().st_size,
                "verified": False,
                "contentType": None,
                "http": None,
            }
            total_bytes += path.stat().st_size
            upload_paths.append(path)
            if args.verify:
                checked += 1
                probed = probe(url)
                info.update(probed)
                if probed["verified"]:
                    verified += 1
                    if probed.get("bytes"):
                        info["bytes"] = probed["bytes"]
                else:
                    print(
                        f"  ✗ {number:02d} {kind} : HTTP {probed.get('http')} — {path.name}",
                        file=sys.stderr,
                    )
            entry[kind] = info
        if entry:
            files[f"{number:02d}"] = entry

    payload = {
        "_comment": (
            "Exports MP3/MIDI hébergés sur Internet Archive. Généré par "
            "scripts/prepare_media.py. requireVerified=true : le site ne publie "
            "que les fichiers dont l'URL a été vérifiée en HTTP 200."
        ),
        "provider": "internet-archive",
        "item": item,
        "baseUrl": base_url,
        "requireVerified": True,
        "checkedAt": datetime.now(timezone.utc).isoformat(timespec="seconds")
        if args.verify
        else None,
        "files": files,
    }
    MEDIA_FILE.parent.mkdir(parents=True, exist_ok=True)
    MEDIA_FILE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(f"✓ {MEDIA_FILE.relative_to(ROOT)} écrit")
    print(f"  {len(found)} titres · {len(upload_paths)} fichiers · {human_size(total_bytes)}")
    if args.verify:
        print(f"  {checked} URLs vérifiées · {verified} disponibles")
    else:
        print("  URLs non vérifiées : lance --verify après l'upload pour les publier.")

    for warning in warnings:
        print(f"⚠ {warning}")

    if verified < len(upload_paths) or not args.verify:
        print("\nProchaine étape — upload sur Internet Archive :")
        print("  pip install internetarchive")
        print("  ia configure")
        command = "  ia upload " + item
        for path in upload_paths:
            command += f' "{path}"'
        command += (
            ' --metadata="title:Candidats 2027 — exports audio et MIDI"'
            ' --metadata="creator:Candidats 2027"'
            ' --metadata="date:2026-11-14"'
            ' --metadata="language:fre"'
            ' --metadata="collection:opensource_audio"'
        )
        print(command)
        print("\nPuis :")
        print(f"  python scripts/prepare_media.py --item {item} --verify")
        print("  python scripts/build_site.py && python scripts/check_site.py")


if __name__ == "__main__":
    main()
