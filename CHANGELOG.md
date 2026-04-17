# Changelog

All notable changes to Softbloom will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Pre-1.0 is iteration territory: breaking changes may land in minor versions.

## [Unreleased]

### Added
- README rebuilt as a live design showcase: hero, palette, typography, shape and motion, components, and logo lockups, each with Softbloom/Nightbloom variants via `<picture>` dark-mode swaps
- `docs/readme/` — generated showcase assets (ten SVGs plus two 2x type specimen PNGs) rendered by a single `build.py` script so they stay in sync with the token values
- Primary logo mark (serif "jw" + sakura petals) in five color variants: `jw-primary`, `jw-primary-dark`, `jw-mono`, `jw-mono-light`, `jw-mono-wine`
- Filled circle badge variant: `jw-circle.svg` / `jw-circle.png`
- Standalone petal mark in sakura-400, petal-cream, and sakura-900 (`petal.svg`, `petal-light.svg`, `petal-wine.svg`), plus raster exports
- Favicon set: `favicon.svg`, `favicon.ico`, `favicon-96x96.png`, `apple-touch-icon.png`, PWA icons (192/512), and `site.webmanifest` starter
- `jw-current.svg`: `currentColor`-driven monogram for CSS-colorable inline use

### Changed
- Replaced placeholder `petal.svg` (geometric ellipse construction) with the finalized brand petal artwork

## [0.1.0] - 2026-04-17

### Added
- Initial token set: colors, typography, spacing, radius, motion
- Light mode (Softbloom) and dark mode (Nightbloom) palettes
- Vanilla CSS stylesheet with `prefers-color-scheme` auto-switching and `data-theme` manual override
- Tailwind preset with semantic and raw color tokens
- Core design language documentation
- Component specs: button, card, tag, input, navigation
- Usage guide with three consumption patterns (vanilla CSS, Tailwind, partial copy)
- CLAUDE.md with maintainer instructions for Claude Code
- MIT license

[Unreleased]: https://github.com/YOUR_USERNAME/softbloom/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/YOUR_USERNAME/softbloom/releases/tag/v0.1.0
