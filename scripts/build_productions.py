#!/usr/bin/env python3
"""Génère une page de production avec ses téléchargements.

Lit `catalog/productions.json` et `site/media_productions.json`.
Copie les documents sources et les sessions ALS dans
`docs/telechargements/productions/<id>/`, puis écrit
`docs/productions/<id>.html`.

Les productions Candidats 2027 gardent leurs pages existantes.

Usage :
    python scripts/build_productions.py
"""

from __future__ import annotations

import html
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote

import build_site

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CATALOG = ROOT / "catalog" / "productions.json"
MEDIA = ROOT / "site" / "media_productions.json"
SOURCES_ROOT = Path(r"C:\Users\admin\dev\ableton-holland-mcp\sources")
ALS_ROOT = Path(r"C:\Users\admin\Music\Ableton Live")
EXPORTS_ROOT = Path(r"C:\Users\admin\Music\exports ableton")

PAGES = DOCS / "productions"
DOWNLOADS = DOCS / "telechargements" / "productions"
USER_PATH_RE = re.compile(r"C:[\\/]Users[\\/][^\\/\s\"<>]+", re.I)


def e(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def resolve(value: str | None) -> Path | None:
    if not value:
        return None
    normalized = str(value).replace("\\", "/")
    if normalized.startswith("sources/"):
        return SOURCES_ROOT / normalized[len("sources/") :]
    if normalized.startswith("Ableton Live/"):
        return ALS_ROOT / normalized[len("Ableton Live/") :]
    if normalized.startswith("exports ableton/"):
        return EXPORTS_ROOT / normalized[len("exports ableton/") :]
    return Path(value)


def safe_text(text: str) -> str:
    return USER_PATH_RE.sub("C:/Users/Public", text)


def doc_label(name: str) -> str:
    lower = name.lower()
    if "parole" in lower:
        return "Paroles"
    if "fiche" in lower or "status" in lower:
        return "Fiche technique"
    if "structure" in lower:
        return "Structure"
    if "clip" in lower:
        return "Notes de clip"
    return "Document"


def copy_documents(production: dict, destination: Path) -> list[tuple[str, str, int]]:
    source_dir = resolve(production.get("source_path"))
    if not source_dir or not source_dir.is_dir():
        return []
    docs = []
    destination.mkdir(parents=True, exist_ok=True)
    for source in sorted(source_dir.glob("*.md")):
        if not source.is_file():
            continue
        text = safe_text(source.read_text(encoding="utf-8", errors="replace"))
        target = destination / source.name
        target.write_text(text, encoding="utf-8")
        docs.append((source.name, doc_label(source.name), target.stat().st_size))
    return docs


def copy_sessions(production: dict, destination: Path) -> list[tuple[str, int, bool]]:
    destination.mkdir(parents=True, exist_ok=True)
    seen: set[str] = set()
    sessions = []
    paths: list[str] = []
    if production.get("als_main"):
        paths.append(production["als_main"])
    for item in production.get("als_matches") or []:
        path = item.get("path")
        if path and path not in paths:
            paths.append(path)
    for index, logical in enumerate(paths[:12]):
        source = resolve(logical)
        if not source or not source.is_file():
            continue
        name = source.name
        if name in seen:
            name = f"{index:02d}-{name}"
        seen.add(name)
        target = destination / name
        try:
            build_site.copy_als_sanitized(source, target)
        except OSError:
            continue
        sessions.append((name, target.stat().st_size, logical == production.get("als_main")))
    return sessions


def media_for(production: dict, manifest: dict) -> dict:
    entry = (manifest.get("files") or {}).get(production["id"], {})
    return {
        kind: item
        for kind, item in entry.items()
        if item.get("verified", False)
    }


def main() -> None:
    if not CATALOG.is_file():
        raise SystemExit("catalog/productions.json absent : lance build_catalog.py")
    productions = json.loads(CATALOG.read_text(encoding="utf-8"))
    manifest = (
        json.loads(MEDIA.read_text(encoding="utf-8")) if MEDIA.is_file() else {"files": {}}
    )

    if PAGES.exists():
        shutil.rmtree(PAGES)
    if DOWNLOADS.exists():
        shutil.rmtree(DOWNLOADS)
    PAGES.mkdir(parents=True, exist_ok=True)
    DOWNLOADS.mkdir(parents=True, exist_ok=True)

    generated = 0
    sitemap_entries: list[tuple[str, str]] = []
    for production in productions:
        if production.get("kind") not in {"source", "als"}:
            continue
        if production.get("album") == "Candidats 2027":
            continue

        docs = copy_documents(production, DOWNLOADS / production["id"] / "documents")
        sessions = copy_sessions(production, DOWNLOADS / production["id"] / "als")
        media = media_for(production, manifest)
        if not docs and not sessions and not media:
            continue

        download_cards = []
        audio_card = ""
        mp3 = media.get("mp3")
        if mp3:
            audio_card = f"""<figure class="audio-card">
  <figcaption class="audio-head">
    <span class="audio-label">Écouter</span>
    <strong>Export audio</strong>
    <span class="audio-source">Internet Archive</span>
  </figcaption>
  <audio controls preload="metadata" src="{e(mp3['url'])}"></audio>
</figure>"""
            download_cards.append(
                build_site.download_card(
                    kind="audio",
                    title="Export MP3",
                    description="Écoute et téléchargement sur Internet Archive.",
                    href=mp3["url"],
                    meta="MP3 · Internet Archive",
                    external=True,
                )
            )
        if media.get("midi"):
            download_cards.append(
                build_site.download_card(
                    kind="midi",
                    title="Export MIDI",
                    description="Fichier MIDI à réouvrir dans un DAW.",
                    href=media["midi"]["url"],
                    meta="MIDI · Internet Archive",
                    external=True,
                )
            )

        for index, (name, label, size) in enumerate(docs):
            download_cards.append(
                build_site.download_card(
                    kind="md",
                    title=label,
                    description=name,
                    href=f"../telechargements/productions/{production['id']}/documents/{quote(name)}",
                    meta=f"Markdown · {build_site.format_size(size)}",
                )
            )

        for name, size, is_main in sessions:
            download_cards.append(
                build_site.download_card(
                    kind="als",
                    title="Session Ableton (.als)" if is_main else "Version Ableton",
                    description=name,
                    href=f"../telechargements/productions/{production['id']}/als/{quote(name)}",
                    meta=f"Live 12 · {build_site.format_size(size)}",
                )
            )

        media_note = ""
        if production.get("album") == "Désir" and not mp3:
            media_note = (
                '<p class="download-note">L’export MP3 de cette production est en cours '
                "de catalogage sur Internet Archive.</p>"
            )

        description = (
            f"{production['title']} — {production['album']}. "
            f"Paroles, documents, session Ableton et exports."
        )
        body = f"""
<div class="wrap">
  <nav class="breadcrumb" aria-label="Fil d’Ariane">
    <a href="../index.html">L’album</a><span aria-hidden="true">/</span>
    <a href="../catalogue.html">Catalogue</a><span aria-hidden="true">/</span>
    <span aria-current="page">{e(production['album'])}</span>
  </nav>
</div>

<header class="song-hero">
  <div class="wrap song-hero-grid">
    <div class="cover cover-large" style="--accent:#284b7a;--accent-soft:#dbe4f2" aria-hidden="true">
      <span class="cover-rule"></span>
      <span class="cover-num">{e(production['album'][:2].upper())}</span>
      <span class="cover-initials">{e((production['title'] or '?')[:2].upper())}</span>
      <span class="cover-style">{e(production['stage'])}</span>
      <span class="cover-ring"></span>
    </div>
    <div class="song-intro">
      <p class="eyebrow">{e(production['album'])} · {e(production['stage'])}</p>
      <h1 class="song-h1"><span class="h1-candidate">{e(production['title'])}</span><span class="h1-title">{e(production.get('candidate') or production['album'])}</span></h1>
      <p class="song-lede">{e(production.get('summary') or production.get('atmosphere') or 'Production du catalogue.')}</p>
      <dl class="meta-chips">
        <div><dt>Tempo</dt><dd>{e(production.get('tempo') or '—')}</dd></div>
        <div><dt>Tonalité</dt><dd>{e(production.get('key') or '—')}</dd></div>
        <div><dt>Sessions ALS</dt><dd>{e(production.get('als_count') or 0)}</dd></div>
        <div><dt>Manque</dt><dd>{e(production.get('missing') or '—')}</dd></div>
      </dl>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#telecharger">Télécharger les fichiers</a>
        <a class="btn btn-ghost" href="../catalogue.html">Retour au catalogue</a>
      </div>
      <p class="status-line"><span class="status-dot" aria-hidden="true"></span>{e(production.get('confidence') or '—')} · rapprochement automatique à vérifier</p>
    </div>
  </div>
</header>

<section class="downloads-section" id="telecharger" aria-labelledby="telecharger-titre">
  <div class="wrap">
    <div class="section-head compact">
      <div>
        <p class="eyebrow">Fichiers</p>
        <h2 id="telecharger-titre">Télécharger</h2>
      </div>
      <p class="section-source">Documents sources · session Ableton · exports publiés.</p>
    </div>
    {audio_card}
    <div class="download-grid">
      {''.join(download_cards)}
    </div>
    {media_note}
    <p class="download-note">Les documents et sessions sont copiés depuis les sources du projet, avec neutralisation des chemins utilisateur. Les MP3 sont hébergés sur Internet Archive.</p>
  </div>
</section>

{self_contribute(production)}
"""
        page = build_site.page(
            f"{production['title']} — {production['album']} · Candidats 2027",
            description,
            1,
            body,
            page_path=f"productions/{production['id']}.html",
            active="catalogue",
            og_type="article",
            og_image="assets/og/album.png",
            keywords=(
                f"{production['title']}, {production['album']}, paroles, fiche "
                "technique, session Ableton, MP3"
            ),
            jsonld=build_site.webpage_jsonld(
                f"{production['title']} — {production['album']}",
                description,
                f"productions/{production['id']}.html",
                f"{build_site.SITE_URL}/assets/og/album.png",
                "CreativeWork",
            ),
        )
        (PAGES / f"{production['id']}.html").write_text(page, encoding="utf-8")
        sitemap_entries.append((production["id"], f"{production['title']} — {production['album']}"))
        generated += 1

    if sitemap_entries:
        import xml.sax.saxutils as saxutils

        lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        ]
        for identifier, label in sorted(sitemap_entries):
            url = f"{build_site.SITE_URL}/productions/{identifier}.html"
            lines.append(
                "  <url>"
                f"<loc>{saxutils.escape(url)}</loc>"
                f"<lastmod>{build_site.ALBUM_DATE_ISO}</lastmod>"
                "<changefreq>monthly</changefreq>"
                "<priority>0.6</priority>"
                "</url>"
            )
        lines.append("</urlset>")
        (DOCS / "sitemap-productions.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
        robots = DOCS / "robots.txt"
        line = f"Sitemap: {build_site.SITE_URL}/sitemap-productions.xml"
        if robots.is_file() and line not in robots.read_text(encoding="utf-8"):
            robots.write_text(
                robots.read_text(encoding="utf-8").rstrip() + "\n" + line + "\n",
                encoding="utf-8",
            )

    print(f"✓ {generated} pages de production générées dans {PAGES}")


def self_contribute(production: dict) -> str:
    title = quote(f"[Contribution] {production['title']} — {production['album']}")
    return f"""<section class="contribute" aria-labelledby="contribuer-titre">
  <div class="contribute-inner">
    <p class="eyebrow">Participer</p>
    <h2 id="contribuer-titre">Cette production est ouverte.</h2>
    <p>Un document à corriger, une session à reprendre, une voix à enregistrer ? Les fichiers sont là pour être améliorés.</p>
    <div class="contribute-actions">
      <a class="btn btn-primary" href="{build_site.REPO_URL}/issues/new?template=contribution.yml&title={title}">Proposer une contribution<span aria-hidden="true">↗</span></a>
      <a class="btn btn-ghost" href="../participer.html#voix">Proposer une voix<span aria-hidden="true">↗</span></a>
    </div>
  </div>
</section>"""


if __name__ == "__main__":
    main()
