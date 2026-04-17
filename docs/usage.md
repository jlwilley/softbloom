# Using Softbloom in a project

Three ways to consume this system, ordered by complexity.

## Option 1: Drop-in CSS (simplest)

Link the stylesheet from GitHub raw or copy the file into your project.

```html
<link rel="stylesheet" href="https://raw.githubusercontent.com/YOUR_USERNAME/softbloom/main/css/softbloom.css">
```

Then use CSS variables in your own stylesheets:

```css
.my-button {
  background: var(--color-brand);
  color: var(--color-text-inverse);
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  transition: all var(--duration-micro) var(--ease-soft-landing);
}
```

Dark mode activates automatically via `prefers-color-scheme`. To force a mode:

```html
<html data-theme="dark">
```

## Option 2: Tailwind preset (recommended for Next.js / React)

### Install

If Softbloom is published to npm:

```bash
npm install @jaredw/softbloom
```

If using as a git submodule or local package:

```bash
npm install github:YOUR_USERNAME/softbloom
```

### Configure

```js
// tailwind.config.js
import softbloom from '@jaredw/softbloom/tailwind/softbloom.preset.js';

export default {
  presets: [softbloom],
  content: ['./app/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
};
```

Import the base CSS once in your root layout:

```js
// app/layout.tsx
import '@jaredw/softbloom/css/softbloom.css';
```

### Use

```jsx
export function Card() {
  return (
    <div className="bg-surface border-hairline border-stone rounded-lg p-5">
      <h3 className="text-xl font-medium text-content">Hello</h3>
      <p className="text-base text-content-secondary mt-2">
        Soft surface, confident structure.
      </p>
    </div>
  );
}
```

## Option 3: Copy what you need

If you just want the tokens and not the full package, the `css/softbloom.tokens.css` file is pure variables with no component styles. Drop it in and go.

## Setting up fonts

Softbloom uses Fraunces, Inter, and JetBrains Mono. In a Next.js project:

```js
// app/layout.tsx
import { Fraunces, Inter, JetBrains_Mono } from 'next/font/google';

const fraunces = Fraunces({
  subsets: ['latin'],
  variable: '--font-display-custom',
});

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-sans-custom',
});

const mono = JetBrains_Mono({
  subsets: ['latin'],
  variable: '--font-mono-custom',
});

export default function RootLayout({ children }) {
  return (
    <html className={`${fraunces.variable} ${inter.variable} ${mono.variable}`}>
      <body>{children}</body>
    </html>
  );
}
```

Then override the Softbloom font families in your project CSS:

```css
:root {
  --font-display: var(--font-display-custom), 'Fraunces', serif;
  --font-sans:    var(--font-sans-custom), 'Inter', sans-serif;
  --font-mono:    var(--font-mono-custom), 'JetBrains Mono', monospace;
}
```

## Best practices

**Use semantic tokens, not raw colors.** `var(--color-brand)` will adapt to dark mode automatically. `var(--sakura-600)` will not.

**Don't invent new tokens in consumer projects.** If you find yourself needing a color that isn't in the system, either use an existing token or propose adding one to the system itself (then use it everywhere).

**Respect the component specs.** If the system says buttons are 36px, don't make yours 40px because the designer on a Figma comp drew them that way. Either update the system or use the spec.

**Test in both modes.** Always check your UI in light AND dark mode before shipping.

**File an issue when something's missing.** This is a living system. When a project needs something that doesn't exist, that's a signal the system should grow.

## Versioning

Pin to a specific version in production projects to avoid surprise breaking changes:

```json
{
  "dependencies": {
    "@jaredw/softbloom": "^0.2.0"
  }
}
```

Pre-1.0, breaking changes are marked in the changelog but not in the version number's major digit (standard semver for unstable APIs).
