#!/usr/bin/env python3
"""Génère la page publique du catalogue des productions.

Lit `catalog/productions.json` et écrit `docs/catalogue.html`.
Le reste du site (accueil, pages de titres, styles) est généré par
`scripts/build_site.py`.

Usage :
    python scripts/build_catalogue.py
"""

from __future__ import annotations

import html
import json
import sys
import unicodedata
from collections import Counter
from pathlib import Path

import build_site

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog" / "productions.json"
OUTPUT = ROOT / "docs" / "catalogue.html"


def e(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", str(text or ""))
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return " ".join(text.lower().split())


def status_group(stage: str) -> str:
    if stage == "maquette exportée":
        return "exportee"
    if stage == "maquette Ableton":
        return "ableton"
    if stage == "documentation seule":
        return "documentation"
    if stage == "session seule":
        return "session"
    if "export" in stage:
        return "export"
    return "autre"


def site_link(item: dict) -> str:
    if item.get("album") == "Candidats 2027" and item.get("candidate"):
        slug = (
            f"{int(item['number']):02d}-"
            f"{build_site.slugify(item['candidate'])}-"
            f"{build_site.slugify(item['title'])}"
        )
        if (ROOT / "docs" / "titres" / f"{slug}.html").is_file():
            return f"titres/{slug}.html"
    production_page = ROOT / "docs" / "productions" / f"{item['id']}.html"
    if production_page.is_file():
        return f"productions/{item['id']}.html"
    return ""


def main() -> None:
    if not CATALOG.is_file():
        raise SystemExit(
            "catalog/productions.json absent : lance d'abord scripts/build_catalog.py"
        )
    productions = json.loads(CATALOG.read_text(encoding="utf-8"))
    total = len(productions)
    albums = sorted({item["album"] for item in productions}, key=normalize)
    album_counts = Counter(item["album"] for item in productions)
    documented = sum(1 for item in productions if item.get("docs"))
    with_als = sum(1 for item in productions if item.get("als_main"))
    sessions = sum(int(item.get("als_count") or 0) for item in productions)
    with_audio = sum(1 for item in productions if item.get("mp3") or item.get("wav"))
    with_midi = sum(1 for item in productions if item.get("midi"))

    stage_counts = Counter(item["stage"] for item in productions)
    group_counts = Counter(status_group(item["stage"]) for item in productions)

    rows = []
    for item in sorted(
        productions,
        key=lambda x: (normalize(x["album"]), x.get("number") or 999, normalize(x["title"])),
    ):
        group = status_group(item["stage"])
        link = site_link(item)
        label = item["title"]
        if item.get("candidate"):
            label = f"{item['candidate']} — {label}"
        title_html = f'<a href="{e(link)}">{e(label)}</a>' if link else e(label)
        candidate = (
            f'<span class="cat-candidate">{e(item["candidate"])}</span>'
            if item.get("candidate")
            else ""
        )
        audio_badges = []
        if item.get("mp3"):
            audio_badges.append('<span class="badge badge-media">MP3</span>')
        if item.get("wav"):
            audio_badges.append('<span class="badge">WAV</span>')
        if item.get("midi"):
            audio_badges.append('<span class="badge">MIDI</span>')
        audio_html = " ".join(audio_badges) or "—"
        als_label = (
            f"{item['als_count']} version(s)"
            if int(item.get("als_count") or 0) > 1
            else ("1 session" if item.get("als_main") else "—")
        )
        search = normalize(
            " ".join(
                str(item.get(key) or "")
                for key in (
                    "album", "number", "title", "candidate", "stage", "docs",
                    "lyrics", "tempo", "key", "style", "atmosphere", "summary", "missing",
                )
            )
        )
        rows.append(
            f'<tr data-catalog-row data-search="{e(search)}" '
            f'data-album="{e(item["album"])}" data-status="{group}" '
            f'data-kind="{e(item.get("kind", ""))}" data-docs="{1 if item.get("docs") else 0}" '
            f'data-confidence="{e(item.get("confidence", ""))}">'
            f'<td class="cat-num">{item.get("number") or "—"}</td>'
            f'<td class="cat-production"><span class="cat-title">{title_html}</span>{candidate}'
            f'<span class="cat-summary" title="{e(item.get("summary", ""))}">{e((item.get("summary") or "")[:120])}</span></td>'
            f'<td class="cat-album">{e(item["album"])}</td>'
            f'<td><span class="cat-status cat-status-{group}">{e(item["stage"])}</span></td>'
            f'<td>{e(als_label)}</td>'
            f'<td class="cat-audio">{audio_html}</td>'
            f'<td>{e(item.get("tempo") or "—")}</td>'
            f'<td>{e(item.get("key") or "—")}</td>'
            f'<td class="cat-missing">{e(item.get("missing") or "—")}</td>'
            f"</tr>"
        )

    album_options = "\n".join(
        f'<option value="{e(album)}">{e(album)} ({album_counts[album]})</option>'
        for album in albums
    )
    status_buttons = [
        ("all", "Tout", total),
        ("exportee", "Maquettes exportées", group_counts["exportee"]),
        ("ableton", "Maquettes Ableton", group_counts["ableton"]),
        ("documentation", "Documentation", group_counts["documentation"]),
        ("session", "Sessions seules", group_counts["session"]),
        ("export", "Exports", group_counts["export"]),
    ]
    buttons_html = "".join(
        f'<button type="button" class="filter{" is-active" if key == "all" else ""}" '
        f'data-catalog-status="{key}" aria-pressed="{"true" if key == "all" else "false"}">'
        f"{e(label)} <span>{count}</span></button>"
        for key, label, count in status_buttons
        if count or key == "all"
    )

    description = (
        f"Catalogue des {total} productions musicales du projet : "
        f"{sessions} sessions Ableton, {with_audio} exports audio, "
        f"{documented} productions documentées. Statut, tempo, tonalité et avancement."
    )
    jsonld = build_site.webpage_jsonld(
        "Catalogue des productions",
        description,
        "catalogue.html",
        f"{build_site.SITE_URL}/assets/og/album.png",
        "CollectionPage",
    )

    body = f"""
<header class="page-hero catalog-hero">
  <div class="wrap">
    <p class="eyebrow">La plateforme</p>
    <h1>Le catalogue<br><em>des productions.</em></h1>
    <p class="lede">Toutes les productions repérées dans les sources, les sessions Ableton et les exports : {total} entrées, {len(albums)} albums et projets, {sessions} sessions ALS. Candidats 2027 n’est plus qu’un album parmi les autres.</p>
    <p class="hero-note">Rapprochements automatiques, à consolider. Les productions documentées renvoient vers leurs pages quand elles existent.</p>
  </div>
</header>

<section class="stats" aria-label="Le catalogue en chiffres">
  <div class="wrap stats-grid">
    <div><strong>{total}</strong><span>productions</span></div>
    <div><strong>{len(albums)}</strong><span>albums / projets</span></div>
    <div><strong>{documented}</strong><span>documentées</span></div>
    <div><strong>{sessions}</strong><span>sessions ALS</span></div>
    <div><strong>{with_audio}</strong><span>exports audio</span></div>
    <div><strong>{with_midi}</strong><span>exports MIDI</span></div>
  </div>
</section>

<section class="catalog-section">
  <div class="wrap">
    <div class="catalog-toolbar">
      <div class="search-field">
        <label for="catalog-search">Rechercher une production</label>
        <input id="catalog-search" type="search" placeholder="Titre, album, style, statut…" autocomplete="off" data-catalog-search>
        <kbd aria-hidden="true">/</kbd>
      </div>
      <label class="catalog-select">
        <span>Album</span>
        <select data-catalog-album>
          <option value="">Tous les albums</option>
          {album_options}
        </select>
      </label>
      <label class="catalog-check">
        <input type="checkbox" data-catalog-docs>
        <span>Masquer les sessions sans fiche</span>
      </label>
    </div>
    <div class="filters catalog-status-filters" role="group" aria-label="Filtrer par statut">
      {buttons_html}
    </div>
    <p class="catalog-count" aria-live="polite"><strong data-catalog-count>{total}</strong> productions affichées</p>

    <div class="table-wrap catalog-table-wrap">
      <table class="catalog-table">
        <thead>
          <tr>
            <th scope="col">N°</th>
            <th scope="col">Production</th>
            <th scope="col">Album</th>
            <th scope="col">Statut</th>
            <th scope="col">ALS</th>
            <th scope="col">Audio</th>
            <th scope="col">Tempo</th>
            <th scope="col">Tonalité</th>
            <th scope="col">Manque</th>
          </tr>
        </thead>
        <tbody>
          {''.join(rows)}
        </tbody>
      </table>
    </div>
    <p class="catalog-empty" data-catalog-empty hidden>Aucune production ne correspond à ces filtres.</p>
    <p class="catalog-note">Le détail machine est dans <code>catalog/productions.csv</code> et <code>catalog/productions.json</code>. Les colonnes « ALS » comptent les versions principales ; les exports audio et MIDI sont ceux de <code>exports ableton</code>.</p>
  </div>
</section>

<section class="catalog-call">
  <div class="wrap narrow">
    <p class="eyebrow">Contribuer</p>
    <h2>Une production à compléter, une voix à enregistrer, une session à rattacher ?</h2>
    <p>Le catalogue est une photo de l’existant, pas une clôture. Corrections de rattachement, exports, MIDI, fiches et interprétations : tout est ouvert.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{build_site.REPO_URL}/issues/new?template=contribution.yml">Proposer une contribution</a>
      <a class="btn btn-ghost" href="participer.html#voix">Proposer une voix</a>
    </div>
  </div>
</section>
<script src="assets/catalogue.js" defer></script>
"""

    page = build_site.page(
        "Catalogue des productions · Candidats 2027",
        description,
        0,
        body,
        page_path="catalogue.html",
        active="catalogue",
        og_type="website",
        og_image="assets/og/album.png",
        keywords=(
            "catalogue, productions musicales, albums, sessions Ableton, "
            "exports audio, Candidats 2027, plateforme collaborative"
        ),
        jsonld=jsonld,
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(page, encoding="utf-8")
    print(
        f"✓ {OUTPUT.relative_to(ROOT)} · {total} productions · "
        f"{sessions} sessions ALS · {with_audio} exports audio"
    )


if __name__ == "__main__":
    main()
