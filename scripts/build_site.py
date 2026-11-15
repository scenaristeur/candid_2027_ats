#!/usr/bin/env python3
"""Génère le site de présentation de l'album « Candidats 2027 ».

Les sources sont ouvertes en LECTURE SEULE. Aucun fichier n'est écrit dans
`ableton-holland-mcp/sources` ni dans le dossier Ableton Live. Toutes les
sorties vont dans `docs/`, prêt pour GitHub Pages.

Usage :
    python scripts/build_site.py
    python scripts/build_site.py --sources "D:/chemin/sources" --als "D:/chemin/als"

Variables d'environnement équivalentes : CANDIDAT_SOURCES, CANDIDAT_ALS_DIR.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import sys
import unicodedata
import zipfile
from datetime import date
from pathlib import Path
from urllib.parse import quote

import markdown as md

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

DEFAULT_SOURCES = Path(
    os.environ.get(
        "CANDIDAT_SOURCES",
        r"C:\Users\admin\dev\ableton-holland-mcp\sources\Candid_2027_ats",
    )
)
DEFAULT_ALS = Path(
    os.environ.get(
        "CANDIDAT_ALS_DIR",
        r"C:\Users\admin\Music\Ableton Live\Candid_2027_ats",
    )
)

REPO_URL = "https://github.com/scenaristeur/candid_2027_ats"
ARCHIVE_ITEM_URL = "https://archive.org/details/candidats-2027-exports"
SITE_URL = os.environ.get("CANDIDAT_SITE_URL", "https://scenaristeur.github.io/candid_2027_ats").rstrip("/")
TRUTH_DATE = "14 novembre 2026"
ALBUM_DATE_ISO = "2026-11-14"
GOOGLE_SITE_VERIFICATION = "a5K2yNZpsgoUVcvzllet8yvUxdDlO5TJaP8tZLZsK-I"
ALBUM_NAME = "Candidats 2027 — l’album"
ALBUM_DESCRIPTION = (
    "Les maquettes de l’album Candidats 2027 : une chanson par candidat à la "
    "présidentielle de 2027. Paroles, fiches techniques et sessions Ableton à "
    "télécharger. Contributions ouvertes aux musicien·nes et surtout aux chanteur·ses."
)

# Palette éditoriale : une couleur par titre, cyclique.
PALETTE = [
    ("#a63a2c", "#f3ddd6"),
    ("#1f5a49", "#d7e8df"),
    ("#284b7a", "#dbe4f2"),
    ("#783a62", "#efdce8"),
    ("#8a5a1c", "#f2e3cc"),
    ("#3e5b2c", "#e0ead5"),
    ("#8a2f48", "#f3d9e2"),
    ("#2f596a", "#d8e9ee"),
]

PARTICLES = {"de", "du", "des", "le", "la", "les", "van", "von", "di", "d'", "l'"}


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def format_size(num: int) -> str:
    if num >= 1024 * 1024:
        return f"{num / (1024 * 1024):.1f} Mo"
    if num >= 1024:
        return f"{num / 1024:.0f} Ko"
    return f"{num} o"


def slugify(text: str) -> str:
    return md.slugify(text)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def initials(name: str) -> str:
    words = [
        word
        for word in re.split(r"[\s\-]+", name)
        if word and word.lower() not in PARTICLES
    ]
    return "".join(word[0] for word in words[:2]).upper() or "27"


def clean_meta(value: str) -> tuple[str, bool]:
    proposal = "proposition" in value.lower()
    value = re.sub(r"\s*\*\([^*]*\)\*", "", value)
    value = re.sub(r"\s*\(proposition[^)]*\)", "", value, flags=re.IGNORECASE)
    value = md.strip_markdown(value)
    return value.strip(), proposal


def parse_meta(text: str) -> dict[str, tuple[str, bool]]:
    head = text.split("\n---", 1)[0]
    meta: dict[str, tuple[str, bool]] = {}
    for line in head.splitlines():
        match = re.match(r"\*\*(.+?)\*\*\s*:\s*(.+)$", line)
        if match:
            meta[md.strip_markdown(match.group(1))] = clean_meta(match.group(2))
    return meta


def section(text: str, prefix: str) -> list[str]:
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.startswith("## ") and md.strip_markdown(line[3:]).startswith(prefix):
            start = index + 1
            break
    if start is None:
        return []
    result = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        result.append(line)
    return result


def parse_brief(text: str) -> dict[str, str]:
    brief: dict[str, str] = {}
    for line in section(text, "1."):
        if not line.strip().startswith("|"):
            continue
        cells = md._split_row(line)
        if len(cells) < 2 or set(cells[0]) <= set("-: "):
            continue
        key = md.strip_markdown(cells[0])
        value = md.strip_markdown("|".join(cells[1:]))
        if key and value:
            brief[key] = value
    return brief


def parse_goals(text: str) -> list[str]:
    goals = []
    for line in section(text, "2."):
        match = re.match(r"\s*[-*+]\s+(.*)$", line)
        if match:
            goals.append(md.strip_markdown(match.group(1)))
    return goals


def parse_checks(text: str) -> list[str]:
    checks = []
    for line in section(text, "7."):
        match = re.match(r"\s*[-*+]\s+(.*)$", line)
        if match:
            checks.append(md.strip_markdown(match.group(1)))
    return checks


def load_tracks(sources: Path, als_dir: Path) -> list[dict]:
    als_files: dict[int, Path] = {}
    if als_dir.is_dir():
        for path in als_dir.rglob("*.als"):
            if not path.is_file() or "Backup" in path.parts:
                continue
            match = re.match(r"^(\d{2})\s*-", path.name)
            if match:
                als_files[int(match.group(1))] = path

    long_files: dict[int, Path] = {}
    long_dir = sources / "_versions_longues"
    if long_dir.is_dir():
        for path in long_dir.iterdir():
            match = re.match(r"^(\d{2})\s*-", path.name)
            if match and path.suffix.lower() == ".md":
                long_files[int(match.group(1))] = path

    tracks = []
    for folder in sorted(p for p in sources.iterdir() if p.is_dir()):
        if not re.match(r"^\d{2}\s*-\s*", folder.name):
            continue
        num = int(folder.name[:2])
        fiche_path = folder / "FICHE_TECHNIQUE.md"
        paroles_path = folder / "PAROLES.md"
        if not fiche_path.is_file() or not paroles_path.is_file():
            continue

        fiche = fiche_path.read_text(encoding="utf-8")
        paroles = paroles_path.read_text(encoding="utf-8")
        meta = parse_meta(fiche)

        heading = next((line[2:].strip() for line in fiche.splitlines() if line.startswith("# ")), "")
        parts = re.split(r"\s+—\s+", heading, maxsplit=2)
        if len(parts) == 3:
            _, candidate, title = parts
        else:
            fallback = folder.name.split(" - ", 2)
            candidate = fallback[1]
            title = fallback[2]

        brief = parse_brief(fiche)
        style_full = meta.get("Style", ("", False))[0]
        style_short = style_full.split(",")[0].strip() if style_full else ""
        accent, accent_soft = PALETTE[(num - 1) % len(PALETTE)]
        full_lyrics = any(
            line.startswith("## ") and "Couplet" in line for line in paroles.splitlines()
        )

        als_path = als_files.get(num)
        long_path = long_files.get(num)

        tracks.append(
            {
                "num": num,
                "candidate": candidate.strip(),
                "title": title.strip(),
                "slug": f"{num:02d}-{slugify(candidate)}-{slugify(title)}",
                "folder": folder,
                "meta": meta,
                "tempo": meta.get("Tempo", ("", False))[0],
                "key": meta.get("Tonalité", ("", False))[0],
                "signature": meta.get("Signature", ("", False))[0],
                "duration": meta.get("Durée cible", ("", False))[0],
                "atmosphere": meta.get("Atmosphère", ("", False))[0],
                "style": style_full,
                "style_short": style_short,
                "status": meta.get("Statut", ("", False))[0],
                "proposal": any(proposal for _, proposal in meta.values()),
                "brief": brief,
                "goals": parse_goals(fiche),
                "checks": parse_checks(fiche),
                "fiche": fiche,
                "paroles": paroles,
                "full_lyrics": full_lyrics,
                "accent": accent,
                "accent_soft": accent_soft,
                "initials": initials(candidate),
                "als": als_path,
                "long": long_path,
                "audio": find_audio(folder.name[:2]),
            }
        )
    return tracks


def find_audio(num: str) -> Path | None:
    audio_dir = SITE / "audio"
    if not audio_dir.is_dir():
        return None
    for suffix in (".mp3", ".ogg", ".m4a", ".wav"):
        candidate = audio_dir / f"{num}{suffix}"
        if candidate.is_file():
            return candidate
    return None


def load_media() -> dict[int, dict[str, dict]]:
    """Charge site/media.json (exports hébergés hors du dépôt).

    Par défaut, seuls les fichiers vérifiés (HTTP 200 sur Internet Archive)
    sont publiés : pas de lecteur cassé si l'upload n'a pas encore été fait.
    """
    path = SITE / "media.json"
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"⚠ site/media.json illisible ({error}) : médias ignorés.")
        return {}

    require_verified = bool(data.get("requireVerified", True))
    media: dict[int, dict[str, dict]] = {}
    for number, entry in (data.get("files") or {}).items():
        try:
            track_number = int(number)
        except (TypeError, ValueError):
            continue
        for kind in ("mp3", "midi"):
            item = entry.get(kind)
            if not item or not item.get("url"):
                continue
            item = dict(item)
            item["_verified"] = bool(item.get("verified"))
            item["_required_verified"] = require_verified
            media.setdefault(track_number, {})[kind] = item
    return media


# --------------------------------------------------------------------------
# Fragments HTML
# --------------------------------------------------------------------------


def jsonld_tag(data: object) -> str:
    raw = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    raw = raw.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return f'<script type="application/ld+json">{raw}</script>'


def duration_iso(value: str) -> str | None:
    match = re.search(r"(\d+)\s*min(?:\s*(\d+))?", value or "")
    if not match:
        return None
    minutes = int(match.group(1))
    seconds = int(match.group(2) or 0)
    parts = "PT"
    if minutes:
        parts += f"{minutes}M"
    if seconds or not minutes:
        parts += f"{seconds}S"
    return parts


def album_jsonld(tracks: list[dict]) -> dict:
    track_nodes = []
    for track in tracks:
        node = {
            "@type": "MusicRecording",
            "@id": f"{SITE_URL}/titres/{track['slug']}.html#recording",
            "name": track["title"],
            "url": f"{SITE_URL}/titres/{track['slug']}.html",
            "trackNumber": track["num"],
            "inLanguage": "fr-FR",
            "byArtist": {"@id": f"{SITE_URL}/#organization"},
            "album": {"@id": f"{SITE_URL}/#album"},
        }
        iso = duration_iso(track["duration"])
        if iso:
            node["duration"] = iso
        if track.get("media", {}).get("mp3"):
            node["audio"] = {
                "@type": "AudioObject",
                "contentUrl": track["media"]["mp3"]["url"],
                "encodingFormat": "audio/mpeg",
            }
        track_nodes.append(node)

    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{SITE_URL}/#website",
                "url": f"{SITE_URL}/",
                "name": "Candidats 2027",
                "description": ALBUM_DESCRIPTION,
                "inLanguage": "fr-FR",
                "publisher": {"@id": f"{SITE_URL}/#organization"},
            },
            {
                "@type": "Organization",
                "@id": f"{SITE_URL}/#organization",
                "name": "Candidats 2027",
                "url": f"{SITE_URL}/",
                "sameAs": [REPO_URL, ARCHIVE_ITEM_URL],
            },
            {
                "@type": "MusicAlbum",
                "@id": f"{SITE_URL}/#album",
                "name": ALBUM_NAME,
                "alternateName": "Candidats 2027",
                "description": ALBUM_DESCRIPTION,
                "url": f"{SITE_URL}/",
                "image": f"{SITE_URL}/assets/og/album.png",
                "datePublished": ALBUM_DATE_ISO,
                "dateModified": ALBUM_DATE_ISO,
                "inLanguage": "fr-FR",
                "numTracks": len(tracks),
                "isAccessibleForFree": True,
                "byArtist": {"@id": f"{SITE_URL}/#organization"},
                "track": track_nodes,
            },
        ],
    }


def song_jsonld(track: dict, description: str, image_url: str) -> dict:
    page_url = f"{SITE_URL}/titres/{track['slug']}.html"
    recording = {
        "@type": "MusicRecording",
        "@id": f"{page_url}#recording",
        "name": track["title"],
        "url": page_url,
        "trackNumber": track["num"],
        "inLanguage": "fr-FR",
        "isAccessibleForFree": True,
        "datePublished": ALBUM_DATE_ISO,
        "dateModified": ALBUM_DATE_ISO,
        "image": image_url,
        "byArtist": {"@id": f"{SITE_URL}/#organization"},
        "album": {"@id": f"{SITE_URL}/#album"},
        "about": {
            "@type": "Person",
            "name": track["candidate"],
            "description": track["brief"].get("Profil", "")[:600],
        },
    }
    iso = duration_iso(track["duration"])
    if iso:
        recording["duration"] = iso
    mp3 = track.get("media", {}).get("mp3")
    if mp3:
        recording["audio"] = {
            "@type": "AudioObject",
            "name": f"{track['candidate']} — {track['title']} (MP3)",
            "contentUrl": mp3["url"],
            "encodingFormat": "audio/mpeg",
            "uploadDate": ALBUM_DATE_ISO,
        }
    return {
        "@context": "https://schema.org",
        "@graph": [
            recording,
            {
                "@type": "BreadcrumbList",
                "@id": f"{page_url}#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "L’album",
                        "item": f"{SITE_URL}/",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": track["title"],
                        "item": page_url,
                    },
                ],
            },
            {
                "@type": "WebPage",
                "@id": page_url,
                "url": page_url,
                "name": f"{track['num']:02d} — {track['candidate']} — {track['title']}",
                "description": description,
                "inLanguage": "fr-FR",
                "datePublished": ALBUM_DATE_ISO,
                "dateModified": ALBUM_DATE_ISO,
                "isPartOf": {"@id": f"{SITE_URL}/#album"},
                "primaryImageOfPage": {"@type": "ImageObject", "url": image_url},
            },
        ],
    }


def webpage_jsonld(name: str, description: str, page_path: str, image_url: str, page_type: str = "WebPage") -> dict:
    page_url = f"{SITE_URL}/{page_path}"
    return {
        "@context": "https://schema.org",
        "@type": page_type,
        "@id": page_url,
        "url": page_url,
        "name": name,
        "description": description,
        "inLanguage": "fr-FR",
        "datePublished": ALBUM_DATE_ISO,
        "dateModified": ALBUM_DATE_ISO,
        "isPartOf": {"@id": f"{SITE_URL}/#website"},
        "primaryImageOfPage": {"@type": "ImageObject", "url": image_url},
        "about": {"@id": f"{SITE_URL}/#album"},
    }


def head(
    title: str,
    description: str,
    depth: int,
    *,
    page_path: str,
    accent: str = "#a63a2c",
    og_type: str = "website",
    og_image: str = "assets/og/album.png",
    keywords: str = "",
    jsonld: object | None = None,
    noindex: bool = False,
) -> str:
    prefix = "../" * depth
    canonical = f"{SITE_URL}/{page_path}" if page_path else f"{SITE_URL}/"
    image_url = f"{SITE_URL}/{og_image.lstrip('/')}"
    robots = (
        "noindex, nofollow"
        if noindex
        else "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    )
    ld = jsonld_tag(jsonld) if jsonld else ""
    extra = '<meta name="color-scheme" content="light dark">'
    if og_type == "article":
        extra += f'<meta property="article:published_time" content="{ALBUM_DATE_ISO}">'
    if og_type == "music.song":
        extra += (
            f'<meta property="music:release_date" content="{ALBUM_DATE_ISO}">'
            f'<meta property="music:album" content="{SITE_URL}/">'
            f'<meta property="music:musician" content="{SITE_URL}/">'
        )
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta name="author" content="Candidats 2027">
<meta name="robots" content="{robots}">
<meta name="keywords" content="{e(keywords)}">
<meta name="theme-color" content="{e(accent)}">
{extra}
<meta name="generator" content="scripts/build_site.py">
<link rel="canonical" href="{e(canonical)}">
<link rel="alternate" hreflang="fr" href="{e(canonical)}">
<meta property="og:type" content="{e(og_type)}">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Candidats 2027 — l’album">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{e(canonical)}">
<meta property="og:image" content="{e(image_url)}">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(title)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(description)}">
<meta name="twitter:image" content="{e(image_url)}">
<meta name="twitter:image:alt" content="{e(title)}">
<meta name="google-site-verification" content="{GOOGLE_SITE_VERIFICATION}">
<link rel="sitemap" type="application/xml" href="{SITE_URL}/sitemap.xml">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}assets/style.css">
{ld}
<script>try{{var t=localStorage.getItem('theme');if(!t&&matchMedia('(prefers-color-scheme: dark)').matches)t='dark';if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
</head>"""


def header(depth: int, active: str = "") -> str:
    prefix = "../" * depth
    home = f"{prefix}index.html"
    links = [
        ("titres", f"{home}#titres", "Les titres"),
        ("catalogue", f"{prefix}catalogue.html", "Catalogue"),
        ("projet", f"{prefix}projet.html", "Le projet"),
        ("participer", f"{prefix}participer.html", "Participer"),
    ]
    nav = "".join(
        f'<a href="{href}"' + (' aria-current="page"' if key == active else "") + f">{label}</a>"
        for key, href, label in links
    )
    return f"""<a class="skip-link" href="#contenu">Aller au contenu</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{home}" aria-label="Candidats 2027, accueil">
      <span class="brand-mark" aria-hidden="true">31</span>
      <span class="brand-text"><strong>Candidats 2027</strong><small>l’album</small></span>
    </a>
    <nav class="main-nav" aria-label="Navigation principale">{nav}</nav>
    <div class="header-tools">
      <a class="github-link" href="{REPO_URL}" rel="noopener" aria-label="Dépôt GitHub">GitHub<span aria-hidden="true">↗</span></a>
      <button class="theme-toggle" type="button" data-theme-toggle aria-label="Changer de thème">
        <span class="theme-icon" aria-hidden="true"></span>
      </button>
    </div>
  </div>
</header>"""


def footer(depth: int) -> str:
    prefix = "../" * depth
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <p class="footer-brand">Candidats 2027 — l’album</p>
      <p class="footer-note">Un album d’information civique : une chanson par candidat à la présidentielle de 2027. Ce sont pour l’instant des maquettes — musicien·nes et surtout chanteur·ses, les contributions sont ouvertes.</p>
    </div>
    <nav aria-label="Liens de pied de page">
      <a href="{prefix}index.html#titres">Les titres</a>
      <a href="{prefix}projet.html">Le projet</a>
      <a href="{prefix}participer.html">Participer</a>
      <a href="{prefix}telechargements/candidats-2027-pack.zip">Tout télécharger</a>
      <a href="{REPO_URL}" rel="noopener">GitHub</a>
    </nav>
    <div>
      <p class="footer-meta">Date de vérité : {TRUTH_DATE}</p>
      <p class="footer-meta">Titres, paroles et musiques générés par IA : brouillons de vulgarisation, potentiellement erronés. Exercice de collaboration musicale et culturelle, sans intention de favoriser ou défavoriser un candidat ; neutralité et égalité de traitement.</p>
      <p class="footer-meta">Textes, musiques et sessions : © leurs auteurs. Diffusion pour l’écoute, l’étude et la reprise ; nous contacter pour tout autre usage.</p>
      <p class="footer-meta">Site statique généré depuis les sources du projet. Aucun traceur.</p>
    </div>
  </div>
</footer>
<script src="{prefix}assets/app.js" defer></script>"""


def ai_banner(depth: int) -> str:
    prefix = "../" * depth
    return f"""<div class="ai-banner" role="note">
  <div class="wrap">
    <span class="ai-tag">IA</span>
    <p><strong>Titres, paroles et musiques générés par IA.</strong> Exercice de collaboration musicale et culturelle, pas un outil politique : aucun candidat n’est soutenu ni défavorisé. Brouillons de vulgarisation, potentiellement erronés — <a href="{prefix}participer.html">corrections bienvenues</a>.</p>
  </div>
</div>"""


def page(
    title: str,
    description: str,
    depth: int,
    body: str,
    *,
    page_path: str,
    accent: str = "#a63a2c",
    active: str = "",
    og_type: str = "website",
    og_image: str = "assets/og/album.png",
    keywords: str = "",
    jsonld: object | None = None,
    noindex: bool = False,
) -> str:
    return f"""{head(title, description, depth, page_path=page_path, accent=accent, og_type=og_type, og_image=og_image, keywords=keywords, jsonld=jsonld, noindex=noindex)}
<body>
{ai_banner(depth)}
{header(depth, active)}
<main id="contenu">
{body}
</main>
{footer(depth)}
</body>
</html>
"""


def cover(track: dict, *, large: bool = False) -> str:
    cls = "cover cover-large" if large else "cover"
    return f"""<div class="{cls}" style="--accent:{e(track['accent'])};--accent-soft:{e(track['accent_soft'])}" aria-hidden="true">
  <span class="cover-rule"></span>
  <span class="cover-num">{track['num']:02d}</span>
  <span class="cover-initials">{e(track['initials'])}</span>
  <span class="cover-style">{e(track['style_short'] or 'Chanson')}</span>
  <span class="cover-ring"></span>
</div>"""


def badges(track: dict) -> str:
    items = []
    if track["als"]:
        items.append('<span class="badge badge-als">Session .als</span>')
    if track.get("has_audio"):
        items.append('<span class="badge badge-media">MP3</span>')
    if track.get("has_midi"):
        items.append('<span class="badge badge-media">MIDI</span>')
    if track["full_lyrics"]:
        items.append('<span class="badge badge-full">Paroles complètes</span>')
    else:
        items.append('<span class="badge">Refrain seul</span>')
    if track["long"]:
        items.append('<span class="badge badge-long">Version longue</span>')
    return "".join(items)


def track_card(track: dict, depth: int = 0) -> str:
    prefix = "../" * depth
    href = f"{prefix}titres/{track['slug']}.html"
    search = normalize(
        f"{track['num']:02d} {track['candidate']} {track['title']} {track['style']} {track['atmosphere']}"
        + (" mp3 audio" if track.get("has_audio") else "")
        + (" midi" if track.get("has_midi") else "")
    )
    return f"""<article class="track-card" data-track data-als="{1 if track['als'] else 0}" data-audio="{1 if track.get('has_audio') else 0}" data-midi="{1 if track.get('has_midi') else 0}" data-lyrics="{'full' if track['full_lyrics'] else 'refrain'}" data-search="{e(search)}">
  <a class="track-link" href="{href}">
    {cover(track)}
    <div class="track-body">
      <p class="track-candidate">{e(track['candidate'])}</p>
      <h3 class="track-title">{e(track['title'])}</h3>
      <p class="track-meta">{e(track['tempo'] or '—')} · {e(track['key'] or '—')} · {e(track['duration'] or '—')}</p>
      <div class="badges">{badges(track)}</div>
    </div>
  </a>
</article>"""


def download_card(
    *,
    kind: str,
    title: str,
    description: str,
    href: str | None,
    meta: str,
    unavailable: str = "",
    extra_link: str = "",
    external: bool = False,
) -> str:
    icon = {
        "als": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 18V6h3l2 4 2-4h3v12h-2.6V9.8L9 14 6.6 9.8V18H4Zm13 0V6h2.8v9.7H23V18h-6Z"/></svg>',
        "md": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h9l5 5v15H6V2Zm8 1.5V8h4.5L14 3.5ZM8 12v6h1.7v-3.4L11 17l1.3-2.4V18H14v-6h-1.7l-1.3 2.5L9.7 12H8Zm7 0v6h2.4a2 2 0 0 0 2-2v-2a2 2 0 0 0-2-2H15Zm1.7 1.5h.7c.2 0 .3.1.3.3v2.4c0 .2-.1.3-.3.3h-.7v-3Z"/></svg>',
        "zip": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h12v20H6V2Zm6 1.5h-1.5V5H12V3.5Zm0 3h-1.5V8H12V6.5Zm0 3h-1.5V11H12V9.5Zm0 3h-1.5v2.5h3V12h-1.5Zm-1.5 6h3v1.5h-3V18Z"/></svg>',
        "long": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v2H4V5Zm0 4h16v2H4V9Zm0 4h10v2H4v-2Zm0 4h7v2H4v-2Z"/></svg>',
        "audio": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18.5A2.5 2.5 0 1 1 6.5 16c.4 0 .8.1 1.1.2V5l9-1.5v3L9.7 7.9v10.6ZM18 15.5a2.5 2.5 0 1 1-2.5-2.5c.4 0 .8.1 1.1.2V7l-3.9.7v2l2.9-.5v6.3Z"/></svg>',
        "midi": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18v14H3V5Zm2 2v10h14V7H5Zm2 2h2v6H7V9Zm4 0h2v3h-2V9Zm0 4h2v2h-2v-2Zm4-4h2v6h-2V9Z"/></svg>',
    }[kind]
    if href:
        external_attrs = ' target="_blank" rel="noopener"' if external else " download"
        return f"""<a class="download-card" href="{href}"{external_attrs}>
  <span class="dl-icon">{icon}</span>
  <span class="dl-text">
    <span class="dl-title">{e(title)}</span>
    <span class="dl-desc">{e(description)}</span>
    <span class="dl-meta">{e(meta)}</span>
  </span>
  <span class="dl-arrow" aria-hidden="true">↓</span>
</a>"""
    return f"""<div class="download-card is-unavailable">
  <span class="dl-icon">{icon}</span>
  <span class="dl-text">
    <span class="dl-title">{e(title)}</span>
    <span class="dl-desc">{e(unavailable)}</span>
    <span class="dl-meta">{e(meta)}</span>
  </span>
  {extra_link}
</div>"""


def contribute_block(track: dict | None = None) -> str:
    voice_link = f"{SITE_URL}/participer.html#voix"
    if track:
        title = quote(f"[Correction] {track['num']:02d} — {track['candidate']} — {track['title']}")
        correction = f"{REPO_URL}/issues/new?template=correction.yml&title={title}"
        contribution_title = quote(f"[Contribution] {track['num']:02d} — {track['candidate']}")
        contribution = f"{REPO_URL}/issues/new?template=contribution.yml&title={contribution_title}"
        voice_title = quote(
            f"[Contribution] {track['num']:02d} — {track['candidate']} — voix / interprétation"
        )
        voice_link = f"{REPO_URL}/issues/new?template=contribution.yml&title={voice_title}"
        intro = f"Une voix, un instrument, une source datée pour «&nbsp;{e(track['title'])}&nbsp;» ?"
    else:
        correction = f"{REPO_URL}/issues/new?template=correction.yml"
        contribution = f"{REPO_URL}/issues/new?template=contribution.yml"
        intro = "Une voix, un instrument, une source datée ?"
    return f"""<section class="contribute" aria-labelledby="contribuer-titre">
  <div class="contribute-inner">
    <p class="eyebrow">Participer</p>
    <h2 id="contribuer-titre">Le projet est ouvert.</h2>
    <p>{intro} Les maquettes sont là pour être reprises : musicien·nes et surtout chanteur·ses, vos contributions sont sollicitées. Le site, les paroles et les fiches sont versionnés : chaque proposition peut être discutée et tracée.</p>
    <div class="contribute-actions">
      <a class="btn btn-primary" href="{voice_link}">Proposer une voix<span aria-hidden="true">↗</span></a>
      <a class="btn btn-ghost" href="{correction}">Proposer une correction factuelle<span aria-hidden="true">↗</span></a>
      <a class="btn btn-ghost" href="{contribution}">Contribuer à une chanson<span aria-hidden="true">↗</span></a>
      <a class="btn btn-ghost" href="{REPO_URL}" rel="noopener">Voir le dépôt<span aria-hidden="true">↗</span></a>
    </div>
    <p class="contribute-note">Règle du projet : on critique le programme, le coût, la faisabilité ou la stratégie — jamais la personne. Tout chiffre doit venir avec sa source et sa date. L’album ne soutient ni ne combat aucun candidat : neutralité et égalité de traitement.</p>
  </div>
</section>"""


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------


def build_index(tracks: list[dict]) -> str:
    total = len(tracks)
    als_count = sum(1 for t in tracks if t["als"])
    full_count = sum(1 for t in tracks if t["full_lyrics"])
    refrain_count = total - full_count
    audio_count = sum(1 for t in tracks if t.get("has_audio"))
    midi_count = sum(1 for t in tracks if t.get("has_midi"))
    mp3_total = sum(1 for t in tracks if t.get("has_mp3_export"))
    midi_total = sum(1 for t in tracks if t.get("has_midi_export"))
    mp3_label = "exports MP3" + (
        f" · {audio_count} en ligne" if audio_count != mp3_total else ""
    )
    midi_label = "exports MIDI" + (
        f" · {midi_count} en ligne" if midi_count != midi_total else ""
    )
    media_stats = f'<div><strong>{mp3_total}</strong><span>{mp3_label}</span></div>'
    if midi_total:
        media_stats += f'<div><strong>{midi_total}</strong><span>{midi_label}</span></div>'
    media_filters = ""
    if audio_count:
        media_filters += f'<button type="button" class="filter" data-filter="audio" aria-pressed="false">MP3 <span>{audio_count}</span></button>'
    if midi_count:
        media_filters += f'<button type="button" class="filter" data-filter="midi" aria-pressed="false">MIDI <span>{midi_count}</span></button>'

    cards = "\n".join(track_card(track) for track in tracks)
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="kicker"><span class="kicker-dot" aria-hidden="true"></span>Album d’information civique · maquettes générées par IA · présidentielle 2027 <span class="status-pill">maquettes</span></p>
      <h1>Candidats<br><em>2027</em></h1>
      <p class="lede">{total} chansons, un candidat par titre. Pour l’instant, ce sont des <strong>maquettes</strong> : les voix, les arrangements et le mix restent à faire. Comprendre ce qui distingue chaque programme, ce qu’il promet, ce qu’il coûte — et ce qu’on peut lui opposer.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#titres">Explorer les {total} titres</a>
        <a class="btn btn-ghost" href="participer.html#voix">Proposer une voix</a>
      </div>
      <p class="hero-note">Musicien·nes, chanteur·ses, interprètes : les maquettes sont ouvertes. Paroles, fiches techniques et sessions Ableton à télécharger. Sources datées du {TRUTH_DATE}.</p>
    </div>
    <div class="hero-poster" aria-hidden="true">
      <div class="poster">
        <span class="poster-ring"></span>
        <span class="poster-ring poster-ring-2"></span>
        <span class="poster-kicker">une chanson<br>par candidat</span>
        <span class="poster-num">31</span>
        <span class="poster-caption">titres · maquettes · paroles</span>
        <span class="poster-stamp">2027</span>
      </div>
    </div>
  </div>
</section>

<section class="stats" aria-label="Le projet en chiffres">
  <div class="wrap stats-grid">
    <div><strong>{total}</strong><span>maquettes</span></div>
    {media_stats}
    <div><strong>{als_count}</strong><span>sessions Ableton publiées</span></div>
    <div><strong>{full_count}</strong><span>paroles complètes</span></div>
    <div><strong>31</strong><span>fiches techniques</span></div>
  </div>
</section>

<section class="maquette-call" id="maquettes" aria-labelledby="maquettes-titre">
  <div class="wrap maquette-grid">
    <div>
      <p class="eyebrow">État du projet</p>
      <h2 id="maquettes-titre">Ce sont encore<br><em>des maquettes.</em></h2>
    </div>
    <div class="maquette-text">
      <p>Les {total} titres existent aujourd’hui à l’état d’ébauches : paroles, fiches techniques, sessions Ableton, exports MP3 et MIDI. Les voix, les arrangements, l’interprétation et le mix restent largement à faire.</p>
      <p><strong>Nous cherchons des musicien·nes — et surtout des chanteur·ses.</strong> Une voix, une guitare, un piano, une basse, des cuivres, un beat, un mix : chaque contribution peut faire avancer un titre. Les maquettes sont là pour être reprises, pas pour être figées.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="participer.html#voix">Proposer une voix</a>
        <a class="btn btn-ghost" href="{REPO_URL}/issues/new?template=contribution.yml&title=%5BContribution%5D%20instrument%20ou%20mix">Proposer un instrument ou un mix</a>
      </div>
    </div>
  </div>
</section>

<section class="tracks-section" id="titres">
  <div class="wrap">
    <div class="section-head">
      <div>
        <p class="eyebrow">L’album</p>
        <h2>Les {total} titres</h2>
        <p class="section-lede">Un ordre de passage tiré au sort, un style par candidat. Clique pour ouvrir la page du morceau, lire les paroles et télécharger les fichiers.</p>
      </div>
      <div class="section-count" aria-live="polite"><strong data-count>{total}</strong><span>titres affichés</span></div>
    </div>

    <div class="toolbar">
      <div class="search-field">
        <label for="track-search">Rechercher</label>
        <input id="track-search" type="search" placeholder="Candidat, titre, style…" autocomplete="off" data-search-input>
        <kbd aria-hidden="true">/</kbd>
      </div>
      <div class="filters" role="group" aria-label="Filtrer les titres">
        <button type="button" class="filter is-active" data-filter="all" aria-pressed="true">Tout <span>{total}</span></button>
        <button type="button" class="filter" data-filter="als" aria-pressed="false">Session .als <span>{als_count}</span></button>
        <button type="button" class="filter" data-filter="full" aria-pressed="false">Paroles complètes <span>{full_count}</span></button>
        <button type="button" class="filter" data-filter="refrain" aria-pressed="false">Refrain seul <span>{refrain_count}</span></button>
        {media_filters}
      </div>
    </div>

    <div class="track-grid" data-track-grid>
      {cards}
    </div>
    <p class="empty-state" data-empty hidden>Aucun titre ne correspond à cette recherche.</p>
  </div>
</section>

<section class="manifesto">
  <div class="wrap manifesto-grid">
    <div>
      <p class="eyebrow">Le principe</p>
      <h2>Une chanson, pas un tract.</h2>
    </div>
    <div class="manifesto-text">
      <p>Chaque titre suit la même forme : ce qui distingue le candidat, son discours, le point de vue de ses partisans, puis un refrain. Le refrain porte l’identité ; les autres sections nourrissent le sens.</p>
      <p>Le projet ne soutient ni ne combat aucun candidat. C’est un exercice de collaboration musicale et culturelle partagé, pas un outil politique visant à favoriser ou défavoriser une candidature : la démarche souhaite respecter la neutralité et l’égalité de traitement entre les candidats. Il cherche à rendre les programmes comparables, à rappeler leur coût et leurs conditions de faisabilité, et à distinguer la critique du programme de l’attaque personnelle.</p>
      <a class="text-link" href="projet.html">Lire la note d’intention et les règles éditoriales<span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

{contribute_block()}
"""
    return page(
        "Candidats 2027 — les maquettes de l’album",
        ALBUM_DESCRIPTION,
        0,
        body,
        page_path="",
        accent="#a63a2c",
        active="titres",
        og_type="music.album",
        og_image="assets/og/album.png",
        keywords=(
            "Candidats 2027, album, maquettes, chansons, présidentielle 2027, "
            "paroles, fiches techniques, Ableton, IA, chanteur, chanteuse, "
            "musicien, contribution, vulgarisation, neutralité"
        ),
        jsonld=album_jsonld(tracks),
    )


def build_song(track: dict, tracks: list[dict]) -> str:
    index = tracks.index(track)
    previous = tracks[index - 1] if index > 0 else None
    following = tracks[index + 1] if index + 1 < len(tracks) else None

    fiche_body = track["fiche"]
    # Retire le titre et le bloc de métadonnées déjà affichés dans l'en-tête.
    if "\n---" in fiche_body:
        fiche_body = fiche_body.split("\n---", 1)[1]
    fiche_html = md.render(fiche_body, demote=0)

    paroles_html = track["paroles"]
    paroles_html = re.sub(r"^# .*\n", "", paroles_html, count=1)
    paroles_html = md.render(paroles_html, breaks=True)

    prefix = "../"
    correction_title = quote(
        f"[Correction] {track['num']:02d} — {track['candidate']} — {track['title']}"
    )
    correction_url = f"{REPO_URL}/issues/new?template=correction.yml&title={correction_title}"
    voice_issue_title = quote(
        f"[Contribution] {track['num']:02d} — {track['candidate']} — voix / interprétation"
    )
    voice_issue_url = f"{REPO_URL}/issues/new?template=contribution.yml&title={voice_issue_title}"
    instrument_title = quote(
        f"[Contribution] {track['num']:02d} — {track['candidate']} — instrument / arrangement"
    )
    instrument_url = f"{REPO_URL}/issues/new?template=contribution.yml&title={instrument_title}"
    als_issue_title = quote(
        f"[Contribution] {track['num']:02d} — {track['candidate']} — session Ableton"
    )
    als_card = download_card(
        kind="als",
        title="Session Ableton (.als)",
        description="Ouvrir, écouter, remixer, proposer une version.",
        href=f"{prefix}telechargements/als/{track['slug']}.als" if track["als"] else None,
        meta=f"Live 12 · {format_size(track['als'].stat().st_size)}" if track["als"] else "Fichier non publié",
        unavailable="La session de ce morceau n’est pas encore publiée. Les paroles et la fiche sont disponibles.",
        extra_link=f'<a class="dl-inline-link" href="{REPO_URL}/issues/new?template=contribution.yml&title={als_issue_title}">Proposer une session ↗</a>',
    )
    long_card = ""
    if track["long"]:
        long_card = download_card(
            kind="long",
            title="Version longue (archive)",
            description="Version d’écriture développée, conservée comme référence.",
            href=f"{prefix}telechargements/versions-longues/{track['slug']}.version-longue.md",
            meta=f"Markdown · {format_size(track['long'].stat().st_size)}",
        )

    media = track.get("media") or {}
    mp3 = media.get("mp3")
    midi = media.get("midi")
    audio_src = None
    audio_source = ""
    if mp3:
        audio_src = mp3["url"]
        audio_source = "Internet Archive"
    elif track["audio"]:
        audio_src = f"{prefix}audio/{track['audio'].name}"
        audio_source = "fichier local"

    audio_card = ""
    if audio_src:
        audio_card = f"""<figure class="audio-card">
  <figcaption class="audio-head">
    <span class="audio-label">Écouter</span>
    <strong>Export audio</strong>
    <span class="audio-source">{e(audio_source)}</span>
  </figcaption>
  <audio controls preload="metadata" src="{e(audio_src)}"></audio>
</figure>"""

    media_cards = ""
    if mp3:
        media_cards += download_card(
            kind="audio",
            title="Export MP3",
            description="Écoute et téléchargement. Fichier hébergé hors du dépôt Git.",
            href=mp3["url"],
            meta=f"MP3 · {format_size(int(mp3.get('bytes') or 0))} · Internet Archive"
            if mp3.get("bytes")
            else "MP3 · Internet Archive",
            external=True,
        )
    if midi:
        media_cards += download_card(
            kind="midi",
            title="Export MIDI",
            description="Partitions et pistes MIDI, à réouvrir dans ton DAW.",
            href=midi["url"],
            meta=f"MIDI · {format_size(int(midi.get('bytes') or 0))} · Internet Archive"
            if midi.get("bytes")
            else "MIDI · Internet Archive",
            external=True,
        )

    brief = track["brief"]
    for_label = brief.get("Pour", "")
    against_label = brief.get("Contre", "")
    profile = brief.get("Profil", "")
    program = brief.get("Programme 2027", "")
    actuality = brief.get("Actualité", "")
    transition = brief.get("Transition Marseillaise", "")
    actions = brief.get("Actions déjà menées", "")
    color = brief.get("Couleur politique", "")

    goals = "".join(f"<li>{e(goal)}</li>" for goal in track["goals"])
    checks = "".join(f"<li>{e(check)}</li>" for check in track["checks"])

    brief_block = ""
    if profile or program:
        for_block = (
            f'<div class="argument argument-for"><h4>Ce que le brief met en avant</h4><p>{e(for_label)}</p></div>'
            if for_label
            else ""
        )
        against_block = (
            f'<div class="argument argument-against"><h4>Ce que le brief oppose</h4><p>{e(against_label)}</p></div>'
            if against_label
            else ""
        )
        details = []
        if color:
            details.append(f"<div><dt>Couleur politique</dt><dd>{e(color)}</dd></div>")
        if actions:
            details.append(f"<div><dt>Actions déjà menées</dt><dd>{e(actions)}</dd></div>")
        if actuality:
            details.append(f"<div><dt>Actualité</dt><dd>{e(actuality)}</dd></div>")
        if transition:
            details.append(f"<div><dt>Transition « Marseillaise »</dt><dd>{e(transition)}</dd></div>")
        brief_block = f"""<section class="brief-section" id="en-bref" aria-labelledby="en-bref-titre">
  <div class="wrap">
    <div class="section-head compact">
      <div>
        <p class="eyebrow">Carte d’identité</p>
        <h2 id="en-bref-titre">En bref</h2>
      </div>
      <p class="section-source">Synthèse issue du brief interne du {TRUTH_DATE}. À vérifier avant enregistrement.</p>
    </div>
    <div class="brief-grid">
      <div class="brief-main">
        <h3>Profil</h3>
        <p>{e(profile)}</p>
        <h3>Programme 2027</h3>
        <p>{e(program)}</p>
        <dl class="brief-details">{''.join(details)}</dl>
      </div>
      <div class="brief-arguments">
        {for_block}
        {against_block}
      </div>
    </div>
  </div>
</section>"""

    goals_block = ""
    if goals:
        goals_block = f"""<section class="goals" aria-labelledby="objectifs-titre">
  <div class="wrap">
    <h2 id="objectifs-titre">Ce que la chanson doit faire</h2>
    <ul>{goals}</ul>
  </div>
</section>"""

    checks_block = ""
    if checks:
        checks_block = f"""<section class="checks" aria-labelledby="verifier-titre">
  <div class="wrap">
    <h2 id="verifier-titre">À vérifier avant d’enregistrer</h2>
    <ul>{checks}</ul>
    <p class="checks-note">Ces points sont des vigilances, pas des affirmations validées. Chaque chiffre doit pouvoir être daté et sourcé.</p>
  </div>
</section>"""

    status_text = track["status"]
    if track["als"] and "aucune session" in status_text.lower():
        status_text = "Session Ableton publiée — les métadonnées de la fiche restent à confirmer."

    lyrics_note = ""
    if not track["full_lyrics"]:
        lyrics_issue_title = quote(
            f"[Contribution] {track['num']:02d} — {track['candidate']} — paroles"
        )
        lyrics_note = f"""<aside class="lyrics-note">
  <p><strong>Refrain seul pour l’instant.</strong> Les couplets, le pont et les sections « point de vue des partisans » restent à écrire. C’est le format cible de l’album ; la porte est ouverte.</p>
  <a class="text-link" href="{REPO_URL}/issues/new?template=contribution.yml&title={lyrics_issue_title}">Proposer des couplets<span aria-hidden="true">→</span></a>
</aside>"""

    prev_link = (
        f'<a class="pager-link pager-prev" href="../titres/{previous["slug"]}.html"><span>← Titre {previous["num"]:02d}</span><strong>{e(previous["title"])}</strong><small>{e(previous["candidate"])}</small></a>'
        if previous
        else "<span></span>"
    )
    next_link = (
        f'<a class="pager-link pager-next" href="../titres/{following["slug"]}.html"><span>Titre {following["num"]:02d} →</span><strong>{e(following["title"])}</strong><small>{e(following["candidate"])}</small></a>'
        if following
        else "<span></span>"
    )

    proposal_note = (
        "<p class=\"proposal-note\">Tempo, tonalité et durée sont des propositions de travail, à valider à l’oreille.</p>"
        if track["proposal"]
        else ""
    )

    body = f"""
<div class="wrap">
  <nav class="breadcrumb" aria-label="Fil d’Ariane">
    <a href="../index.html">L’album</a><span aria-hidden="true">/</span><a href="../index.html#titres">Titres</a><span aria-hidden="true">/</span><span aria-current="page">{track['num']:02d}</span>
  </nav>
</div>

<header class="song-hero">
  <div class="wrap song-hero-grid">
    {cover(track, large=True)}
    <div class="song-intro">
      <p class="eyebrow">Titre {track['num']:02d} sur 31 · {e(track['style_short'] or 'Chanson')}</p>
      <h1 class="song-h1"><span class="h1-candidate">{e(track['candidate'])}</span><span class="h1-title">{e(track['title'])}</span></h1>
      <p class="song-lede">{e(track['atmosphere'])}{(' — ' + e(track['style'])) if track['style'] and track['style'] != track['atmosphere'] else ''}</p>
      <dl class="meta-chips">
        <div><dt>Tempo</dt><dd>{e(track['tempo'] or '—')}</dd></div>
        <div><dt>Tonalité</dt><dd>{e(track['key'] or '—')}</dd></div>
        <div><dt>Signature</dt><dd>{e(track['signature'] or '—')}</dd></div>
        <div><dt>Durée cible</dt><dd>{e(track['duration'] or '—')}</dd></div>
      </dl>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#telecharger">Télécharger les fichiers</a>
        <a class="btn btn-ghost" href="#paroles">Lire les paroles</a>
      </div>
      {proposal_note}
      <p class="status-line"><span class="status-dot" aria-hidden="true"></span>{e(status_text)}</p>
    </div>
  </div>
</header>

<aside class="voice-callout" aria-labelledby="voix-titre">
  <div class="voice-callout-text">
    <p class="eyebrow">Maquette ouverte</p>
    <h2 id="voix-titre">Il manque une voix.</h2>
    <p>Ce titre est encore une maquette. Tu chantes, tu joues d’un instrument, tu mixes ? Propose une interprétation, une piste ou un arrangement : les contributions de musicien·nes et surtout de chanteur·ses sont sollicitées.</p>
  </div>
  <div class="voice-callout-actions">
    <a class="btn btn-primary" href="{voice_issue_url}">Proposer une voix</a>
    <a class="btn btn-ghost" href="{instrument_url}">Proposer un instrument</a>
  </div>
</aside>

<section class="downloads-section" id="telecharger" aria-labelledby="telecharger-titre">
  <div class="wrap">
    <div class="section-head compact">
      <div>
        <p class="eyebrow">Fichiers sources</p>
        <h2 id="telecharger-titre">Télécharger</h2>
      </div>
      <p class="section-source">{'Session Ableton disponible' if track['als'] else 'Session Ableton à venir'} · paroles et fiche toujours disponibles.</p>
    </div>
    {audio_card}
    <div class="download-grid">
      {media_cards}
      {als_card}
      {download_card(kind="md", title="Paroles (Markdown)", description="Le texte complet, sections et notes de prudence.", href=f"{prefix}telechargements/paroles/{track['slug']}.paroles.md", meta=f"Markdown · {format_size(len(track['paroles'].encode('utf-8')))}")}
      {download_card(kind="md", title="Fiche technique (Markdown)", description="Brief, structure, palette, mix et steps de production.", href=f"{prefix}telechargements/fiches/{track['slug']}.fiche-technique.md", meta=f"Markdown · {format_size(len(track['fiche'].encode('utf-8')))}")}
      {long_card}
    </div>
    <p class="download-note">Les sessions Ableton, paroles et fiches sont copiées à l’identique depuis les sources du projet, sans modification. Les exports MP3 et MIDI sont hébergés sur Internet Archive pour ne pas alourdir le dépôt Git ; ils restent téléchargeables depuis cette page.</p>
  </div>
</section>

{brief_block}

<section class="lyrics-section" id="paroles" aria-labelledby="paroles-titre">
  <div class="wrap lyrics-layout">
    <div class="lyrics-head">
      <p class="eyebrow">Paroles</p>
      <h2 id="paroles-titre">Le texte</h2>
      <p class="section-source">Version de travail — le texte évolue à l’écoute et à la vérification des faits.</p>
    </div>
    <aside class="ai-note">
      <strong>Brouillon généré par IA.</strong> Les paroles et la fiche technique ci-dessous sont des ébauches de vulgarisation : elles peuvent contenir des erreurs, des approximations ou des maladresses. Cet album est un exercice de collaboration musicale et culturelle, pas un outil politique visant à favoriser ou défavoriser un candidat. <a href="{correction_url}">Signaler une erreur ou proposer une correction</a>.
    </aside>
    {lyrics_note}
    <article class="prose lyrics">
      {paroles_html}
    </article>
  </div>
</section>

{goals_block}

<section class="fiche-section" id="fiche" aria-labelledby="fiche-titre">
  <div class="wrap">
    <div class="section-head compact">
      <div>
        <p class="eyebrow">Production</p>
        <h2 id="fiche-titre">Fiche technique</h2>
      </div>
      <a class="text-link" href="{prefix}telechargements/fiches/{track['slug']}.fiche-technique.md">Télécharger le Markdown<span aria-hidden="true">↓</span></a>
    </div>
    <article class="prose fiche">
      {fiche_html}
    </article>
  </div>
</section>

{checks_block}

{contribute_block(track)}

<nav class="wrap pager" aria-label="Titres précédent et suivant">
  {prev_link}
  {next_link}
</nav>
"""
    description = (
        f"Paroles, fiche technique et maquette de « {track['title']} » "
        f"({track['candidate']}). Titre {track['num']:02d}/31 de l’album "
        "Candidats 2027, ouvert aux contributions."
    )
    image_rel = f"assets/og/{track['num']:02d}.png"
    image_url = f"{SITE_URL}/{image_rel}"
    return page(
        f"Paroles de « {track['title']} » — {track['candidate']} | Candidats 2027",
        description,
        1,
        body,
        page_path=f"titres/{track['slug']}.html",
        accent=track["accent"],
        active="titres",
        og_type="music.song",
        og_image=image_rel,
        keywords=(
            f"{track['candidate']}, {track['title']}, {track['style_short']}, "
            "maquette, chanson, présidentielle 2027, paroles, fiche technique, "
            "voix, chanteur, musicien, contribution, Candidats 2027"
        ),
        jsonld=song_jsonld(track, description, image_url),
    )


def build_project(album_text: str) -> str:
    # Sépare les lignes de métadonnées du préambule (Dossier / Date / État),
    # que Markdown fusionnerait sinon en un seul paragraphe.
    album_text = re.sub(
        r"(?m)^(\*\*[^\n]+\*\*\s*:.*)\n(?=\*\*)",
        r"\1\n\n",
        album_text,
    )
    body_html = md.render(album_text)
    body = f"""
<header class="page-hero">
  <div class="wrap narrow">
    <p class="eyebrow">Le projet</p>
    <h1>Une chanson par candidat.<br><em>Rien de plus, rien de moins.</em></h1>
    <p class="lede">Note d’intention, méthode de production et règles éditoriales de l’album Candidats 2027. Les titres, paroles et musiques sont générés par IA : ce sont pour l’instant des maquettes, potentiellement erronées. Les contributions de musicien·nes et surtout de chanteur·ses sont sollicitées. C’est un exercice de collaboration musicale et culturelle partagé, pas un outil politique visant à favoriser ou défavoriser un candidat ; la démarche vise la neutralité et l’égalité. Ce document est daté du {TRUTH_DATE}.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="telechargements/album/Album.MD" download>Télécharger la note (Markdown)</a>
      <a class="btn btn-ghost" href="index.html#titres">Voir les titres</a>
    </div>
  </div>
</header>
<section class="prose-page">
  <div class="wrap narrow">
    <article class="prose project">
      {body_html}
    </article>
  </div>
</section>
{contribute_block()}
"""
    description = (
        "Note d’intention, méthode de production et règles éditoriales de l’album "
        "Candidats 2027 : des maquettes générées par IA, ouvertes aux musicien·nes "
        "et surtout aux chanteur·ses."
    )
    return page(
        "Le projet · Candidats 2027",
        description,
        0,
        body,
        page_path="projet.html",
        active="projet",
        og_type="article",
        og_image="assets/og/album.png",
        keywords=(
            "Candidats 2027, projet, note d’intention, règles éditoriales, "
            "chansons, présidentielle 2027, IA, neutralité"
        ),
        jsonld=webpage_jsonld(
            "Le projet · Candidats 2027",
            description,
            "projet.html",
            f"{SITE_URL}/assets/og/album.png",
            "AboutPage",
        ),
    )


def build_contribute() -> str:
    correction = f"{REPO_URL}/issues/new?template=correction.yml"
    contribution = f"{REPO_URL}/issues/new?template=contribution.yml"
    voice = (
        f"{REPO_URL}/issues/new?template=contribution.yml&title="
        + quote("[Contribution] voix / interprétation")
    )
    instrument = (
        f"{REPO_URL}/issues/new?template=contribution.yml&title="
        + quote("[Contribution] instrument / arrangement")
    )
    body = f"""
<header class="page-hero">
  <div class="wrap narrow">
    <p class="eyebrow">Participer</p>
    <h1>Le projet est un<br><em>chantier ouvert.</em></h1>
    <p class="lede">Les paroles, les fiches et les sessions sont des ébauches générées par IA, publiées pour être lues, jouées, corrigées et surtout <strong>interprétées</strong>. Ce sont des maquettes : les voix, les arrangements et le mix restent à faire. L’album est un exercice de collaboration musicale et culturelle partagé, pas un outil politique : il ne vise ni à favoriser ni à défavoriser un candidat, et revendique la neutralité et l’égalité de traitement.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{voice}">Proposer une voix<span aria-hidden="true">↗</span></a>
      <a class="btn btn-ghost" href="{correction}">Signaler une erreur factuelle<span aria-hidden="true">↗</span></a>
      <a class="btn btn-ghost" href="{contribution}">Proposer une contribution<span aria-hidden="true">↗</span></a>
    </div>
  </div>
</header>

<section class="voice-section" id="voix" aria-labelledby="voix-titre">
  <div class="wrap voice-inner">
    <div>
      <p class="eyebrow">Appel à voix</p>
      <h2 id="voix-titre">Les maquettes attendent<br><em>des interprètes.</em></h2>
    </div>
    <div>
      <p>Les titres sont des maquettes : les instruments, les paroles et les fiches existent, mais les voix ne sont pas encore enregistrées. C’est le moment de proposer une interprétation, une couleur, une intention.</p>
      <p><strong>Chanteur·ses, chanteurs, chanteuses, musicien·nes :</strong> une voix lead, un chœur, une guitare, un piano, une basse, des cuivres, un beat ou un mix peuvent suffire à faire exister un titre. Aucune contribution n’est trop petite.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{voice}">Proposer une voix<span aria-hidden="true">↗</span></a>
        <a class="btn btn-ghost" href="{instrument}">Proposer un instrument<span aria-hidden="true">↗</span></a>
      </div>
    </div>
  </div>
</section>

<section class="participate">
  <div class="wrap">
    <div class="participate-grid">
      <article class="participate-card">
        <span class="participate-num">01</span>
        <h2>Vérifier un fait</h2>
        <p>Un chiffre, une date, un score, une procédure : signale le passage exact, la source et sa date. La hiérarchie du projet est simple : programme officiel, fait institutionnel daté, presse datée, brief interne.</p>
        <a class="text-link" href="{correction}">Ouvrir une correction<span aria-hidden="true">↗</span></a>
      </article>
      <article class="participate-card">
        <span class="participate-num">02</span>
        <h2>Écrire ou réécrire</h2>
        <p>Les titres 01 à 08 et 14 à 31 n’ont encore qu’un refrain. Couplets, ponts, sections « point de vue des partisans » : propose un texte qui tient la forme et les règles de prudence.</p>
        <a class="text-link" href="{contribution}">Proposer des paroles<span aria-hidden="true">↗</span></a>
      </article>
      <article class="participate-card">
        <span class="participate-num">03</span>
        <h2>Jouer, chanter, mixer</h2>
        <p>Une session Ableton est publiée pour chaque maquette disponible. Tu peux la reprendre, enregistrer une voix, changer un instrument ou mixer — à condition de documenter ce que tu changes dans la fiche technique.</p>
        <a class="text-link" href="index.html#titres">Voir les sessions<span aria-hidden="true">↗</span></a>
      </article>
      <article class="participate-card">
        <span class="participate-num">04</span>
        <h2>Améliorer le site</h2>
        <p>Le site est statique, généré depuis les sources du projet. Accessibilité, mise en page, liens, téléchargements : les propositions techniques sont bienvenues sur le dépôt.</p>
        <a class="text-link" href="{REPO_URL}" rel="noopener">Voir le dépôt<span aria-hidden="true">↗</span></a>
      </article>
    </div>
  </div>
</section>

<section class="rules">
  <div class="wrap narrow">
    <p class="eyebrow">Règles éditoriales</p>
    <h2>Ce qui tient le projet.</h2>
    <ol class="rules-list">
      <li><strong>Critiquer le programme, pas la personne.</strong> Coût, financement, faisabilité, majorité nécessaire, compatibilité constitutionnelle ou européenne, stratégie électorale, contradiction interne.</li>
      <li><strong>Aucun fait judiciaire dans un refrain.</strong> Une procédure n’est nommée que si elle est indispensable au sens : juridiction, date, statut exact — jamais résumée par un mot qui accuse.</li>
      <li><strong>Un chiffre = une source + une date.</strong> La chanson doit pouvoir dire « au {TRUTH_DATE} ».</li>
      <li><strong>Pas d’insinuation.</strong> Une formule qui laisse entendre sans documenter est retirée.</li>
      <li><strong>Nom officiel dans chaque refrain.</strong> Et pas de présentation comme candidat de quelqu’un qui ne l’est pas.</li>
      <li><strong>Les partisans parlent en leur nom.</strong> Leurs paroles sont présentées comme un point de vue, pas comme une vérité objective.</li>
      <li><strong>Neutralité et égalité.</strong> L’album est un exercice de collaboration musicale et culturelle, pas un support de campagne : aucun candidat n’est soutenu ni défavorisé, et chaque titre reçoit le même traitement.</li>
    </ol>
    <p class="rules-note">Ces règles sont issues de la note de projet. Elles s’appliquent à chaque refrain, à chaque fiche et à chaque contribution. L’album est une expérimentation éditoriale : les titres, paroles et musiques ont été générés par IA, sans valeur de validation factuelle. Chaque correction documentée est bienvenue.</p>
  </div>
</section>

<section class="workflow">
  <div class="wrap narrow">
    <p class="eyebrow">Méthode</p>
    <h2>Comment une contribution devient un titre.</h2>
    <div class="workflow-steps">
      <div><span>1</span><h3>Issue</h3><p>La proposition est ouverte sur GitHub avec le titre concerné, le passage visé et une source datée.</p></div>
      <div><span>2</span><h3>Discussion</h3><p>On vérifie le fait, on écoute la version existante, on discute de la formulation et du style.</p></div>
      <div><span>3</span><h3>Intégration</h3><p>Le texte ou la session est intégré, la fiche technique est mise à jour, le site est régénéré.</p></div>
      <div><span>4</span><h3>Écoute</h3><p>La maquette est validée à l’oreille par extraits avant d’être figée. On ne rouvre pas une maquette validée sans raison.</p></div>
    </div>
  </div>
</section>

{contribute_block()}
"""
    description = (
        "Contribuer à l’album Candidats 2027 : proposer une voix, un instrument, "
        "un mix, vérifier un fait, écrire des paroles ou améliorer le site. "
        "Les maquettes sont ouvertes aux musicien·nes et surtout aux chanteur·ses."
    )
    return page(
        "Participer · Candidats 2027",
        description,
        0,
        body,
        page_path="participer.html",
        active="participer",
        og_type="article",
        og_image="assets/og/album.png",
        keywords=(
            "Candidats 2027, participer, contribution, corrections, paroles, "
            "Ableton, chansons, présidentielle 2027"
        ),
        jsonld=webpage_jsonld(
            "Participer · Candidats 2027",
            description,
            "participer.html",
            f"{SITE_URL}/assets/og/album.png",
        ),
    )


def build_404() -> str:
    body = """
<header class="page-hero error-page">
  <div class="wrap narrow">
    <p class="eyebrow">Erreur 404</p>
    <h1>Ce titre n’est pas<br><em>au programme.</em></h1>
    <p class="lede">La page demandée n’existe pas ou a changé d’adresse. L’album, lui, est toujours là.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="index.html">Retour à l’album</a>
      <a class="btn btn-ghost" href="index.html#titres">Voir les titres</a>
    </div>
  </div>
</header>
"""
    return page(
        "Page introuvable · Candidats 2027",
        "La page demandée n’existe pas ou a changé d’adresse.",
        0,
        body,
        page_path="404.html",
        og_image="assets/og/album.png",
        noindex=True,
    )


# --------------------------------------------------------------------------
# Écriture
# --------------------------------------------------------------------------


def prepare_docs() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    for name in ("assets", "titres", "telechargements", "audio"):
        target = DOCS / name
        if target.exists():
            shutil.rmtree(target)
    for name in ("index.html", "projet.html", "participer.html", "404.html"):
        target = DOCS / name
        if target.exists():
            target.unlink()
    (DOCS / "titres").mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)


def copy_assets() -> None:
    assets_out = DOCS / "assets"
    assets_out.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SITE / "assets" / "style.css", assets_out / "style.css")
    shutil.copy2(SITE / "assets" / "app.js", assets_out / "app.js")
    shutil.copy2(SITE / "assets" / "favicon.svg", assets_out / "favicon.svg")
    if (SITE / "assets" / "catalogue.js").is_file():
        shutil.copy2(SITE / "assets" / "catalogue.js", assets_out / "catalogue.js")
    og_src = SITE / "assets" / "og"
    if og_src.is_dir():
        shutil.copytree(og_src, assets_out / "og", dirs_exist_ok=True)


def write_downloads(tracks: list[dict], sources: Path, album_text: str) -> None:
    base = DOCS / "telechargements"
    for sub in ("als", "paroles", "fiches", "versions-longues", "album"):
        (base / sub).mkdir(parents=True, exist_ok=True)

    for track in tracks:
        shutil.copyfile(
            track["folder"] / "PAROLES.md",
            base / "paroles" / f"{track['slug']}.paroles.md",
        )
        shutil.copyfile(
            track["folder"] / "FICHE_TECHNIQUE.md",
            base / "fiches" / f"{track['slug']}.fiche-technique.md",
        )
        if track["als"]:
            shutil.copy2(track["als"], base / "als" / f"{track['slug']}.als")
        if track["long"]:
            shutil.copyfile(
                track["long"],
                base / "versions-longues" / f"{track['slug']}.version-longue.md",
            )
        if track["audio"]:
            audio_out = DOCS / "audio"
            audio_out.mkdir(exist_ok=True)
            shutil.copy2(track["audio"], audio_out / track["audio"].name)

    shutil.copyfile(sources / "Album.MD", base / "album" / "Album.MD")

    manifest = {
        "album": "Candidats 2027",
        "truthDate": ALBUM_DATE_ISO,
        "generatedFrom": "ableton-holland-mcp/sources/Candid_2027_ats (lecture seule)",
        "tracks": [
            {
                "number": track["num"],
                "candidate": track["candidate"],
                "title": track["title"],
                "style": track["style"],
                "tempo": track["tempo"],
                "key": track["key"],
                "duration": track["duration"],
                "status": track["status"],
                "files": {
                    "als": f"als/{track['slug']}.als" if track["als"] else None,
                    "paroles": f"paroles/{track['slug']}.paroles.md",
                    "ficheTechnique": f"fiches/{track['slug']}.fiche-technique.md",
                    "versionLongue": f"versions-longues/{track['slug']}.version-longue.md"
                    if track["long"]
                    else None,
                },
                "media": {
                    "mp3": (track.get("media", {}).get("mp3") or {}).get("url"),
                    "midi": (track.get("media", {}).get("midi") or {}).get("url"),
                },
            }
            for track in tracks
        ],
    }
    (base / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    readme = f"""CANDIDATS 2027 — L'ALBUM
=======================

Pack de téléchargement généré depuis les sources du projet.
Date de vérité : {TRUTH_DATE}

Contenu
-------
- paroles/           les paroles de chaque titre (Markdown)
- fiches/            les fiches techniques (Markdown)
- als/               les sessions Ableton disponibles
- versions-longues/  les versions d'écriture développées (archives)
- album/Album.MD     la note de projet
- manifest.json      l'index des fichiers

Médias
------
Les exports MP3 et MIDI ne sont pas inclus dans ce ZIP : ils sont hébergés
sur Internet Archive pour ne pas alourdir le dépôt Git. Les URLs publiées
figurent dans manifest.json et sur la page de chaque titre.

Chaque titre suit la forme : différence -> discours -> partisans -> refrain.
Les tempos, tonalités et durées sont des propositions de travail.

Avertissement
-------------
Les titres, paroles et musiques ont été générés par IA. Ce sont des brouillons
de vulgarisation : ils peuvent contenir des erreurs factuelles, juridiques ou
artistiques. Ils ne constituent ni une source de référence ni une validation
des programmes présentés. Les corrections documentées sont bienvenues.

Cet album est un exercice de collaboration musicale et culturelle partagé,
pas un outil politique visant à favoriser ou défavoriser un candidat.
La démarche souhaite respecter la neutralité et l'égalité de traitement
entre les candidats.

État du projet
--------------
Ce sont pour l'instant des maquettes : les voix, les arrangements et le mix
restent à faire. Les contributions de musicien·nes et surtout de chanteur·ses
sont sollicitées. Une voix, un instrument, un beat ou un mix peuvent suffire
à faire exister un titre.

Règles
------
- Critiquer le programme, pas la personne.
- Un chiffre = une source + une date.
- Aucun fait judiciaire dans un refrain.
- Les paroles des partisans sont leur point de vue, pas une vérité objective.

Textes, musiques et sessions : © leurs auteurs.
Diffusion pour l'écoute, l'étude et la reprise ; nous contacter pour tout autre usage.

Dépôt : {REPO_URL}
Site  : {SITE_URL}/
"""
    (base / "LISEZ-MOI.txt").write_text(readme, encoding="utf-8")

    # Archive complète (hors elle-même).
    pack = base / "candidats-2027-pack.zip"
    with zipfile.ZipFile(pack, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(base.rglob("*")):
            if path.is_file() and path != pack:
                archive.write(path, path.relative_to(base).as_posix())


def write_pages(tracks: list[dict], sources: Path, album_text: str) -> None:
    (DOCS / "index.html").write_text(build_index(tracks), encoding="utf-8")
    (DOCS / "projet.html").write_text(build_project(album_text), encoding="utf-8")
    (DOCS / "participer.html").write_text(build_contribute(), encoding="utf-8")
    (DOCS / "404.html").write_text(build_404(), encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    for track in tracks:
        (DOCS / "titres" / f"{track['slug']}.html").write_text(
            build_song(track, tracks), encoding="utf-8"
        )


def write_extras(tracks: list[dict]) -> None:
    entries = [
        (f"{SITE_URL}/", "1.0", f"{SITE_URL}/assets/og/album.png", "Candidats 2027 — l’album"),
        (f"{SITE_URL}/catalogue.html", "0.9", f"{SITE_URL}/assets/og/album.png", "Catalogue des productions"),
        (f"{SITE_URL}/projet.html", "0.7", f"{SITE_URL}/assets/og/album.png", "Le projet"),
        (f"{SITE_URL}/participer.html", "0.7", f"{SITE_URL}/assets/og/album.png", "Participer"),
    ]
    entries += [
        (
            f"{SITE_URL}/titres/{track['slug']}.html",
            "0.8",
            f"{SITE_URL}/assets/og/{track['num']:02d}.png",
            f"{track['num']:02d} — {track['candidate']} — {track['title']}",
        )
        for track in tracks
    ]
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
    )
    for url, priority, image, title in entries:
        sitemap += (
            "  <url>"
            f"<loc>{e(url)}</loc>"
            f"<lastmod>{ALBUM_DATE_ISO}</lastmod>"
            "<changefreq>monthly</changefreq>"
            f"<priority>{priority}</priority>"
            "<image:image>"
            f"<image:loc>{e(image)}</image:loc>"
            f"<image:title>{e(title)}</image:title>"
            "</image:image>"
            "</url>\n"
        )
    sitemap += "</urlset>\n"
    (DOCS / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (DOCS / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--als", type=Path, default=DEFAULT_ALS)
    args = parser.parse_args()

    sources: Path = args.sources
    als_dir: Path = args.als
    if not (sources / "Album.MD").is_file():
        raise SystemExit(f"Sources introuvables : {sources}")
    if not als_dir.is_dir():
        print(f"⚠ Dossier Ableton introuvable ({als_dir}) : aucune session ne sera publiée.")

    tracks = load_tracks(sources, als_dir)
    if not tracks:
        raise SystemExit("Aucun titre trouvé dans les sources.")

    media = load_media()
    for track in tracks:
        entries = media.get(track["num"], {})
        track["media_all"] = entries
        track["media"] = {
            kind: item
            for kind, item in entries.items()
            if item.get("_verified") or not item.get("_required_verified")
        }
        track["has_audio"] = bool(track["media"].get("mp3") or track["audio"])
        track["has_midi"] = bool(track["media"].get("midi"))
        track["has_mp3_export"] = bool(entries.get("mp3") or track["audio"])
        track["has_midi_export"] = bool(entries.get("midi"))

    album_text = (sources / "Album.MD").read_text(encoding="utf-8")

    prepare_docs()
    copy_assets()
    write_downloads(tracks, sources, album_text)
    write_pages(tracks, sources, album_text)
    write_extras(tracks)

    als_count = sum(1 for track in tracks if track["als"])
    print(f"✓ {len(tracks)} titres · {als_count} sessions Ableton · site généré dans {DOCS}")


if __name__ == "__main__":
    main()
