---
layout: class-notes
title: "Variables, conditionals and loops"
tags: variables-conditional-statements-and-while-loops
---

# Variables, conditionals and loops

After this meeting students should:

- Understand the coursework exercise and the group aspect
- Understand the how to use a for loop and a while loop
- Know what they need to do to prepare for their seventh tutorial and how to
  make groups.

### Coursework

Explain goal of coursework:

> To build and present a Python library to solve a mathematical problem of your
> choice.

How it will be assessed (15 minute presentation and 2 page (max) paper).

Groups of 4. Self select and see instructions in email.

I recommend you meet regularly.

Have an agenda for every meeting.

Single point of contact.

### Problem

    Explain to students that we will be solving the following problem:

    A perfect number is a positive integer whose divisors (excluding itself) sum to
    itself. For example, :math:`6` is a perfect number because :math:`6 = 1 + 2 +
    3`.

    1. How many perfect numbers are there less than 20?
    2. What is the next perfect number?

### Solution

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

Note that we can combine all booleans using `all`::

    >>> all(checks)
    False

Or `any`::

    >>> any(checks)
    True

We cam also count them (as before) using `sum`::

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

### After class communication

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I went over 2 separate things:

    1. The group coursework (please read the end of this email where action is
       required).
    2. Variables, loops and conditionals.

    I recommend working through the following chapter of the class text:
    https://vknight.org/pfm/building-tools/01-variables-conditionals-loops/introduction/main.html

    IMPORTANT ACTION REQUIRED

    For your group coursework you have until <DEADLINE> to form groups with 4
    people. I am letting you self select groups. If you do not have a group by
    <DEADLINE> I will create a group for you.

    ---

    Please get in touch if I can assist with anything,
    Vince

### Some common difficulties

Create a set::

    >>> set_1 = set((-1, 1, 1, 2, 3, 5))
    >>> set_1
    {1, 2, 3, 5, -1}
    >>> set_2 = set(range(10))
    >>> set_2
    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

Union::

    >>> set_1 | set_2
    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1}

Intersection::

    >>> set_1 & set_2
    {1, 2, 3, 5}

Set subtraction::

    >>> set_1 - set_2
    {-1}

Set inclusion::

    >>> set_1 <= set_2
    False

Reasons for using sets:

- The ability to to the above operations.
- Immediate removal of duplicates.
- Checking inclusion.

Run the following timing examples::

    N = 10 ** 4
    numbers_as_range = range(N)
    numbers_as_list = list(numbers_as_range)
    numbers_as_tuple = tuple(numbers_as_range)
    numbers_as_set = set(numbers_as_range)

Testing the list::

    %%timeit
    5000 in numbers_as_list

Testing the tuple::

    %%timeit
    5000 in numbers_as_tuple

Testing the set::

    %%timeit
    5000 in numbers_as_set

Testing the range itself::

    %%timeit
    5000 in numbers_as_range

Modulo
++++++

Give some examples of modula arithmetic::

    >>> 5 % 2
    1
    >>> 17 % 9
    8
    >>> for i in range(24 * 5):
    ...     print(i % 24)
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
