---
layout: class-notes
title: "Functions and data structures"
tags: functions-and-data-structures
---

## Format

A group-work week. The single hour is **not** a lecture: students work
through this topic on their own, and the session is there for you to
**answer questions and signpost**. Nothing below is material to deliver.

Open by asking what people got stuck on. If the room is silent, the
minutes are the way in: ask a group what went into their *questions
arising* box this week. That is what the box is for, and it makes the
point that the minutes are useful to them rather than only to the mark.

## What students work through on their own

- [Functions and data structures]({{ site.baseurl }}/topics/functions-and-data-structures.html),
  and the corresponding chapter of
  [Python for Mathematics](https://vknight.org/pfm/).

Each member reports on it at the group meeting, which is the first
standing item on every agenda.

## Questions that come up

**"When should something be a function?"** When it has a name worth
giving it. For the project the practical answer is firmer: anything the
tests need to call separately has to be a function.

**"List, tuple, set or dictionary?"** Push back to the mathematics. Is
order meaningful? Are duplicates meaningful? Is it a lookup from one
thing to another? The answer usually falls out of those three.

**"Can a function return more than one thing?"** Yes, and it returns a
tuple when it does. Worth showing, since several projects want it.

## Signposts

- The [Assessment]({{ site.baseurl }}/assessment/) page, for how this
  topic shows up in the marking criteria.
- The [example projects]({{ site.baseurl }}/assessment/example-projects/),
  which are worked submissions at the level of a good project.
- The [Meeting minutes: Week 4]({{ site.baseurl }}/topics/meeting-minutes-week-4.html)
  page for this week's form.

## Reference

The material below is **not delivered in class**. It is kept here as a
worked treatment of the topic to draw on when answering questions.

### Functions and data structures

### First meeting

After this meeting students should:

- Have an understanding of functions.
- Have an understanding of lists.

### Problem

Explain to students that we will be solving the following problem:

    Verify the following identity for all integer values of $0 \leq a \leq
    100$, $0 \leq b \leq 100$ and $1 \leq n \leq 10$:

    $$(a + b) ^ n = \sum_{i=0}^n\binom{n}{i} a ^ i b ^ {n - i}$$

### Solution

Now show::

    >>> def get_lhs(a, b, n):
    ...     """
    ...     Compute (a + b) ^ n directly
    ...     """
    ...     return (a + b) ** n
    >>> get_lhs(a=5, b=10, n=5)
    759375
    >>> import scipy.special
    >>> def get_rhs(a, b, n):
    ...     """
    ...     Compute the right hand side of the identity which aims to calculate
    ...     a summation of powers a^ib^(n - i) with a binomial coefficient.
    ...     """
    ...     return sum(scipy.special.binom(n, i) * a ** i * b ** (n - i) for i in range(n + 1))
    >>> get_rhs(a=5, b=10, n=5)
    np.float64(759375.0)

Ask if this confirms the identity?

Now create the following function to check the identify::

    >>> def check_identity(a, b, n):
    ...     """
    ...     Check the relationship
    ...     """
    ...     return get_lhs(a=a, b=b, n=n) == get_rhs(a=a, b=b, n=n)

Now create all checks::

    >>> checks = [
    ...    check_identity(a=a_val, b=b_val, n=n_val)
    ...    for a_val in range(101) for b_val in range(101) for n_val in range(1, 11)
    ... ]

Note that we can check all of them::

    >>> all(checks)
    False

Ask why this is the case. Have a discussion leading to the fix::

    >>> def get_rhs(a, b, n):
    ...     """
    ...     Compute the right hand side of the identity which aims to calculate
    ...     a summation of powers a^ib^(n - i) with a binomial coefficient.
    ...     """
    ...     return sum(int(scipy.special.binom(n, i)) * a ** i * b ** (n - i) for i in range(n + 1))

Re define `check_identity`:

    >>> def check_identity(a, b, n):
    ...     """
    ...     Check the relationship
    ...     """
    ...     return get_lhs(a=a, b=b, n=n) == get_rhs(a=a, b=b, n=n)

Now create all checks::

    >>> checks = [
    ...    check_identity(a=a_val, b=b_val, n=n_val)
    ...    for a_val in range(101) for b_val in range(101) for n_val in range(1, 11)
    ... ]

Note that we can check all of them::

    >>> all(checks)
    True

Come back: with time take any questions.

Point at resources.

### Communications

### After class

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I we used functions and list comprehensions. The chapter we
    are covering this week also includes sections on dictionaries and sets.

    In preparation for your tutorial please work through the following chapter:
    https://vknight.org/pfm/building-tools/02-functions-and-data-structures/introduction/main.html

    Please get in touch if I can assist with anything,
    Vince
