Variables, conditionals and loops
=================================

First meeting
-------------

After this meeting students should:

- Understand the coursework exercise and the group aspect
- Understand the how to use a for loop and a while loop
- Know what they need to do to prepare for their seventh tutorial and how to
  make groups.

Coursework
**********

TODO
Explain goal of coursework.

How it will be assessed (15 minute presentation).

Problem
*******

Explain to students that we will be solving the following problem:

A perfect number is a positive integer whose divisors (excluding itself) sum to
itself.  For example, :math:`6` is a perfect number because :math:`6 = 1 + 2 +
3`.

1. How many perfect numbers are there less than 20?
2. What is the next perfect number?

Solution
********

Group exercise (breakout rooms of 3): ask students to spend 5 minutes writing a
plan to tackle that problem (not necessarily carrying out each step).

We start by writing a function that checks if a number is perfect::

    >>> def is_perfect(n):
    ...     """
    ...     Checks if a number n is perfect.
    ...     """
    ...     return sum(i for i in range(1, n) if (n % i == 0)) == n
    >>> is_perfect(5)
    False
    >>> is_perfect(6)
    True

Now we can check all numbers up until 20::

    >>> checks = [is_perfect(n) for n in range(1, 21)]

Note that we can combine all booleans using :code:`all`::

    >>> all(checks)
    False

Or :code:`any`::

    >>> any(checks)
    True

We cam also count them (as before) using :code:`sum`::

    >>> sum(checks)
    1

We are there using a list comprehension (as before) **but** we can also use a
`for` loop::

    >>> count = 0
    >>> for n in range(1, 21):
    ...     if is_perfect(n):
    ...         count += 1
    >>> count
    1

Discuss how the `for` loop works.


Now to answer the other question, **we do not know** how many times we need to
iterate the code so we use a `while` loop::

    >>> n = 7
    >>> while not is_perfect(n):
    ...     n += 1
    >>> n
    28

Indeed the prime divisors of 28 are::

    >>> import sympy as sym
    >>> sym.primefactors(28)
    [2, 7]

And::

    >>> 1 + 2 + 4 + 7 + 14
    28


We can repeat the above to find the 3rd perfect number::

    >>> n = 29
    >>> while not is_perfect(n):
    ...     n += 1
    >>> n
    496

Indeed the divisors of 496 are::

    >>> import sympy as sym
    >>> sym.primefactors(496)
    [2, 31]

And::

    >>> 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248
    496


After class email
-----------------

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I went over TODO Write description of for, while

    In preparation for your tutorial tomorrow please work through the eighth
    chapter of the Python for mathematics book:
    TODO Correct url

    IMPORTANT ACTION REQUIRED

    TODO Invite students to form groups

    Please get in touch if I can assist with anything,
    Vince
