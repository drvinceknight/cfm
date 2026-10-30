---
layout: class-notes
title: "Testing of code"
tags: testing
---

## Run sheet

One row per slide, to glance at while the deck is on screen. The
reasoning behind every answer is in the sections below. Deck:
[/deck/testing/main.pdf]({{ site.baseurl }}/deck/testing/main.pdf).

| Slide | On screen | What you fill in or say |
|--:|:--|:--|
| 2 | You have now read all three | Modular, documented, tested. Together they are the Scope criterion, 50% of the project mark |
| 3 | One line, two parts | A claim that must be true, then the message you read when it is not. Push on the second: name what was expected |
| 4 | How many tests does this need? | **Three**, because the function does three things. Count behaviours, not functions |
| 5 | Your tests all pass. Are you done? | Zero, one, an empty input, a negative. Take a real function from a group in the room |
| 6 | How do you test something random? | Seeding. Also worth giving: assert the set of values over 1000 rolls, or that each count falls in a range |
| 7 | Where the tests live | `test_<library>.py`, one function per behaviour, each with a docstring, calls at the bottom, then `python test_tsp.py`. No `pytest` needed |
| 8 | What is a doctest for? | To check the documentation is still true. Not where the mathematics is tested. `python -m doctest README.md`. Both are required |
| 9 | So which function is untested? | Group work, ten minutes, not a question to you. Walk the room. A group that cannot list its own functions has a bigger problem |
| 10 | Eight files, in Week 11 | Ask which one nobody has started. Usually `contribution.md` and the presentation, and both are cheap to start |
| 11 | From here to the deadline | Minutes this week, then finish it. No more timetabled meetings after this |
| 12 | Before you leave | The fifth and last minutes; a name against each of the eight files, recorded in the minutes |

## Format

A group-work week. The single hour is **not** a lecture: students work
through this topic on their own, and the session is there for you to
**answer questions and signpost**. The deck below is questions to put
to the room, not material to read out, and the reference section at the
end is not delivered at all.

Open by asking what people got stuck on. If the room is silent, the
minutes are the way in: ask a group what went into their *questions
arising* box this week. That is what the box is for, and it makes the
point that the minutes are useful to them rather than only to the mark.

## Timing

A full session, and the last of the five group-project weeks. The hour
is still questions and signposting rather than a lecture, but the deck
gives it a spine for when the room has nothing to ask.

| Section | Minutes |
|:--|--:|
| Open with what people got stuck on | 6 |
| Slide 2: the three pillars, now all read | 4 |
| Slides 3 to 8: the testing questions | 24 |
| Slide 9: which function is untested? | 10 |
| Slides 10 and 11: the eight files, and the run in | 8 |
| Slide 12: before you leave | 8 |

If the room is talking, let it. The questions they bring beat the
slides. Slide 9 is the one not to cut, and slide 12 is the other: this
is the last timetabled meeting week, so it is the last cheap
opportunity to catch a group that has three of the eight files and no
plan for the rest.

## The deck

There is a write-on deck at
[/deck/testing/main.pdf]({{ site.baseurl }}/deck/testing/main.pdf).
Slides 3 to 8 each carry a short listing, a question and a workspace
for the answer the room gives. Slides 9 and 10 are filled in by each
group for itself rather than by you. Answers are at the end of these
notes.

## What students work through on their own

- [Testing of code]({{ site.baseurl }}/topics/testing-of-code.html),
  and the corresponding chapter of
  [Python for Mathematics](https://vknight.org/pfm/).

Each member reports on it at the group meeting, which is the first
standing item on every agenda.

## Questions that come up

**"How many tests do we need?"** The criterion is that the tests cover
all functionality of the code and the documentation, so the question to
turn back on them is which function is currently untested.

**"Our tests all pass, are we done?"** Ask what happens at the
boundaries: zero, one, an empty input, a negative where only positives
were considered. The exemplary band specifically mentions edge cases the
tutorial does not exercise.

**"Do we need pytest?"** No. Assertion statements in a
`test_<library>.py` that runs top to bottom are sufficient and are what
the example projects use.

## Signposts

- The [Assessment]({{ site.baseurl }}/assessment/) page, for how this
  topic shows up in the marking criteria.
- The [example projects]({{ site.baseurl }}/assessment/example-projects/),
  which are worked submissions at the level of a good project.
- The [Meeting minutes: Week 10]({{ site.baseurl }}/topics/meeting-minutes-week-10.html)
  page for this week's form.

## Communications

### Before class

Send the following message before class:

    Hi all,

    This week's topic is automated testing, which is the last of the
    three chapters on turning code that works into software.

    This is also the last group meeting week: Week 10 minutes are the
    fifth and final set that your engagement record is built from.

    Worth bringing: a list of the functions in your library. We will
    work out which of them are not yet tested.

    Please get in touch if I can assist with anything,
    Vince

### After class

Send the following message after class:

    Hi all,

    Today we went through automated testing, and each group listed the
    functions in its library that have no test yet.

    The topic pages:

    - Testing of code: https://vknight.org/cfm/topics/testing-of-code.html
    - The chapter in Python for Mathematics:
      https://vknight.org/pfm/building-tools/07-testing/tutorial/main.html

    From here to the deadline there are no more timetabled meetings.
    What is left is the eight files:

    1. main.tex
    2. main.pdf
    3. references.bib
    4. <library>.py
    5. test_<library>.py
    6. README.md
    7. presentation.mp4
    8. contribution.md

    If something in your group is not working, this is the week to
    raise it in the contact hour rather than the week before
    submission.

    Please get in touch if I can assist with anything,
    Vince

## Answers for the deck

**Slide 2, the three pillars.** Nothing to elicit, but it is worth
thirty seconds. Modularisation, documentation and testing are the three
chapters they have now read, and the Scope criterion is all three
together at 50% of the project mark. Small functions are easy to test
and easy to document; tests are what make documentation that is
verified possible.

**Slide 3, one line, two parts.** After `assert` comes a claim that
must be true, and then an optional string that is shown when it is not.
Push the second part: the string is the message their future self reads
when the test fails, so `"The function gave the wrong answer"` is
weaker than a sentence naming what was expected.

**Slide 4, how many tests does this need?** Three, because the function
does three things. Groups count functions and write one test each; the
thing to count is behaviours. This is the same argument as the
modularisation week from the other direction: a function that needs ten
tests is probably several functions.

**Slide 5, your tests all pass.** Zero, one, an empty input and a
negative where only positives were considered. The exemplary band asks
specifically for edge cases that the tutorial does not exercise, and
these four are where they usually live. Take a real function from a
group in the room rather than a made-up one.

**Slide 6, how do you test something random?** Seeding. `random.seed(0)`
fixes the sequence without making the function deterministic in use, so
the assertion holds every run. Worth adding the second technique: for a
thousand rolls you can assert the set of values obtained, or that each
count falls in an expected range, which tests the behaviour rather than
one draw.

**Slide 7, where the tests live.** A separate `test_<library>.py`, one
function per behaviour, each with a docstring saying what it checks, and
the calls at the bottom so that `python test_tsp.py` runs them. They do
not need `pytest`, and the example projects do not use it. The reason to
use functions rather than a flat script is that each one has somewhere
to document what it checks.

**Slide 8, what is a doctest for?** To check that the documentation is
still true. It is not where the mathematics gets tested, and using it
that way makes the README unreadable. `python -m doctest README.md`
runs them. Both are required separately: the doctests are documentation
that is verified, the test file is the test suite.

**Slide 9, which function is untested?** This is group work, not a
question to you, and it is the ten minutes of the hour that produce
actions in the minutes. Walk the room. A group that cannot list its own
functions has a bigger problem than testing, and that is worth knowing
now.

**Slide 10, the eight files.** The tick boxes are for them. The useful
answer is the uncomfortable one, so ask which file nobody has started.
In most years that is `contribution.md` and the presentation, and both
are cheap to start and expensive to leave.

## Reference

The material below is **not delivered in class**. It is kept here as a
worked treatment of the topic to draw on when answering questions.

After this meeting students should:

- Understand the general structure required for documentation
- Understand how to write further markdown

### First meeting

After this meeting students should:

- Understand how assertion statements work
- Understand how to write unit tests using assert statements
- Understand how to write tests for documentation

### Testing software

Discuss how we will write automated tests for the `tsp` library we wrote in the
first section.

### Writing the unit tests

Write the following in a `test_tsp.py` file::

    import numpy as np
    import matplotlib.pyplot as plt

    import tsp

    def test_get_tour_with_no_seed():
        number_of_stops = 4
        tour = tsp.get_tour(number_of_stops=number_of_stops)
        assert np.array_equal(tour, np.array([0, 1, 2, 3, 0]))

    def test_get_tour_with_seed_0():
        number_of_stops = 4
        seed = 0
        tour = tsp.get_tour(number_of_stops=number_of_stops, seed=seed)
        assert np.array_equal(tour, np.array([0, 3, 2, 1, 0])), f"Obtained output is {tour}"

    def test_get_tour_with_seed_1():
        number_of_stops = 4
        seed = 1
        tour = tsp.get_tour(number_of_stops=number_of_stops, seed=seed)
        assert np.array_equal(tour, np.array([0, 1, 3, 2, 0])), f"Obtained output is {tour}"


    def test_swap_cities():
        tour = [0, 1, 3, 2, 4, 0]
        steps = (4, 1)
        new_tour = tsp.swap_cities(tour=tour, steps=steps)
        assert new_tour == [0, 4, 2, 3, 1, 0], f"Obtained output is {new_tour}"


    def test_get_cost():
        distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))
        tour = [0, 1, 2, 3, 0]
        cost = tsp.get_cost(tour=tour, distance_matrix=distance_matrix)
        assert cost == 24


    def test_run_2_opt_algorithm_with_seed_0():
        distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))
        number_of_stops = 4
        seed = 0
        iterations = 50
        tour = tsp.run_2_opt_algorithm(number_of_stops=number_of_stops,
                distance_matrix=distance_matrix, seed=seed, iterations=iterations)
        assert tour == [0, 2, 3, 1, 0], f"Obtained output is {tour}"

    def test_run_2_opt_algorithm_with_seed_1():
        distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))
        number_of_stops = 4
        seed = 1
        iterations = 50
        tour = tsp.run_2_opt_algorithm(number_of_stops=number_of_stops,
                distance_matrix=distance_matrix, seed=seed, iterations=iterations)
        assert tour == [0, 2, 1, 3, 0], f"Obtained output is {tour}"

    def test_plot_tour():
        x = np.array([2, 3])
        y = np.array([2, 3])
        tour = np.array([0, 1, 0])
        plot = tsp.plot_tour(x=x, y=y, tour=tour)
        assert plot is None

    test_get_tour_with_no_seed()
    test_get_tour_with_seed_0()
    test_get_tour_with_seed_1()
    test_swap_cities()
    test_get_cost()
    test_run_2_opt_algorithm_with_seed_0()
    test_run_2_opt_algorithm_with_seed_1()
    test_plot_tour()

Run the above tests by running:

    $ python test_tsp.py

Depending on time now discuss refactoring some of the code. For example:

- Modify `swap_cities` to be called `swap_steps` as this name is more generic.
- Possibly modify `swap_cities`/`swap_steps` so that it can handle numpy array
  outputs.

At each step modify the source code and then modify the tests.

Discuss importance of tests as a debugging tool.

Testing the documentation

---

Modify the documentation in the `README.md` file to use doctests::

    # TSP

    A library for solving instances of the travelling sales agent problem

    ## Tutorial

    In this tutorial we will see how to use `tsp` to solve instances of the
    [Travelling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

    Assuming we have the following distance matrix:

    ```python
    >>> import numpy as np
    >>> distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))

    ```

    We can obtain a tour using the following:

    ```python
    >>> import tsp  # doctest: +SKIP
    >>> tour = tsp.run_2_opt_algorithm(number_of_stops=4, distance_matrix=distance_matrix, iterations=1000, seed=0)  # doctest: +SKIP
    >>> tour  # doctest: +SKIP
    [0, 3, 1, 2, 0]

    ```

    The `tsp` library includes further functionality which you can read in the
    How To guides.

**Note** that the doctests are skipped when checked for this documentation.

Run the doc tests by typing::

    $ python -m doctest README.md

Discussion around 3 pillars of software development

---

Specifically look at diagram in further information section:
https://vknight.org/pfm/building-tools/07-testing/why/main.html#how-are-modularisation-documentation-and-testing-related

### Communications

### After class

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I went over automated testing.

    In class we wrote unit and doctests for the Travelling Salesagent Problem.
    You can find a different example (studying snakes and ladders) here:
    https://vknight.org/pfm/building-tools/07-testing/tutorial/main.html

    Please get in touch if I can assist with anything,
    Vince
