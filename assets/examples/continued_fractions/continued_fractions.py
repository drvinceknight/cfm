"""Continued fractions of rational numbers.

We compute the continued fraction expansion of a rational number with the
Euclidean algorithm, then turn the resulting list of integer coefficients
into a list of convergent rationals.
"""

import sympy


def continued_fraction(rational_number, maximum_terms):
    """Return the continued fraction expansion of a rational number.

    The continued fraction expansion of a number $r$ is a sequence of
    integers $a_0, a_1, a_2, \\dots$ such that

    $$r = a_0 + \\cfrac{1}{a_1 + \\cfrac{1}{a_2 + \\dots}}.$$

    For a rational input the expansion terminates after finitely many
    steps; the loop stops as soon as the remainder is zero.

    Parameters
    ----------
    rational_number : sympy.Rational, int, or float
        The number to expand.
    maximum_terms : int
        The maximum number of coefficients to compute.

    Returns
    -------
    list of int
        The coefficients ``[a_0, a_1, ..., a_k]``.
    """
    coefficients = []
    remaining = sympy.Rational(rational_number)
    for _ in range(maximum_terms):
        integer_part = sympy.floor(remaining)
        coefficients.append(int(integer_part))
        fractional_part = remaining - integer_part
        if fractional_part == 0:
            break
        remaining = 1 / fractional_part
    return coefficients


def convergents(coefficients):
    """Return the list of convergents of a continued fraction.

    The convergents are the rational numbers obtained by truncating the
    expansion after each term. We use the standard recursion

    $$\\frac{p_n}{q_n}
    = \\frac{a_n p_{n - 1} + p_{n - 2}}{a_n q_{n - 1} + q_{n - 2}}.$$

    Parameters
    ----------
    coefficients : list of int
        The continued fraction coefficients ``[a_0, a_1, ...]``.

    Returns
    -------
    list of sympy.Rational
        The successive convergents.
    """
    result = []
    earlier_numerator, current_numerator = 0, 1
    earlier_denominator, current_denominator = 1, 0
    for coefficient in coefficients:
        next_numerator = coefficient * current_numerator + earlier_numerator
        next_denominator = coefficient * current_denominator + earlier_denominator
        result.append(sympy.Rational(next_numerator, next_denominator))
        earlier_numerator, current_numerator = current_numerator, next_numerator
        earlier_denominator, current_denominator = (
            current_denominator,
            next_denominator,
        )
    return result


def golden_ratio_convergents(number_of_terms):
    """Return the first convergents of the golden ratio.

    The golden ratio $\\varphi = (1 + \\sqrt{5}) / 2$ has the simplest
    possible continued fraction expansion: $[1; 1, 1, 1, \\dots]$.
    The convergents are ratios of consecutive Fibonacci numbers.

    Parameters
    ----------
    number_of_terms : int
        The number of convergents to return.

    Returns
    -------
    list of sympy.Rational
        Successive convergents of the golden ratio.
    """
    return convergents([1] * number_of_terms)
