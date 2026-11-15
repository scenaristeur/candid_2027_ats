#!/usr/bin/env python3
"""Construit le catalogue des productions du projet.

Le script lit en LECTURE SEULE :
- les sources éditoriales : C:\\Users\\admin\\dev\\ableton-holland-mcp\\sources
- les projets Ableton Live : C:\\Users\\admin\\Music\\Ableton Live
- les exports audio/MIDI : C:\\Users\\admin\\Music\\exports ableton

Il écrit uniquement dans catalog/ :
- productions.csv / productions.json : une ligne par production
- PRODUCTIONS.md : tableau lisible groupé par album
- als_versions.csv : inventaire de chaque session .als principale
- exports.csv : inventaire de chaque export audio/MIDI
- README.md : méthode et statistiques

Usage :
    python scripts/build_catalog.py
    python scripts/build_catalog.py --sources ... --als ... --exports ...
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"
CACHE = CATALOG / ".cache" / "als.json"

DEFAULT_SOURCES = Path(
    os.environ.get(
        "CANDIDAT_SOURCES_ALL",
        r"C:\Users\admin\dev\ableton-holland-mcp\sources",
    )
)
DEFAULT_ALS = Path(
    os.environ.get(
        "CANDIDAT_ALS_ALL",
        r"C:\Users\admin\Music\Ableton Live",
    )
)
DEFAULT_EXPORTS = Path(
    os.environ.get(
        "CANDIDAT_EXPORTS_ALL",
        r"C:\Users\admin\Music\exports ableton",
    )
)

MEDIA_SUFFIXES = {".mp3": "mp3", ".wav": "wav", ".mid": "midi", ".midi": "midi", ".flac": "flac"}
TRACK_DOC_RE = re.compile(r"(fiche[ _-]?technique|paroles|status|structure|clip)", re.I)
EXCLUDED_DOC_RE = re.compile(
    r"^(album|readme|lisez|methode|méthode|plan|synthese|synthèse|prompt|analyse|"
    r"description|traduction|traducion|guitares|remakes|notes?|fourvi|vieux|lyon|"
    r"croix|brotteaux|etats|pentes|confluence|vaise|guilloti|gerland|bellecour|"
    r"duchene|duchère|bonus|_)",
    re.I,
)

STOPWORDS = {
    "project", "projet", "copie", "copy", "version", "final", "finale", "mix", "review",
    "opencode", "open", "code", "avant", "apres", "après", "new", "old", "test", "tests",
    "preparation", "préparation", "prep", "with", "vocals", "vocal", "voix", "sans", "instru",
    "instrumental", "refactor", "skills", "guepe", "guêpe", "charge", "cpu", "automation",
    "confus", "first", "bass", "basse", "drum", "drums", "guit", "guitare", "origin", "origine",
    "review", "corrige", "corrigé", "modif", "modifié", "brut", "demo", "démo", "master",
    "remaster", "export", "wav", "mp3", "als", "copie", "le", "la", "les", "de", "du", "des",
    "un", "une", "et", "a", "au", "aux", "en", "pour", "par", "sur", "the", "of", "and",
}

ALBUM_CANONICAL = {
    "melody where are you": "Melody, Where are you",
    "mascu": "Masculinisme",
    "masculinisme": "Masculinisme",
    "strates gemmes": "Strates@Gemmes",
    "strates gemmes faut des parts": "Strates@Gemmes",
    "resonnances": "Résonnances",
    "candid 2027 ats": "Candidats 2027",
    "sous le costume la poudre": "Sous le costume la poudre",
    "souslecostumelapoudre": "Sous le costume la poudre",
    "deconnectes": "Transmissions",
    "le train des possibles": "Transmissions",
}


def canonical_album(name: str) -> str:
    key = norm(name).replace("  ", " ")
    return ALBUM_CANONICAL.get(key, name)


def e(value: object) -> str:
    return str(value).replace("\r", " ").replace("\n", " ").strip()


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text or "")
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower().replace("&", " et ")
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def slug(text: str) -> str:
    text = norm(text)
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-") or "sans-titre"


def tokens(text: str) -> set[str]:
    return {word for word in norm(text).split() if len(word) > 2 and word not in STOPWORDS}


def match_title(text: str) -> str:
    text = re.sub(r"^\d{1,3}\s*[-–—]\s*", "", text or "")
    text = re.sub(r"\([^)]*\)", " ", text)
    text = re.split(r"\s+[—–]\s+", text)[0]
    text = re.sub(
        r"\b(fiche[ _-]?technique|reprise|remake|adaptation|version|sans voix|with vocals)\b.*$",
        "",
        text,
        flags=re.I,
    )
    text = re.sub(r"(?<=[A-Za-z])\d+\s*$", "", text)
    return clean(text)


def overlap(left: str, right: str) -> float:
    a, b = tokens(left), tokens(right)
    if not a or not b:
        return 0.0
    return len(a & b) / max(len(a), len(b))


def read_text(path: Path, limit: int = 400_000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:limit]
    except OSError:
        return ""


def md_meta(text: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    head = text.split("\n---", 1)[0]
    for line in head.splitlines():
        match = re.match(r"\*\*(.+?)\*\*\s*:\s*(.+)$", line)
        if match:
            key = re.sub(r"[*_`]", "", match.group(1)).strip()
            value = re.sub(r"\s*\*\([^*]*\)\*", "", match.group(2)).strip()
            meta[key] = clean(value)
    return meta


def md_section(text: str, prefix: str) -> list[str]:
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.startswith("## ") and clean(re.sub(r"[*_`]", "", line[3:])).startswith(prefix):
            start = index + 1
            break
    if start is None:
        return []
    out = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        out.append(line)
    return out


def md_bullets(lines: Iterable[str]) -> list[str]:
    out = []
    for line in lines:
        match = re.match(r"\s*[-*+]\s+(.*)$", line)
        if match:
            out.append(clean(re.sub(r"[*_`]", "", match.group(1))))
    return out


def first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return clean(line[2:])
    return ""


def first_paragraph(text: str) -> str:
    for block in re.split(r"\n\s*\n", text):
        block = block.strip()
        if not block or block.startswith(("#", "|", "-", ">", "**", "```")):
            continue
        return clean(re.sub(r"[*_`]", "", block))
    return ""


def is_track_doc(path: Path) -> bool:
    name = path.name.lower()
    if name.startswith("_"):
        return False
    if TRACK_DOC_RE.search(name):
        return True
    if EXCLUDED_DOC_RE.search(name):
        return False
    return True


def discover_source_tracks(album_dir: Path) -> list[dict]:
    md_files = [
        p
        for p in album_dir.rglob("*.md")
        if p.is_file()
        and not any(part.startswith("_") for part in p.relative_to(album_dir).parts)
    ]
    if not md_files:
        return []

    doc_dirs: set[Path] = set()
    for path in md_files:
        if path.name.lower().startswith("_"):
            continue
        parent = path.parent
        stem = norm(path.stem)
        folder = norm(parent.name)
        if TRACK_DOC_RE.search(path.name) or (stem and (stem in folder or folder in stem)):
            doc_dirs.add(parent)
        elif not any(
            child.is_dir() and any(child.glob("*.md"))
            for child in parent.iterdir()
        ):
            doc_dirs.add(parent)

    # Si aucun dossier de piste n'est identifié, l'album lui-même est la piste.
    if not doc_dirs:
        doc_dirs.add(album_dir)

    # Ne garder que les dossiers sans descendant déjà sélectionné.
    selected = []
    for directory in sorted(doc_dirs):
        if any(other != directory and directory in other.parents for other in doc_dirs):
            continue
        selected.append(directory)
    if not selected:
        selected = [album_dir]

    tracks = []
    for directory in sorted(selected):
        docs = sorted(p for p in directory.glob("*.md") if p.is_file())
        if not docs and directory != album_dir:
            continue
        text = "\n".join(read_text(p) for p in docs)
        fiche = next(
            (p for p in docs if "fiche" in p.name.lower() or "status" in p.name.lower()),
            None,
        )
        paroles = next((p for p in docs if "parole" in p.name.lower()), None)
        fiche_text = read_text(fiche) if fiche else text
        meta = md_meta(fiche_text) if fiche else {}
        title = clean(first_heading(fiche_text)) or directory.name
        title = re.sub(r"^\d+\s*[-–—]\s*", "", title).strip()
        title = re.sub(r"\s*[—–-]\s*Fiche technique.*$", "", title, flags=re.I).strip()
        if " — " in title:
            title = title.split(" — ", 1)[0].strip()

        folder_title = re.sub(r"^\d+\s*[-–—]\s*", "", directory.name).strip()
        doc_title = clean(first_heading(fiche_text))
        doc_title = re.sub(
            r"^(fiche[ _-]?technique|status|paroles|analyse|adaptation|clip)\s*[—–:-]\s*",
            "",
            doc_title,
            flags=re.I,
        ).strip()
        doc_title = re.sub(
            r"\s*[—–-]\s*(fiche[ _-]?technique|status|paroles|analyse)\b.*$",
            "",
            doc_title,
            flags=re.I,
        ).strip()
        has_number = bool(re.match(r"^\d", directory.name))
        if directory == album_dir:
            title = re.sub(r"\s+Project$", "", album_dir.name, flags=re.I).strip()
        elif has_number and folder_title:
            title = folder_title
        elif doc_title and not re.match(
            r"^(fiche|status|paroles|analyse|adaptation|album|readme)", doc_title, re.I
        ):
            title = doc_title
        else:
            title = folder_title or title
        number_match = re.match(r"^(\d{1,3})", directory.name)
        number = int(number_match.group(1)) if number_match else None

        candidate = ""
        parts = re.split(r"\s+[-–—]\s+", folder_title, maxsplit=2)
        if len(parts) >= 3 and album_dir.name.lower().startswith("candid"):
            candidate = parts[1].strip()
            title = parts[2].strip()

        goals = md_bullets(md_section(fiche_text, "2."))
        summary = " ".join(goals[:3])
        if not summary:
            summary = " — ".join(x for x in (meta.get("Atmosphère", ""), meta.get("Style", "")) if x)
        if not summary:
            summary = first_paragraph(fiche_text)[:300]

        paroles_text = read_text(paroles) if paroles else text
        if re.search(r"^## .*(Couplet|Pont)", text, re.M | re.I):
            lyrics = "complètes"
        elif re.search(r"^## .*Refrain", text, re.M | re.I):
            lyrics = "refrain"
        elif paroles_text and re.search(r"^## ", paroles_text, re.M):
            lyrics = "refrain"
        else:
            lyrics = "aucune"

        tracks.append(
            {
                "album": canonical_album(album_dir.name),
                "source_dir": directory,
                "title": title or folder_title or album_dir.name,
                "candidate": candidate,
                "number": number,
                "docs": [p.name for p in docs],
                "has_fiche": bool(docs),
                "has_paroles": bool(paroles) or lyrics != "aucune",
                "lyrics": lyrics,
                "tempo": meta.get("Tempo", ""),
                "key": meta.get("Tonalité", ""),
                "signature": meta.get("Signature", ""),
                "duration": meta.get("Durée cible", ""),
                "style": meta.get("Style", ""),
                "atmosphere": meta.get("Atmosphère", ""),
                "status_source": meta.get("Statut", ""),
                "summary": summary[:420],
                "intention": " ".join(goals[:4])[:500],
                "updated": max((p.stat().st_mtime for p in docs), default=0),
                "kind": "source",
            }
        )
    # Fusionne les doublons de casing/accents (ex. Lyon 01 Lumiere / Lumière).
    unique: dict[tuple, dict] = {}
    for track in tracks:
        key = (track["number"], slug(track["title"]))
        current = unique.get(key)
        if current is None or len(track["docs"]) > len(current["docs"]):
            unique[key] = track
    return sorted(unique.values(), key=lambda x: (x["number"] or 999, norm(x["title"])))


def scan_sources(root: Path) -> tuple[list[dict], list[dict]]:
    records = []
    albums = []
    if not root.is_dir():
        return records, albums
    for album_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        tracks = discover_source_tracks(album_dir)
        if tracks:
            albums.append({"name": canonical_album(album_dir.name), "path": album_dir, "tracks": len(tracks)})
            records.extend(tracks)
    return records, albums


# ---------------------------------------------------------------------------
# Sessions Ableton
# ---------------------------------------------------------------------------


def parse_als(path: Path) -> dict:
    raw = path.read_bytes()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    text = raw.decode("utf-8", errors="replace")
    tempo_match = re.search(r"<Tempo>.*?<Manual Value=\"([\d.]+)\"", text, re.S)
    tempo = float(tempo_match.group(1)) if tempo_match else None
    tracks = {
        "midi": len(re.findall(r"<MidiTrack\b", text)),
        "audio": len(re.findall(r"<AudioTrack\b", text)),
        "return": len(re.findall(r"<ReturnTrack\b", text)),
    }
    names = []
    for match in re.finditer(r'<EffectiveName Value="([^"]*)"', text):
        name = clean(match.group(1))
        if name and name not in names:
            names.append(name)
    return {
        "tempo": tempo,
        "midi_tracks": tracks["midi"],
        "audio_tracks": tracks["audio"],
        "return_tracks": tracks["return"],
        "tracks_total": tracks["midi"] + tracks["audio"],
        "clips": len(re.findall(r"<Clip\b", text)),
        "audio_clips": len(re.findall(r"<AudioClip\b", text)),
        "midi_clips": len(re.findall(r"<MidiClip\b", text)),
        "track_names": names[:12],
        "xml_chars": len(text),
    }


def scan_als(root: Path) -> list[dict]:
    if not root.is_dir():
        return []
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    cache = {}
    if CACHE.is_file():
        try:
            cache = json.loads(CACHE.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            cache = {}

    records = []
    paths = [
        p
        for p in root.rglob("*.als")
        if p.is_file() and "Backup" not in p.parts
    ]
    for index, path in enumerate(paths, 1):
        if index % 50 == 0:
            print(f"  ALS {index}/{len(paths)}…")
        stat = path.stat()
        key = f"{path}|{stat.st_mtime_ns}|{stat.st_size}"
        parsed = cache.get(key)
        if not parsed:
            try:
                parsed = parse_als(path)
            except (OSError, EOFError, gzip.BadGzipFile, UnicodeError) as error:
                parsed = {"error": str(error)}
            cache[key] = parsed
        top = path.relative_to(root).parts[0]
        records.append(
            {
                "path": path,
                "album": canonical_album(top),
                "raw_album": top,
                "project": path.parent.name,
                "stem": path.stem,
                "tempo": parsed.get("tempo"),
                "midi_tracks": parsed.get("midi_tracks", 0),
                "audio_tracks": parsed.get("audio_tracks", 0),
                "tracks_total": parsed.get("tracks_total", 0),
                "clips": parsed.get("clips", 0),
                "track_names": parsed.get("track_names", []),
                "updated": stat.st_mtime,
                "size": stat.st_size,
                "error": parsed.get("error"),
            }
        )
    CACHE.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
    return records


def scan_exports(root: Path) -> list[dict]:
    if not root.is_dir():
        return []
    records = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        kind = MEDIA_SUFFIXES.get(path.suffix.lower())
        if not kind:
            continue
        rel = path.relative_to(root)
        top = rel.parts[0] if len(rel.parts) > 1 else "_racine"
        records.append(
            {
                "path": path,
                "scope": canonical_album(top),
                "raw_scope": top,
                "stem": path.stem,
                "kind": kind,
                "size": path.stat().st_size,
                "updated": path.stat().st_mtime,
            }
        )
    return records


# ---------------------------------------------------------------------------
# Rapprochement
# ---------------------------------------------------------------------------


def source_album_matches(source_album: str, als_album: str) -> bool:
    a, b = norm(source_album), norm(als_album)
    if not a or not b:
        return False
    if a == b or a in b or b in a:
        return True
    return overlap(a, b) >= 0.5


def score_candidate(title: str, album: str, number: int | None, candidate: dict) -> float:
    stem = candidate["stem"]
    score = 0.0
    t, s = norm(match_title(title)), norm(match_title(stem))
    title_score = 0.0
    if t and s:
        if t == s:
            title_score += 10
        elif f" {t} " in f" {s} " or f" {s} " in f" {t} ":
            title_score += 6
        title_score += overlap(match_title(title), match_title(stem)) * 7
        if len(t) >= 6 and len(s) >= 6:
            ratio = SequenceMatcher(None, t, s).ratio()
            if ratio >= 0.88:
                title_score += ratio * 6
    score += title_score
    if number is not None and title_score >= 2.5:
        if re.match(rf"^0?{number}\b", s):
            score += 3
    if title_score > 0 and source_album_matches(album, candidate.get("album") or candidate.get("scope") or ""):
        score += 1
    return score


def match_records(track: dict, als: list[dict], exports: list[dict], single_album: bool = False) -> tuple[list[dict], list[dict], str]:
    als_candidates = [item for item in als if source_album_matches(track["album"], item["album"])]
    if not als_candidates:
        als_candidates = [
            item
            for item in als
            if norm(track["title"]) and norm(track["title"]) == norm(item["stem"])
        ]
    scored_als = sorted(
        ((score_candidate(track["title"], track["album"], track["number"], item), item) for item in als_candidates),
        key=lambda pair: (pair[0], pair[1]["updated"]),
        reverse=True,
    )
    scored_als = [(score, item) for score, item in scored_als if score >= 3.0]
    if not scored_als and single_album:
        scored_als = [
            (1.0, item)
            for item in sorted(als_candidates, key=lambda item: item["updated"], reverse=True)
        ]

    export_candidates = [item for item in exports if item["scope"].lower() in {track["album"].lower(), "_racine"}]
    if track["album"] == "Candidats 2027" and track["number"] is not None:
        filtered = []
        for item in export_candidates:
            number_match = re.match(r"^0?(\d{1,3})\b", item["stem"])
            if number_match and int(number_match.group(1)) != track["number"]:
                continue
            filtered.append(item)
        export_candidates = filtered
    if not export_candidates:
        export_candidates = [
            item
            for item in exports
            if norm(track["title"]) and norm(track["title"]) in norm(item["stem"])
        ]
    scored_exports = sorted(
        ((score_candidate(track["title"], track["album"], track["number"], item), item) for item in export_candidates),
        key=lambda pair: (pair[0], pair[1]["updated"]),
        reverse=True,
    )
    scored_exports = [(score, item) for score, item in scored_exports if score >= 2.5]
    if not scored_exports and single_album:
        scored_exports = [
            (1.0, item)
            for item in sorted(export_candidates, key=lambda item: item["updated"], reverse=True)
            if item["scope"].lower() == track["album"].lower()
        ]

    confidence = "faible"
    if not scored_als and not scored_exports:
        confidence = "sans objet"
    elif scored_als:
        confidence = "élevée" if scored_als[0][0] >= 7 else "moyenne"
    elif scored_exports:
        confidence = "moyenne"
    if single_album and (scored_als or scored_exports) and scored_als and scored_als[0][0] <= 1.0:
        confidence = "faible"
    return [item for _, item in scored_als], [item for _, item in scored_exports], confidence


def stage_for(track: dict, als: list[dict], exports: list[dict]) -> str:
    has_docs = bool(track["docs"])
    has_als = bool(als)
    has_audio = any(item["kind"] in {"mp3", "wav"} for item in exports)
    has_midi = any(item["kind"] == "midi" for item in exports)
    if has_docs and has_als and has_audio:
        return "maquette exportée"
    if has_docs and has_als:
        return "maquette Ableton"
    if has_als and has_audio:
        return "export + session"
    if has_docs and has_audio:
        return "export sans session"
    if has_docs:
        return "documentation seule"
    if has_als:
        return "session seule"
    if has_audio:
        return "export seul"
    if has_midi:
        return "MIDI seul"
    return "à identifier"


def missing_for(track: dict, als: list[dict], exports: list[dict]) -> str:
    missing = []
    if not track["has_fiche"]:
        missing.append("fiche")
    if not track["has_paroles"]:
        missing.append("paroles")
    if not als:
        missing.append("session ALS")
    if not any(item["kind"] in {"mp3", "wav"} for item in exports):
        missing.append("export audio")
    return ", ".join(missing) or "—"


def make_id(album: str, title: str, number: int | None, seen: set[str]) -> str:
    base = f"{slug(album)}--{slug(title)}"
    if number is not None:
        base = f"{slug(album)}--{number:02d}-{slug(title)}"
    candidate = base
    index = 2
    while candidate in seen:
        candidate = f"{base}-{index}"
        index += 1
    seen.add(candidate)
    return candidate


def choose_track_for(candidate: dict, tracks: list[dict], *, is_export: bool) -> tuple[dict | None, float]:
    """Choisit la meilleure production source pour une session ou un export."""
    if is_export:
        scope = candidate["scope"]
        album_candidates = [t for t in tracks if t["album"].lower() == scope.lower()]
        candidates = album_candidates if scope != "_racine" and album_candidates else tracks
    else:
        album_candidates = [t for t in tracks if source_album_matches(t["album"], candidate["album"])]
        exact_candidates = [
            t for t in tracks if norm(t["title"]) == norm(candidate["stem"])
        ]
        candidates = list({id(t): t for t in album_candidates + exact_candidates}.values())

    best: tuple[float, dict] | None = None
    for track in candidates:
        if is_export and track["album"] == "Candidats 2027" and track["number"] is not None:
            number_match = re.match(r"^0?(\d{1,3})\b", candidate["stem"])
            if number_match and int(number_match.group(1)) != track["number"]:
                continue
        score = score_candidate(track["title"], track["album"], track["number"], candidate)
        if best is None or score > best[0]:
            best = (score, track)
    threshold = 2.5 if is_export else 3.0
    if best and best[0] >= threshold:
        return best[1], best[0]
    return None, 0.0


def build() -> tuple[list[dict], list[dict], list[dict], list[dict], list[dict]]:
    source_tracks, source_albums = scan_sources(DEFAULT_SOURCES)
    print(f"Sources : {len(source_tracks)} productions dans {len(source_albums)} albums")
    print("Sessions Ableton : scan…")
    als = scan_als(DEFAULT_ALS)
    print(f"  {len(als)} sessions principales")
    exports = scan_exports(DEFAULT_EXPORTS)
    print(f"Exports : {len(exports)} fichiers audio/MIDI")

    assigned_als: set[str] = set()
    assigned_exports: set[str] = set()
    seen_ids: set[str] = set()
    productions = []
    album_track_counts = Counter(track["album"] for track in source_tracks)
    als_assign: dict[int, list[tuple[float, dict]]] = defaultdict(list)
    export_assign: dict[int, list[tuple[float, dict]]] = defaultdict(list)

    # Rapprochement global : chaque session/export va à la production la plus proche.
    for item in als:
        track, score = choose_track_for(item, source_tracks, is_export=False)
        if track is not None:
            als_assign[id(track)].append((score, item))
    for item in exports:
        track, score = choose_track_for(item, source_tracks, is_export=True)
        if track is not None:
            export_assign[id(track)].append((score, item))

    assigned_als.update(str(item["path"]) for values in als_assign.values() for _, item in values)
    assigned_exports.update(str(item["path"]) for values in export_assign.values() for _, item in values)

    # Repli pour les albums à une seule production (sessions restées orphelines).
    for track in source_tracks:
        if not als_assign.get(id(track)) and album_track_counts[track["album"]] == 1:
            for item in als:
                if str(item["path"]) in assigned_als:
                    continue
                if source_album_matches(track["album"], item["album"]):
                    als_assign[id(track)].append((1.0, item))
                    assigned_als.add(str(item["path"]))
        if not export_assign.get(id(track)) and album_track_counts[track["album"]] == 1:
            for item in exports:
                if str(item["path"]) in assigned_exports:
                    continue
                if item["scope"] == track["album"]:
                    export_assign[id(track)].append((1.0, item))
                    assigned_exports.add(str(item["path"]))

    for track in source_tracks:
        als_values = sorted(
            als_assign.get(id(track), []),
            key=lambda pair: (-pair[0], -pair[1]["updated"]),
        )
        export_values = sorted(
            export_assign.get(id(track), []),
            key=lambda pair: (-pair[0], -pair[1]["updated"]),
        )
        als_matches = [item for _, item in als_values]
        export_matches = [item for _, item in export_values]
        best_als = als_values[0][0] if als_values else 0.0
        best_export = export_values[0][0] if export_values else 0.0
        if als_matches:
            confidence = "élevée" if best_als >= 7 else ("moyenne" if best_als >= 3 else "faible")
        elif export_matches:
            confidence = "moyenne" if best_export >= 2.5 else "faible"
        else:
            confidence = "sans objet"

        mp3 = next((item for item in export_matches if item["kind"] == "mp3"), None)
        wav = next((item for item in export_matches if item["kind"] == "wav"), None)
        midi = next((item for item in export_matches if item["kind"] == "midi"), None)
        productions.append(
            {
                "id": make_id(track["album"], track["title"], track["number"], seen_ids),
                "album": track["album"],
                "number": track["number"],
                "title": track["title"],
                "candidate": track["candidate"],
                "stage": stage_for(track, als_matches, export_matches),
                "docs": "fiche + paroles" if track["has_fiche"] and track["has_paroles"] else ("documents" if track["has_fiche"] else ("paroles" if track["has_paroles"] else "")),
                "lyrics": track["lyrics"],
                "als_main": als_matches[0]["path"] if als_matches else None,
                "als_count": len(als_matches),
                "als_tempo": als_matches[0]["tempo"] if als_matches else None,
                "als_tracks": als_matches[0]["tracks_total"] if als_matches else None,
                "als_clips": als_matches[0]["clips"] if als_matches else None,
                "als_updated": als_matches[0]["updated"] if als_matches else None,
                "mp3": mp3["path"] if mp3 else None,
                "wav": wav["path"] if wav else None,
                "midi": midi["path"] if midi else None,
                "tempo": track["tempo"] or (f"{als_matches[0]['tempo']:g} BPM" if als_matches and als_matches[0]["tempo"] else ""),
                "key": track["key"],
                "signature": track["signature"],
                "duration": track["duration"],
                "style": track["style"],
                "atmosphere": track["atmosphere"],
                "summary": track["summary"],
                "intention": track["intention"],
                "status_source": track["status_source"],
                "missing": missing_for(track, als_matches, export_matches),
                "confidence": confidence,
                "source_path": track["source_dir"],
                "updated": max(track["updated"], als_matches[0]["updated"] if als_matches else 0),
                "als_matches": als_matches,
                "export_matches": export_matches,
                "kind": "source",
            }
        )

    # Sessions Ableton non rattachées : une ligne par stem distinct et par album.
    unassigned = [item for item in als if str(item["path"]) not in assigned_als]
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for item in unassigned:
        groups[(item["album"], norm(item["stem"]))].append(item)
    for (album, _), items in sorted(groups.items()):
        items.sort(key=lambda item: item["updated"], reverse=True)
        main = items[0]
        export_matches = [
            item
            for item in exports
            if str(item["path"]) not in assigned_exports
            and score_candidate(main["stem"], album, None, item) >= 2.5
        ]
        export_matches.sort(key=lambda item: item["updated"], reverse=True)
        assigned_exports.update(str(item["path"]) for item in export_matches)
        mp3 = next((item for item in export_matches if item["kind"] == "mp3"), None)
        wav = next((item for item in export_matches if item["kind"] == "wav"), None)
        midi = next((item for item in export_matches if item["kind"] == "midi"), None)
        productions.append(
            {
                "id": make_id(album, main["stem"], None, seen_ids),
                "album": album,
                "number": None,
                "title": re.sub(r"^(Copie|Copy)\s+", "", main["stem"]).strip(),
                "candidate": "",
                "stage": "session seule" if not export_matches else "export + session",
                "docs": "",
                "lyrics": "aucune",
                "als_main": main["path"],
                "als_count": len(items),
                "als_tempo": main["tempo"],
                "als_tracks": main["tracks_total"],
                "als_clips": main["clips"],
                "als_updated": main["updated"],
                "mp3": mp3["path"] if mp3 else None,
                "wav": wav["path"] if wav else None,
                "midi": midi["path"] if midi else None,
                "tempo": f"{main['tempo']:g} BPM" if main["tempo"] else "",
                "key": "",
                "signature": "",
                "duration": "",
                "style": "",
                "atmosphere": " · ".join(main["track_names"][:4]),
                "summary": "Session Ableton sans fiche source. Pistes : " + ", ".join(main["track_names"][:6]) if main["track_names"] else "Session Ableton sans fiche source.",
                "intention": "",
                "status_source": "",
                "missing": "fiche, paroles" + ("" if export_matches else ", export audio"),
                "confidence": "sans objet",
                "source_path": None,
                "updated": max([main["updated"]] + [item["updated"] for item in export_matches]),
                "als_matches": items,
                "export_matches": export_matches,
                "kind": "als",
            }
        )

    # Exports non rattachés.
    for item in exports:
        if str(item["path"]) in assigned_exports:
            continue
        productions.append(
            {
                "id": make_id(item["scope"], item["stem"], None, seen_ids),
                "album": item["scope"],
                "number": None,
                "title": item["stem"],
                "candidate": "",
                "stage": "export seul",
                "docs": "",
                "lyrics": "aucune",
                "als_main": None,
                "als_count": 0,
                "als_tempo": None,
                "als_tracks": None,
                "als_clips": None,
                "als_updated": None,
                "mp3": item["path"] if item["kind"] == "mp3" else None,
                "wav": item["path"] if item["kind"] == "wav" else None,
                "midi": item["path"] if item["kind"] == "midi" else None,
                "tempo": "",
                "key": "",
                "signature": "",
                "duration": "",
                "style": "",
                "atmosphere": "",
                "summary": "Export sans fiche ni session identifiée.",
                "intention": "",
                "status_source": "",
                "missing": "fiche, paroles, session ALS",
                "confidence": "sans objet",
                "source_path": None,
                "updated": item["updated"],
                "als_matches": [],
                "export_matches": [item],
                "kind": "export",
            }
        )

    return productions, als, exports, source_tracks, source_albums


# ---------------------------------------------------------------------------
# Écriture
# ---------------------------------------------------------------------------


def iso_date(timestamp: float | None) -> str:
    if not timestamp:
        return ""
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")


def rel(path: Path | None, root: Path | None = None) -> str:
    if not path:
        return ""
    p = Path(path)
    candidates = [
        (DEFAULT_ALS, "Ableton Live"),
        (DEFAULT_EXPORTS, "exports ableton"),
        (DEFAULT_SOURCES, "sources"),
        (ROOT, ""),
    ]
    for base, label in candidates:
        try:
            relative = p.resolve().relative_to(base.resolve()).as_posix()
        except (ValueError, OSError):
            continue
        return f"{label}/{relative}" if label else relative
    return p.as_posix()


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def md_cell(text: object, limit: int = 100) -> str:
    value = e(text)
    value = value.replace("|", "\\|")
    if len(value) > limit:
        value = value[: limit - 1].rstrip() + "…"
    return value or "—"


def write_markdown(productions: list[dict], source_albums: list[dict]) -> None:
    by_album: dict[str, list[dict]] = defaultdict(list)
    for item in productions:
        by_album[item["album"]].append(item)

    total = len(productions)
    docs = sum(1 for item in productions if item["docs"])
    als_count = sum(1 for item in productions if item["als_main"])
    audio_count = sum(1 for item in productions if item["mp3"] or item["wav"])
    midi_count = sum(1 for item in productions if item["midi"])
    source_count = sum(1 for item in productions if item["kind"] == "source")
    als_only = sum(1 for item in productions if item["kind"] == "als")
    export_only = sum(1 for item in productions if item["kind"] == "export")

    lines = [
        "# Catalogue des productions",
        "",
        f"**Date d’inventaire** : 2026-11-15 · **Branche** : `plateforme-productions`  ",
        f"**Périmètre** : sources éditoriales, sessions Ableton Live et exports audio/MIDI.",
        "",
        "> Première passe automatique. Les rapprochements sont heuristiques : la colonne",
        "> `Confiance` indique `élevée`, `moyenne` ou `faible`. Les lignes `faible` sont à",
        "> vérifier manuellement. Les fichiers sources n’ont pas été modifiés.",
        "",
        "## Vue d’ensemble",
        "",
        "| Indicateur | Nombre |",
        "| :--- | ---: |",
        f"| Productions cataloguées | {total} |",
        f"| Productions avec documentation | {docs} |",
        f"| Productions avec session Ableton | {als_count} |",
        f"| Productions avec export audio | {audio_count} |",
        f"| Productions avec MIDI | {midi_count} |",
        f"| Sessions ALS inventoriées | {sum(item['als_count'] for item in productions)} |",
        f"| Productions issues des sources | {source_count} |",
        f"| Lignes ALS sans fiche source | {als_only} |",
        f"| Exports sans production identifiée | {export_only} |",
        "",
        "## Productions par album",
        "",
        "| Album | Productions | Docs | ALS | Audio | MIDI | Manque le plus fréquent |",
        "| :--- | ---: | ---: | ---: | ---: | ---: | :--- |",
    ]
    for album in sorted(by_album, key=lambda name: norm(name)):
        items = by_album[album]
        missing = Counter()
        for item in items:
            for part in item["missing"].split(","):
                part = part.strip()
                if part and part != "—":
                    missing[part] += 1
        common = missing.most_common(3)
        common_text = ", ".join(f"{name} ({count})" for name, count in common) or "—"
        lines.append(
            f"| {md_cell(album, 44)} | {len(items)} | "
            f"{sum(1 for x in items if x['docs'])} | "
            f"{sum(1 for x in items if x['als_main'])} | "
            f"{sum(1 for x in items if x['mp3'] or x['wav'])} | "
            f"{sum(1 for x in items if x['midi'])} | {md_cell(common_text, 60)} |"
        )

    lines += ["", "## Productions documentées", ""]
    source_by_album: dict[str, list[dict]] = defaultdict(list)
    for item in productions:
        if item["kind"] == "source":
            source_by_album[item["album"]].append(item)

    for album in sorted(source_by_album, key=lambda name: norm(name)):
        items = source_by_album[album]
        lines += [
            f"### {album}",
            "",
            "| N° | Production | Statut | Confiance | ALS | Audio | Tempo | Tonalité | Intention / particularité | Manque |",
            "| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        ]
        for item in sorted(items, key=lambda x: (x["number"] or 999, norm(x["title"]))):
            als_label = f"{item['als_count']} session(s)" if item["als_count"] > 1 else ("1 session" if item["als_main"] else "—")
            audio_label = "MP3" if item["mp3"] else ("WAV" if item["wav"] else "—")
            summary = item["summary"] or item["atmosphere"] or item["status_source"] or "—"
            lines.append(
                f"| {item['number'] or '—'} | {md_cell(item['title'], 48)} | "
                f"{md_cell(item['stage'], 28)} | {item['confidence']} | "
                f"{als_label} | {audio_label} | "
                f"{md_cell(item['tempo'], 14)} | {md_cell(item['key'], 18)} | "
                f"{md_cell(summary, 110)} | {md_cell(item['missing'], 44)} |"
            )
        lines.append("")

    weak = [
        item
        for item in productions
        if item["kind"] == "source" and item["confidence"] == "faible"
    ]
    if weak:
        lines += [
            "## Rapprochements à vérifier",
            "",
            "> Ces productions ont un rattachement automatique de confiance faible.",
            "> Vérifier la session et l’export proposés avant de les considérer comme acquis.",
            "",
            "| Album | Production | Session proposée | Export proposé |",
            "| :--- | :--- | :--- | :--- |",
        ]
        for item in sorted(weak, key=lambda x: (norm(x["album"]), norm(x["title"]))):
            session = rel(item["als_main"], ROOT) if item["als_main"] else "—"
            export = item["mp3"] or item["wav"] or item["midi"] or ""
            lines.append(
                f"| {md_cell(item['album'], 30)} | {md_cell(item['title'], 44)} | "
                f"{md_cell(session, 70)} | {md_cell(rel(Path(export), ROOT) if export else '', 70)} |"
            )
        lines.append("")

    lines += [
        "## Sessions Ableton sans fiche source",
        "",
        "> Le détail de chaque version `.als` est dans `als_versions.csv`. Cette vue",
        "> regroupe les sessions par album.",
        "",
        "| Album | Lignes / versions | Sessions | Audio | Exemples de titres | Manque |",
        "| :--- | ---: | ---: | ---: | :--- | :--- |",
    ]
    als_by_album: dict[str, list[dict]] = defaultdict(list)
    for item in productions:
        if item["kind"] == "als":
            als_by_album[item["album"]].append(item)
    for album in sorted(als_by_album, key=lambda name: norm(name)):
        items = als_by_album[album]
        examples = " · ".join(md_cell(item["title"], 34) for item in items[:4])
        missing = Counter()
        for item in items:
            for part in item["missing"].split(","):
                part = part.strip()
                if part and part != "—":
                    missing[part] += 1
        common = ", ".join(f"{name} ({count})" for name, count in missing.most_common(3)) or "—"
        lines.append(
            f"| {md_cell(album, 38)} | {len(items)} | "
            f"{sum(item['als_count'] for item in items)} | "
            f"{sum(1 for item in items if item['mp3'] or item['wav'])} | "
            f"{md_cell(examples, 100)} | {md_cell(common, 60)} |"
        )

    lines += [
        "",
        "## Exports sans production identifiée",
        "",
        "| Export | Type | Date | Chemin |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for item in sorted(
        (x for x in productions if x["kind"] == "export"),
        key=lambda x: norm(x["title"]),
    ):
        kind = "MP3" if item["mp3"] else ("WAV" if item["wav"] else "MIDI")
        path = item["mp3"] or item["wav"] or item["midi"] or ""
        path_label = rel(Path(path), ROOT) if path else ""
        lines.append(
            f"| {md_cell(item['title'], 60)} | {kind} | {iso_date(item['updated'])} | {md_cell(path_label, 100)} |"
        )

    lines += [
        "",
        "## Fichiers",
        "",
        "- `productions.csv` : une ligne par production, tous les champs.",
        "- `productions.json` : version structurée pour un futur site.",
        "- `als_versions.csv` : chaque session Ableton principale, avec tempo, pistes, clips et rattachement.",
        "- `exports.csv` : chaque export audio/MIDI et son rattachement.",
        "- `README.md` : méthode, conventions et prochaines étapes.",
        "",
        "## Lecture des statuts",
        "",
        "- **maquette exportée** : docs + session ALS + export audio.",
        "- **maquette Ableton** : docs + session ALS, sans export audio.",
        "- **documentation seule** : paroles/fiche, pas encore de session.",
        "- **session seule** : `.als` sans fiche source.",
        "- **export seul** : MP3/WAV/MIDI sans fiche ni session identifiée.",
        "",
        "## Prochaines étapes proposées",
        "",
        "1. Corriger les rapprochements `faible` dans `productions.csv`.",
        "2. Compléter les fiches manquantes pour les sessions seules.",
        "3. Exporter les maquettes sans audio et ajouter les MIDI.",
        "4. Ajouter une colonne « album éditorial » et un statut de validation musicale.",
        "5. Faire du catalogue la base d’une plateforme multi-albums.",
    ]
    (CATALOG / "PRODUCTIONS.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    global DEFAULT_SOURCES, DEFAULT_ALS, DEFAULT_EXPORTS
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--als", type=Path, default=DEFAULT_ALS)
    parser.add_argument("--exports", type=Path, default=DEFAULT_EXPORTS)
    args = parser.parse_args()

    DEFAULT_SOURCES, DEFAULT_ALS, DEFAULT_EXPORTS = args.sources, args.als, args.exports
    CATALOG.mkdir(parents=True, exist_ok=True)

    productions, als, exports, source_tracks, source_albums = build()
    fields = [
        "id", "album", "number", "title", "candidate", "stage", "docs", "lyrics",
        "als_main", "als_count", "als_tempo", "als_tracks", "als_clips", "als_updated",
        "mp3", "wav", "midi", "tempo", "key", "signature", "duration", "style",
        "atmosphere", "summary", "intention", "status_source", "missing", "confidence",
        "source_path", "updated", "kind",
    ]
    csv_rows = []
    for item in productions:
        row = dict(item)
        for key in ("als_main", "mp3", "wav", "midi", "source_path"):
            row[key] = rel(row[key], ROOT) if row[key] else ""
        row["als_updated"] = iso_date(row["als_updated"])
        row["updated"] = iso_date(row["updated"])
        csv_rows.append(row)
    write_csv(CATALOG / "productions.csv", csv_rows, fields)

    json_rows = []
    for item in productions:
        row = dict(item)
        row["als_main"] = rel(row["als_main"], ROOT) if row["als_main"] else ""
        row["mp3"] = rel(row["mp3"], ROOT) if row["mp3"] else ""
        row["wav"] = rel(row["wav"], ROOT) if row["wav"] else ""
        row["midi"] = rel(row["midi"], ROOT) if row["midi"] else ""
        row["source_path"] = rel(row["source_path"], ROOT) if row["source_path"] else ""
        row["als_updated"] = iso_date(row["als_updated"])
        row["updated"] = iso_date(row["updated"])
        row["als_matches"] = [
            {
                "stem": x["stem"],
                "project": x["project"],
                "path": rel(x["path"], ROOT),
                "tempo": x["tempo"],
                "tracks": x["tracks_total"],
                "clips": x["clips"],
                "updated": iso_date(x["updated"]),
            }
            for x in row["als_matches"]
        ]
        row["export_matches"] = [
            {
                "stem": x["stem"],
                "kind": x["kind"],
                "path": rel(x["path"], ROOT),
                "size": x["size"],
                "updated": iso_date(x["updated"]),
            }
            for x in row["export_matches"]
        ]
        json_rows.append(row)
    (CATALOG / "productions.json").write_text(
        json.dumps(json_rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    als_fields = ["album", "project", "stem", "tempo", "tracks_total", "clips", "updated", "size", "path"]
    write_csv(
        CATALOG / "als_versions.csv",
        [
            {
                **item,
                "path": rel(item["path"], ROOT),
                "updated": iso_date(item["updated"]),
            }
            for item in sorted(als, key=lambda x: (norm(x["album"]), norm(x["stem"]), -x["updated"]))
        ],
        als_fields,
    )

    export_fields = ["scope", "stem", "kind", "size", "updated", "path"]
    write_csv(
        CATALOG / "exports.csv",
        [
            {
                **item,
                "path": rel(item["path"], ROOT),
                "updated": iso_date(item["updated"]),
            }
            for item in sorted(exports, key=lambda x: (norm(x["scope"]), norm(x["stem"]), x["kind"]))
        ],
        export_fields,
    )

    write_markdown(productions, source_albums)

    (CATALOG / "README.md").write_text(
        "# Catalogue des productions\n\n"
        "Ce dossier est généré par `scripts/build_catalog.py`.\n\n"
        "## Fichiers\n\n"
        "- `PRODUCTIONS.md` : vue lisible, groupée par album.\n"
        "- `productions.csv` : une ligne par production.\n"
        "- `productions.json` : données structurées pour un futur site.\n"
        "- `als_versions.csv` : inventaire des sessions `.als` principales.\n"
        "- `exports.csv` : inventaire des exports audio/MIDI.\n\n"
        "## Régénérer\n\n"
        "```powershell\npython scripts/build_catalog.py\n```\n\n"
        "Les sources sont lues en lecture seule. Seul `catalog/` est écrit.\n",
        encoding="utf-8",
    )

    print(f"✓ catalogue écrit dans {CATALOG}")
    print(f"  {len(productions)} productions · {len(als)} sessions ALS · {len(exports)} exports")


if __name__ == "__main__":
    main()
