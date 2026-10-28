---
layout: class-notes
title: "LaTeX and Writing Mathematics"
tags: writing
---

## Format

A group-work week. The single hour is **not** a lecture on LaTeX:
students work through the LaTeX notes themselves. This week is one of
the two exceptions to the question-and-signpost format, because the hour
is given over to the **mathematics subject librarian**, who runs a
session on researching sources.

## In class session

The librarian runs the hour on finding and evaluating sources for the
paper. Introduce them, then hand over.

Before you do, spend two minutes connecting the session to the mark,
because students who think of the librarian slot as optional will not
engage with it. The **Research** criterion is 20% of the group project
and is assessed on two things: whether the paper describes how the
software compares to other commonly used packages, and whether the
references are complete, appropriately cited and properly formatted.
That is precisely what the session is about. Point at the
[Research criteria]({{ site.baseurl }}/assessment/#research-20) on
screen before handing over.

Stay for the hour and take any questions at the end. Questions about
LaTeX itself belong here too, since this is the week students start
writing.

## The deck

There is a write-on deck at
[/deck/latex-and-writing-mathematics/main.pdf]({{ site.baseurl }}/deck/latex-and-writing-mathematics/main.pdf).
It is deliberately not an hour of material, because the hour is not
ours. It comes in two halves.

Slides 2 to 4 are the two minutes before you hand over. Slide 4 is the
one worth doing properly: each group names three tools that already do
something like what their library will do, and says what theirs does
differently. That is the state of the field in the only form a student
can act on, and there is a workspace for the answer.

Slides 5 to 10 are for the questions at the end, and for students to
work through afterwards. Three are LaTeX, two are modularisation. When
the room goes quiet, put one up rather than asking again whether anyone
has a question. Answers are at the end of these notes.

## What students work through on their own

- [LaTeX notes](https://vknight.org/tex/): the tutorials covering the
  document structure, mathematics, figures, tables and bibliographies.
- ['Some Guidelines for Good Mathematical Writing' by Francis Su]({{ site.baseurl }}/assets/pdf/writing-mathematics-guidelines/main.pdf)
- ['A guide to writing mathematics' by Kevin Lee]({{ site.baseurl }}/assets/pdf/a-guide-to-writing-mathematics/main.pdf)

They also need `references.bib`, which is one of the eight submitted
files. The librarian session is where the content of that file comes
from, so the two halves of this week fit together: the notes teach the
mechanics of citing, the session is about what is worth citing.

## This week's Python

The Python chapter this week is modularisation, and slides 9 and 10
cover the two things that catch people.

**Slide 9, name this function without using 'and'.** You cannot, which
is the answer. `add_tip_and_get_bill_share` is two functions:
`add_tip`, which returns a total with the tip included, and
`get_bill_share`, which divides a total by the number of payers. The
rule to give them is that a function should be small enough to test on
its own and nameable without the word 'and'. Resist giving a line
count. The chapter they read is explicit that arbitrary line limits
often add more complexity than they remove.

**Slide 10, why did importing it draw a plot?** Because importing a
file runs everything at its top level, and this one calls `get_tour`
and `plot_tour` there. The library holds functions; the code that uses
them belongs in another file, or under `if __name__ == "__main__":`.
This is also the week to say that the submission is a single
`<library>.py`, so modular means the functions inside one file are
separable, not that there are many files.

## Questions that come up

**"Can we use Overleaf?"** Yes. It removes the installation problem
entirely and supports collaboration, which matters for a group paper.
The notes cover a local installation for anyone who prefers one.

**"How many references do we need?"** There is no number. The criterion
is whether everything that should be cited is cited, and whether the
state of the field is accurate. A paper with four well-integrated
references scores better than one with twenty in a bibliography the body
never refers to.

**"Does the paper have to be three pages?"** Yes, and it is a limit
worth taking seriously: a great deal of the writing mark is about
organisation, and organising three pages is the exercise.

## Communications

### Before class

Send the following message before class:

    Hi all,

    This week's session is run by the mathematics subject librarian, on
    finding and evaluating sources for your paper.

    This is worth taking seriously: the Research component is 20% of the
    group project mark, and it is assessed on your state of the field
    and on your references. That is exactly what this session covers.

    Separately, you should be working through the LaTeX notes yourself:
    https://vknight.org/tex/

    Please get in touch if I can assist with anything,
    Vince

### After class

Send the following message after class:

    Hi all,

    Thank you to the subject librarian for today's session on
    researching sources.

    A reminder of what you work through on your own this week:

    - The LaTeX notes: https://vknight.org/tex/
    - Guidelines for good mathematical writing:
      https://vknight.org/cfm/assets/pdf/writing-mathematics-guidelines/main.pdf
    - A guide to writing mathematics:
      https://vknight.org/cfm/assets/pdf/a-guide-to-writing-mathematics/main.pdf

    Your references.bib file is one of the eight files you submit, and
    the references are part of the Research marking criterion.

    Please get in touch if I can assist with anything,
    Vince

## Answers for the deck

**Slide 4, name three tools.** Every year a group says there is nothing
else like their library. It is almost never true, and it is the answer
that scores worst, because the criterion is explicitly about how the
software compares with commonly used packages. Push for named tools:
`numpy`, `scipy`, `sympy`, a specific library on PyPI, whatever their
A-level teacher used. What theirs does differently can be small and
honest, such as handling one case in a way the general tool does not
make obvious.

**Slide 6, where is the title?** `\maketitle` is missing. The preamble
says what the title is; `\maketitle` is what puts it on the page. This
one catches almost everybody once.

**Slide 7, why is my citation a question mark?** They have run
`pdflatex` but not `bibtex`, and then not `pdflatex` twice more. Say
that Overleaf does all four for them and a local install does not,
since the groups that hit this are the ones who installed something.
The same answer covers a `Figure ??` cross reference, which needs the
second `pdflatex`.

**Slide 8, two habits to drop.** The first is a preference and they can
take it or leave it: `\(...\)` and `\[...\]` are easier to find in the
source than `$...$`, and they fail more usefully when unclosed. The
second is not a preference. A figure is a float, so LaTeX puts it where
it fits, which may be the next page or the one before. 'In the picture
below' is therefore sometimes simply false, where `Figure~\ref{...}` is
always true. The tilde stops a line break between the word and the
number.
