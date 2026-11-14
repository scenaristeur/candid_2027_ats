#!/usr/bin/env python3
"""Vérifie le site généré : liens locaux, structure HTML, fichiers attendus.

Usage : python scripts/check_site.py
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"


class StructureChecker(HTMLParser):
    void = {
        "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr", "path",
    }

    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []
        self.problems: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag not in self.void:
            self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in self.void:
            return
        if not self.stack:
            self.problems.append(f"fermeture sans ouverture : {tag}")
            return
        if self.stack[-1] == tag:
            self.stack.pop()
            return
        if tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.problems.append(f"balise non fermée : {self.stack.pop()}")
            if self.stack:
                self.stack.pop()
        else:
            self.problems.append(f"fermeture orpheline : {tag}")


def check_links() -> list[str]:
    errors: list[str] = []
    checked = 0
    for page in sorted(DOCS.rglob("*.html")):
        text = page.read_text(encoding="utf-8")
        for attr in ("href", "src"):
            for match in re.finditer(rf'{attr}="([^"]+)"', text):
                url = match.group(1)
                if url.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
                    continue
                path = url.split("#", 1)[0].split("?", 1)[0]
                if not path:
                    continue
                target = (page.parent / unquote(path)).resolve()
                checked += 1
                try:
                    target.relative_to(DOCS.resolve())
                except ValueError:
                    errors.append(f"{page.relative_to(DOCS)} → hors site : {url}")
                    continue
                if not target.exists():
                    errors.append(f"{page.relative_to(DOCS)} → manquant : {url}")
    print(f"{checked} liens locaux vérifiés")
    return errors


def check_structure() -> list[str]:
    errors: list[str] = []
    for page in sorted(DOCS.rglob("*.html")):
        checker = StructureChecker()
        checker.feed(page.read_text(encoding="utf-8"))
        problems = checker.problems + [f"reste ouvert : {tag}" for tag in checker.stack]
        if problems:
            errors.append(f"{page.relative_to(DOCS)} : {', '.join(problems[:5])}")
    return errors


def main() -> None:
    if not (DOCS / "index.html").is_file():
        raise SystemExit("docs/index.html absent : lance d'abord scripts/build_site.py")

    errors = check_links() + check_structure()

    pages = list((DOCS / "titres").glob("*.html"))
    if len(pages) != 31:
        errors.append(f"31 pages de titres attendues, {len(pages)} trouvées")

    for required in (
        DOCS / "telechargements" / "manifest.json",
        DOCS / "telechargements" / "candidats-2027-pack.zip",
        DOCS / "telechargements" / "album" / "Album.MD",
        DOCS / ".nojekyll",
    ):
        if not required.exists():
            errors.append(f"fichier attendu absent : {required.relative_to(DOCS)}")

    if errors:
        print("\n".join(errors))
        raise SystemExit(1)

    print(f"✓ {len(pages)} pages de titres, liens et structure HTML valides")


if __name__ == "__main__":
    main()
