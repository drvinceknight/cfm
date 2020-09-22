import pathlib

import jinja2
import markdown
from invoke import task

ROOT = "cfm"
TITLE = "Computing for mathematics"
DESCRIPTION = "An undergraduate course introducing programming, through Python, to mathematicians."
KEYWORDS = "python, mathematics, jupyter, mathematics"
AUTHOR = "Vince Knight"
SOURCE_FILE_PATH = pathlib.Path("main.md")


def render_template(template_file, template_vars, searchpath="./templates/"):
    """
    Render a jinja2 template
    """
    templateLoader = jinja2.FileSystemLoader(searchpath=searchpath)
    template_env = jinja2.Environment(loader=templateLoader)
    template = template_env.get_template(template_file)
    return template.render(template_vars)


@task
def build(
    c,
    source_file_path=SOURCE_FILE_PATH,
    root=ROOT,
    title=TITLE,
    description=DESCRIPTION,
    keywords=KEYWORDS,
    author=AUTHOR,
):
    """
    Build the single page site.
    """
    md_string = source_file_path.read_text()
    content = markdown.markdown(md_string)
    html = render_template(
        "home.html",
        {
            "content": content,
            "root": ROOT,
            "title": TITLE,
            "description": DESCRIPTION,
            "keywords": KEYWORDS,
            "author": AUTHOR,
        },
    )
    with open("index.html", "w") as f:
        f.write(html)

@task
def test(c):
    """
    Test all notebooks

    The purpose of this is to mainly test that the assessment is correct.
    """
    c.run("pytest --nbval --current-env")
