import sympy as sym


def newton_step(expression, variable, current_value):
    """
    Apply one Newton-Raphson step to ``expression`` at ``current_value``.

    Given an expression $f$ and a variable $x$, with current value
    $x_n$, return

    $$
        x_{n + 1} = x_n - \\frac{f(x_n)}{f'(x_n)}.
    $$

        Parameters
    ----------
    expression : sympy.Expr
        the symbolic expression $f(x)$
    variable : sympy.Symbol
        the symbol that appears in ``expression``
    current_value : sympy.Expr or numeric
        the current iterate $x_n$, preferably symbolic (use ``sympy.S``)

    Returns
    -------
    sympy.Expr
        the next iterate $x_{n + 1}$ as a symbolic value
    """
    derivative = sym.diff(expression, variable)
    function_value = expression.subs({variable: current_value})
    derivative_value = derivative.subs({variable: current_value})
    return current_value - function_value / derivative_value


def iterate(expression, variable, initial_value, number_of_iterations):
    """
    Apply ``number_of_iterations`` Newton-Raphson steps to ``expression``.

    Starting at ``initial_value``, return the list of iterates
    $x_0, x_1, \\dots, x_N$, where $N$ is ``number_of_iterations``.

        Parameters
    ----------
    expression : sympy.Expr
        the symbolic expression $f(x)$
    variable : sympy.Symbol
        the symbol that appears in ``expression``
    initial_value : sympy.Expr or numeric
        the starting iterate $x_0$
    number_of_iterations : int
        the number of Newton steps to take

    Returns
    -------
    list
        the list of $N + 1$ iterates
    """
    iterates = [initial_value]
    for _ in range(number_of_iterations):
        iterates.append(newton_step(expression, variable, iterates[-1]))
    return iterates


def find_root(expression, variable, initial_value, tolerance, maximum_iterations):
    """
    Iterate Newton-Raphson until the change is within ``tolerance``.

    Take Newton steps starting at ``initial_value``. Stop as soon as two
    successive iterates differ by less than ``tolerance`` (in absolute
    value), or after ``maximum_iterations`` steps have been taken.

        Parameters
    ----------
    expression : sympy.Expr
        the symbolic expression $f(x)$
    variable : sympy.Symbol
        the symbol that appears in ``expression``
    initial_value : sympy.Expr or numeric
        the starting iterate $x_0$
    tolerance : float
        the convergence tolerance on $|x_{n + 1} - x_n|$
    maximum_iterations : int
        the maximum number of iterations to take

    Returns
    -------
    tuple
        the pair ``(root, iterations)``, where ``root`` is the final
        iterate and ``iterations`` is the number of steps taken
    """
    current_value = initial_value
    for iteration in range(1, maximum_iterations + 1):
        next_value = newton_step(expression, variable, current_value)
        if abs(float(next_value - current_value)) < tolerance:
            return next_value, iteration
        current_value = next_value
    return current_value, maximum_iterations
