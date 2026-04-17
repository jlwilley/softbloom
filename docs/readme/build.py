"""Generate README showcase assets for Softbloom.

Writes SVG swatches, component specimens, shape and motion diagrams, and
PNG typography specimens under docs/readme/. Tokens are mirrored from
tokens/colors.json so a single source of truth still lives there; if you
update tokens, rerun this script and commit the regenerated assets.

Usage:
    python docs/readme/build.py

Requires Chrome or Edge on PATH or at a standard install location to
rasterize typography specimens.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from textwrap import dedent

OUT = Path(__file__).parent
ROOT = OUT.parent.parent
LOGO = ROOT / "logo"

# --- Token mirrors (kept in sync with tokens/colors.json) -----------------

LIGHT = {
    "bg_app": "#FAF6F2",
    "bg_surface": "#FFFFFF",
    "bg_muted": "#F2EBE4",
    "bg_inverse": "#7A2640",
    "ink": "#2B1F1C",
    "bark": "#6B5A52",
    "taupe": "#A89589",
    "stone": "#E0D5CA",
    "linen": "#F2EBE4",
    "paper": "#FAF6F2",
    "brand": "#B84668",
    "brand_deep": "#7A2640",
    "brand_wash": "#FFF7F9",
    "sakura_50": "#FFF7F9",
    "sakura_100": "#FBE4EC",
    "sakura_200": "#F5B8CD",
    "sakura_400": "#E87FA0",
    "sakura_600": "#B84668",
    "sakura_900": "#5C1A2E",
    "lilac": "#EFE4F0",
    "lilac_text": "#4A2C52",
    "sage": "#DDE8DC",
    "sage_text": "#2A3D2C",
    "honey": "#F7E6D2",
    "honey_text": "#5C3A1F",
    "wine": "#7A2640",
    "inverse_text": "#FFE8F0",
}

DARK = {
    "bg_app": "#1A0F12",
    "bg_surface": "#261619",
    "bg_muted": "#3D2530",
    "bg_inverse": "#D4577A",
    "ink": "#FFE8F0",
    "bark": "#8A6578",
    "taupe": "#6E5260",
    "stone": "#3D2530",
    "linen": "#261619",
    "paper": "#1A0F12",
    "brand": "#D4577A",
    "brand_deep": "#9F3754",
    "brand_wash": "#4A1A2A",
    "sakura_50": "#3D2530",
    "sakura_100": "#4A1A2A",
    "sakura_200": "#9F3754",
    "sakura_400": "#D4577A",
    "sakura_600": "#F289AD",
    "sakura_900": "#FFE8F0",
    "lilac": "#3A2F42",
    "lilac_text": "#D5C4DA",
    "sage": "#2D3A2F",
    "sage_text": "#B5D1B7",
    "honey": "#4A3820",
    "honey_text": "#E8C998",
    "wine": "#5C3848",
    "inverse_text": "#FFE8F0",
}

# Shared style block embedded in each SVG so fonts fall back gracefully on
# GitHub (where custom fonts don't load) but render properly when Fraunces,
# Inter, and JetBrains Mono are installed locally or the SVG is opened
# inside a page that loads them.
FONT_STACK_DISPLAY = "'Fraunces', 'GT Super', Georgia, 'Times New Roman', serif"
FONT_STACK_SANS = "'Inter', 'General Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
FONT_STACK_MONO = "'JetBrains Mono', 'IBM Plex Mono', 'Cascadia Code', ui-monospace, monospace"


def style_block(t: dict) -> str:
    return dedent(f"""
    <style>
      .bg {{ fill: {t['bg_app']}; }}
      .surface {{ fill: {t['bg_surface']}; }}
      .muted-surface {{ fill: {t['bg_muted']}; }}
      .display {{ font-family: {FONT_STACK_DISPLAY}; font-weight: 400; fill: {t['ink']}; }}
      .display-italic {{ font-family: {FONT_STACK_DISPLAY}; font-weight: 400; font-style: italic; fill: {t['ink']}; }}
      .sans {{ font-family: {FONT_STACK_SANS}; font-weight: 400; fill: {t['ink']}; }}
      .sans-medium {{ font-family: {FONT_STACK_SANS}; font-weight: 500; fill: {t['ink']}; }}
      .mono {{ font-family: {FONT_STACK_MONO}; font-weight: 400; fill: {t['bark']}; }}
      .mono-ink {{ font-family: {FONT_STACK_MONO}; font-weight: 400; fill: {t['ink']}; }}
      .label {{ font-family: {FONT_STACK_SANS}; font-weight: 500; fill: {t['ink']}; }}
      .secondary {{ font-family: {FONT_STACK_SANS}; font-weight: 400; fill: {t['bark']}; }}
      .tertiary {{ font-family: {FONT_STACK_SANS}; font-weight: 400; fill: {t['taupe']}; }}
      .eyebrow {{ font-family: {FONT_STACK_SANS}; font-weight: 500; fill: {t['bark']}; letter-spacing: 0.08em; text-transform: uppercase; }}
      .swatch {{ stroke: {t['stone']}; stroke-width: 0.5; }}
    </style>
    """).strip()


# --- Petal mark paths (shared across hero and logo lockups) ---------------

PETAL_PATHS = dedent("""
    <path d="M65.722,56.344C64.034,53.66 52.775,35.753 65.819,16.711C72.968,6.273 74.472,16.509 78.588,18.268C80.151,18.936 80.012,17.98 85.663,12.684C91.068,7.618 113.164,43.17 82.271,66.183C77.884,69.451 73.233,65.664 65.722,56.344Z"/>
    <path d="M93.876,68.643C95.393,65.406 106.526,41.657 133.424,47.851C140.41,49.46 143.122,50.282 139.871,56.712C135.707,64.948 143.123,62.436 146.489,66.509C149.757,70.463 126.314,100.706 95.835,81.017C89.739,77.08 91.589,75.53 93.876,68.643Z"/>
    <path d="M46.467,87.257C43.355,87.49 21.845,89.099 11.812,69.35C9.441,64.682 20.955,63.512 19.808,60.427C17.4,53.955 13.02,51.79 19.429,49.337C51.567,37.033 70.842,73.774 65.523,78.523C58.09,85.158 48.117,86.959 46.467,87.257Z"/>
    <path d="M114.031,138.394C113.347,140.452 113.38,143.899 103.678,140.081C76.435,129.36 81.876,91.728 88.475,91.27C125.959,88.669 132.62,132.425 124.503,132.421C123.858,132.421 124.023,131.855 116.495,131.453C115.148,131.381 115.604,132.144 114.031,138.394Z"/>
    <path d="M43.88,138.418C42.871,132.813 42.91,132.842 42.79,132.365C42.133,129.746 32.68,134.228 31.505,131.498C26.176,119.119 40.651,88.637 69.532,91.233C74.89,91.714 83.776,126.799 54.607,139.757C43.078,144.878 43.896,138.463 43.88,138.418Z"/>
    <path d="M71.923,80.511C73.94,70.363 82.29,74.466 83.51,75.488C93.2,83.618 73.69,96.632 71.923,80.511Z"/>
""").strip()


def petal_mark(x: float, y: float, size: float, color: str, rotation: float = 0) -> str:
    # Native petal art is ~160 units wide (roughly 0..160). Scale accordingly.
    scale = size / 160.0
    cx = x + size / 2
    cy = y + size / 2
    rot = f"rotate({rotation} {cx} {cy})" if rotation else ""
    return (
        f'<g transform="{rot} translate({x} {y}) scale({scale}) translate(-5 -5)" '
        f'fill="{color}">{PETAL_PATHS}</g>'
    )


# --- Hero ------------------------------------------------------------------


def hero_svg(t: dict) -> str:
    W, H = 1280, 560
    petal = petal_mark(64, 160, 220, t["sakura_400"], rotation=-8)
    # Accent swatch strip at the bottom of the hero
    ramp = [t["sakura_50"], t["sakura_100"], t["sakura_200"], t["sakura_400"], t["sakura_600"], t["sakura_900"]]
    neutrals = [t["paper"], t["linen"], t["stone"], t["bark"], t["ink"]]
    swatch_size = 56
    gap = 8
    ramp_x = 360
    ramp_y = 420
    ramp_cells = ""
    for i, c in enumerate(ramp):
        ramp_cells += (
            f'<rect x="{ramp_x + i * (swatch_size + gap)}" y="{ramp_y}" '
            f'width="{swatch_size}" height="{swatch_size}" rx="4" '
            f'fill="{c}" class="swatch"/>'
        )
    neutral_x = 360 + 6 * (swatch_size + gap) + 24
    for i, c in enumerate(neutrals):
        ramp_cells += (
            f'<rect x="{neutral_x + i * (swatch_size + gap)}" y="{ramp_y}" '
            f'width="{swatch_size}" height="{swatch_size}" rx="4" '
            f'fill="{c}" class="swatch"/>'
        )

    return dedent(f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Softbloom — softness held by structure">
      {style_block(t)}
      <rect class="bg" width="{W}" height="{H}"/>
      {petal}
      <g>
        <text x="360" y="220" class="eyebrow" font-size="14">A personal design system · by jlwilley</text>
        <text x="360" y="308" class="display" font-size="88" letter-spacing="-0.02em">Softbloom.</text>
        <text x="360" y="360" class="display-italic" font-size="32" fill="{t['brand']}">softness held by structure.</text>
        <text x="360" y="404" class="secondary" font-size="16">Sakura-inspired colorways. Editorial type. 0.5px borders. Two modes: Softbloom &amp; Nightbloom.</text>
      </g>
      {ramp_cells}
      <text x="360" y="508" class="mono" font-size="11">SAKURA 50 → 900</text>
      <text x="{neutral_x}" y="508" class="mono" font-size="11">PAPER → INK</text>
    </svg>
    """).strip()


# --- Palette swatches ------------------------------------------------------


def palette_svg(t: dict, *, dark: bool) -> str:
    W = 1200

    if dark:
        ramps = [
            ("Glow pinks · the hero", [
                ("--petal", "#FFE8F0", "Body text"),
                ("--bloom", "#F8B8CE", "Soft accent"),
                ("--rose", "#F289AD", "Mid accent"),
                ("--carmine", "#D4577A", "Primary brand"),
                ("--cherry", "#9F3754", "Depth, focus"),
                ("--ember", "#4A1A2A", "Brand wash, danger"),
            ]),
            ("Night foundation · the workhorse", [
                ("--obsidian", "#0F0709", "Deepest ground"),
                ("--midnight", "#1A0F12", "App background"),
                ("--plum", "#261619", "Card surface"),
                ("--mulberry", "#3D2530", "Default border"),
                ("--dusk", "#8A6578", "Secondary text"),
                ("--petal", "#FFE8F0", "Primary text"),
            ]),
            ("Supporting accents · used sparingly", [
                ("--night-lilac", "#3A2F42", "Secondary states"),
                ("--moss", "#2D3A2F", "Success"),
                ("--amber", "#4A3820", "Warmth, warnings"),
                ("--wine", "#5C3848", "Depth"),
            ]),
        ]
    else:
        ramps = [
            ("Sakura · the hero", [
                ("--sakura-50", "#FFF7F9", "Softest wash"),
                ("--sakura-100", "#FBE4EC", "Tag backgrounds"),
                ("--sakura-200", "#F5B8CD", "Chart fills"),
                ("--sakura-400", "#E87FA0", "Decorative mid"),
                ("--sakura-600", "#B84668", "Primary brand"),
                ("--sakura-900", "#5C1A2E", "Dark text on pink"),
            ]),
            ("Warm neutrals · the workhorse", [
                ("--paper", "#FAF6F2", "App background"),
                ("--linen", "#F2EBE4", "Secondary surface"),
                ("--stone", "#E0D5CA", "Default border"),
                ("--taupe", "#A89589", "Tertiary text"),
                ("--bark", "#6B5A52", "Secondary text"),
                ("--ink", "#2B1F1C", "Primary text"),
            ]),
            ("Supporting accents · used sparingly", [
                ("--lilac", "#EFE4F0", "Secondary states"),
                ("--sage", "#DDE8DC", "Success, grounding"),
                ("--honey", "#F7E6D2", "Warmth, warnings"),
                ("--wine", "#7A2640", "Depth, focus"),
            ]),
        ]

    swatch_w = 176
    swatch_h = 120
    gap = 12
    left = 40
    row_label_h = 28
    row_vgap = 24
    row_gap = 40

    y = 130
    cells = ""
    for title, items in ramps:
        cells += f'<text x="{left}" y="{y}" class="eyebrow" font-size="11">{title}</text>\n'
        y += row_label_h
        for i, (token, color, desc) in enumerate(items):
            x = left + i * (swatch_w + gap)
            cells += (
                f'<rect x="{x}" y="{y}" width="{swatch_w}" height="{swatch_h}" rx="4" '
                f'fill="{color}" class="swatch"/>\n'
                f'<text x="{x}" y="{y + swatch_h + 22}" class="mono-ink" font-size="12">{token}</text>\n'
                f'<text x="{x}" y="{y + swatch_h + 40}" class="mono" font-size="11">{color.upper()}</text>\n'
                f'<text x="{x}" y="{y + swatch_h + 58}" class="tertiary" font-size="11">{desc}</text>\n'
            )
        y += swatch_h + 68 + row_gap - row_vgap

    H = y + 20

    mode_name = "Nightbloom · dark mode" if dark else "Softbloom · light mode"

    return dedent(f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{mode_name} palette">
      {style_block(t)}
      <rect class="bg" width="{W}" height="{H}"/>
      <text x="{left}" y="68" class="display" font-size="40" letter-spacing="-0.02em">Palette</text>
      <text x="{left}" y="96" class="secondary" font-size="14">{mode_name}</text>
      {cells}
    </svg>
    """).strip()


# --- Component showcase ----------------------------------------------------


def components_svg(t: dict, *, dark: bool) -> str:
    W = 1200

    def button(x, y, label, variant):
        h = 36
        pad = 16
        w = pad * 2 + len(label) * 7.4
        if variant == "primary":
            bg = t["brand"]
            fg = "#FFFFFF" if not dark else t["ink"]
            border = "none"
            return (
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}"/>'
                f'<text x="{x + w/2}" y="{y + 23}" class="sans-medium" fill="{fg}" font-size="13" text-anchor="middle">{label}</text>'
            )
        if variant == "secondary":
            return (
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
                f'fill="transparent" stroke="{t["brand"]}" stroke-width="0.5"/>'
                f'<text x="{x + w/2}" y="{y + 23}" class="sans-medium" fill="{t["brand_deep"]}" font-size="13" text-anchor="middle">{label}</text>'
            )
        # ghost
        return (
            f'<text x="{x + w/2}" y="{y + 23}" class="sans-medium" fill="{t["bark"]}" font-size="13" text-anchor="middle">{label}</text>'
        )

    # --- Button panel
    buttons_panel = dedent(f"""
    <g transform="translate(40 140)">
      <text class="eyebrow" font-size="11" y="0">Button</text>
      <text class="secondary" font-size="13" y="24">Primary, secondary, and ghost. 36px default, 0.5px hairline, 10px radius.</text>
      <g transform="translate(0 54)">
        {button(0, 0, "Primary action", "primary")}
        {button(170, 0, "Secondary", "secondary")}
        {button(310, 0, "Ghost", "ghost")}
      </g>
      <g transform="translate(0 110)">
        <text class="mono" font-size="11" x="0" y="0">filled, high emphasis</text>
        <text class="mono" font-size="11" x="170" y="0">outlined, medium</text>
        <text class="mono" font-size="11" x="310" y="0">text-only, low</text>
      </g>
    </g>
    """).strip()

    # --- Card panel
    card_panel = dedent(f"""
    <g transform="translate(40 340)">
      <text class="eyebrow" font-size="11" y="0">Card</text>
      <text class="secondary" font-size="13" y="24">Bounded container. 16px radius, 0.5px border, 20px padding.</text>
      <g transform="translate(0 50)">
        <rect width="360" height="180" rx="16" fill="{t['bg_surface']}" stroke="{t['stone']}" stroke-width="0.5"/>
        <text class="eyebrow" font-size="10" x="24" y="36">This week</text>
        <text class="display" font-size="22" x="24" y="72" letter-spacing="-0.01em">Active sessions</text>
        <line x1="24" y1="94" x2="336" y2="94" stroke="{t['stone']}" stroke-width="0.5"/>
        <text class="sans-medium" font-size="32" x="24" y="138" letter-spacing="-0.02em">12,418</text>
        <text class="secondary" font-size="13" x="24" y="160">+4.2% vs last week</text>
        <circle cx="316" cy="132" r="6" fill="{t['sakura_400']}"/>
      </g>
      <!-- Featured variant -->
      <g transform="translate(400 50)">
        <rect width="360" height="180" rx="16" fill="{t['bg_surface']}" stroke="{t['brand']}" stroke-width="2"/>
        <text class="eyebrow" font-size="10" x="24" y="36" fill="{t['brand']}">Featured</text>
        <text class="display" font-size="22" x="24" y="72" letter-spacing="-0.01em">Recommended plan</text>
        <line x1="24" y1="94" x2="336" y2="94" stroke="{t['stone']}" stroke-width="0.5"/>
        <text class="sans" font-size="13" x="24" y="120">Use the 2px feature border only for</text>
        <text class="sans" font-size="13" x="24" y="138">intentional emphasis. Never as default.</text>
      </g>
      <!-- Muted variant -->
      <g transform="translate(800 50)">
        <rect width="360" height="180" rx="16" fill="{t['bg_muted']}" stroke="{t['stone']}" stroke-width="0.5"/>
        <text class="eyebrow" font-size="10" x="24" y="36">Muted</text>
        <text class="display" font-size="22" x="24" y="72" letter-spacing="-0.01em">Section within section</text>
        <line x1="24" y1="94" x2="336" y2="94" stroke="{t['stone']}" stroke-width="0.5"/>
        <text class="sans" font-size="13" x="24" y="120">Elevation via background shift, not</text>
        <text class="sans" font-size="13" x="24" y="138">shadow. A quiet recess, not a rise.</text>
      </g>
    </g>
    """).strip()

    # --- Input panel
    input_panel = dedent(f"""
    <g transform="translate(40 610)">
      <text class="eyebrow" font-size="11" y="0">Input</text>
      <text class="secondary" font-size="13" y="24">36px height, focus ring via 3px brand-wash glow.</text>
      <g transform="translate(0 50)">
        <!-- default -->
        <rect width="240" height="36" rx="10" fill="{t['bg_surface']}" stroke="{t['stone']}" stroke-width="0.5"/>
        <text class="tertiary" font-size="14" x="12" y="23">your@email.com</text>
        <text class="mono" font-size="11" x="0" y="60">default</text>

        <!-- focus -->
        <g transform="translate(280 0)">
          <rect x="-3" y="-3" width="246" height="42" rx="13" fill="{t['brand_wash']}"/>
          <rect width="240" height="36" rx="10" fill="{t['bg_surface']}" stroke="{t['brand']}" stroke-width="0.5"/>
          <text class="sans" font-size="14" x="12" y="23" fill="{t['ink']}">jlwilley</text>
          <line x1="72" y1="11" x2="72" y2="25" stroke="{t['brand']}" stroke-width="1"/>
          <text class="mono" font-size="11" x="0" y="60">focus · 3px brand-wash ring</text>
        </g>

        <!-- filled -->
        <g transform="translate(560 0)">
          <rect width="240" height="36" rx="10" fill="{t['bg_surface']}" stroke="{t['stone']}" stroke-width="0.5"/>
          <text class="sans" font-size="14" x="12" y="23" fill="{t['ink']}">softness held by structure</text>
          <text class="mono" font-size="11" x="0" y="60">filled</text>
        </g>
      </g>
    </g>
    """).strip()

    # --- Tag panel
    tag_panel = dedent(f"""
    <g transform="translate(40 770)">
      <text class="eyebrow" font-size="11" y="0">Tag</text>
      <text class="secondary" font-size="13" y="24">Pill-shaped. 100 fill + 900 text from the same ramp. Never black on color.</text>
      <g transform="translate(0 54)">
        {tag_pill(0, 0, "sakura", t["sakura_100"], t["sakura_900"])}
        {tag_pill(110, 0, "lilac", t["lilac"], t["lilac_text"])}
        {tag_pill(190, 0, "sage", t["sage"], t["sage_text"])}
        {tag_pill(280, 0, "honey", t["honey"], t["honey_text"])}
      </g>
      <text class="mono" font-size="11" x="0" y="92">bg {t['sakura_100']}  text {t['sakura_900']}</text>
      <text class="mono" font-size="11" x="440" y="92">22px height · 10px horizontal padding · font-size 12</text>
    </g>
    """).strip()

    H = 870
    mode = "Nightbloom · dark mode" if dark else "Softbloom · light mode"

    return dedent(f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Component showcase · {mode}">
      {style_block(t)}
      <rect class="bg" width="{W}" height="{H}"/>
      <text x="40" y="68" class="display" font-size="40" letter-spacing="-0.02em">Components</text>
      <text x="40" y="96" class="secondary" font-size="14">Button · Card · Input · Tag · {mode}</text>
      {buttons_panel}
      {card_panel}
      {input_panel}
      {tag_panel}
    </svg>
    """).strip()


def tag_pill(x, y, label, bg, fg) -> str:
    w = 12 + len(label) * 7.5 + 8
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="999" fill="{bg}"/>'
        f'<text x="{x + w/2}" y="{y + 15}" class="sans" font-size="12" fill="{fg}" text-anchor="middle">{label}</text>'
    )


# --- Shape and motion ------------------------------------------------------


def shape_motion_svg(t: dict) -> str:
    W = 1200
    H = 440

    # Radii: 4 / 10 / 16 / pill
    def radius_tile(x, label, token, radius):
        return dedent(f"""
        <g transform="translate({x} 160)">
          <rect width="168" height="168" rx="{radius}" fill="{t['bg_surface']}" stroke="{t['stone']}" stroke-width="0.5"/>
          <text class="label" font-size="15" x="24" y="36">{label}</text>
          <text class="mono" font-size="11" x="24" y="56">{token}</text>
        </g>
        """).strip()

    tiles = "".join([
        radius_tile(40, "4px", "--radius-sm", 4),
        radius_tile(228, "10px", "--radius-md", 10),
        radius_tile(416, "16px", "--radius-lg", 16),
        radius_tile(604, "999px", "--radius-pill", 84),
    ])

    # Motion curve (ease-out-quint sampling)
    # y = 1 - (1 - x)^5
    curve_points = []
    import math
    for i in range(101):
        x = i / 100
        y = 1 - (1 - x) ** 5
        # Map to local coords
        curve_points.append((x * 240, (1 - y) * 168))
    path_d = "M " + " L ".join(f"{px:.2f},{py:.2f}" for px, py in curve_points)

    motion_panel = dedent(f"""
    <g transform="translate(832 160)">
      <rect width="320" height="168" rx="16" fill="{t['bg_surface']}" stroke="{t['stone']}" stroke-width="0.5"/>
      <g transform="translate(40 16)">
        <!-- axes -->
        <line x1="0" y1="168" x2="240" y2="168" stroke="{t['stone']}" stroke-width="0.5"/>
        <line x1="0" y1="0" x2="0" y2="168" stroke="{t['stone']}" stroke-width="0.5"/>
        <path d="{path_d}" fill="none" stroke="{t['brand']}" stroke-width="2" stroke-linecap="round"/>
        <circle cx="0" cy="168" r="3" fill="{t['brand_deep']}"/>
        <circle cx="240" cy="0" r="3" fill="{t['brand_deep']}"/>
      </g>
      <text class="label" font-size="13" x="40" y="12" opacity="0">.</text>
    </g>
    <text class="mono" font-size="11" x="872" y="354">ease-out-quint</text>
    <text class="mono" font-size="11" x="872" y="370">cubic-bezier(0.22, 1, 0.36, 1)</text>
    """).strip()

    return dedent(f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Shape and motion">
      {style_block(t)}
      <rect class="bg" width="{W}" height="{H}"/>
      <text x="40" y="68" class="display" font-size="40" letter-spacing="-0.02em">Shape &amp; motion</text>
      <text x="40" y="96" class="secondary" font-size="14">Four radii. One easing curve. 0.5px borders, always.</text>
      <text x="40" y="138" class="eyebrow" font-size="11">Corner radii</text>
      <text x="832" y="138" class="eyebrow" font-size="11">Soft landing</text>
      {tiles}
      {motion_panel}
    </svg>
    """).strip()


# --- Logo lockups ----------------------------------------------------------


import re as _re


def _inline_logo_svg(filename: str) -> str:
    """Return the inner content of a logo SVG file (everything inside
    the root <svg> element) so it can be dropped into a nested <svg>.

    Strips editor-specific namespaced attributes (serif:*, sodipodi:*,
    inkscape:*) that would otherwise trigger namespace errors when the
    inner content is reparented into a root that doesn't declare them.
    """
    raw = (LOGO / filename).read_text(encoding="utf-8")
    raw = _re.sub(r"<\?xml[^?]*\?>", "", raw)
    raw = _re.sub(r"<!DOCTYPE[^>]*>", "", raw)
    m = _re.search(r"<svg\b[^>]*>(.*)</svg>\s*$", raw, flags=_re.DOTALL)
    inner = m.group(1).strip() if m else raw.strip()
    inner = _re.sub(r'\s+(?:serif|sodipodi|inkscape):[\w-]+="[^"]*"', "", inner)
    return inner


def logo_lockups_svg(t: dict, *, dark: bool) -> str:
    W = 1200
    H = 500

    # Tile container + embedded logo artwork at the file's native viewBox.
    def tile(x, y, w, h, label, use_case, token, logo_inner, art_size=160, art_y=32, bg=None):
        bg = bg or t["bg_surface"]
        art_x = (w - art_size) / 2
        return dedent(f"""
        <g transform="translate({x} {y})">
          <rect width="{w}" height="{h}" rx="16" fill="{bg}" stroke="{t['stone']}" stroke-width="0.5"/>
          <svg x="{art_x}" y="{art_y}" width="{art_size}" height="{art_size}" viewBox="0 0 2000 2000" preserveAspectRatio="xMidYMid meet">
            {logo_inner}
          </svg>
          <text class="label" font-size="14" x="24" y="{h - 56}">{label}</text>
          <text class="secondary" font-size="12" x="24" y="{h - 36}">{use_case}</text>
          <text class="mono" font-size="11" x="24" y="{h - 16}">{token}</text>
        </g>
        """).strip()

    tile_h = 280

    # File selection per mode
    primary_file = "jw-primary-dark.svg" if dark else "jw-primary.svg"
    mono_file = "jw-mono-light.svg" if dark else "jw-mono.svg"
    petal_file = "petal-light.svg" if dark else "petal.svg"
    # jw-circle.svg has its own wine disc + cream mark, works on both bgs

    primary_inner = _inline_logo_svg(primary_file)
    mono_inner = _inline_logo_svg(mono_file)
    circle_inner = _inline_logo_svg("jw-circle.svg")
    petal_inner = _inline_logo_svg(petal_file)

    x0 = 40
    tw = 272
    gap = 16

    tiles = "".join([
        tile(x0 + 0 * (tw + gap), 140, tw, tile_h,
             "Primary", "Hero contexts, splash, letterhead",
             primary_file, primary_inner),
        tile(x0 + 1 * (tw + gap), 140, tw, tile_h,
             "Monochrome", "Where color would compete",
             mono_file, mono_inner),
        tile(x0 + 2 * (tw + gap), 140, tw, tile_h,
             "Circle", "Avatars, app icons, favicon",
             "jw-circle.svg", circle_inner, bg=t["bg_muted"]),
        tile(x0 + 3 * (tw + gap), 140, tw, tile_h,
             "Petal mark", "Small contexts, 16px minimum",
             petal_file, petal_inner),
    ])

    mode = "Nightbloom" if dark else "Softbloom"

    return dedent(f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Logo lockups · {mode}">
      {style_block(t)}
      <rect class="bg" width="{W}" height="{H}"/>
      <text x="40" y="68" class="display" font-size="40" letter-spacing="-0.02em">Logo lockups</text>
      <text x="40" y="96" class="secondary" font-size="14">Serif jw monogram with a five-petal sakura mark. Each lockup is tuned for a specific context.</text>
      {tiles}
    </svg>
    """).strip()


# --- Typography specimen (PNG via headless Chrome) ------------------------


def type_specimen_html(t: dict, mode_label: str) -> str:
    # HTML self-contained specimen, rendered offscreen by Chrome headless.
    return dedent(f"""
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8">
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,400&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
      <style>
        * {{ box-sizing: border-box; }}
        html, body {{ margin: 0; padding: 0; }}
        body {{
          width: 1200px;
          background: {t['bg_app']};
          font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
          color: {t['ink']};
          padding: 48px 40px;
        }}
        .display-serif {{ font-family: 'Fraunces', Georgia, serif; font-weight: 400; }}
        .italic {{ font-style: italic; }}
        .sans {{ font-family: 'Inter', -apple-system, sans-serif; }}
        .mono {{ font-family: 'JetBrains Mono', ui-monospace, monospace; }}
        h1.hero {{
          font-family: 'Fraunces', Georgia, serif;
          font-weight: 400;
          font-size: 40px;
          letter-spacing: -0.02em;
          margin: 0 0 8px;
          color: {t['ink']};
        }}
        .eyebrow {{
          font-family: 'Inter', sans-serif;
          font-weight: 500;
          font-size: 11px;
          letter-spacing: 0.08em;
          text-transform: uppercase;
          color: {t['bark']};
          margin: 0 0 4px;
        }}
        .subtitle {{ color: {t['bark']}; font-size: 14px; margin: 0 0 32px; }}
        .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }}
        .section + .section {{ margin-top: 40px; }}
        .row {{ display: flex; align-items: baseline; gap: 16px; padding: 8px 0; border-bottom: 0.5px solid {t['stone']}; }}
        .row:last-child {{ border-bottom: none; }}
        .token {{ flex: 0 0 120px; color: {t['bark']}; font-family: 'JetBrains Mono', monospace; font-size: 11px; }}
        .size-label {{ flex: 0 0 60px; color: {t['taupe']}; font-family: 'JetBrains Mono', monospace; font-size: 11px; text-align: right; }}
        .sample {{ color: {t['ink']}; }}
        .size-1 {{ font-size: 48px; line-height: 1.2; letter-spacing: -0.02em; }}
        .size-2 {{ font-size: 32px; line-height: 1.2; letter-spacing: -0.02em; }}
        .size-3 {{ font-size: 28px; line-height: 1.2; letter-spacing: -0.02em; }}
        .size-4 {{ font-size: 22px; line-height: 1.3; }}
        .size-5 {{ font-size: 18px; line-height: 1.4; }}
        .size-6 {{ font-size: 16px; line-height: 1.5; }}
        .size-7 {{ font-size: 15px; line-height: 1.5; }}
        .size-8 {{ font-size: 14px; line-height: 1.5; }}
        .size-9 {{ font-size: 13px; line-height: 1.5; }}
        .size-10 {{ font-size: 12px; line-height: 1.5; }}
        .family-card {{
          background: {t['bg_surface']};
          border: 0.5px solid {t['stone']};
          border-radius: 16px;
          padding: 24px;
        }}
        .family-label {{
          font-family: 'Inter', sans-serif;
          font-weight: 500;
          font-size: 11px;
          letter-spacing: 0.08em;
          text-transform: uppercase;
          color: {t['bark']};
          margin: 0 0 8px;
        }}
        .family-name {{
          font-family: 'Inter', sans-serif;
          font-weight: 500;
          font-size: 13px;
          color: {t['ink']};
          margin: 0 0 24px;
        }}
        .family-sample {{ color: {t['ink']}; }}
        .weight-row {{ display: flex; gap: 24px; margin-top: 20px; font-size: 13px; color: {t['bark']}; font-family: 'JetBrains Mono', monospace; }}
        .color-swatch {{ display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 6px; vertical-align: -1px; }}
      </style>
    </head>
    <body>
      <p class="eyebrow">Typography · {mode_label}</p>
      <h1 class="hero">Fraunces, Inter, &amp; JetBrains Mono.</h1>
      <p class="subtitle">Two weights only, 400 and 500. Sentence case always. No mid-sentence bolding.</p>

      <div class="section">
        <p class="eyebrow" style="margin-bottom: 16px;">Families</p>
        <div class="grid">
          <div class="family-card">
            <p class="family-label">Display</p>
            <p class="family-name">Fraunces · variable serif</p>
            <div class="display-serif family-sample" style="font-size: 48px; line-height: 1.1; letter-spacing: -0.02em;">Softness held<br>by structure.</div>
            <div class="weight-row"><span>400 regular</span><span style="font-weight:500;">500 medium</span><span class="italic" style="font-family:'Fraunces',serif; font-style:italic;">italic</span></div>
          </div>
          <div class="family-card">
            <p class="family-label">UI · Body</p>
            <p class="family-name">Inter · grotesk sans</p>
            <div class="sans family-sample" style="font-size: 20px; line-height: 1.5;">The workhorse. Every button, label, paragraph, tooltip, and form input runs on Inter at 14px.</div>
            <div class="weight-row"><span>400 regular</span><span style="font-weight:500;">500 medium</span></div>
          </div>
        </div>

        <div class="grid" style="margin-top: 16px;">
          <div class="family-card">
            <p class="family-label">Mono</p>
            <p class="family-name">JetBrains Mono · ligatures</p>
            <div class="mono family-sample" style="font-size: 15px; line-height: 1.6;">
              --sakura-600: #B84668;<br>
              --radius-md:&nbsp;&nbsp;&nbsp;10px;<br>
              --ease:&nbsp;cubic-bezier(.22,1,.36,1);
            </div>
          </div>
          <div class="family-card">
            <p class="family-label">Japanese · Decorative</p>
            <p class="family-name">Shippori Mincho · used sparingly</p>
            <div class="display-serif family-sample" style="font-size: 48px; line-height: 1.2; letter-spacing: -0.02em;">桜 <span style="color: {t['brand']};">•</span> bloom</div>
            <div class="weight-row"><span>Decorative pull quotes only · not UI</span></div>
          </div>
        </div>
      </div>

      <div class="section" style="margin-top: 48px;">
        <p class="eyebrow" style="margin-bottom: 12px;">Scale</p>
        <div class="row"><div class="token">--text-5xl</div><div class="size-label">48 / hero</div><div class="sample display-serif size-1">Softbloom.</div></div>
        <div class="row"><div class="token">--text-4xl</div><div class="size-label">32 / h1</div><div class="sample display-serif size-2">A sakura-inspired system.</div></div>
        <div class="row"><div class="token">--text-3xl</div><div class="size-label">28 / h2</div><div class="sample display-serif size-3">Softness held by structure.</div></div>
        <div class="row"><div class="token">--text-2xl</div><div class="size-label">22 / h3</div><div class="sample sans size-4" style="font-weight:500;">Card heading, editorial moment</div></div>
        <div class="row"><div class="token">--text-xl</div><div class="size-label">18 / sub</div><div class="sample sans size-5">Subheadings and emphasized UI</div></div>
        <div class="row"><div class="token">--text-lg</div><div class="size-label">16 / body</div><div class="sample sans size-6">Long-form body copy for readable paragraphs.</div></div>
        <div class="row"><div class="token">--text-md</div><div class="size-label">15 / emph</div><div class="sample sans size-7">Emphasized UI text and list items.</div></div>
        <div class="row"><div class="token">--text-base</div><div class="size-label">14 / ui</div><div class="sample sans size-8">Default UI text. The most common size on the screen.</div></div>
        <div class="row"><div class="token">--text-sm</div><div class="size-label">13 / meta</div><div class="sample sans size-9" style="color: {t['bark']};">Secondary UI text. Labels, meta, timestamps.</div></div>
        <div class="row"><div class="token">--text-xs</div><div class="size-label">12 / caption</div><div class="sample sans size-10" style="color: {t['taupe']}; letter-spacing: 0.08em; text-transform: uppercase;">Small uppercase labels with 0.08em tracking</div></div>
      </div>
    </body>
    </html>
    """).strip()


def find_browser() -> str:
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    for name in ("chrome", "msedge", "google-chrome", "chromium"):
        found = shutil.which(name)
        if found:
            return found
    raise RuntimeError("No Chrome/Edge found for PNG rendering.")


def render_png(html_path: Path, png_path: Path, width: int, height: int) -> None:
    browser = find_browser()
    # Chrome headless screenshot. --force-device-scale-factor=2 renders at 2x.
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        "--force-device-scale-factor=2",
        f"--window-size={width},{height}",
        f"--screenshot={png_path}",
        "--virtual-time-budget=8000",
        f"--default-background-color=00000000",
        html_path.as_uri(),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if not png_path.exists():
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        raise RuntimeError(f"Chrome did not produce {png_path}")


def trim_png_trailing_bg(path: Path, bg_hex: str, margin: int = 48) -> None:
    """Crop trailing rows that are uniformly the background color.

    Leaves `margin` CSS pixels of breathing room below the last content row
    (scaled by device pixel ratio inferred from image width).
    """
    try:
        from PIL import Image
    except ImportError:
        return
    r, g, b = int(bg_hex[1:3], 16), int(bg_hex[3:5], 16), int(bg_hex[5:7], 16)
    img = Image.open(path).convert("RGB")
    w, h = img.size
    dpr = max(1, round(w / 1200))
    pixels = img.load()
    # Find the last non-background row (scan from bottom up).
    last = 0
    for y in range(h - 1, -1, -1):
        # Sample across the row — check a handful of x positions for speed.
        for x in range(0, w, 8):
            pr, pg, pb = pixels[x, y]
            if abs(pr - r) + abs(pg - g) + abs(pb - b) > 6:
                last = y
                break
        if last:
            break
    new_h = min(h, last + margin * dpr)
    if new_h < h:
        img.crop((0, 0, w, new_h)).save(path, "PNG")


def type_specimen_png(t: dict, mode_label: str, out_name: str) -> None:
    html = type_specimen_html(t, mode_label)
    html_path = OUT / f".{out_name}.html"
    html_path.write_text(html, encoding="utf-8")
    try:
        png_path = OUT / out_name
        # Render taller than needed so content never clips, then post-trim
        # the trailing uniform-background area.
        render_png(html_path, png_path, width=1200, height=1680)
        trim_png_trailing_bg(png_path, bg_hex=t["bg_app"])
    finally:
        try:
            html_path.unlink()
        except FileNotFoundError:
            pass


# --- Main ------------------------------------------------------------------


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    targets = [
        ("hero-light.svg", hero_svg(LIGHT)),
        ("hero-dark.svg", hero_svg(DARK)),
        ("palette-light.svg", palette_svg(LIGHT, dark=False)),
        ("palette-dark.svg", palette_svg(DARK, dark=True)),
        ("components-light.svg", components_svg(LIGHT, dark=False)),
        ("components-dark.svg", components_svg(DARK, dark=True)),
        ("shape-motion-light.svg", shape_motion_svg(LIGHT)),
        ("shape-motion-dark.svg", shape_motion_svg(DARK)),
        ("logo-lockups-light.svg", logo_lockups_svg(LIGHT, dark=False)),
        ("logo-lockups-dark.svg", logo_lockups_svg(DARK, dark=True)),
    ]
    for name, contents in targets:
        (OUT / name).write_text(contents, encoding="utf-8")
        print(f"wrote {name}")

    type_specimen_png(LIGHT, "Softbloom · light mode", "type-specimen-light.png")
    print("wrote type-specimen-light.png")
    type_specimen_png(DARK, "Nightbloom · dark mode", "type-specimen-dark.png")
    print("wrote type-specimen-dark.png")


if __name__ == "__main__":
    main()
