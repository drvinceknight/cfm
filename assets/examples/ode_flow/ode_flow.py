"""Solving and sampling initial value problems for first-order ODEs.

We use ``sympy.dsolve`` to solve initial value problems of the form
$y'(t) = f(t, y(t))$ with $y(t_0) = y_0$, and we sample the resulting
symbolic solution at a list of times to give a list of floats that can
be plotted or compared with a numerical reference.
"""

import sympy as sym


def solve_initial_value_problem(
    right_hand_side, time_variable, function, initial_time, initial_value
):
    """Return the symbolic solution to a first-order initial value problem.

    Solves $y'(t) = f(t, y(t))$ subject to $y(t_0) = y_0$.

    Parameters
    ----------
    right_hand_side : sympy.Expr
        The right-hand side $f(t, y(t))$ as a symbolic expression in
        ``time_variable`` and ``function(time_variable)``.
    time_variable : sympy.Symbol
        The independent variable $t$.
    function : sympy.Function
        The unknown function $y$.
    initial_time : sympy.Expr or numeric
        The initial time $t_0$.
    initial_value : sympy.Expr or numeric
        The value of the function at the initial time, $y_0$.

    Returns
    -------
    sympy.Expr
        The right-hand side of the symbolic solution.
    """
    equation = sym.Eq(function(time_variable).diff(time_variable), right_hand_side)
    solution = sym.dsolve(
        equation,
        function(time_variable),
        ics={function(initial_time): initial_value},
    )
    return solution.rhs


def trajectory(solution_expression, time_variable, sample_times):
    """Sample a symbolic solution at the given times.

    Parameters
    ----------
    solution_expression : sympy.Expr
        The symbolic solution as returned by
        :func:`solve_initial_value_problem`.
    time_variable : sympy.Symbol
        The independent variable $t$.
    sample_times : iterable of numeric
        The times at which to evaluate the solution.

    Returns
    -------
    list of float
        The values of the solution at each sample time.
    """
    return [float(solution_expression.subs({time_variable: time})) for time in sample_times]


def verify_solution(solution_expression, right_hand_side, time_variable, function):
    """Return ``True`` if ``solution_expression`` satisfies the ODE.

    We substitute the candidate solution into the right-hand side and
    compare with the derivative of the candidate solution; the ODE is
    satisfied when the difference simplifies to zero.

    Parameters
    ----------
    solution_expression : sympy.Expr
        The candidate solution.
    right_hand_side : sympy.Expr
        The right-hand side $f(t, y(t))$.
    time_variable : sympy.Symbol
        The independent variable $t$.
    function : sympy.Function
        The unknown function $y$.

    Returns
    -------
    bool
        ``True`` if the candidate solves the ODE.
    """
    derivative = sym.diff(solution_expression, time_variable)
    right_hand_side_at_solution = right_hand_side.subs(function(time_variable), solution_expression)
    return sym.simplify(derivative - right_hand_side_at_solution) == 0
