from fractions import Fraction

import dice


def test_roll_returns_the_requested_number_of_dice():
    result = dice.roll(5, seed=0)
    assert len(result) == 5


def test_roll_values_are_in_range():
    result = dice.roll(50, sides=6, seed=1)
    assert all(1 <= face <= 6 for face in result)


def test_roll_with_seed_is_reproducible():
    first = dice.roll(10, seed=42)
    second = dice.roll(10, seed=42)
    assert first == second


def test_simulate_sums_returns_correct_length():
    sums = dice.simulate_sums(2, 100, seed=0)
    assert len(sums) == 100


def test_simulate_sums_values_are_in_range():
    sums = dice.simulate_sums(2, 100, sides=6, seed=0)
    assert all(2 <= total <= 12 for total in sums)


def test_empirical_distribution_sums_to_one():
    samples = [2, 3, 3, 4, 4, 4, 5]
    distribution = dice.empirical_distribution(samples)
    assert abs(sum(distribution.values()) - 1) < 1e-12


def test_theoretical_distribution_for_one_die_is_uniform():
    distribution = dice.theoretical_distribution(1, sides=6)
    assert distribution == {face: Fraction(1, 6) for face in range(1, 7)}


def test_theoretical_distribution_for_two_dice_sums_to_one():
    distribution = dice.theoretical_distribution(2, sides=6)
    assert sum(distribution.values()) == 1


def test_theoretical_distribution_for_two_dice_known_values():
    distribution = dice.theoretical_distribution(2, sides=6)
    assert distribution[2] == Fraction(1, 36)
    assert distribution[7] == Fraction(6, 36)
    assert distribution[12] == Fraction(1, 36)


def test_summary_statistics_on_known_data():
    samples = [2, 3, 4, 5, 6]
    mean, median, sample_standard_deviation = dice.summary_statistics(samples)
    assert mean == 4
    assert median == 4
    assert abs(sample_standard_deviation - 1.5811388300841898) < 1e-10


test_roll_returns_the_requested_number_of_dice()
test_roll_values_are_in_range()
test_roll_with_seed_is_reproducible()
test_simulate_sums_returns_correct_length()
test_simulate_sums_values_are_in_range()
test_empirical_distribution_sums_to_one()
test_theoretical_distribution_for_one_die_is_uniform()
test_theoretical_distribution_for_two_dice_sums_to_one()
test_theoretical_distribution_for_two_dice_known_values()
test_summary_statistics_on_known_data()
