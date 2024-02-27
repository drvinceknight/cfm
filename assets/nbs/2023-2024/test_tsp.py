import numpy as np
import matplotlib.pyplot as plt

import tsp


def test_get_tour_with_no_seed():
    number_of_stops = 4
    tour = tsp.get_tour(number_of_stops=number_of_stops)
    assert tour == [0, 1, 2, 3, 0], f"The value of tour is {tour}"


def test_get_tour_with_no_seed_and_6_stops():
    number_of_stops = 6
    tour = tsp.get_tour(number_of_stops=number_of_stops)
    assert tour == [0, 1, 2, 3, 4, 5, 0], f"The value of tour is {tour}"



def test_get_tour_with_seed_5_and_6_stops():
    number_of_stops = 6
    seed = 5
    tour = tsp.get_tour(number_of_stops=number_of_stops, seed=seed)
    assert len(tour) == number_of_stops + 1
    assert tour == [0, 5, 1, 2, 3, 4, 0], f"The value of tour is {tour}"


def test_get_tour_with_seed_10_and_6_stops():
    number_of_stops = 6
    seed = 10
    tour = tsp.get_tour(number_of_stops=number_of_stops, seed=seed)
    assert len(tour) == number_of_stops + 1
    assert tour == [0, 3, 4, 1, 5, 2, 0], f"The value of tour is {tour}"

def test_swap_cities():
    tour = [0, 1, 3, 2, 4, 0]
    steps = 4, 1
    new_tour = tsp.swap_cities(tour=tour, steps=steps)
    assert new_tour == [0, 4, 2, 3, 1, 0], f"Obtained tour was: {new_tour}"


def test_plot_tour():
    """
    This tests the plotting functionality.

    NOTE it only tests that the code is run and no unexpected output or
    errors are raised
    """
    x = np.array((2, 3))
    y = np.array((2, 3))
    tour = np.array((0, 1, 0))
    plot = tsp.plot_tour(tour=tour, x=x, y=y)
    assert plot is None


test_get_tour_with_no_seed()
test_get_tour_with_no_seed_and_6_stops()
test_get_tour_with_seed_5_and_6_stops()
test_get_tour_with_seed_10_and_6_stops()
test_swap_cities()
test_plot_tour()