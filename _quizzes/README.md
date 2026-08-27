# Quizzes

Each `*.yml` file here is a short multiple-choice quiz, named by the topic
tag (e.g. `algebra.yml` attaches to the topic whose frontmatter has
`tag: algebra`). `build.py` reads each file, validates that exactly one
option is marked correct in every question, and embeds the quiz as JSON in
the matching topic page. `assets/js/quiz.js` runs the quiz in the browser
and reshuffles questions and options on every attempt.

## Format

```yaml
title: Algebra
pick: 5            # optional: show 5 random questions from the pool
questions:
  - q: "Question text (LaTeX with \\( ... \\) is supported)."
    options:
      - text: "the correct option"
        correct: true
      - text: "a distractor"
      - text: "another distractor"
      - text: "a fourth distractor"
    explain: "Optional feedback shown after answering."
```

Rules:

- Each question must have exactly one option with `correct: true`; the
  build fails otherwise.
- Maths uses MathJax delimiters `\\( ... \\)` and `\\[ ... \\]`, re-typeset
  after each question is rendered.
- `pick` and `explain` are optional. Omit `pick` to show the whole pool.
