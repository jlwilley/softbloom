# Component specifications

Starter set of core components. Each spec includes purpose, anatomy, variants, and a code example using Softbloom tokens.

Add new components here as you build them. Follow the pattern: purpose → anatomy → tokens used → variants → example.

## Button

Primary interactive affordance. Three visual weights: primary (filled), secondary (outlined), ghost (text-only).

### Anatomy

- Height: 36px default, 28px small, 44px large
- Horizontal padding: 16px default, 12px small, 20px large
- Border radius: `--radius-md` (10px)
- Border: `--border-hairline` (0.5px)
- Font: `--text-sm` (13px), weight 500
- Transition: all `--duration-micro` `--ease-soft-landing`

### Variants

**Primary** (filled, high emphasis)
- Background: `--color-brand`
- Text: `--color-text-inverse`
- Border: none
- Hover: background `--color-brand-deep`, scale `--scale-hover-lift`
- Active: scale `--scale-pressed`

**Secondary** (outlined, medium emphasis)
- Background: transparent
- Text: `--color-brand-deep`
- Border: 0.5px solid `--color-brand`
- Hover: background `--color-brand-wash`

**Ghost** (text-only, low emphasis)
- Background: transparent
- Text: `--color-text-secondary`
- Border: none
- Hover: background `--color-bg-muted`

### Example

```html
<button class="btn btn-primary">Primary action</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-ghost">Ghost</button>

<style>
.btn {
  height: 36px;
  padding: 0 16px;
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  cursor: pointer;
  transition: all var(--duration-micro) var(--ease-soft-landing);
}
.btn-primary {
  background: var(--color-brand);
  color: var(--color-text-inverse);
  border: none;
}
.btn-primary:hover {
  background: var(--color-brand-deep);
  transform: scale(var(--scale-hover-lift));
}
</style>
```

## Card

A bounded container for a single concept.

### Anatomy

- Background: `--color-bg-surface`
- Border: `--border-hairline` solid `--color-border`
- Radius: `--radius-lg` (16px)
- Padding: 20px default
- Optional header, body, footer zones separated by a 0.5px divider

### Variants

**Default** — standard card, white in light mode, plum in dark
**Featured** — 2px `--color-brand` border, otherwise identical. Use sparingly.
**Muted** — background `--color-bg-muted` instead of surface. For sections within sections.

### Example

```html
<article class="card">
  <header class="card-header">
    <p class="eyebrow">This week</p>
    <h3>Active sessions</h3>
  </header>
  <div class="card-body">...</div>
</article>

<style>
.card {
  background: var(--color-bg-surface);
  border: 0.5px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 20px;
}
.eyebrow {
  font-size: var(--text-xs);
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: var(--tracking-wide);
  font-weight: var(--weight-medium);
}
</style>
```

## Tag / pill

Small categorical labels. Pill-shaped.

### Anatomy

- Height: 22px (4px vertical padding)
- Horizontal padding: 10px
- Border radius: `--radius-pill`
- Font: `--text-xs` (12px), weight 400

### Color mapping

Always use the 100 fill + 900 text from the same ramp:
- Sakura: bg `--sakura-100`, text `--sakura-900`
- Lilac: bg `--lilac`, text `#4A2C52`
- Sage: bg `--sage`, text `#2A3D2C`
- Honey: bg `--honey`, text `#5C3A1F`

Never black text on colored pills.

## Input

Text input, single-line.

### Anatomy

- Height: 36px
- Horizontal padding: 12px
- Border: 0.5px solid `--color-border`
- Border radius: `--radius-md`
- Background: `--color-bg-surface`
- Text: `--text-base`, `--color-text-primary`
- Placeholder: `--color-text-tertiary`
- Focus: border `--color-brand`, box-shadow `0 0 0 3px var(--color-brand-wash)`

### Example

```html
<input type="text" class="input" placeholder="Your name" />

<style>
.input {
  height: 36px;
  padding: 0 12px;
  border: 0.5px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-bg-surface);
  font-size: var(--text-base);
  color: var(--color-text-primary);
  transition: all var(--duration-micro) var(--ease-soft-landing);
}
.input:focus {
  outline: none;
  border-color: var(--color-brand);
  box-shadow: 0 0 0 3px var(--color-brand-wash);
}
</style>
```

## Navigation

Horizontal nav bar.

### Anatomy

- Bottom border: 0.5px solid `--color-border`
- Vertical padding: 16px
- Link color: `--color-text-secondary` default, `--color-text-primary` on active
- Active link: font-weight 500
- Gap between links: 18px
- Logo on left, links on right (or whatever makes sense)

---

*More components to be added as they're built. Follow the same structure: purpose, anatomy, variants, code.*
