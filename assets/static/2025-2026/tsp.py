"""
This is source code for the tsp library...
"""
import numpy as np
import matplotlib.pyplot as plt

def plot_tour(x, y, tour):
    ordered_x = x[tour]
    ordered_y = y[tour]
    plt.figure()
    plt.scatter(x, y)
    plt.plot(ordered_x, ordered_y)


def get_tour(number_of_stops, seed=None):
    internal_stops = list(range(1, number_of_stops))
    if seed is not None:
        np.random.seed(seed)
        np.random.shuffle(internal_stops)
    return [0] + internal_stops + [0]
def swap_cities(tour, steps):
    i, j = sorted(steps)
    new_tour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
    return new_tour
def get_cost(tour, distance_matrix):
    return sum(
        distance_matrix[current_stop, next_stop]
        for current_stop, next_stop in
        zip(tour[:-1], tour[1:])
    )

def run_2_opt_algorithm(
    number_of_stops,
    distance_matrix,
    iterations,
    filename=None,
    seed=None,
):
    tour = get_tour(number_of_stops=number_of_stops, seed=seed)
    best_cost = get_cost(tour=tour, distance_matrix=distance_matrix)
    for _ in range(iterations):
        two_indices = np.random.choice(range(1, number_of_stops), 2)
        candidate_tour = swap_cities(tour=tour, steps=two_indices)
        if (cost:=get_cost(tour=candidate_tour, distance_matrix=distance_matrix)) <= best_cost:
            best_cost = cost
            tour = candidate_tour
    return tour