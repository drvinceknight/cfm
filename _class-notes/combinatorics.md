---
layout: class-notes
title: "Combinatorics"
tags: combinatorics
---

## First meeting

After this meeting students should:

- Understand how to use the itertools library to solve combinatorial
  problems.
- Know what they need to do to prepare for their fifth tutorial.

### Problem

Explain to students that we will be solving the following problem:

The digits 1, 2, 3 and 4 are arranged in random order, for form a
four-digit number.

1.  How many different four-digit numbers can be formed?

2.  How many different four-digit numbers:

    : 1. Are even. 2. Are less than 4000.

### Solution

Group exercise (breakout rooms of 3): ask students to spend 5 minutes
writing a plan to tackle that problem (not necessarily carrying out each
step).

Now show how to get code to do this:

    >>> import itertools
    >>> digits = range(1, 5)
    >>> digits
    range(1, 5)

Explain what that is and how it can be useful to encapsulate the
instructions for a set of objects as opposed to the objects themselves.:

    >>> tuple(digits)
    (1, 2, 3, 4)

Explain how we are mainly going to be using `itertools`:

    >>> permutations = itertools.permutations(digits)
    >>> permutations  # doctest: +SKIP
    <itertools.permutations object at 0x7fe267f1b5e0>
    >>> permutations = tuple(itertools.permutations(digits))
    >>> permutations
    ((1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1))
    >>> len(permutations)
    24

Note that we can confirm this theoretically:

    >>> import math
    >>> math.factorial(4)
    24

For the next part of the question we want to consider our permutations
and only count the ones that have an even last digit:

    >>> sum((permutation[3] + 1) % 2 for permutation in permutations)
    12

Be sure to explain:

- The indexing.
- The summation mod 2: $\sum_{\pi \in \Pi} \pi_4 + 1 \mod 2$

Note that this can be calculated theoretically. The last digit can
either be 2 or 4. For each of those there are $3!$ possibilities for the
other digits:

    >>> 2 * math.factorial(3)
    12

For the last question show that we will compute the following:

$$\sum_{\pi \in \Pi \text{ if }\pi_1 10 ^ 3 + \pi_2 10 ^ 2 + \pi_3 10 + \pi_4 \leq 4000} 1$$

Here is the code that corresponds to that:

    >>> sum(
    ...     1
    ...     for permutation in permutations
    ...     if permutation[0] * 10 ** 3
    ...     + permutation[1] * 10 ** 2
    ...     + permutation[2] * 10
    ...     + permutation[3]
    ...     <= 4000
    ... )
    18

Again confirm this theoretically. For a number to be less than 4000 it
needs to start with either 1, 2 or 3. For each of those possibilities
there are $3!$ permutations of the remaining digits:

    >>> 3 * math.factorial(3)
    18

Come back: with time take any questions.

Point at resources.

## After class email

Send the following email after class:

    Hi all,

    A recording of today's class is available at <>.

    In this class I went over a demonstration of using Python to solve a
    combinatorial problem. We used a computer to directly generate permutations
    of objects.

    - We mainly used the itertools library
    - The range tool allowed us to access specific ranges of numbers.
    - We saw how to sum over sets as a way of counting specific objects.

    One thing I did not cover explicitly is using the itertools library to
    generate combinations (where order does not matter).
    You can see this here:
    https://vknight.org/pfm/tools-for-mathematics/05-combinations-permutations/how/main.html#creating-combinations-of-a-given-set-of-elements

    We also did not cover how to compute directly binomial and permutation
    coefficients which is also covered in the how to section of the book.

    In preparation for your tutorial tomorrow please work through the fifth
    chapter of the Python for mathematics book:
    https://vknight.org/pfm/tools-for-mathematics/05-combinations-permutations/introduction/main.html

    Please get in touch if I can assist with anything,
    Vince

## Second meeting

We will cover two points of dicciulty:

- Understanding the summation notation
- Understanding the ordering of a combination specifically by
  revisiting the COMPUTER problem.

Consider:

$$\sum_{i=0}^{100}i ^ 2$$

Discuss the images at <https://github.com/drvinceknight/pfm/issues/120>

Then discuss the COMPUTER solution.

Highlight what happens when we add another `P` to the end:

    >>> letters = ("C", "O", "M", "P", "U", "T", "E", "R", "P")
    >>> selections = tuple(itertools.combinations(letters, 3))
    >>> sum(1 for selection in selections if selection == ("O", "P", "T"))
    1

However:

    >>> sum(1 for selection in selections if selection == ("O", "P", "T") or selection == ("O", "T", "P"))
    2
