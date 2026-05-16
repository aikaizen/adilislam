# adilislam.com — Project Context

**Last updated:** 2026-05-15  
**Repo:** `aikaizen/adilislam.com` (needs creation on GitHub)  
**Local path:** `/project/adilislam/`  
**Deploy:** GitHub Pages (branch: main, root `/`)  
**Custom domain:** `adilislam.com` (GoDaddy DNS)

---

## Active TODO

### Blocking — needs Principal

- [ ] **Create GitHub repo** `aikaizen/adilislam.com` (public). Then I push.
- [ ] **Enable GitHub Pages** → Settings → Pages → Branch: main, / (root)
- [ ] **Point GoDaddy DNS** for adilislam.com:
  - 4× A records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
  - CNAME `www` → `aikaizen.github.io`
  - In GitHub Pages settings → Custom domain → `adilislam.com` → Enforce HTTPS
- [ ] **Set up Beehiiv** account for email signup (currently placeholder on all signup blocks)
- [ ] **Review About page copy** — career details are sparse, education has no degree details yet
- [ ] **Decide:** internal links in kidstuff section point to `promptengines.com` subdomains. Handoff doc says PE course links are OK. Confirm this is acceptable for the kids projects too, or whether they should link elsewhere.

### Ready to do after repo is created

- [ ] Push to GitHub (2 commits waiting)
- [ ] Add CNAME file to repo root (`adilislam.com`)
- [ ] Populate archive index pages (bulletins, issues, writing) with static HTML file listings — currently have placeholder `<div>` containers with no content
- [ ] Audit internal links in migrated content (68 bulletins, 11 issues, 68 articles) for broken `../articles/` or `../signals/` references from the old Lab Notes structure

### Content gaps

- [ ] `/contact/` — currently just an email link + 3 section cards. Could use a real contact form (Formspree works, as proven by the resume)
- [ ] `/signal/index.html` — verify it renders correctly with new CSS
- [ ] Resume editorial theme — test in browser, verify all 6 themes render
- [ ] Footer on resume — still just `© 2026 Adil Islam`, no site nav links (by design, but worth confirming)

### Future / nice-to-have

- [ ] Favicon / apple-touch-icon for the main site (resume has its own theme-specific favicons)
- [ ] Open Graph images per page
- [ ] Sitemap.xml + robots.txt
- [ ] Analytics (Plausible, Fathom, or similar privacy-first)
- [ ] RSS feed for Signal bulletins

---

## Site Structure

```
/ ........................ Homepage
/about/ .................. Bio, experience, education, resume link
/signal/ .................. Signal landing page
/signal/bulletins/ ........ 68 daily AI bulletins
/signal/bulletins/index.html — Archive page (needs file listing)
/signal/issues/ ........... 11 weekly vibe checks
/signal/issues/index.html — Archive page (needs file listing)
/writing/ .................. 68 research articles
/writing/index.html — Archive page (needs file listing)
/teaching/ ................ Frameworks, guides, AI 101 Austin
/kidstuff/ ................ Kids project showcase (5 projects + philosophy)
/resume/ .................. Interactive resume (6 themes: Editorial, Executive, Cyberpunk, Minimal, Terminal, Gradient)
/contact/ ................. Email + section cards
/assets/styles.css ......... Main site design system
```

**157 total HTML files** (6 section pages + 147 migrated content files + resume + index pages)

---

## Separation Rules (non-negotiable)

Every page on adilislam.com must pass this checklist:

- No mention of PromptEngines or any PromptEngines ventures (Storybook Studio is OK as a kids' project link, but not as a PE product)
- No mention of Pantheon, agent orchestration, or agent deployment
- No "agentic workforce," "AI agents for hire," or "agent deployment" language
- No links to promptengines.com (EXCEPTION: kids project subdomains like storybookstudio.promptengines.com, toybox, thinkybooks, etc. — these are education/product pages, not competitive)
- No GitHub link pointing to PromptEngines org
- No pricing, "Book a Scoping Call," or commercial GTM language
- IBM title is accurate: Band 10 PM / Program Director (NOT executive band)
- Tone is educator/practitioner, NOT vendor/founder
- adilislam.com email ≠ Pantheon domain email
- adilislam.com social accounts ≠ Pantheon social accounts

---

## Design System

**Main site** (`/assets/styles.css`):
- Dark theme: `#09090b` bg, `#131316` elevated, `#e8e6e1` text
- Accent: `#e05a30` (warm orange-red)
- Fonts: Fraunces (display/serif), Inter (body), JetBrains Mono (metadata)
- 1px border dividers, no shadows, no gradients, no rounded bubbles
- Eyebrow labels: mono uppercase with accent line prefix
- Grain texture overlay via SVG filter

**Resume** (`/resume/index.html`, self-contained):
- 6 themes: **Editorial** (default, matches main site), Executive, Cyberpunk, Minimal, Terminal, Gradient
- Editorial theme uses identical palette + Fraunces/Inter/JetBrains Mono
- Has sticky site nav topbar linking back to adilislam.com pages
- Formspree contact form at bottom
- Grain texture in Editorial, scan lines in Cyberpunk, CRT overlay in Terminal

**Voice** (from copywriting-voice skill):
- Declarative headlines. No "I believe," no "I write about."
- No emojis as UI elements
- No negation patterns ("No hype." → just "Daily intelligence.")
- No LinkedIn-template phrases
- Credentials stated plainly: "Harvard. Dartmouth. Amherst." — never "3× Ivy League"

---

## Tech Notes

- All pages use `../assets/styles.css` with relative paths (works for `file:///` local viewing)
- Resume is self-contained HTML with inline CSS + JS (~80KB)
- No build step, no framework, no CI. Just HTML + CSS. Push to main = deploy.
- Formspree endpoint in resume: `https://formspree.io/f/mwvnodar`
- Beehiiv email signup blocks are placeholders across all section pages

---

## Git Log

```
9f22957 Resume: add Editorial theme, site nav, scrub PromptEngines refs
b1c33ff Redesign: add Kids section, upgrade homepage, nav/footer on all pages
3ad61d7 Remove all negation patterns from copy
aee6166 About page: new copy from Principal. Resume placeholder at /resume/.
c255581 Fix CSS path resolution for local file:// viewing
b70e848 Complete rewrite: editorial voice, PE-matched taste, zero emojis
89958eb Remove Ivy League branding, replace with Graduate Degrees
```

**Remote not set yet.** Waiting for `aikaizen/adilislam.com` repo creation on GitHub.