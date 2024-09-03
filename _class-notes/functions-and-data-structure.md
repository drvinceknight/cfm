---
layout: class-notes
title: "Functions and data structures"
tags: functions-and-data-structures
---

# Functions and data structures

## First meeting

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

## After class communication

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I we used functions and list comprehensions. The chapter we
    are covering this week also includes sections on dictionaries and sets.

    In preparation for your tutorial please work through the following chapter:
    https://vknight.org/pfm/building-tools/02-functions-and-data-structures/introduction/main.html

    Please get in touch if I can assist with anything,
    Vince
