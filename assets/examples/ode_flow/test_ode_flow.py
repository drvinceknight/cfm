import ode_flow
import sympy as sym


def test_solve_exponential_growth():
    time = sym.Symbol("t")
    y = sym.Function("y")
    solution = ode_flow.solve_initial_value_problem(y(time), time, y, 0, 1)
    assert sym.simplify(solution - sym.exp(time)) == 0


def test_solve_constant_growth():
    time = sym.Symbol("t")
    y = sym.Function("y")
    solution = ode_flow.solve_initial_value_problem(1, time, y, 0, 0)
    assert sym.simplify(solution - time) == 0


def test_solve_with_explicit_time_dependence():
    time = sym.Symbol("t")
    y = sym.Function("y")
    solution = ode_flow.solve_initial_value_problem(2 * time, time, y, 0, 0)
    assert sym.simplify(solution - time**2) == 0


def test_solve_with_non_zero_initial_time():
    time = sym.Symbol("t")
    y = sym.Function("y")
    solution = ode_flow.solve_initial_value_problem(y(time), time, y, 1, sym.exp(1))
    assert sym.simplify(solution - sym.exp(time)) == 0


def test_trajectory_length_matches_samples():
    time = sym.Symbol("t")
    solution = sym.exp(time)
    values = ode_flow.trajectory(solution, time, [0, 1, 2, 3])
    assert len(values) == 4


def test_trajectory_recovers_known_values():
    time = sym.Symbol("t")
    solution = time**2
    values = ode_flow.trajectory(solution, time, [0, 1, 2, 3])
    assert values == [0.0, 1.0, 4.0, 9.0]


def test_verify_solution_accepts_correct_solution():
    time = sym.Symbol("t")
    y = sym.Function("y")
    assert ode_flow.verify_solution(sym.exp(time), y(time), time, y)


def test_verify_solution_rejects_incorrect_solution():
    time = sym.Symbol("t")
    y = sym.Function("y")
    assert not ode_flow.verify_solution(time, y(time), time, y)


test_solve_exponential_growth()
test_solve_constant_growth()
test_solve_with_explicit_time_dependence()
test_solve_with_non_zero_initial_time()
test_trajectory_length_matches_samples()
test_trajectory_recovers_known_values()
test_verify_solution_accepts_correct_solution()
test_verify_solution_rejects_incorrect_solution()
