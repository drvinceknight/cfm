"""Summary statistics implemented from scratch.

We provide the mean, the median, the population and sample standard
deviations, and the three quartiles. Every function is implemented
directly from its definition rather than by calling the standard
``statistics`` module.
"""

import math


def mean(values):
    """Return the arithmetic mean $\\bar{x} = (1/n) \\sum_i x_i$."""
    return sum(values) / len(values)


def median(values):
    """Return the median of ``values``.

    The data is first sorted. For an odd number of values the median
    is the middle value; for an even number of values it is the
    average of the two middle values.
    """
    sorted_values = sorted(values)
    number_of_values = len(sorted_values)
    midpoint = number_of_values // 2
    if number_of_values % 2 == 1:
        return sorted_values[midpoint]
    return (sorted_values[midpoint - 1] + sorted_values[midpoint]) / 2


def population_standard_deviation(values):
    """Return the population standard deviation (divisor $n$).

    $$\\sigma = \\sqrt{(1/n) \\sum_i (x_i - \\bar{x})^2}.$$
    """
    average = mean(values)
    squared_deviations = sum((value - average) ** 2 for value in values)
    return math.sqrt(squared_deviations / len(values))


def sample_standard_deviation(values):
    """Return the sample standard deviation (divisor $n - 1$).

    $$s = \\sqrt{(1/(n - 1)) \\sum_i (x_i - \\bar{x})^2}.$$
    """
    average = mean(values)
    squared_deviations = sum((value - average) ** 2 for value in values)
    return math.sqrt(squared_deviations / (len(values) - 1))


def quartiles(values):
    """Return the three quartiles $(Q_1, Q_2, Q_3)$ of ``values``.

    We use the 'exclusive' method: the $k$-th quartile is at the
    fractional 1-indexed position $k(n + 1)/4$, with linear
    interpolation between the surrounding sorted values. This matches
    ``statistics.quantiles(values, n=4)`` from the standard library.
    """
    sorted_values = sorted(values)
    number_of_values = len(sorted_values)
    cut_points = []
    for quartile_index in (1, 2, 3):
        position = quartile_index * (number_of_values + 1) / 4
        lower_rank = int(position)
        fraction = position - lower_rank
        if lower_rank < 1:
            cut_value = sorted_values[0]
        elif lower_rank >= number_of_values:
            cut_value = sorted_values[-1]
        else:
            lower_value = sorted_values[lower_rank - 1]
            upper_value = sorted_values[lower_rank]
            cut_value = lower_value + fraction * (upper_value - lower_value)
        cut_points.append(cut_value)
    return tuple(cut_points)
