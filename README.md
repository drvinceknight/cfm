# Computing for Mathematics

A course for undergraduate mathematics students covering:

- The use of Python to solve mathematical problems: the main text used is
  <https://vknight.org/pfm/cover.html>
- The use of LaTeX to communicate mathematics.
- Presentation.

The site is published at <https://vknight.org/cfm/>.

## Source layout

All content lives in collection directories at the repository root:

| Directory       | Output path                          |
| --------------- | ------------------------------------ |
| `_topics/`      | `topics/{slug}.html`                 |
| `_assessment/`  | `assessment/index.html`              |
| `_class-notes/` | `class-notes/{slug}.html`            |
| `_posts/`       | `posts/{slug}.html`                  |
| `_faqs/`        | rendered inside the home page        |
| `_data/`        | `toc.yml`, `projects.yml`            |

Templates are in `templates/`, CSS in `assets/css/style.css`, and the
static build script is `build.py`.

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then:

```bash
uv sync --group dev
```

## Build

```bash
uv run python build.py
```

Outputs are written in-place: `index.html`, `topics/*.html`,
`class-notes/*.html`, `posts/*.html`, `assessment/index.html`.

Preview with:

```bash
python -m http.server 8000
# then open http://localhost:8000/cfm/
```

(The site lives under the `/cfm/` base URL when published, so a quick
local preview is easier if you symlink the repo at `./cfm`.)

## Deploy

The built HTML is committed to the repository. The
`.github/workflows/deploy.yml` workflow uploads the repo to GitHub Pages
on every push to `main`. Run `uv run python build.py` before committing.
