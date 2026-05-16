# adilislam.com

Personal brand site for Adil Islam — AI product strategy, daily Signal briefings, research articles, free frameworks, and kids' projects.

## Quick Start

```bash
# Just open index.html — no build step, no framework, no server needed
open index.html
```

All pages use relative paths (`../assets/styles.css`) and work with `file:///` local viewing.

## Deploy

GitHub Pages from `main` branch, root `/`. Custom domain: `adilislam.com`.

## Structure

```
/                    Homepage — 4 sections + Kids + latest Signal
/about/              Bio, experience timeline, education, resume link
/signal/             Signal landing
/signal/bulletins/   68 daily AI bulletins
/signal/issues/      11 weekly vibe checks
/writing/            68 research articles
/teaching/           Frameworks, guides, AI 101 Austin course
/kidstuff/           Kids project showcase (5 projects + philosophy)
/resume/             Interactive resume (6 themes, self-contained)
/contact/            Email + section cards
/assets/styles.css   Dark editorial design system
```

## Design

- **Theme:** Dark editorial (`#09090b` bg, `#e05a30` accent)
- **Fonts:** Fraunces (display), Inter (body), JetBrains Mono (metadata)
- **Voice:** Declarative, structural, educator tone. No emojis, no negation patterns, no first-person brand voice.

## Separation Rules

This site is **legally separated** from any other business entity. Key rules:

- No mentions of any other company or product brand
- No links to commercial product pages from this site
- No vendor/founder language — educator/practitioner tone only
- Kids project links point to those projects' own sites

## Tech

- Static HTML + CSS. No build step, no JS frameworks, no CI.
- Resume page (`/resume/`) is self-contained with 6 switchable themes and inline styles.
- Push to `main` = deploy via GitHub Pages.