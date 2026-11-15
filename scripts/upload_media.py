#!/usr/bin/env python3
"""Envoie les exports MP3/MIDI vers l'item Internet Archive du projet.

Le script lit les clés IA-S3 depuis `.env` (ou les variables
`IA_ACCESS_KEY_ID` / `IA_SECRET_ACCESS_KEY`), compare les empreintes MD5 avec
les fichiers déjà présents sur Internet Archive, et n'envoie que les nouveaux
fichiers ou ceux qui ont changé.

Usage :
    python scripts/upload_media.py --item candidats-2027-exports
    python scripts/upload_media.py --item candidats-2027-exports --dry-run

Puis le script relance `prepare_media.py --verify` pour mettre à jour
`site/media.json`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

from internetarchive import get_session

try:
    from prepare_media import DEFAULT_EXPORTS, USER_AGENT, scan
except ImportError:  # exécution depuis un autre répertoire
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from prepare_media import DEFAULT_EXPORTS, USER_AGENT, scan

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env"
UPLOADER_USER_AGENT = "Candidats2027-uploader/1.0 (DeepSeek V4.1 Flash 1017)"


def load_credentials() -> tuple[str, str]:
    values: dict[str, str] = {}
    if ENV_FILE.is_file():
        for raw in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip().lower()] = value.strip().strip('"').strip("'")

    access = (
        values.get("internet_archive_s3_access_key")
        or os.environ.get("IA_ACCESS_KEY_ID")
        or os.environ.get("INTERNET_ARCHIVE_S3_ACCESS_KEY")
    )
    secret = (
        values.get("internet_archive_s3_secret_key")
        or os.environ.get("IA_SECRET_ACCESS_KEY")
        or os.environ.get("INTERNET_ARCHIVE_S3_SECRET_KEY")
    )
    if not access or not secret:
        raise SystemExit(
            "Clés Internet Archive absentes. Renseigne "
            "INTERNET_ARCHIVE_S3_ACCESS_key et INTERNET_ARCHIVE_S3_SECRET_KEY "
            "dans .env, ou IA_ACCESS_KEY_ID / IA_SECRET_ACCESS_KEY."
        )
    return access, secret


def md5(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def remote_files(item: str) -> dict[str, dict]:
    try:
        with urllib.request.urlopen(
            urllib.request.Request(
                f"https://archive.org/metadata/{item}",
                headers={"User-Agent": USER_AGENT},
            ),
            timeout=30,
        ) as response:
            data = json.load(response)
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError):
        return {}
    return {entry.get("name"): entry for entry in data.get("files", []) if entry.get("name")}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exports", type=Path, default=DEFAULT_EXPORTS)
    parser.add_argument("--item", default="candidats-2027-exports")
    parser.add_argument("--title", default="Candidats 2027 - exports audio et MIDI")
    parser.add_argument("--creator", default="Candidats 2027")
    parser.add_argument("--date", default="2026-11-14")
    parser.add_argument("--description", default="")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-verify", action="store_true")
    args = parser.parse_args()

    item = args.item.strip()
    access, secret = load_credentials()

    found, warnings = scan(args.exports)
    if not found:
        raise SystemExit(f"Aucun MP3/MIDI trouvé dans {args.exports}")

    local_files = sorted(
        path for entries in found.values() for path in entries.values()
    )
    existing = remote_files(item)

    to_upload: list[Path] = []
    for path in local_files:
        remote = existing.get(path.name)
        if remote and remote.get("md5") == md5(path):
            print(f"= déjà présent : {path.name}")
            continue
        action = "remplacer" if remote else "envoyer"
        print(f"+ {action} : {path.name} ({path.stat().st_size / (1024 * 1024):.1f} Mo)")
        to_upload.append(path)

    if not to_upload:
        print("✓ Tous les fichiers sont déjà à jour sur Internet Archive.")
    elif args.dry_run:
        print(f"Mode dry-run : {len(to_upload)} fichier(s) seraient envoyés.")
    else:
        metadata = {
            "title": args.title,
            "creator": args.creator,
            "date": args.date,
            "language": "fre",
            "mediatype": "audio",
            "collection": "opensource_audio",
            "description": args.description
            or (
                "Exports MP3 et MIDI de l'album Candidats 2027 : trente et une "
                "chansons, une par candidat à la présidentielle de 2027. Exercice "
                "de collaboration musicale et culturelle partagé, sans intention de "
                "favoriser ou défavoriser un candidat. Titres, paroles et musiques "
                "générés par IA : brouillons de vulgarisation, potentiellement "
                "erronés, corrections bienvenues. "
                "Site : https://scenaristeur.github.io/candid_2027_ats/"
            ),
            "subject": [
                "Candidats 2027",
                "chansons",
                "exercice musical",
                "vulgarisation",
                "intelligence artificielle",
            ],
        }
        session = get_session(
            config={"general": {"user_agent_suffix": UPLOADER_USER_AGENT}}
        )
        item_obj = session.get_item(item)
        responses = item_obj.upload(
            files=[str(path) for path in to_upload],
            metadata=metadata,
            access_key=access,
            secret_key=secret,
            retries=5,
            retries_sleep=5,
            verbose=True,
        )
        failed = False
        for response in responses or []:
            status = getattr(response, "status_code", None)
            print(f"HTTP {status} {getattr(response, 'url', '')}")
            if status is None or status >= 400:
                failed = True
        if failed:
            raise SystemExit("Upload incomplet : vérifie les erreurs ci-dessus.")
        print("✓ Upload terminé")

    if not args.skip_verify:
        command = [
            sys.executable,
            str(ROOT / "scripts" / "prepare_media.py"),
            "--item",
            item,
            "--exports",
            str(args.exports),
            "--verify",
        ]
        print("\nVérification des URLs…")
        subprocess.run(command, check=False)

    for warning in warnings:
        print(f"⚠ {warning}")


if __name__ == "__main__":
    main()
