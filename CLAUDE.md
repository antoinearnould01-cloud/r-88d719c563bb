# Repository rules

Personal research portfolio of Antoine Arnould. Static site served by GitHub Pages from
`main` (root), with `.nojekyll`. Site language: English. Tone: sober, factual, academic.

## Permanent rules

- No framework, no `npm`, no build step, no CDN, no analytics, no cookies.
- Every resource is served from this repository; every library is copied and frozen in
  `assets/vendor/`. Fonts are system fonts only.
- All public content must be non-confidential: no unpublished data, no names of third
  parties without Antoine's agreement.
- No phone number, no postal address. Contact e-mail: `aarnould@ethz.ch`.
- Every page carries `<meta name="robots" content="noindex">`; `robots.txt` disallows everything.
- Adding a project = one folder in `projects/` + one entry in `assets/projects.js`, nothing else.
- Project pages contain only what is in the project's own sources (report, repository).
  Invent nothing.
- Commits are authored by Antoine Arnould with the address
  `340576116+antoinearnould01-cloud@users.noreply.github.com`, without any attribution
  line to an assistant; no mention of an assistant anywhere in the site or the repository.

## Adding a project

1. `python tools/new_project.py <slug> "<Title>"` (or copy `projects/_template/` by hand and
   add the entry to `assets/projects.js`).
2. Fill `projects/<slug>/index.html`. Section order is fixed: Summary, Question, Model and
   method, Results (3 to 6 figures with captions), Interactive (optional), My contribution,
   Limits and open questions, Code and documents, Skills. Delete empty sections.
3. Figures go in `projects/<slug>/img/`: PNG or WebP, at most 1600 px wide, under 300 kB if
   possible, with `alt` text, `loading="lazy"`, and a link to the full image.
4. Complete the entry in `assets/projects.js`; the largest `order` is listed first;
   `hidden: true` keeps a project off the home page.
5. Check locally with `python -m http.server`, then push.

## Conventions

- Equations: LaTeX between `$...$` and `$$...$$`, rendered by `assets/vendor/katex/`
  (version 0.16.11, do not update). In HTML write `&lt;`, `&gt;`, `&amp;` inside equations.
- Colours and fonts are CSS variables at the top of `assets/site.css`; light and dark themes
  follow `prefers-color-scheme`.
- Project pages use relative paths (`../../assets/...`) so the site also opens from disk.
- Widgets are plain JavaScript files in `assets/widgets/`, one per file. A widget that shows a
  textbook model must say so and stay distinct from project results.

## Before pushing

- Pages render at 375, 768 and 1280 px, in light and dark themes.
- No request to another domain when a page loads.
- All internal links are relative and work; external links have been tested.
