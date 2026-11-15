# Research portfolio

Static site (plain HTML, CSS and JavaScript, no build step), published with GitHub Pages
from the `main` branch at <https://antoinearnould01-cloud.github.io/r-88d719c563bb/>.
The address is not listed anywhere: share it by link only.

## Add a project

1. `python tools/new_project.py <slug> "<Title>"` creates `projects/<slug>/` from the template and adds a hidden entry to `assets/projects.js`.
2. Fill the sections of `projects/<slug>/index.html` and put the figures in `projects/<slug>/img/` (PNG or WebP, at most 1600 px wide, under 300 kB).
3. Complete the entry in `assets/projects.js` (summary, place, period, type, tags, cover image) and set `hidden: false`; the largest `order` is shown first.
4. Check locally: `python -m http.server`, then open <http://localhost:8000>.
5. `git push`. GitHub Pages publishes in about a minute.

To remove a project: `python tools/new_project.py --remove <slug>`.

## Layout

```
index.html                 home page
projects/<slug>/           one folder per project (index.html + img/)
projects/_template/        template of a project page
assets/site.css            all styles
assets/site.js             project cards, equation rendering
assets/projects.js         list of projects shown on the home page
assets/widgets/            interactive simulations, one file each
assets/vendor/katex/       frozen copy of KaTeX 0.16.11
files/                     CV (PDF)
tools/new_project.py       create or remove a project
```

Equations are written in LaTeX between `$...$` or `$$...$$` and rendered by the local copy
of KaTeX. Nothing is loaded from another domain. The site is not indexed by search engines
(`noindex` on every page, `robots.txt`).
