#!/usr/bin/env python3
r"""Prépare une copie propre des exports pour Archive.org.

Le script ne modifie jamais les fichiers d'origine. Il copie les médias dans un
dossier de sortie et, pour les MP3, supprime toutes les métadonnées ID3 existantes
(noms, commentaires, pochettes, e-mails, logiciels, etc.) avant d'écrire des tags
publics minimaux.

Usage :
    python scripts/sanitize_media.py `
      --input  "C:\Users\admin\Music\exports ableton\Candid_2027_ats" `
      --output "C:\Users\admin\Music\archive_clean\Candid_2027_ats"

Puis :
    python scripts/upload_media.py --exports "<dossier de sortie>" --item candidats-2027-exports
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

try:
    from mutagen.id3 import COMM, ID3, TALB, TCON, TDRC, TIT2, TPE1
    from mutagen.mp3 import MP3
except ImportError:  # pragma: no cover
    print("Mutagen est requis : python -m pip install mutagen", file=sys.stderr)
    raise

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

DEFAULT_INPUT = Path(
    r"C:\Users\admin\Music\exports ableton\Candid_2027_ats"
)
DEFAULT_OUTPUT = Path(
    r"C:\Users\admin\Music\archive_clean\Candid_2027_ats"
)
PUBLIC_COMMENT = (
    "Maquette générée par IA — corrections bienvenues. "
    "https://scenaristeur.github.io/candid_2027_ats/"
)
SENSITIVE_RE = re.compile(
    r"(@|C:[\\/]Users[\\/]|/Users/|\\Users\\|https?://|www\.)", re.I
)


def clean_title(stem: str) -> str:
    title = re.sub(r"^\d{1,3}\s*[-–—]\s*", "", stem).strip()
    title = re.sub(r"\.{2,}$", "", title).strip()
    return title or stem


def safe_tag_value(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def sanitize_mp3(source: Path, destination: Path, artist: str, album: str) -> dict:
    source_audio = MP3(str(source))
    original_tags = list(source_audio.tags.keys()) if source_audio.tags else []
    original_values = [str(value) for value in (source_audio.tags or {}).values()]
    personal = any(SENSITIVE_RE.search(value) for value in original_values)

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)

    audio = MP3(str(destination))
    if audio.tags:
        audio.tags.clear()
    audio.tags = ID3()
    audio.tags.add(TIT2(encoding=3, text=clean_title(source.stem)))
    audio.tags.add(TPE1(encoding=3, text=artist))
    audio.tags.add(TALB(encoding=3, text=album))
    audio.tags.add(TDRC(encoding=3, text="2026"))
    audio.tags.add(TCON(encoding=3, text="Chanson"))
    audio.tags.add(COMM(encoding=3, lang="fra", desc="", text=PUBLIC_COMMENT))
    audio.save()

    check = MP3(str(destination))
    remaining = sorted(check.tags.keys()) if check.tags else []
    return {
        "source": str(source),
        "destination": str(destination),
        "original_tags": original_tags,
        "remaining_tags": remaining,
        "personal_pattern_removed": personal,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--artist", default="Candidats 2027")
    parser.add_argument("--album", default="Candidats 2027 — maquettes")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.input.is_dir():
        raise SystemExit(f"Dossier d'entrée introuvable : {args.input}")
    if args.input.resolve() == args.output.resolve():
        raise SystemExit("L'entrée et la sortie doivent être différentes.")

    files = sorted(
        path
        for path in args.input.rglob("*")
        if path.is_file() and path.suffix.lower() in {".mp3", ".wav", ".mid", ".midi"}
    )
    if not files:
        raise SystemExit(f"Aucun média trouvé dans {args.input}")

    report = []
    for source in files:
        relative = source.relative_to(args.input)
        destination = args.output / relative
        if args.dry_run:
            report.append(
                {
                    "source": str(source),
                    "destination": str(destination),
                    "kind": source.suffix.lower(),
                    "dry_run": True,
                }
            )
            continue
        if source.suffix.lower() == ".mp3":
            report.append(sanitize_mp3(source, destination, args.artist, args.album))
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            report.append(
                {
                    "source": str(source),
                    "destination": str(destination),
                    "kind": source.suffix.lower(),
                    "copied_without_tag_processing": True,
                }
            )

    if not args.dry_run:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "sanitization-report.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    print(f"{'[dry-run] ' if args.dry_run else ''}{len(report)} fichier(s) préparé(s)")
    print(f"  entrée : {args.input}")
    print(f"  sortie : {args.output}")
    if not args.dry_run:
        for item in report:
            if item.get("original_tags"):
                print(
                    f"  tags retirés : {Path(item['source']).name} "
                    f"({len(item['original_tags'])} tags)"
                )
        print("  tags publics : titre, artiste, album, année, genre, commentaire")
        print("  rapport : sanitization-report.json")


if __name__ == "__main__":
    main()
