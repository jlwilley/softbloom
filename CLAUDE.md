# CLAUDE.md

This file gives Claude Code the context it needs to work effectively in this repo.

## Project overview

Softbloom is a personal design system built around a sakura (cherry blossom) aesthetic. The system has two modes: **Softbloom** (light) and **Nightbloom** (dark). It's designed to be consumed across multiple frontend projects (portfolios, client work, internal tools) as a single source of truth for colors, typography, spacing, motion, and shape.

The system is opinionated. Every choice follows from one design philosophy: **softness held by structure.** Soft surfaces, confident skeletons.

## Your role when working in this repo

You are the maintainer. When I ask you to make changes, you should:

1. **Protect the design philosophy.** Before adding or changing any token, ask whether it fits the "softness held by structure" principle. If I propose something that breaks the system (for example, a bright saturated blue, or a 2px border), push back. Explain why. Offer alternatives that fit the system.

2. **Keep the system coherent.** Every token change ripples. If I update `--sakura-600`, you need to check:
   - Does the dark mode equivalent need to shift?
   - Does it still have sufficient contrast against `--paper` and `--ink`?
   - Does it still work in the Tailwind preset?
   - Does the component documentation need updating?

3. **Document changes in the changelog.** Every meaningful change gets an entry in `CHANGELOG.md` under `## Unreleased`. Group changes by Added/Changed/Removed/Fixed.

4. **Keep the three sources in sync.** Tokens live canonically in `tokens/*.json`. The `css/softbloom.css` file and `tailwind/softbloom.preset.js` are derived from those. If I change a JSON token, update the CSS and Tailwind files to match. If I ask you to automate this later with Style Dictionary, do that.

5. **Never break existing consumers silently.** This system is imported into other projects. Renaming a token is a breaking change. If I ask you to rename something pre-1.0, do it. Post-1.0, deprecate with an alias and warn.

## Repository structure

```
softbloom/
├── README.md                  # Front door, quick start, principles
├── CLAUDE.md                  # This file
├── CHANGELOG.md               # Release history
├── LICENSE                    # MIT
├── package.json               # npm metadata for consumption
├── tokens/                    # Canonical token source (JSON)
│   ├── colors.json
│   ├── typography.json
│   ├── spacing.json
│   ├── radius.json
│   └── motion.json
├── css/                       # Derived CSS output
│   ├── softbloom.css          # Light mode + prefers-color-scheme dark
│   └── softbloom.tokens.css   # Raw variables only, no selectors
├── tailwind/
│   └── softbloom.preset.js    # Tailwind preset export
├── logo/
│   ├── jw-primary.svg         # Primary serif + petal mark
│   ├── jw-mono.svg            # Monochrome variant
│   ├── petal.svg              # Standalone petal for small contexts
│   └── favicon/               # Exported favicon sizes
├── docs/
│   ├── design-language.md     # Philosophy, shape, type, motion
│   ├── components.md          # Component specifications
│   └── usage.md               # How to consume this in a project
└── examples/                  # Optional reference implementations
```

## Design principles (enforce these)

These aren't suggestions. When writing code, proposing changes, or answering design questions, these rules apply:

### Color
- **Warm neutrals only.** Never propose cool grays. If I ask for gray, use `--taupe`, `--bark`, or `--stone`.
- **Never pure black for text.** Body text is `--ink` (`#2B1F1C`) in light mode, `--petal` (`#FFE8F0`) in dark mode.
- **Pink is the hero, not decoration.** It should do emotional work. Never suggest pink for a decorative border, background pattern, or non-brand context.
- **Two color ramps per screen, max.** If a component uses sakura and sage, it doesn't also use lilac and honey.
- **Text on colored backgrounds uses the 800 or 900 stop of that same ramp,** never black or gray.

### Shape
- **Three corner radii: 4px, 10px, 16px.** Plus `999px` (pill) for specific uses. Never mix more than two in one component.
- **Borders are 0.5px.** Always. Never 1px. Never 2px except for "featured" accent cases.
- **No rounded corners on single-sided borders.** If using `border-left`, set `border-radius: 0`.

### Typography
- **Two weights only: 400 and 500.** Never 600 or 700. Never italic for UI (display serifs are the exception).
- **Sentence case always.** Never Title Case. Never ALL CAPS except for small uppercase labels with `letter-spacing: 0.08em`.
- **No mid-sentence bolding.** Bold is for headings and labels.
- **Display font: Fraunces.** UI font: Inter or General Sans. Mono: JetBrains Mono.

### Spacing
- **4px base unit.** Multiples only: 4, 8, 12, 16, 24, 32, 48.
- **Generous whitespace.** When in doubt, add more padding. This system leans toward breathing room.

### Motion
- **Ease-out-quint: `cubic-bezier(0.22, 1, 0.36, 1)`.** Slow finish. Soft landing.
- **Durations: 200ms (micro), 400ms (state), 600ms (page).**
- **Hover scale 1.01 or 1.02 max.** Never 1.05.

### Elevation
- **Shift via background, not shadow.** Cards elevate by shifting background, not by drop shadow.
- **If a shadow is necessary:** warm, subtle. `0 1px 3px rgba(107, 90, 82, 0.06)` in light mode. Never pink-tinted.

## Common tasks

### Adding a new token

1. Add it to the appropriate JSON file in `tokens/`
2. Update `css/softbloom.css` and `css/softbloom.tokens.css`
3. Update `tailwind/softbloom.preset.js` if it's a class-generating token
4. Document it in `docs/design-language.md` with intent/usage notes
5. Add a changelog entry under `## Unreleased > Added`

### Changing an existing token value

1. Verify the change passes contrast checks against paired tokens (WCAG AA minimum for body text)
2. Update JSON → CSS → Tailwind in that order
3. Check all docs references and mockup examples
4. Changelog entry under `## Unreleased > Changed`
5. Flag in your response if this is a visual breaking change

### Adding a component spec

1. Add to `docs/components.md` with: purpose, anatomy, variants, spacing, motion, accessibility notes, code example
2. Use existing tokens only. If you find yourself wanting a new token, STOP and propose adding the token first.
3. Changelog entry under `## Unreleased > Added`

### Responding to "does this fit the system?"

Walk through the five-part test from the README:
1. Soft surface, confident structure?
2. Pink doing emotional work or decoration?
3. Works in grayscale?
4. Feels intentional or generic?
5. Enough whitespace?

Answer honestly. Tell me when something doesn't fit, and propose a version that does.

## What to push back on

- Requests to add colors outside the palette without a clear system-level reason
- Requests to use 1px borders instead of 0.5px (this is a signature decision)
- Requests to use 700+ weight (breaks the restraint)
- Requests to add drop shadows beyond the subtle warm shadow token
- "Can you just make this one thing bright saturated pink" — no, that's what `--sakura-400` is for, use the ramp
- "Let's add a second accent color to this screen" when two color families are already in play
- Requests for emoji in UI (not part of the system aesthetic)

When you push back, be kind and direct. Explain the principle, propose an alternative that does fit. I want you to protect the system, not just execute instructions.

## Tone for documentation

When you write docs, follow these:
- Sentence case for headings
- Short paragraphs, not walls of text
- Code examples for every concept
- Direct language, no fluff
- Never use "simply" or "just" or "easy" in instructions (condescending)
- Never use em dashes in running prose

## When you're not sure

Ask me. This system is personal and I have opinions. If you're making a design choice without a clear token-level mapping, surface it instead of guessing.
