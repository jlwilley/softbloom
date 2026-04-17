# Design language

The Softbloom design language in full. This is the source of truth for every decision downstream: component specs, logo direction, motion, voice.

## Philosophy

**Softness held by structure.**

The central tension of the system is the interplay between delicate surfaces and confident skeletons. A cherry blossom petal is soft, but the branch it sits on is deliberate. Every component should feel this way: quiet, well-made, generous with space, and held together by invisible but unshakable structure.

This system should never feel:
- Saccharine or childish (bubblegum pinks, rounded-everything, glitter)
- Corporate or sterile (pure grays, sharp everything, zero warmth)
- Performatively feminine (dripping with flourish, hearts, sparkles)

It should feel:
- Editorial (like a well-designed magazine)
- Considered (every choice has a reason)
- Warm (inviting, not clinical)
- Quiet (restraint as a feature)

## Color

Two modes: **Softbloom** (light) and **Nightbloom** (dark). Both share the same philosophy and structure. Dark mode is not an inversion; it's a parallel palette with the same personality.

### Light mode

**Sakura ramp** (the hero):
- `--sakura-50` `#FFF7F9` softest wash, section backgrounds
- `--sakura-100` `#FBE4EC` tag backgrounds, subtle fills
- `--sakura-200` `#F5B8CD` chart fills, soft accents
- `--sakura-400` `#E87FA0` decorative mid-tone (use sparingly)
- `--sakura-600` `#B84668` primary brand, buttons, links
- `--sakura-900` `#5C1A2E` dark text on pink surfaces

**Warm neutrals** (the workhorse):
- `--paper` `#FAF6F2` app background
- `--linen` `#F2EBE4` secondary surface
- `--stone` `#E0D5CA` default border
- `--taupe` `#A89589` tertiary text
- `--bark` `#6B5A52` secondary text
- `--ink` `#2B1F1C` primary text (never pure black)

**Supporting accents** (used sparingly):
- `--lilac` `#EFE4F0` secondary states
- `--sage` `#DDE8DC` success
- `--honey` `#F7E6D2` warmth, warnings
- `--wine` `#7A2640` depth, focus

### Dark mode (Nightbloom)

**Night foundation:**
- `--obsidian` `#0F0709`
- `--midnight` `#1A0F12` app background
- `--plum` `#261619` card surfaces
- `--mulberry` `#3D2530` borders
- `--dusk` `#8A6578` tertiary text

**Glow pinks:**
- `--petal` `#FFE8F0` body text
- `--bloom` `#F8B8CE` soft accent
- `--rose` `#F289AD` mid accent
- `--carmine` `#D4577A` primary brand
- `--cherry` `#9F3754` depth

### Color rules

1. **Two ramps per screen, max.** A component may pair sakura with sage, or sakura with lilac, but not all four.
2. **Pink does emotional work.** Never decoration. If pink is only there to "add color," remove it.
3. **Text on colored backgrounds uses the 800 or 900 stop from the same ramp.** Never black, never gray.
4. **Warm neutrals only.** Cool grays fight the pink.
5. **Primary text is never pure black.** `--ink` in light mode, `--petal` in dark.

## Shape

### Corner radii

Four radii, chosen deliberately:

- **`--radius-sm` (4px)** chips, tags, inline interactive elements
- **`--radius-md` (10px)** default for buttons, inputs, small cards
- **`--radius-lg` (16px)** containers, modals, hero surfaces
- **`--radius-pill` (999px)** counters, status badges, avatars only

**Rule:** never mix more than two radii in one component group. A pill button next to a rounded-10 button next to a sharp chip reads chaotic. Pick a hierarchy.

### Border weight

All borders are `--border-hairline` (0.5px). Always. On high-DPI screens 0.5px renders crisp and refined; 1px looks clunky against this palette.

The only exception: `--border-feature` (2px) for "featured" or "recommended" accent cards. This is a deliberate emphasis signal, not a default.

Never use rounded corners on single-sided borders. If you're using `border-left` as an accent, `border-radius` must be `0`.

### Elevation

Elevation via **background shift**, not shadow. Cards rise by shifting background color, not by drop shadow. This keeps the system flat and modern.

When shadow is necessary (hover states, modals, menus), use the subtle warm shadow tokens. Never pink-tinted shadows. Never glow effects. Never neumorphism.

## Typography

### Families

- **Display**: `Fraunces` (Google Fonts, variable). Used at 28px and above for headings, hero text, editorial moments.
- **UI/Body**: `Inter` or `General Sans`. All UI text, body copy, labels.
- **Mono**: `JetBrains Mono` or `IBM Plex Mono`. Code, tokens, data.
- **Japanese**: `Shippori Mincho` or `Noto Serif JP`. Used for Japanese text and the occasional decorative pull quote. Used sparingly.

### Weights

**Two weights only: 400 (regular) and 500 (medium).**

Never 600 or 700. Heavy weights fight the restraint of the system. If something needs more emphasis than 500 provides, change the size or color instead.

### Sizes

The scale is deliberate and compact. Most UI lives between 12px and 18px. Large sizes are reserved for true hero moments.

| Token | Size | Use |
|-------|------|-----|
| `--text-xs` | 12px | Small labels, captions |
| `--text-sm` | 13px | Secondary UI text |
| `--text-base` | 14px | Default UI text |
| `--text-md` | 15px | Emphasized UI |
| `--text-lg` | 16px | Body copy |
| `--text-xl` | 18px | Subheadings |
| `--text-2xl` | 22px | h3, card headings |
| `--text-3xl` | 28px | h2, section headings |
| `--text-4xl` | 32px | h1, page titles |
| `--text-5xl` | 48px | Hero display |

### Case and tracking

- **Sentence case everywhere.** Never Title Case. Never ALL CAPS.
- Small uppercase labels (eyebrow text above cards, for example) use `letter-spacing: 0.08em` and render at `--text-xs` or `--text-sm`.
- Large headings use `letter-spacing: -0.02em` to feel refined.
- **No mid-sentence bolding.** Bold is for headings and labels.

## Spacing

A 4px base unit. The system leans toward generous whitespace. When in doubt, add more.

- Component internal padding: 12px (tight), 16px (default), 24px (generous)
- Vertical rhythm between sections: 24px, 32px, 48px, 64px
- Gap between related items: 8px or 12px
- Gap between distinct items: 16px or 24px

## Iconography

- **Phosphor Icons** (regular or light weight) as the default set
- **Lucide** as the backup
- Never Material Icons (too Google), never Font Awesome (too dated)
- Stroke weight: 1.5px, not 2px
- Sizes: 16px inline, 20px standalone, 24px hero. Pick one per context, stick with it.
- Icons inherit `currentColor`. Never hardcode fill colors.

## Motion

Motion is where the system gets its feeling. Without it, Softbloom is a pretty static palette. With the right motion, it bloooms.

### Easing

**Default: `--ease-soft-landing`** (`cubic-bezier(0.22, 1, 0.36, 1)`).

This is ease-out-quint, which means fast start, slow finish. Like a door swinging gently closed. Every interaction should feel like a soft landing, not a punch.

### Duration

- `--duration-micro` (200ms) for hovers, focus, small state changes
- `--duration-state` (400ms) for opens, closes, toggles
- `--duration-page` (600ms) for page transitions

Never faster than 200ms (feels abrupt). Never slower than 600ms for anything other than decorative motion.

### Scale

- Hover lift: `1.01` or `1.02` max. Never `1.05` (cartoonish).
- Pressed state: `0.98` for tactile feedback.

### Staggering

When a list of items enters the page, stagger them by 40ms each. Everything should feel like it's blooming into place, not slamming down.

## Elevation

One decorative element per screen, maximum. A section might have:
- A soft gradient wash, OR
- A floating petal SVG, OR
- A delicate ornamental divider

Not two. Not three. One. The rest of the screen should be confident structure.

## Voice and writing

Tone guidelines for UI copy, documentation, marketing:
- Direct and warm, not corporate
- Short sentences, not walls of text
- Never use "simply," "just," or "easy" (condescending)
- Sentence case for all headings, buttons, labels
- No em dashes in running prose
- No exclamation points except in genuinely celebratory contexts

## The on-brand test

When deciding if something fits the system, run through these five questions:

1. Does it have a soft surface but confident structure?
2. Is the pink doing emotional work, or is it decoration?
3. Would the hierarchy still work in grayscale?
4. Does it feel intentional or generic?
5. Is there enough whitespace that it doesn't feel cramped?

If any answer is no, something's off. Fix the answer, then ship.
