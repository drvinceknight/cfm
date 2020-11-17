Probability week
================

First meeting
-------------

After this meeting students should:

- Understand how to use the random library to simulate random events
- Know what they need to do to prepare for their sixth tutorial.

Problem
*******

Explain to students that we will be solving the following problem:

A delivery company delivers fragile items. If a delivery is on time it is
usually because it was rushed.
The probability that an item is delivered on time is
:math:`0.75`. The probability that an item is broken given that it arrived on
time is :math:`0.3` and if it is late :math:`0.2`.

1. What is the probability that an item is late?
2. Given that an item is broken what is the probability that it was on time?


Solution
********

Group exercise (breakout rooms of 3): ask students to spend 5 minutes writing a
plan to tackle that problem (not necessarily carrying out each step).

Now explain that we are going get a computer to simulate the described events
from which we can measure the probabilities (and theoretically compare to the
expected results).

Now show how to get code to first write a function to simulate a delivery::

    >>> import random
    >>> def is_delivery_late():
    ...     """
    ...     A function to randomly simulate if a delivery is late or not.
    ...     """
    ...     return random.random() > 0.75

Spend some time explaining what is happening here, including:

- The random library
- Functions (importance of white space, importance of the docstring, the help
  statement...)
- The return statement

Now we will use that function to create a number of experiments::

    >>> number_of_repetitions = 10000
    >>> samples = [is_delivery_late() for repetition in range(number_of_repetitions)]
    >>> samples  # doctest: +SKIP
    [True, False, True, ..., False, True, False]

We can confirm the number of samples::

    >>> len(samples)
    10000

We can now confirm the probability::

    >>> sum(sample for sample in samples) / number_of_repetitions  # doctest: +SKIP
    0.2459

Now explain that we will cover the entire question by writing a function to
simulate both the delivery and whether or not the item is broken::


    >>> def sample_experiment():
    ...     """
    ...     This samples a delivery and depending on whether or not it is late
    ...     selects whether or not the item is broken.
    ...     """
    ...     is_late = is_delivery_late()
    ...
    ...     if is_late is True:
    ...         probability_of_broken = 0.2
    ...     else:
    ...         probability_of_broken = 0.3
    ...
    ...     is_broken = random.random() < probability_of_broken
    ...     return is_late, is_broken

We can use this to confirm the previous result::

    >>> samples = [sample_experiment() for repetition in range(number_of_repetitions)] 
    >>> sum(is_broken for is_late, is_broken in samples) / number_of_repetitions # doctest: +SKIP
    0.2699

Now we can compute the probability of an item being on time if it is broken::

    >>> samples_with_broken = [(is_late, is_broken) for is_late, is_broken in samples if is_broken is True]
    >>> sum(is_late for is_late, is_broken in samples_with_broken) / len(samples_with_broken)  # doctest: +SKIP
    0.18114406

Note that we can use Bayes' theorem to confirm this theoretically:

.. math::

    P(\text{On time}|\text{Broken}) = \frac{P(\text{Broken} | \text{On time})P(\text{On time})}{P(\text{Broken})}

We have:

.. math::

    P(\text{Broken} | \text{On time}) = 0.3

.. math::

    P(\text{On time}) = 0.75

.. math::

    P(\text{Broken}) = 0.3 \times 0.75 + 0.2 \times 0.25

We can compute this::

    >>> probability_of_on_time_if_broken = 0.3 * 0.75 / (0.3 * 0.75 + 0.2 * 0.25)
    >>> probability_of_on_time_if_broken  # doctest: +ELLIPSIS
    0.818181...

Thus the probability for the question is::

    >>> 1 - probability_of_on_time_if_broken  # doctest: +ELLIPSIS
    0.181818...

Come back: with time take any questions.

Point at resources.

After class email
-----------------

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I went over a demonstration of using Python to solve a
    probabilitistic problem. I demontrated how to simulate random events and
    measure probabilities directly. We did this using the following Python
    tools:

    - Writing functions.
    - List comprehensions.

    In preparation for your tutorial tomorrow please work through the sixth
    chapter of the Python for mathematics book:
    https://vknight.org/pfm/tools-for-mathematics/06-probability/introduction/main.html

    Please get in touch if I can assist with anything,
    Vince
