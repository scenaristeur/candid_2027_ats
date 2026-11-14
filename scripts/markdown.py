"""Petit moteur Markdown sans dépendance, suffisant pour les fiches du projet.

Fonctionnalités : titres, paragraphes, gras/italique, code inline, liens,
listes, citations, tableaux, blocs de code et séparateurs.
Tout le texte est échappé : les documents sources ne peuvent pas injecter de HTML.
"""

from __future__ import annotations

import html
import re
import unicodedata

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_UL_RE = re.compile(r"^\s*[-*+]\s+(.*)$")
_OL_RE = re.compile(r"^\s*(\d+)[.)]\s+(.*)$")
_HR_RE = re.compile(r"^\s*([-*_])(?:\s*\1){2,}\s*$")
_TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "section"


def _inline(text: str) -> str:
    """Échappe puis applique les marques inline."""
    out = html.escape(text, quote=False)

    # Code inline d'abord : son contenu ne doit pas être interprété.
    codes: list[str] = []

    def _code(match: re.Match[str]) -> str:
        codes.append(match.group(1))
        return f"\x00CODE{len(codes) - 1}\x00"

    out = re.sub(r"`([^`]+)`", _code, out)

    # Liens [texte](url)
    def _link(match: re.Match[str]) -> str:
        label, url = match.group(1), match.group(2)
        safe = html.escape(html.unescape(url), quote=True)
        if safe.startswith(("javascript:", "data:")):
            safe = "#"
        return f'<a href="{safe}">{label}</a>'

    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", _link, out)

    # Gras puis italique.
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    out = re.sub(r"__(.+?)__", r"<strong>\1</strong>", out)

    for index, code in enumerate(codes):
        out = out.replace(f"\x00CODE{index}\x00", f"<code>{code}</code>")
    return out


def _split_row(line: str) -> list[str]:
    """Découpe une ligne de tableau en ignorant les barres dans le code inline."""
    line = line.strip()
    cells: list[str] = []
    buffer: list[str] = []
    in_code = False
    for char in line:
        if char == "`":
            in_code = not in_code
        if char == "|" and not in_code:
            cells.append("".join(buffer).strip())
            buffer = []
        else:
            buffer.append(char)
    cells.append("".join(buffer).strip())
    if line.startswith("|") and cells:
        cells = cells[1:]
    if line.endswith("|") and cells:
        cells = cells[:-1]
    return cells


def _is_table_start(lines: list[str], i: int) -> bool:
    return (
        i + 1 < len(lines)
        and "|" in lines[i]
        and _TABLE_SEP_RE.match(lines[i + 1]) is not None
    )


def _render_table(rows: list[list[str]], aligns: list[str]) -> str:
    def cell(tag: str, content: str, index: int) -> str:
        align = aligns[index] if index < len(aligns) else ""
        attr = f' class="ta-{align}"' if align else ""
        return f"<{tag}{attr}>{_inline(content)}</{tag}>"

    head = "".join(cell("th", c, i) for i, c in enumerate(rows[0]))
    body = "".join(
        "<tr>" + "".join(cell("td", c, i) for i, c in enumerate(row)) + "</tr>"
        for row in rows[1:]
    )
    thead = f"<thead><tr>{head}</tr></thead>" if any(c.strip() for c in rows[0]) else ""
    return (
        '<div class="table-wrap"><table>'
        + thead
        + "<tbody>"
        + body
        + "</tbody></table></div>"
    )


def _alignments(separator: str) -> list[str]:
    result = []
    for cell in _split_row(separator):
        left, right = cell.startswith(":"), cell.endswith(":")
        if left and right:
            result.append("center")
        elif right:
            result.append("right")
        elif left:
            result.append("left")
        else:
            result.append("")
    return result


def render(text: str, *, breaks: bool = False, demote: int = 0, start_ids: bool = True) -> str:
    """Rend un document Markdown en HTML.

    breaks=True conserve les retours à la ligne simples (utile pour les paroles).
    demote décale les niveaux de titre (1 -> h2, etc.).
    """
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    list_tag = ""
    quote_lines: list[str] = []
    used_ids: dict[str, int] = {}

    def flush_paragraph() -> None:
        nonlocal paragraph
        if not paragraph:
            return
        joiner = "<br>\n" if breaks else " "
        out.append(f"<p>{joiner.join(_inline(line.strip()) for line in paragraph)}</p>")
        paragraph = []

    def flush_list() -> None:
        nonlocal list_items, list_tag
        if not list_items:
            return
        items = "".join(f"<li>{_inline(item)}</li>" for item in list_items)
        out.append(f"<{list_tag}>{items}</{list_tag}>")
        list_items = []
        list_tag = ""

    def flush_quote() -> None:
        nonlocal quote_lines
        if not quote_lines:
            return
        joiner = "<br>\n" if breaks else " "
        out.append(
            "<blockquote><p>"
            + joiner.join(_inline(line) for line in quote_lines)
            + "</p></blockquote>"
        )
        quote_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.strip().startswith("```"):
            flush_paragraph()
            flush_list()
            flush_quote()
            language = line.strip()[3:].strip()
            code: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            escaped = html.escape("\n".join(code), quote=False)
            cls = f' class="language-{html.escape(language, quote=True)}"' if language else ""
            out.append(f"<pre><code{cls}>{escaped}</code></pre>")
            i += 1
            continue

        if not line.strip():
            flush_paragraph()
            flush_list()
            flush_quote()
            i += 1
            continue

        heading = _HEADING_RE.match(line)
        if heading:
            flush_paragraph()
            flush_list()
            flush_quote()
            level = min(6, max(2, len(heading.group(1)) + demote))
            if demote == 0:
                level = len(heading.group(1))
            title = heading.group(2).strip()
            plain = re.sub(r"[*_`]", "", title)
            base = slugify(plain)
            if start_ids:
                count = used_ids.get(base, 0)
                used_ids[base] = count + 1
                anchor = base if count == 0 else f"{base}-{count + 1}"
                out.append(f'<h{level} id="{anchor}">{_inline(title)}</h{level}>')
            else:
                out.append(f"<h{level}>{_inline(title)}</h{level}>")
            i += 1
            continue

        if _HR_RE.match(line):
            flush_paragraph()
            flush_list()
            flush_quote()
            out.append("<hr>")
            i += 1
            continue

        if _is_table_start(lines, i):
            flush_paragraph()
            flush_list()
            flush_quote()
            header = _split_row(lines[i])
            aligns = _alignments(lines[i + 1])
            rows = [header]
            i += 2
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                rows.append(_split_row(lines[i]))
                i += 1
            out.append(_render_table(rows, aligns))
            continue

        unordered = _UL_RE.match(line)
        ordered = _OL_RE.match(line)
        if unordered or ordered:
            flush_paragraph()
            flush_quote()
            tag = "ul" if unordered else "ol"
            if list_tag != tag:
                flush_list()
                list_tag = tag
            list_items.append((unordered or ordered).group(unordered and 1 or 2))
            i += 1
            continue

        if line.lstrip().startswith(">"):
            flush_paragraph()
            flush_list()
            quote_lines.append(line.lstrip()[1:].lstrip())
            i += 1
            continue

        if list_tag and line[:1].isspace():
            list_items[-1] = list_items[-1].rstrip() + " " + line.strip()
            i += 1
            continue

        paragraph.append(line)
        i += 1

    flush_paragraph()
    flush_list()
    flush_quote()
    return "\n".join(out)


def strip_markdown(text: str) -> str:
    """Texte brut approximatif, pour les attributs et les résumés."""
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_#>|]", "", text)
    return re.sub(r"\s+", " ", text).strip()
