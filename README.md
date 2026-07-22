# Python — A Practical Guide

A single-page, self-contained Python reference guide (basics → data structures → OOP → advanced topics), with practice questions after every chapter.

## Files

- `output.html` — the final page. Open it directly in a browser, or serve it from GitHub Pages.
- `generate.py` — the source of truth. All chapter content lives in a `CHAPTERS` list here.

## Making changes

Don't hand-edit `output.html` — edit `generate.py` instead and regenerate:

```bash
python3 generate.py
```

Each chapter is defined with a small `chapter(...)` call, e.g.:

```python
chapter("for-loop", "08", "For Loop", "Control Flow", [
    p("A for loop walks through any iterable..."),
    code("""
for i in range(5):
    print(i)
"""),
], [
    q(1, "Print all even numbers from 1 to 20 using a for loop.", "1 to 20", "2 4 6 ... 20"),
])
```

- `p(...)` — a paragraph
- `h3(...)` — a subheading
- `code(...)` — a syntax-highlighted code block
- `ul([...])` — a bullet list
- `table(headers, rows)` — a reference table
- `note("info"|"warn", title, text)` — a callout box
- `q(num, text, input, output)` — a practice question (input/output are optional)

To add a new chapter, add a new `chapter(...)` call anywhere in the list — order in the list controls order on the page and in the sidebar nav. Chapters with the same 4th argument (group name) get grouped under one sidebar label.

## Publishing

```bash
git init
git add .
git commit -m "Initial Python guide"
git remote add origin <your-repo-url>
git push -u origin main
```

If you want it live on the web for free, enable GitHub Pages on the repo. The site now generates an `index.html` homepage automatically, so GitHub Pages will serve it correctly.
