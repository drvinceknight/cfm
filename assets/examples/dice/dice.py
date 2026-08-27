"""Simulation and exact distributions for sums of fair dice.

We provide a small library that simulates rolls of one or more fair
$s$-sided dice, computes the empirical distribution of the simulated
sums, and gives the exact distribution as a dictionary of
``fractions.Fraction`` for comparison.
"""

import random
import statistics as st
from fractions import Fraction


def roll(number_of_dice, sides=6, seed=None):
    """Return a tuple of ``number_of_dice`` faces from fair $s$-sided dice.

    Parameters
    ----------
    number_of_dice : int
        The number of dice to roll.
    sides : int, optional
        The number of sides on each die (default 6).
    seed : int, optional
        A seed for ``random.seed`` for reproducible rolls.

    Returns
    -------
    tuple of int
        The face values, each between 1 and ``sides``.
    """
    if seed is not None:
        random.seed(seed)
    return tuple(random.randint(1, sides) for _ in range(number_of_dice))


def simulate_sums(number_of_dice, number_of_rolls, sides=6, seed=None):
    """Return a list of simulated sums of ``number_of_dice`` dice.

    Each entry is the total of a single roll of ``number_of_dice`` fair
    $s$-sided dice.

    Parameters
    ----------
    number_of_dice : int
        The number of dice in each roll.
    number_of_rolls : int
        The number of rolls to simulate.
    sides : int, optional
        The number of sides on each die (default 6).
    seed : int, optional
        A seed for ``random.seed`` for reproducible simulations.

    Returns
    -------
    list of int
        The simulated sums, of length ``number_of_rolls``.
    """
    if seed is not None:
        random.seed(seed)
    sums = []
    for _ in range(number_of_rolls):
        total = sum(random.randint(1, sides) for _ in range(number_of_dice))
        sums.append(total)
    return sums


def empirical_distribution(samples):
    """Return the empirical (relative-frequency) distribution.

    Parameters
    ----------
    samples : list of int
        The observed sums.

    Returns
    -------
    dict of {int: float}
        A mapping from each observed value to its relative frequency.
    """
    total = len(samples)
    counts = {}
    for value in samples:
        counts[value] = counts.get(value, 0) + 1
    return {value: count / total for value, count in counts.items()}


def theoretical_distribution(number_of_dice, sides=6):
    """Return the exact distribution of the sum of ``number_of_dice`` dice.

    The distribution is computed by repeated convolution of the
    single-die distribution. We use ``fractions.Fraction`` so the
    probabilities are exact rationals.

    Parameters
    ----------
    number_of_dice : int
        The number of dice in the sum.
    sides : int, optional
        The number of sides on each die (default 6).

    Returns
    -------
    dict of {int: Fraction}
        A mapping from each possible total to its exact probability.
    """
    single_die_probability = Fraction(1, sides)
    distribution = {face: single_die_probability for face in range(1, sides + 1)}
    for _ in range(number_of_dice - 1):
        next_distribution = {}
        for current_total, current_probability in distribution.items():
            for face in range(1, sides + 1):
                key = current_total + face
                next_distribution[key] = (
                    next_distribution.get(key, Fraction(0))
                    + current_probability * single_die_probability
                )
        distribution = next_distribution
    return distribution


def summary_statistics(samples):
    """Return ``(mean, median, sample_standard_deviation)`` of ``samples``.

    Parameters
    ----------
    samples : list of int or float
        The observations.

    Returns
    -------
    tuple
        ``(mean, median, sample_standard_deviation)``.
    """
    return st.mean(samples), st.median(samples), st.stdev(samples)
