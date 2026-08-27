"""Solving real quadratic equations symbolically.

We use ``sympy.solveset`` to find the roots of $a x^2 + b x + c$, the
discriminant to classify the nature of the roots, and a small helper to
compute the coordinates of the vertex of the corresponding parabola.
"""

import sympy


def discriminant(quadratic_coefficient, linear_coefficient, constant_coefficient):
    """Return the discriminant of $a x^2 + b x + c$.

    Parameters
    ----------
    quadratic_coefficient : int, float, or sympy expression
        The coefficient of $x^2$.
    linear_coefficient : int, float, or sympy expression
        The coefficient of $x$.
    constant_coefficient : int, float, or sympy expression
        The constant term.

    Returns
    -------
    sympy expression
        The discriminant $b^2 - 4 a c$.
    """
    return linear_coefficient**2 - 4 * quadratic_coefficient * constant_coefficient


def solutions(
    quadratic_coefficient,
    linear_coefficient,
    constant_coefficient,
    variable,
):
    """Return the real solutions of $a x^2 + b x + c = 0$.

    We pass the expression to ``sympy.solveset`` over ``sympy.S.Reals``;
    the return type is a :class:`sympy.Set`, which is the recommended
    interface in :mod:`sympy`.

    Parameters
    ----------
    quadratic_coefficient : int, float, or sympy expression
        The coefficient of $x^2$.
    linear_coefficient : int, float, or sympy expression
        The coefficient of $x$.
    constant_coefficient : int, float, or sympy expression
        The constant term.
    variable : sympy.Symbol
        The unknown.

    Returns
    -------
    sympy.Set
        The set of real roots.
    """
    expression = (
        quadratic_coefficient * variable**2 + linear_coefficient * variable + constant_coefficient
    )
    return sympy.solveset(expression, variable, domain=sympy.S.Reals)


def number_of_real_roots(quadratic_coefficient, linear_coefficient, constant_coefficient):
    """Return the number of real roots: 0, 1, or 2.

    The result is based on the sign of the discriminant. We treat the
    repeated-root case (discriminant zero) as one root.
    """
    delta = discriminant(quadratic_coefficient, linear_coefficient, constant_coefficient)
    if delta > 0:
        return 2
    if delta == 0:
        return 1
    return 0


def vertex(quadratic_coefficient, linear_coefficient, constant_coefficient):
    """Return the vertex $(x, y)$ of $y = a x^2 + b x + c$.

    Parameters
    ----------
    quadratic_coefficient : int, float, or sympy expression
        The coefficient of $x^2$.
    linear_coefficient : int, float, or sympy expression
        The coefficient of $x$.
    constant_coefficient : int, float, or sympy expression
        The constant term.

    Returns
    -------
    tuple of sympy expressions
        The coordinates $(x_v, y_v)$ of the vertex.
    """
    a_value = sympy.S(quadratic_coefficient)
    b_value = sympy.S(linear_coefficient)
    c_value = sympy.S(constant_coefficient)
    x_vertex = -b_value / (2 * a_value)
    y_vertex = c_value - b_value**2 / (4 * a_value)
    return x_vertex, y_vertex
