"""The binomial distribution: PMF, CDF, mean, variance, and simulation.

A binomial random variable counts the number of successes in $n$
independent Bernoulli trials each with success probability $p$. We
provide the probability mass function, the cumulative distribution
function, the mean, the variance, and a simulator. The binomial
coefficient is computed exactly with ``scipy.special.comb``.
"""

import random

import scipy.special


def pmf(number_of_successes, number_of_trials, success_probability):
    """Return the binomial PMF $P(X = k)$ for $X \\sim \\text{Bin}(n, p)$.

    Parameters
    ----------
    number_of_successes : int
        The number of successes $k$.
    number_of_trials : int
        The number of trials $n$.
    success_probability : float
        The probability of success on a single trial, $p \\in [0, 1]$.

    Returns
    -------
    float
        The probability $P(X = k)$.
    """
    coefficient = scipy.special.comb(number_of_trials, number_of_successes, exact=True)
    return (
        coefficient
        * success_probability**number_of_successes
        * (1 - success_probability) ** (number_of_trials - number_of_successes)
    )


def cdf(number_of_successes, number_of_trials, success_probability):
    """Return the binomial CDF $P(X \\le k)$.

    Parameters
    ----------
    number_of_successes : int
        The number of successes $k$.
    number_of_trials : int
        The number of trials $n$.
    success_probability : float
        The probability of success on a single trial.

    Returns
    -------
    float
        The cumulative probability $P(X \\le k)$.
    """
    return sum(
        pmf(value, number_of_trials, success_probability)
        for value in range(number_of_successes + 1)
    )


def mean(number_of_trials, success_probability):
    """Return the binomial mean $n p$."""
    return number_of_trials * success_probability


def variance(number_of_trials, success_probability):
    """Return the binomial variance $n p (1 - p)$."""
    return number_of_trials * success_probability * (1 - success_probability)


def simulate(number_of_trials, success_probability, number_of_simulations, seed=None):
    """Simulate draws from $\\text{Bin}(n, p)$.

    Each draw is the number of successes in ``number_of_trials``
    independent Bernoulli trials with success probability
    ``success_probability``.

    Parameters
    ----------
    number_of_trials : int
        The number of Bernoulli trials per draw.
    success_probability : float
        The probability of success on a single trial.
    number_of_simulations : int
        The number of binomial draws to simulate.
    seed : int, optional
        A seed for ``random.seed`` for reproducible simulations.

    Returns
    -------
    list of int
        The simulated success counts.
    """
    if seed is not None:
        random.seed(seed)
    samples = []
    for _ in range(number_of_simulations):
        successes = sum(1 for _ in range(number_of_trials) if random.random() < success_probability)
        samples.append(successes)
    return samples
