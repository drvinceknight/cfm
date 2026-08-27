import statistics as st

import stats_from_scratch


def test_mean_matches_statistics_module():
    values = [1, 2, 3, 4, 5, 6, 7]
    assert stats_from_scratch.mean(values) == st.mean(values)


def test_mean_of_constant_sequence():
    assert stats_from_scratch.mean([4, 4, 4, 4]) == 4


def test_median_of_odd_length_sequence():
    assert stats_from_scratch.median([1, 2, 3, 4, 5]) == 3


def test_median_of_even_length_sequence():
    assert stats_from_scratch.median([1, 2, 3, 4]) == 2.5


def test_median_matches_statistics_module():
    values = [3, 1, 4, 1, 5, 9, 2, 6]
    assert stats_from_scratch.median(values) == st.median(values)


def test_population_standard_deviation_matches_statistics_module():
    values = [1, 2, 3, 4, 5, 6]
    assert abs(stats_from_scratch.population_standard_deviation(values) - st.pstdev(values)) < 1e-12


def test_sample_standard_deviation_matches_statistics_module():
    values = [2, 4, 4, 4, 5, 5, 7, 9]
    assert abs(stats_from_scratch.sample_standard_deviation(values) - st.stdev(values)) < 1e-12


def test_quartiles_match_statistics_module():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ours = stats_from_scratch.quartiles(values)
    theirs = tuple(st.quantiles(values, n=4))
    assert all(abs(ours[index] - theirs[index]) < 1e-12 for index in range(len(ours)))


def test_quartiles_known_small_example():
    values = [1, 2, 3, 4, 5]
    quartile_one, quartile_two, quartile_three = stats_from_scratch.quartiles(values)
    assert (quartile_one, quartile_two, quartile_three) == (1.5, 3.0, 4.5)


test_mean_matches_statistics_module()
test_mean_of_constant_sequence()
test_median_of_odd_length_sequence()
test_median_of_even_length_sequence()
test_median_matches_statistics_module()
test_population_standard_deviation_matches_statistics_module()
test_sample_standard_deviation_matches_statistics_module()
test_quartiles_match_statistics_module()
test_quartiles_known_small_example()
