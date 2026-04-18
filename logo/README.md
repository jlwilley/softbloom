# Logo assets

## Primary mark (serif "jw" + sakura petals)

| File | Use |
| --- | --- |
| `jw-primary.svg` | Default. Sakura-900 strokes, sakura-400 petals. Light backgrounds. |
| `jw-primary-dark.svg` | Inverse. Petal-cream strokes for dark backgrounds. |
| `jw-mono.svg` | Monochrome in `--ink`. Use where color would compete. |
| `jw-mono-light.svg` | Monochrome in `--petal` for dark backgrounds. |
| `jw-mono-wine.svg` | Monochrome in sakura-900 for tonal light surfaces. |
| `jw-current.svg` | Monochrome using `currentColor`. Inline the SVG and set CSS `color` to drive the fill. |
| `jw-circle.svg` / `jw-circle.png` | Filled wine disc with cream mark. Avatars, app icons, small contexts needing a bounded shape. |

## Wordmark (full "jlwilley" lockup)

The full signature: sakura petals paired with the serif wordmark. Use on hero surfaces, brand headers, and anywhere the monogram alone would underplay the name.

| File | Use |
| --- | --- |
| `jw-wordmark.svg` | Default. Sakura-900 wordmark, sakura-400 petals. Light backgrounds. |
| `jw-wordmark-dark.svg` | Inverse. Petal-cream wordmark, dark-rose petals. Dark backgrounds. |
| `jw-wordmark-current.svg` | Monochrome using `currentColor`. Inline the SVG and set CSS `color` to drive both petals and wordmark from one property. |

Minimum width: 160px. Below that, reach for `jw-primary.svg` or the standalone petal.

## Petal mark (standalone)

The five-petal sakura mark without the monogram. Use at small sizes or where the full lockup would feel heavy.

| File | Use |
| --- | --- |
| `petal.svg` / `petal.png` | Default sakura-400 pink. |
| `petal-light.svg` | Petal-cream for dark backgrounds. |
| `petal-wine.svg` | Sakura-900 for restrained tonal use. |
| `petal-full.png` / `petal-light-full.png` | Full-bleed raster exports. |

## Favicon

`favicon/` contains `favicon.svg`, `favicon.ico`, `favicon-96x96.png`, `apple-touch-icon.png` (180x180), and PWA icons at 192/512. `site.webmanifest` is a starter; consumers should replace `name`, `short_name`, and `theme_color` per their app.

## Design constraints

- Primary color: `--sakura-900` (#5C1A2E). Accent petal: `--sakura-400` (#E87FA0).
- Monogram must hold up from 24px through 512px.
- Petal-only mark: 16px minimum.

## Clear space

Minimum clear space around the primary mark: equal to the height of the "w" character.
