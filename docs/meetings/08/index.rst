Variables, conditionals and loops
=================================

Pre class email
---------------

Send the following email before class::

    Hi all,

    I hope you are all well.

    This is a brief email to make you aware of a few things:

    - The class timetable and weekly schedule for this Semester is available
      here: https://vknight.org/cfm/
    - This coming week, we will have class on Tuesday at 0900 am (feel free to
      bring breakfast). This week we
      will be covering this chapter
      https://vknight.org/pfm/building-tools/01-variables-conditionals-loops/introduction/main.html.
    - This Semester your assessment is a group exercise. I am letting you self
      select groups (groups of 4) but will assist anyone unable to find a group.
      We will discuss this more on Tuesday.

    Important: My wife and I are expecting our second child any day now, so at
    some point over the next couple of weeks I will not be around (for a week).
    Your weekly tutorial will still take place (with the usual expectations that
    you work through the weekly content and use the tutorial to ask questions)
    and we have sufficient time in the schedule to catch up.

    Please get in touch if I can assist with anything,
    Vince

First meeting
-------------

After this meeting students should:

- Understand the coursework exercise and the group aspect
- Understand the how to use a for loop and a while loop
- Know what they need to do to prepare for their seventh tutorial and how to
  make groups.

Coursework
**********

Explain goal of coursework:

> To build and present a Python library to solve a mathematical problem of your
  choice.

How it will be assessed (15 minute presentation and 2 page (max) paper).

Groups of 4. Self select and see instructions in email.

Agree on deadline for formation of group.

I recommend you meet regularly.

Have an agenda for every meeting.

Single point of contact.

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

    In this class I went over 2 separate things:

    1. The group coursework (please read the end of this email where action is
       required).
    2. Variables, loops and conditionals.

    In preparation for your tutorial tomorrow please work through the eighth
    chapter of the Python for mathematics book:
    https://vknight.org/pfm/building-tools/01-variables-conditionals-loops/introduction/main.html

    IMPORTANT ACTION REQUIRED

    For your group coursework you have until <DEADLINE> to form groups with 4
    people. I am letting you self select groups. If you do not have a group by
    <DEADLINE> I will create a group for you.

    Once you have created a group, 1 member of your group must email me (CC'ing
    in all other members) with subject: "Group formed"

    In the email please tell me the name of your group (you can be imaginative)
    and also which member of your group is the point of contact.

    ---

    Please get in touch if I can assist with anything,
    Vince
