import newton
import sympy as sym


def test_newton_step_on_quadratic():
    """
    Check one Newton step on f(x) = x ^ 2 - 2, starting at x = 1.

    The derivative is 2 x, so the step gives

        x - (x ^ 2 - 2) / (2 x) = (x ^ 2 + 2) / (2 x).

    At x = 1 this is 3 / 2.
    """
    x = sym.Symbol("x")
    next_value = newton.newton_step(x**2 - 2, x, sym.S(1))
    expected_next_value = sym.S(3) / 2
    assert next_value == expected_next_value, (
        f"Expected {expected_next_value}, obtained {next_value}."
    )


def test_newton_step_on_cubic():
    """
    Check one Newton step on f(x) = x ^ 3 - 8, starting at x = 1.

    The derivative is 3 x ^ 2, so the step gives

        x - (x ^ 3 - 8) / (3 x ^ 2) = (2 x ^ 3 + 8) / (3 x ^ 2).

    At x = 1 this is 10 / 3.
    """
    x = sym.Symbol("x")
    next_value = newton.newton_step(x**3 - 8, x, sym.S(1))
    expected_next_value = sym.S(10) / 3
    assert next_value == expected_next_value, (
        f"Expected {expected_next_value}, obtained {next_value}."
    )


def test_iterate_returns_correct_length():
    """
    Check that ``iterate`` returns ``number_of_iterations + 1`` values.

    Starting at x = 1 and taking 4 steps on f(x) = x ^ 2 - 2, the result
    should contain five entries (the initial value and four iterates).
    """
    x = sym.Symbol("x")
    iterates = newton.iterate(x**2 - 2, x, sym.S(1), number_of_iterations=4)
    assert len(iterates) == 5, f"Expected 5 iterates, obtained {len(iterates)}."


def test_iterate_starts_at_initial_value():
    """
    The first entry returned by ``iterate`` is the initial value itself.
    """
    x = sym.Symbol("x")
    initial_value = sym.S(2)
    iterates = newton.iterate(x**2 - 2, x, initial_value, number_of_iterations=3)
    assert iterates[0] == initial_value, (
        f"Expected first iterate {initial_value}, obtained {iterates[0]}."
    )


def test_find_root_recovers_sqrt_two():
    """
    Newton-Raphson on f(x) = x ^ 2 - 2 from x = 1 should converge to
    sqrt(2). We check that the final iterate matches to within the
    convergence tolerance.
    """
    x = sym.Symbol("x")
    root, _ = newton.find_root(
        x**2 - 2,
        x,
        sym.S(1),
        tolerance=10**-10,
        maximum_iterations=50,
    )
    expected_root = sym.sqrt(2)
    assert abs(float(root - expected_root)) < 10**-10, (
        f"Expected sqrt(2) ~ {float(expected_root)}, obtained {float(root)}."
    )


def test_find_root_terminates_within_few_iterations():
    """
    Newton-Raphson on a smooth function with a good starting point should
    converge quickly. We check that fewer than 20 iterations suffice for
    f(x) = x ^ 2 - 2 starting at x = 1 with tolerance 10 ^ -10.
    """
    x = sym.Symbol("x")
    _, iterations = newton.find_root(
        x**2 - 2,
        x,
        sym.S(1),
        tolerance=10**-10,
        maximum_iterations=50,
    )
    assert iterations < 20, f"Expected fewer than 20 iterations, took {iterations}."


def test_find_root_respects_maximum_iterations():
    """
    With a very small ``maximum_iterations`` budget, ``find_root`` should
    stop early and return the iterate it has reached.
    """
    x = sym.Symbol("x")
    _, iterations = newton.find_root(
        x**2 - 2,
        x,
        sym.S(1),
        tolerance=10**-50,
        maximum_iterations=3,
    )
    assert iterations == 3, f"Expected to stop at the iteration cap of 3, took {iterations}."


test_newton_step_on_quadratic()
test_newton_step_on_cubic()
test_iterate_returns_correct_length()
test_iterate_starts_at_initial_value()
test_find_root_recovers_sqrt_two()
test_find_root_terminates_within_few_iterations()
test_find_root_respects_maximum_iterations()
