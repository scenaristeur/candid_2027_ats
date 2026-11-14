#!/usr/bin/env python3
"""Génère les images Open Graph du site (1200 × 630).

Usage :
    python scripts/make_og.py

Les images sont écrites dans site/assets/og/ puis copiées dans docs/assets/og/
par scripts/build_site.py. Elles servent aux aperçus sociaux (Open Graph,
Twitter/X, LinkedIn, etc.).
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from build_site import DEFAULT_ALS, DEFAULT_SOURCES, SITE, load_tracks  # noqa: E402

WIDTH, HEIGHT = 1200, 630
PAPER = "#f5f0e7"
PAPER_2 = "#ece5d9"
INK = "#171512"
MUTED = "#6e6659"
LINE = "#d8cebd"
CREAM = "#f5f0e7"

FONT_DIR = Path(r"C:\Windows\Fonts")
GEORGIA_BOLD = FONT_DIR / "georgiab.ttf"
GEORGIA_ITALIC = FONT_DIR / "georgiai.ttf"
GEORGIA = FONT_DIR / "georgia.ttf"
SEGOE_BOLD = FONT_DIR / "segoeuib.ttf"
SEGOE = FONT_DIR / "segoeui.ttf"


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    if path.is_file():
        return ImageFont.truetype(str(path), size)
    fallback = FONT_DIR / "arial.ttf"
    return ImageFont.truetype(str(fallback), size)


def text_width(draw: ImageDraw.ImageDraw, text: str, use_font: ImageFont.FreeTypeFont) -> float:
    box = draw.textbbox((0, 0), text, font=use_font)
    return box[2] - box[0]


def wrap(
    draw: ImageDraw.ImageDraw,
    text: str,
    use_font: ImageFont.FreeTypeFont,
    max_width: int,
) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if text_width(draw, candidate, use_font) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def fit_lines(
    draw: ImageDraw.ImageDraw,
    text: str,
    path: Path,
    sizes: tuple[int, ...],
    max_width: int,
    max_lines: int,
) -> tuple[ImageFont.FreeTypeFont, list[str]]:
    for size in sizes:
        use_font = font(path, size)
        lines = wrap(draw, text, use_font, max_width)
        if len(lines) <= max_lines:
            return use_font, lines
    use_font = font(path, sizes[-1])
    lines = wrap(draw, text, use_font, max_width)[:max_lines]
    if lines:
        lines[-1] = lines[-1].rstrip(" .,;:") + "…"
    return use_font, lines


def base_image() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    draw = ImageDraw.Draw(image)
    for offset in range(-HEIGHT, WIDTH + HEIGHT, 42):
        draw.line((offset, 0, offset + HEIGHT, HEIGHT), fill=PAPER_2, width=1)
    draw.rectangle((28, 28, WIDTH - 28, HEIGHT - 28), outline=LINE, width=2)
    return image, draw


def draw_circle(
    draw: ImageDraw.ImageDraw,
    accent: str,
    number: str,
    initials: str,
    *,
    dark: bool,
) -> None:
    cx, cy, radius = 978, 315, 188
    fill = INK if dark else accent
    draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=fill)
    draw.ellipse(
        (cx - radius + 20, cy - radius + 20, cx + radius - 20, cy + radius - 20),
        outline="#ffffff",
        width=2,
    )
    number_font = font(GEORGIA_BOLD, 128)
    draw.text((cx, cy - 10), number, font=number_font, fill=CREAM, anchor="mm")
    if initials:
        initials_font = font(SEGOE_BOLD, 28)
        draw.text((cx, cy + 100), initials, font=initials_font, fill=CREAM, anchor="mm")


def draw_album_og(path: Path) -> None:
    image, draw = base_image()
    draw.rectangle((72, 92, 78, 150), fill="#a63a2c")
    draw.text((96, 96), "CANDIDATS 2027 · L’ALBUM", font=font(SEGOE_BOLD, 22), fill=MUTED)

    title_font = font(GEORGIA_BOLD, 122)
    year_font = font(GEORGIA_ITALIC, 132)
    draw.text((78, 142), "Candidats", font=title_font, fill=INK)
    draw.text((78, 274), "2027", font=year_font, fill="#a63a2c")

    draw.text(
        (82, 448),
        "31 maquettes · 31 candidats",
        font=font(SEGOE_BOLD, 32),
        fill=INK,
    )
    draw.text(
        (82, 496),
        "Une chanson par candidat à la présidentielle.",
        font=font(GEORGIA, 27),
        fill=MUTED,
    )
    draw.text(
        (82, 550),
        "Maquettes ouvertes · voix et instruments bienvenus",
        font=font(SEGOE, 21),
        fill=MUTED,
    )

    draw_circle(draw, "#a63a2c", "31", "2027", dark=True)
    image.save(path, "PNG", optimize=True)


def draw_song_og(track: dict, path: Path) -> None:
    image, draw = base_image()
    draw.rectangle((72, 92, 78, 150), fill=track["accent"])
    draw.text(
        (96, 96),
        f"TITRE {track['num']:02d} / 31 · {(track['style_short'] or 'CHANSON').upper()}",
        font=font(SEGOE_BOLD, 20),
        fill=MUTED,
    )

    candidate_font, candidate_lines = fit_lines(
        draw, track["candidate"], GEORGIA_BOLD, (72, 64, 56), 640, 2
    )
    y = 142
    for line in candidate_lines:
        draw.text((78, y), line, font=candidate_font, fill=INK)
        y += int(candidate_font.size * 1.05)

    title_font, title_lines = fit_lines(
        draw, track["title"], GEORGIA_ITALIC, (50, 44, 38), 640, 3
    )
    y += 12
    for line in title_lines:
        draw.text((82, y), line, font=title_font, fill=track["accent"])
        y += int(title_font.size * 1.12)

    draw.text((82, 548), "Candidats 2027 · maquette ouverte · propose ta voix", font=font(SEGOE, 21), fill=MUTED)

    draw_circle(draw, track["accent"], f"{track['num']:02d}", track["initials"], dark=False)
    image.save(path, "PNG", optimize=True)


def main() -> None:
    out = SITE / "assets" / "og"
    out.mkdir(parents=True, exist_ok=True)
    tracks = load_tracks(DEFAULT_SOURCES, DEFAULT_ALS)
    if not tracks:
        raise SystemExit("Aucun titre trouvé pour générer les images Open Graph.")

    draw_album_og(out / "album.png")
    for track in tracks:
        draw_song_og(track, out / f"{track['num']:02d}.png")
    print(f"✓ {len(tracks) + 1} images Open Graph générées dans {out}")


if __name__ == "__main__":
    main()
