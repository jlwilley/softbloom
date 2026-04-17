/**
 * Softbloom Tailwind preset
 *
 * Usage in your project's tailwind.config.js:
 *
 *   import softbloom from '@jaredw/softbloom/tailwind/softbloom.preset.js';
 *
 *   export default {
 *     presets: [softbloom],
 *     content: ['./src/**\/*.{js,ts,jsx,tsx}'],
 *   };
 */

/** @type {import('tailwindcss').Config} */
export default {
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        sakura: {
          50:  '#FFF7F9',
          100: '#FBE4EC',
          200: '#F5B8CD',
          400: '#E87FA0',
          600: '#B84668',
          900: '#5C1A2E',
        },
        paper: '#FAF6F2',
        linen: '#F2EBE4',
        stone: '#E0D5CA',
        taupe: '#A89589',
        bark:  '#6B5A52',
        ink:   '#2B1F1C',

        lilac: '#EFE4F0',
        sage:  '#DDE8DC',
        honey: '#F7E6D2',
        wine:  '#7A2640',

        night: {
          obsidian: '#0F0709',
          midnight: '#1A0F12',
          plum:     '#261619',
          mulberry: '#3D2530',
          wine:     '#5C3848',
          dusk:     '#8A6578',
          petal:    '#FFE8F0',
          bloom:    '#F8B8CE',
          rose:     '#F289AD',
          carmine:  '#D4577A',
          cherry:   '#9F3754',
        },

        // Semantic aliases (use these in components when possible)
        surface: {
          DEFAULT: 'var(--color-bg-surface)',
          app:     'var(--color-bg-app)',
          muted:   'var(--color-bg-muted)',
        },
        content: {
          DEFAULT:   'var(--color-text-primary)',
          secondary: 'var(--color-text-secondary)',
          tertiary:  'var(--color-text-tertiary)',
        },
        brand: {
          DEFAULT: 'var(--color-brand)',
          deep:    'var(--color-brand-deep)',
          wash:    'var(--color-brand-wash)',
        },
      },

      fontFamily: {
        display: ['Fraunces', 'GT Super', 'Georgia', 'serif'],
        sans:    ['Inter', 'General Sans', '-apple-system', 'sans-serif'],
        mono:    ['JetBrains Mono', 'IBM Plex Mono', 'ui-monospace', 'monospace'],
        jp:      ['Shippori Mincho', 'Noto Serif JP', 'serif'],
      },

      fontSize: {
        'xs':   ['12px', { lineHeight: '1.4' }],
        'sm':   ['13px', { lineHeight: '1.5' }],
        'base': ['14px', { lineHeight: '1.6' }],
        'md':   ['15px', { lineHeight: '1.6' }],
        'lg':   ['16px', { lineHeight: '1.7' }],
        'xl':   ['18px', { lineHeight: '1.5' }],
        '2xl':  ['22px', { lineHeight: '1.3' }],
        '3xl':  ['28px', { lineHeight: '1.2' }],
        '4xl':  ['32px', { lineHeight: '1.2', letterSpacing: '-0.02em' }],
        '5xl':  ['48px', { lineHeight: '1.1', letterSpacing: '-0.02em' }],
      },

      fontWeight: {
        regular: '400',
        medium:  '500',
      },

      letterSpacing: {
        tight:  '-0.02em',
        normal: '0',
        wide:   '0.08em',
      },

      spacing: {
        // Tailwind's defaults are already 4px-based, but these are our canonical set
        '0':  '0',
        '1':  '4px',
        '2':  '8px',
        '3':  '12px',
        '4':  '16px',
        '5':  '20px',
        '6':  '24px',
        '8':  '32px',
        '10': '40px',
        '12': '48px',
        '16': '64px',
        '20': '80px',
      },

      borderRadius: {
        none: '0',
        sm:   '4px',
        md:   '10px',
        lg:   '16px',
        pill: '999px',
      },

      borderWidth: {
        hairline: '0.5px',
        feature:  '2px',
      },

      boxShadow: {
        sm: '0 1px 3px rgba(107, 90, 82, 0.06)',
        md: '0 2px 8px rgba(107, 90, 82, 0.08)',
        lg: '0 8px 24px rgba(107, 90, 82, 0.10)',
      },

      transitionDuration: {
        micro: '200ms',
        state: '400ms',
        page:  '600ms',
      },

      transitionTimingFunction: {
        'soft-landing': 'cubic-bezier(0.22, 1, 0.36, 1)',
        'soft-start':   'cubic-bezier(0.65, 0, 0.35, 1)',
      },

      scale: {
        '98':  '0.98',
        '101': '1.01',
        '102': '1.02',
      },
    },
  },
};
