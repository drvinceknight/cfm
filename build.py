#!/usr/bin/env python3
"""Build script for the Computing for Mathematics course site.

Reads Jekyll-style sources from ``_topics/``, ``_assessment/``,
``_class-notes/``, ``_posts/``, ``_faqs/``, ``_data/``, and renders Jinja2
templates to the repo root.  The built HTML is committed to the repo and
deployed via GitHub Pages.

URLs in the rendered output are relative to each page's depth, so the same
output works both at the repo root (``python -m http.server``) and under
the ``/cfm/`` subpath used in production.

Usage::

    uv run python build.py
"""

from __future__ import annotations

import datetime
import json
import pathlib
import re
import shutil
import subprocess
from typing import Any

import frontmatter
import jinja2
import markdown as md_module
import yaml
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

SITE_TITLE = "Computing for Mathematics"
ROOT = pathlib.Path(__file__).parent

# Source content uses ``{{ site.baseurl }}`` as a path prefix.  At source
# load time we rewrite it to this placeholder; per-page rendering then
# substitutes the relative baseurl for the page being rendered.
BASEURL_PLACEHOLDER = "__BASEURL__"

Item = dict[str, Any]


def slugify(text: str) -> str:
    """Match Jekyll's default ``slugify`` filter."""
    value = str(text).lower().strip()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"[\s_]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def render_markdown(text: str) -> str:
    return md_module.markdown(
        text,
        extensions=[
            "extra",
            "tables",
            "fenced_code",
            "toc",
            "pymdownx.arithmatex",
            "pymdownx.magiclink",
        ],
        extension_configs={"pymdownx.arithmatex": {"generic": True}},
    )


_BASEURL_RE = re.compile(r"\{\{\s*site\.baseurl\s*\}\}")


def resolve_liquid_refs(text: str) -> str:
    """Replace Liquid ``{{ site.baseurl }}`` with our internal placeholder.

    Tolerant of arbitrary whitespace (including newlines) between the
    braces, so a markdown source line that wraps inside the URL still
    substitutes correctly.
    """
    return _BASEURL_RE.sub(BASEURL_PLACEHOLDER, text)


def _excerpt(content_html: str) -> str:
    match = re.search(r"<p>(.*?)</p>", content_html, re.DOTALL)
    return f"<p>{match.group(1)}</p>" if match else ""


def load_item(path: pathlib.Path) -> Item:
    raw = frontmatter.load(path)
    data: Item = dict(raw.metadata)
    data["slug"] = path.stem
    content = resolve_liquid_refs(raw.content)
    data["content_html"] = render_markdown(content)
    data["excerpt"] = _excerpt(data["content_html"])
    return data


def load_collection(path: pathlib.Path) -> list[Item]:
    if not path.exists():
        return []
    return [load_item(p) for p in sorted(path.glob("*.md"))]


_POST_FILENAME = re.compile(r"(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")


def load_posts(path: pathlib.Path) -> list[Item]:
    if not path.exists():
        return []
    posts: list[Item] = []
    for filepath in sorted(path.glob("*.md")):
        match = _POST_FILENAME.match(filepath.name)
        if not match:
            continue
        year, month, day, _ = match.groups()
        raw = frontmatter.load(filepath)
        data: Item = dict(raw.metadata)
        data["slug"] = filepath.stem
        data["date_obj"] = datetime.date(int(year), int(month), int(day))
        data["date_str"] = data["date_obj"].isoformat()
        content = resolve_liquid_refs(raw.content)
        data["content_html"] = render_markdown(content)
        data["excerpt"] = _excerpt(data["content_html"])
        posts.append(data)
    return sorted(posts, key=lambda p: p["date_obj"], reverse=True)


def _video_url_html(line: str) -> str:
    rendered = render_markdown(line)
    return re.sub(r"^<p>|</p>$", "", rendered.strip())


def _attach_video_html(topics: list[Item]) -> None:
    for topic in topics:
        urls = topic.get("video_urls") or []
        topic["video_urls_html"] = [_video_url_html(u) for u in urls]


def load_toc(path: pathlib.Path) -> list[Any]:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def load_quizzes(path: pathlib.Path) -> dict[str, Item]:
    """Read quiz YAML files, keyed by filename stem (the topic tag).

    Each YAML file must have a list of ``questions``, and each question must
    have exactly one option marked ``correct: true``.
    """
    quizzes: dict[str, Item] = {}
    if not path.exists():
        return quizzes
    for filepath in sorted(path.glob("*.yml")):
        quiz = yaml.safe_load(filepath.read_text())
        for question in quiz.get("questions", []):
            n_correct = sum(
                1 for option in question.get("options", []) if option.get("correct")
            )
            if n_correct != 1:
                raise ValueError(
                    f"{filepath.name}: question "
                    f"'{question.get('q', '?')[:50]}' has {n_correct} correct "
                    f"options (exactly one required)"
                )
        quizzes[filepath.stem] = quiz
    return quizzes


_NOTE_LABELS = (
    ("vknight.org/pfm", "Python for mathematics"),
    ("vknight.org/tex", "Mathematical writing notes"),
    ("vknight.org/pop", "Principles of presentations"),
    ("github.com/drvinceknight/pom", "Project organisation notes"),
)


def note_label(url: str, page_title: str = "") -> str:
    """Return readable link text for a notes URL instead of the raw URL."""
    for needle, label in _NOTE_LABELS:
        if needle in url:
            return f"{label}: {page_title}" if page_title else label
    return url


def make_env() -> jinja2.Environment:
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(ROOT / "templates"),
        autoescape=False,
    )
    env.filters["slugify"] = slugify
    env.filters["note_label"] = note_label
    env.filters["quiz_json"] = lambda value: json.dumps(value)
    env.globals["site_title"] = SITE_TITLE
    return env


def _has_tag(item: Item, tag: str) -> bool:
    tags = item.get("tags")
    if tags is None:
        return False
    if isinstance(tags, str):
        return tags == tag
    return tag in tags


def _related_posts(tag: str, posts: list[Item]) -> list[Item]:
    if not tag:
        return []
    return [p for p in posts if _has_tag(p, tag)]


def _related_class_notes(tag: str, class_notes: list[Item]) -> list[Item]:
    if not tag:
        return []
    return [n for n in class_notes if _has_tag(n, tag)]


def _baseurl_for(output_path: pathlib.Path) -> str:
    """Compute the relative ``baseurl`` for a page at ``output_path``.

    The output is the path of the rendered HTML relative to ``ROOT``; we
    return a string like ``..`` or ``../..`` such that
    ``{baseurl}/assets/css/style.css`` resolves correctly from that page.
    """
    relative = output_path.relative_to(ROOT)
    depth = len(relative.parts) - 1
    if depth <= 0:
        return "."
    return "/".join([".."] * depth)


def _render(env: jinja2.Environment, template_name: str, output_path: pathlib.Path, **context: Any) -> None:
    baseurl = _baseurl_for(output_path)
    html = env.get_template(template_name).render(baseurl=baseurl, **context)
    html = html.replace(BASEURL_PLACEHOLDER, baseurl)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")


_PYGMENTS_FORMATTER = HtmlFormatter(nowrap=True)


def render_code(body: str, language: str) -> str:
    """Return the body highlighted by Pygments as inner HTML."""
    try:
        lexer = get_lexer_by_name(language)
    except ClassNotFound:
        lexer = get_lexer_by_name("text")
    return highlight(body, lexer, _PYGMENTS_FORMATTER)


_EXAMPLE_DESCRIPTIONS = {
    "binomial": "The probability mass function, cumulative distribution "
                "function, mean, variance, and a simulator for the binomial "
                "distribution.",
    "continued_fractions": "The continued fraction expansion of a rational "
                           "number and the resulting list of convergents.",
    "dice": "Simulated and exact distributions for the sum of fair dice.",
    "markov": "Finite discrete-time Markov chains: the distribution after "
              "$n$ steps and the stationary distribution.",
    "newton": "The Newton-Raphson method for finding roots of "
              "single-variable expressions, with symbolic differentiation.",
    "ode_flow": "Solving and sampling first-order initial value problems "
                "for ordinary differential equations.",
    "quadratic": "Real quadratic equations: the discriminant, the set of "
                 "real roots, the number of real roots, and the vertex of "
                 "the parabola.",
    "stats_from_scratch": "The mean, the median, the population and sample "
                          "standard deviations, and the three quartiles, "
                          "implemented directly from their definitions.",
}


def discover_example_projects(examples_dir: pathlib.Path) -> list[Item]:
    """Find each ``assets/examples/<name>/`` directory and list its files."""
    if not examples_dir.exists():
        return []
    projects: list[Item] = []
    for project_dir in sorted(examples_dir.iterdir()):
        if not project_dir.is_dir():
            continue
        slug = project_dir.name
        library_path = project_dir / f"{slug}.py"
        test_path = project_dir / f"test_{slug}.py"
        readme_path = project_dir / "README.md"
        files: list[Item] = []
        if library_path.exists():
            files.append({
                "path": f"{slug}.py",
                "label": f"{slug}.py",
                "language": "python",
                "body": render_code(library_path.read_text(), "python"),
            })
        if test_path.exists():
            files.append({
                "path": f"test_{slug}.py",
                "label": f"test_{slug}.py",
                "language": "python",
                "body": render_code(test_path.read_text(), "python"),
            })
        if readme_path.exists():
            files.append({
                "path": "README.md",
                "label": "README.md",
                "language": "markdown",
                "body": render_code(readme_path.read_text(), "markdown"),
            })
        paper_main = project_dir / "paper" / "main.tex"
        paper_bib = project_dir / "paper" / "references.bib"
        if paper_main.exists():
            files.append({
                "path": "paper-main.tex",
                "label": "paper/main.tex",
                "language": "latex",
                "body": render_code(paper_main.read_text(), "latex"),
            })
        if paper_bib.exists():
            files.append({
                "path": "paper-references.bib",
                "label": "paper/references.bib",
                "language": "bibtex",
                "body": render_code(paper_bib.read_text(), "bibtex"),
            })
        paper_pdf = project_dir / "paper" / "main.pdf"
        projects.append({
            "slug": slug,
            "title": slug,
            "description": _EXAMPLE_DESCRIPTIONS.get(slug, ""),
            "files": files,
            "paper_pdf": (
                f"assets/examples/{slug}/paper/main.pdf"
                if paper_pdf.exists() else None
            ),
        })
    return projects


def build_pdfs() -> None:
    """Compile each ``tex/{minutes,agendas}/*.tex`` and copy the PDF into ``assets/``.

    The build is skipped silently when ``pdflatex`` is not on PATH so that
    contributors without a TeX installation can still run the HTML build.
    Committed PDFs in ``assets/`` continue to be served in that case.
    """
    if not shutil.which("pdflatex"):
        print("pdflatex not found; skipping PDF builds.")
        return

    def _pdf_is_up_to_date(pdf: pathlib.Path, sources: list[pathlib.Path]) -> bool:
        if not pdf.exists():
            return False
        pdf_mtime = pdf.stat().st_mtime
        return all(s.stat().st_mtime <= pdf_mtime for s in sources if s.exists())

    for sub in ("minutes", "agendas"):
        src_dir = ROOT / "tex" / sub
        if not src_dir.exists():
            continue
        out_dir = ROOT / "assets" / sub
        out_dir.mkdir(parents=True, exist_ok=True)
        sources = sorted(p for p in src_dir.glob("*.tex") if not p.name.startswith("_"))
        for source in sources:
            pdf = source.with_suffix(".pdf")
            output_pdf = out_dir / pdf.name
            if _pdf_is_up_to_date(output_pdf, [source]) and _pdf_is_up_to_date(pdf, [source]):
                continue
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", source.name],
                cwd=src_dir,
                capture_output=True,
                text=True,
                check=False,
            )
            if not pdf.exists():
                print(f"pdflatex failed for {source}:\n{result.stdout[-1000:]}")
                continue
            shutil.copy(pdf, output_pdf)
        for ext in (".aux", ".log", ".out"):
            for stale in src_dir.glob(f"*{ext}"):
                stale.unlink()

    examples_dir = ROOT / "assets" / "examples"
    if examples_dir.exists():
        for paper_dir in sorted(examples_dir.glob("*/paper")):
            source = paper_dir / "main.tex"
            if not source.exists():
                continue
            paper_sources = [source, *paper_dir.glob("*.bib")]
            if _pdf_is_up_to_date(paper_dir / "main.pdf", paper_sources):
                continue
            subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "main.tex"],
                cwd=paper_dir, capture_output=True, text=True, check=False,
            )
            if (paper_dir / "references.bib").exists():
                subprocess.run(
                    ["bibtex", "main"],
                    cwd=paper_dir, capture_output=True, text=True, check=False,
                )
                subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode", "main.tex"],
                    cwd=paper_dir, capture_output=True, text=True, check=False,
                )
            subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "main.tex"],
                cwd=paper_dir, capture_output=True, text=True, check=False,
            )
            for ext in (".aux", ".log", ".out", ".bbl", ".blg"):
                for stale in paper_dir.glob(f"*{ext}"):
                    stale.unlink()


def build() -> None:
    env = make_env()

    topics = load_collection(ROOT / "_topics")
    _attach_video_html(topics)
    class_notes = load_collection(ROOT / "_class-notes")
    assessment_items = load_collection(ROOT / "_assessment")
    faqs = load_collection(ROOT / "_faqs")
    posts = load_posts(ROOT / "_posts")
    toc = load_toc(ROOT / "_data" / "toc.yml")
    projects = load_toc(ROOT / "_data" / "projects.yml")
    quizzes_by_tag = load_quizzes(ROOT / "_quizzes")

    _render(env, "home.html", ROOT / "index.html", toc=toc, faqs=faqs, posts=posts)

    start_here_path = ROOT / "_start-here" / "index.md"
    if start_here_path.exists():
        _render(
            env,
            "page.html",
            ROOT / "start-here" / "index.html",
            page=load_item(start_here_path),
        )

    for topic in topics:
        tag = topic.get("tag") or ""
        _render(
            env,
            "topic.html",
            ROOT / "topics" / f"{topic['slug']}.html",
            topic=topic,
            related_posts=_related_posts(tag, posts),
            related_class_notes=_related_class_notes(tag, class_notes),
            quiz=quizzes_by_tag.get(tag),
        )

    individual_notes = [n for n in class_notes if n["slug"] != "index"]
    for note in individual_notes:
        _render(env, "class-notes.html", ROOT / "class-notes" / f"{note['slug']}.html", note=note)
    _render(
        env,
        "class-notes-index.html",
        ROOT / "class-notes" / "index.html",
        notes=sorted(individual_notes, key=lambda n: n.get("title", "")),
    )

    for post in posts:
        _render(env, "post.html", ROOT / "posts" / f"{post['slug']}.html", post=post)

    assessment_doc = next(
        (item for item in assessment_items if item.get("slug") == "index"),
        {"content_html": ""},
    )
    assessment_tag = assessment_doc.get("tag") or "assessment"
    _render(
        env,
        "assessment.html",
        ROOT / "assessment" / "index.html",
        assessment=assessment_doc,
        projects=projects,
        related_posts=[p for p in posts if _has_tag(p, assessment_tag)],
    )

    geometric_mean_doc = next(
        (item for item in assessment_items if item.get("slug") == "geometric-mean"),
        None,
    )
    if geometric_mean_doc:
        _render(
            env,
            "page.html",
            ROOT / "assessment" / "geometric-mean" / "index.html",
            page=geometric_mean_doc,
        )

    example_projects_doc = next(
        (item for item in assessment_items if item.get("slug") == "example-projects"),
        None,
    )
    if example_projects_doc:
        examples = discover_example_projects(ROOT / "assets" / "examples")
        example_projects_doc["examples"] = examples
        _render(
            env,
            "example-projects.html",
            ROOT / "assessment" / "example-projects" / "index.html",
            page=example_projects_doc,
        )
        for example in examples:
            for file_entry in example["files"]:
                _render(
                    env,
                    "code-file.html",
                    ROOT / "assessment" / "example-projects" / example["slug"]
                    / file_entry["path"] / "index.html",
                    page={
                        "title": file_entry["label"],
                        "project": example["slug"],
                        "language": file_entry["language"],
                        "body": file_entry["body"],
                    },
                )


if __name__ == "__main__":
    build()
    build_pdfs()
