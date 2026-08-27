import binomial


def test_pmf_at_zero_for_fair_coin():
    assert abs(binomial.pmf(0, 10, 0.5) - 1 / 1024) < 1e-12


def test_pmf_at_mode_for_fair_coin():
    assert abs(binomial.pmf(5, 10, 0.5) - 252 / 1024) < 1e-12


def test_pmf_sums_to_one_over_all_outcomes():
    total = sum(binomial.pmf(value, 10, 0.3) for value in range(11))
    assert abs(total - 1) < 1e-12


def test_cdf_at_largest_outcome_is_one():
    assert abs(binomial.cdf(10, 10, 0.3) - 1) < 1e-12


def test_cdf_is_monotone():
    values = [binomial.cdf(value, 10, 0.3) for value in range(11)]
    assert all(values[index] <= values[index + 1] for index in range(len(values) - 1))


def test_mean_of_fair_coin_is_half_trials():
    assert binomial.mean(10, 0.5) == 5.0


def test_variance_of_fair_coin():
    assert binomial.variance(10, 0.5) == 2.5


def test_simulate_returns_correct_length():
    samples = binomial.simulate(10, 0.5, 100, seed=0)
    assert len(samples) == 100


def test_simulate_values_are_in_range():
    samples = binomial.simulate(10, 0.5, 100, seed=1)
    assert all(0 <= value <= 10 for value in samples)


def test_simulated_mean_is_close_to_theoretical():
    samples = binomial.simulate(20, 0.5, 5000, seed=42)
    empirical_mean = sum(samples) / len(samples)
    assert abs(empirical_mean - 10) < 0.3


test_pmf_at_zero_for_fair_coin()
test_pmf_at_mode_for_fair_coin()
test_pmf_sums_to_one_over_all_outcomes()
test_cdf_at_largest_outcome_is_one()
test_cdf_is_monotone()
test_mean_of_fair_coin_is_half_trials()
test_variance_of_fair_coin()
test_simulate_returns_correct_length()
test_simulate_values_are_in_range()
test_simulated_mean_is_close_to_theoretical()
