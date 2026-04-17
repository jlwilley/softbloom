# Softbloom

A personal design system by jlwilley. Sakura-inspired, editorial, quiet but confident.

The system is built around a single idea: **softness held by structure**. Every choice, from the color ramps to the corner radii to the motion curves, balances a soft surface against a confident skeleton.

## What's in here

- `tokens/` — Design tokens in JSON (Style Dictionary compatible)
- `css/` — Vanilla CSS variables for light and dark mode
- `tailwind/` — A Tailwind preset you can extend from
- `logo/` — SVG logo files in all lockups
- `docs/` — The full design language, component specs, and usage guide

## Quick start

### In a vanilla HTML/CSS project

```html
<link rel="stylesheet" href="https://raw.githubusercontent.com/YOUR_USERNAME/softbloom/main/css/softbloom.css">
```

Then use the variables:

```css
.my-card {
  background: var(--color-surface);
  color: var(--color-text-primary);
  border: 0.5px solid var(--color-border);
  border-radius: var(--radius-lg);
}
```

### In a Tailwind project

```js
// tailwind.config.js
import softbloom from './path/to/softbloom/tailwind/softbloom.preset.js';

export default {
  presets: [softbloom],
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
};
```

Then use the utility classes:

```jsx
<div className="bg-paper text-ink border-stone rounded-lg p-4">
  <h2 className="text-sakura-600">Hello sakura</h2>
</div>
```

## The palette at a glance

### Light mode (Softbloom)

| Token | Hex | Role |
|-------|-----|------|
| `--sakura-50` | `#FFF7F9` | Softest background wash |
| `--sakura-600` | `#B84668` | Primary brand, buttons, links |
| `--sakura-900` | `#5C1A2E` | Dark text on pink, deep accents |
| `--paper` | `#FAF6F2` | App background |
| `--ink` | `#2B1F1C` | Body text (never pure black) |
| `--wine` | `#7A2640` | Depth, focus states |

### Dark mode (Nightbloom)

| Token | Hex | Role |
|-------|-----|------|
| `--obsidian` | `#0F0709` | Deepest background |
| `--midnight` | `#1A0F12` | App background |
| `--plum` | `#261619` | Card surfaces |
| `--rose` | `#F289AD` | Primary accent |
| `--petal` | `#FFE8F0` | Body text (never pure white) |

Full palette and tokens are in `docs/design-language.md`.

## Principles

1. **Softness held by structure.** Soft surfaces, confident skeletons.
2. **Pink does emotional work.** Neutrals do the heavy lifting. Never decorate with pink.
3. **Warm neutrals, never cool grays.** Cool grays fight the pink.
4. **0.5px borders, always.** Not 1px. Refinement lives in the details.
5. **Two type weights, 400 and 500.** Never 700.
6. **One decorative element per screen, max.**
7. **Grayscale test.** If hierarchy fails in grayscale, it fails.

## Versioning

This system follows semantic versioning once published. Pre-1.0 is iteration territory: breaking changes as the system matures. Post-1.0, tokens are locked and changes go through proper deprecation.

- `0.x.x` — active iteration, expect breaking changes
- `1.0.0` — first stable release
- See `CHANGELOG.md` for release history

## Contributing

This is a personal system, but issues and suggestions are welcome. See `docs/usage.md` for how to work with it in your own projects.

## License

MIT. Use it, remix it, make it yours.
