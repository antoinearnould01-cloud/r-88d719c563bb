#!/usr/bin/env python3
"""Create (or remove) a project page from the template.

    python tools/new_project.py <slug> "<Title>"     create projects/<slug>/ and its list entry
    python tools/new_project.py --remove <slug>      delete projects/<slug>/ and its list entry

Standard library only. The new entry is added to assets/projects.js with
"hidden: true"; set it to false once the page is ready.
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR = ROOT / "projects"
TEMPLATE_DIR = PROJECTS_DIR / "_template"
LIST_FILE = ROOT / "assets" / "projects.js"

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LIST_END_RE = re.compile(r"^\];[ \t]*$", re.MULTILINE)


def entry_re(slug):
    """Match one entry of the list (entries contain no nested braces)."""
    return re.compile(r"[ \t]*\{[^{}]*\bslug:\s*\"" + re.escape(slug) + r"\"[^{}]*\},?[ \t]*\n")


def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def create(slug, title):
    target = PROJECTS_DIR / slug
    if target.exists():
        sys.exit(f"error: {target.relative_to(ROOT)} already exists")
    listing = LIST_FILE.read_text(encoding="utf-8")
    if entry_re(slug).search(listing):
        sys.exit(f"error: assets/projects.js already has an entry for '{slug}'")
    end = LIST_END_RE.search(listing)
    if not end:
        sys.exit("error: could not find the closing '];' line in assets/projects.js")

    shutil.copytree(TEMPLATE_DIR, target)
    (target / "img").mkdir(exist_ok=True)
    page = target / "index.html"
    page.write_text(
        page.read_text(encoding="utf-8").replace("{{TITLE}}", html_escape(title)),
        encoding="utf-8",
        newline="\n",
    )

    orders = [int(n) for n in re.findall(r"\border:\s*(\d+)", listing)]
    entry = (
        "  {\n"
        f"    slug: {json.dumps(slug)},\n"
        f"    title: {json.dumps(title, ensure_ascii=False)},\n"
        '    summary: "One-line summary.",\n'
        '    where: "Place", when: "Period", kind: "Research project",\n'
        '    tags: ["Keyword"],\n'
        f'    image: "projects/{slug}/img/cover.png",\n'
        f"    order: {max(orders, default=0) + 1}, hidden: true\n"
        "  },\n"
    )
    listing = listing[: end.start()] + entry + listing[end.start():]
    LIST_FILE.write_text(listing, encoding="utf-8", newline="\n")

    print(f"created projects/{slug}/index.html")
    print("added a hidden entry to assets/projects.js")
    print("next: fill the page, add figures to img/, complete the entry, set hidden: false")


def remove(slug):
    target = PROJECTS_DIR / slug
    listing = LIST_FILE.read_text(encoding="utf-8")
    new_listing, count = entry_re(slug).subn("", listing, count=1)
    if not target.exists() and count == 0:
        sys.exit(f"error: no project named '{slug}'")
    if target.exists():
        shutil.rmtree(target)
        print(f"deleted projects/{slug}/")
    if count:
        LIST_FILE.write_text(new_listing, encoding="utf-8", newline="\n")
        print("removed its entry from assets/projects.js")


def main():
    parser = argparse.ArgumentParser(description="Create or remove a project page.")
    parser.add_argument("--remove", action="store_true", help="remove the project instead of creating it")
    parser.add_argument("slug", help="folder name: lowercase letters, digits and hyphens")
    parser.add_argument("title", nargs="?", help="project title (required when creating)")
    args = parser.parse_args()

    if not SLUG_RE.match(args.slug):
        sys.exit("error: the slug must use lowercase letters, digits and hyphens only")
    if args.remove:
        remove(args.slug)
    else:
        if not args.title:
            sys.exit("error: a title is required")
        create(args.slug, args.title)


if __name__ == "__main__":
    main()
