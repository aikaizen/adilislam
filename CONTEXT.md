# adilislam.com — Project Context

**Last updated:** 2026-05-15  
**Repo:** `aikaizen/adilislam` → https://github.com/aikaizen/adilislam  
**Local path:** `/project/adilislam/`  
**Deploy:** GitHub Pages (branch: main, root `/`)  
**Custom domain:** `adilislam.com` (GoDaddy DNS)

---

## Active TODO

### Blocking — needs Principal

- [x] Create GitHub repo `aikaizen/adilislam` — DONE
- [ ] **Enable GitHub Pages** → Settings → Pages → Branch: main, / (root)
- [ ] **Point GoDaddy DNS** for adilislam.com:
  - 4× A records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
  - CNAME `www` → `aikaizen.github.io`
  - In GitHub Pages settings → Custom domain → `adilislam.com` → Enforce HTTPS
- [ ] **Set up Beehiiv** account for email signup (currently placeholder on all signup blocks)
- [ ] **Review About page copy** — career details are sparse, education has no degree details yet
- [ ] **Decide:** kids project links currently point to their live product URLs on promptengines.com subdomains. Phase 2 is to create xyz.adilislam.com subdomains and re-point. For now, URLs work.

### Ready to do

- [ ] Populate archive index pages (bulletins, issues, writing) with static HTML file listings — currently have placeholder `<div>` containers
- [ ] Audit internal links in migrated content for broken references from old structure

### Content gaps

- [ ] `/contact/` — currently just email + 3 section cards. Could use a real contact form
- [ ] Resume editorial theme — browser test all 6 themes
- [ ] Footer on resume — minimal `© 2026 Adil Islam`, no site nav (by design)

### Future / nice-to-have

- [ ] Favicon / apple-touch-icon for main site
- [ ] Open Graph images per page
- [ ] Sitemap.xml + robots.txt
- [ ] Analytics (Plausible, Fathom, or similar)
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
/resume/ .................. Interactive resume (6 themes)
/contact/ ................. Email + section cards
/assets/styles.css ......... Main site design system
```

**157 total HTML files**

---

## Separation Rules (non-negotiable)

Every page on adilislam.com must pass this checklist:

- No mention of any other company or product brand name
- No vendor/founder language — educator/practitioner tone only
- No pricing, booking, or commercial language
- IBM title is accurate: Band 10 PM / Program Director (NOT executive band)
- Kids project links go to those products' own URLs — not agency or consulting pages
- This site's email and social accounts are separate from any other entity

---

## Design System

**Main site** (`/assets/styles.css`):
- Dark theme: `#09090b` bg, `#131316` elevated, `#e8e6e1` text
- Accent: `#e05a30`
- Fonts: Fraunces (display/serif), Inter (body), JetBrains Mono (metadata)
- 1px border dividers, no shadows, no gradients, no rounded bubbles
- Eyebrow labels: mono uppercase with accent line prefix
- Grain texture overlay via SVG filter

**Resume** (`/resume/index.html`, self-contained):
- 6 themes: Editorial (default), Executive, Cyberpunk, Minimal, Terminal, Gradient
- Editorial matches main site palette + Fraunces/Inter/JetBrains Mono
- Sticky site nav links back to adilislam.com pages

**Voice** (from copywriting-voice skill):
- Declarative headlines. No "I believe," no "I write about."
- No emojis as UI elements
- No negation patterns ("No hype." → "Daily intelligence.")
- No LinkedIn-template phrases
- Credentials stated plainly: "Harvard. Dartmouth. Amherst."

---

## Tech Notes

- All pages use `../assets/styles.css` with relative paths (works for local file:// viewing)
- Resume is self-contained HTML with inline CSS + JS (~80KB)
- No build step, no framework, no CI. Push to main = deploy.
- CNAME file present for `adilislam.com` custom domain
- Formspree endpoint in resume: `https://formspree.io/f/mwvnodar`
- Beehiiv signup blocks are placeholders

---

## Git Log

```
d1f9657 Add CNAME for adilislam.com custom domain
47bd65d Add CONTEXT.md and README.md
9f22957 Resume: add Editorial theme, site nav, scrub brand refs
b1c33ff Redesign: add Kids section, upgrade homepage, nav/footer on all pages
3ad61d7 Remove all negation patterns from copy
aee6166 About page: new copy. Resume placeholder at /resume/.
c255581 Fix CSS path resolution for local file:// viewing
b70e848 Complete rewrite: editorial voice, taste-matched design
89958eb Replace Ivy League branding with Graduate Degrees
```