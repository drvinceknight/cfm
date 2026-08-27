import markov
import sympy as sym


def test_is_stochastic_accepts_valid_matrix():
    transition = sym.Matrix(
        [
            [sym.Rational(7, 10), sym.Rational(3, 10)],
            [sym.Rational(4, 10), sym.Rational(6, 10)],
        ]
    )
    assert markov.is_stochastic(transition)


def test_is_stochastic_rejects_invalid_matrix():
    bad_matrix = sym.Matrix(
        [
            [sym.Rational(7, 10), sym.Rational(2, 10)],
            [sym.Rational(4, 10), sym.Rational(6, 10)],
        ]
    )
    assert not markov.is_stochastic(bad_matrix)


def test_one_step_distribution_from_first_state():
    initial = sym.Matrix([[1, 0]])
    transition = sym.Matrix(
        [
            [sym.Rational(7, 10), sym.Rational(3, 10)],
            [sym.Rational(4, 10), sym.Rational(6, 10)],
        ]
    )
    result = markov.n_step_distribution(initial, transition, 1)
    expected = sym.Matrix([[sym.Rational(7, 10), sym.Rational(3, 10)]])
    assert result == expected


def test_zero_steps_returns_initial_distribution():
    initial = sym.Matrix([[sym.Rational(1, 2), sym.Rational(1, 2)]])
    transition = sym.Matrix(
        [
            [sym.Rational(7, 10), sym.Rational(3, 10)],
            [sym.Rational(4, 10), sym.Rational(6, 10)],
        ]
    )
    result = markov.n_step_distribution(initial, transition, 0)
    assert result == initial


def test_stationary_distribution_of_two_state_chain():
    transition = sym.Matrix(
        [
            [sym.Rational(7, 10), sym.Rational(3, 10)],
            [sym.Rational(4, 10), sym.Rational(6, 10)],
        ]
    )
    result = markov.stationary_distribution(transition)
    expected = sym.Matrix([[sym.Rational(4, 7), sym.Rational(3, 7)]])
    assert result == expected


def test_stationary_distribution_satisfies_balance():
    transition = sym.Matrix(
        [
            [sym.Rational(7, 10), sym.Rational(3, 10)],
            [sym.Rational(4, 10), sym.Rational(6, 10)],
        ]
    )
    stationary = markov.stationary_distribution(transition)
    assert stationary * transition == stationary


def test_high_power_converges_to_stationary():
    initial = sym.Matrix([[1, 0]])
    transition = sym.Matrix(
        [
            [sym.Rational(7, 10), sym.Rational(3, 10)],
            [sym.Rational(4, 10), sym.Rational(6, 10)],
        ]
    )
    long_run = markov.n_step_distribution(initial, transition, 50)
    stationary = markov.stationary_distribution(transition)
    error = max(abs(float(long_run[0, index] - stationary[0, index])) for index in range(2))
    assert error < 1e-10


test_is_stochastic_accepts_valid_matrix()
test_is_stochastic_rejects_invalid_matrix()
test_one_step_distribution_from_first_state()
test_zero_steps_returns_initial_distribution()
test_stationary_distribution_of_two_state_chain()
test_stationary_distribution_satisfies_balance()
test_high_power_converges_to_stationary()
