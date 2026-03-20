import tsp

import numpy as np
import matplotlib.pyplot as plt


def test_get_tour_with_no_seed():
    """
    With 4 stops the expected tour with no shuffling (ie no seed) is:

    0 -> 1 -> 2 -> 3 -> 0

    Start at 0 and go back to 0.
    """
    number_of_stops = 4
    tour = tsp.get_tour(number_of_stops=number_of_stops)
    expected_tour = [0, 1, 2, 3, 0]
    assert tour == expected_tour, f"The obtained tour is: {tour}, the expected tour is {expected_tour}"

def test_get_tour_with_seed_0():
    """
    This tests a random run of the get_tour with seed=0
    """
    number_of_stops = 4
    seed = 0
    tour = tsp.get_tour(number_of_stops=number_of_stops, seed=seed)
    expected_tour = [0, 3, 2, 1, 0]
    assert tour == expected_tour, f"The obtained tour is: {tour}, the expected tour is {expected_tour}"


def test_get_tour_with_seed_1():
    """
    This tests a random run of the get_tour with seed=0
    """
    number_of_stops = 4
    seed = 1
    tour = tsp.get_tour(number_of_stops=number_of_stops, seed=seed)
    expected_tour = [0, 1, 3, 2, 0]
    assert tour == expected_tour, f"The obtained tour is: {tour}, the expected tour is {expected_tour}"



test_get_tour_with_no_seed()
test_get_tour_with_seed_0()
test_get_tour_with_seed_1()