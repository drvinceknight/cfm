---
layout: class-notes
title: "Modularisation of code"
tags: modularisation
---

After this meeting students should:

- Understand the idea of modularising code itself.
- Understand how to import a file from a file.

Show students the following code and ask them to go in breakout rooms and
discuss what it does:

    >>> def run_2_opt_algorithm(
    ...     number_of_stops,
    ...     distance_matrix,
    ...     iterations,
    ...     seed=None,
    ... ):
    ...
    ...     internal_stops = list(range(1, number_of_stops))
    ...     if seed is not None:
    ...         np.random.seed(seed)
    ...         np.random.shuffle(internal_stops)
    ...     tour = [0] + internal_stops + [0]
    ...     best_cost = sum(
    ...         distance_matrix[current_stop, next_stop]
    ...         for current_stop, next_stop in
    ...         zip(tour[:-1], tour[1:])
    ...         )
    ...     for _ in range(iterations):
    ...
    ...         two_indices = np.random.choice(range(1, number_of_stops), 2)
    ...         i, j = sorted(two_indices)
    ...
    ...         candidate_tour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
    ...
    ...         candidate_cost = sum(
    ...             distance_matrix[current_stop, next_stop]
    ...             for current_stop, next_stop in
    ...             zip(candidate_tour[:-1], candidate_tour[1:])
    ...             )
    ...
    ...         if (candidate_cost) <= best_cost:
    ...             best_cost = candidate_cost
    ...             tour = candidate_tour
    ...
    ...     return tour

## The mathematical problem considered

Ask students what the travelling sales agent problem is.

Have a discussion about it.

Consider the following 25 stops with coordinates as follows::

    >>> import numpy as np
    >>> x = np.array([13, 16, 22,  1,  4, 28,  4,  8, 10, 20, 22, 19,  5, 24,  7, 25, 25, 13, 27,  2,  7,  8, 24, 15, 25])
    >>> y = np.array([18,  6, 26, 14,  9, 10, 21, 20, 17, 20,  6, 16, 16,  1, 19,  4, 25, 18, 20, 20, 20, 15,  8,  1,  2])

We can visualise this::

    >>> import matplotlib.pyplot as plt
    >>> plt.scatter(x, y)
    <matplotlib...

A python library called `sklearn` has a lot of functionality that can be
used to look at data, for example we can get the distances here::

    >>> import sklearn.metrics.pairwise
    >>> distance_matrix = sklearn.metrics.pairwise.euclidean_distances(tuple(zip(x, y)))
    >>> distance_matrix
    array([[ 0.        , 12.36931688, ...

Show how the problem is indeed solved (copy the code above and put it in a
notebook).

We can use the above code to find a tour::

    >>> tour = run_2_opt_algorithm(number_of_stops=25, distance_matrix=distance_matrix, iterations=500, seed=0)
    >>> tour
    [0, 17, 14, 20, 7, 8, 21, 12, 6, 19, 3, 4, 11, 23, 1, 10, 13, 15, 24, 22, 5, 18, 16, 2, 9, 0]

We want to plot this tour so we need to recover the coordinates::

    >>> def plot_tour(x, y, tour):
    ...     ordered_x = x[tour]
    ...     ordered_y = y[tour]
    ...     plt.figure()
    ...     plt.scatter(x, y)
    ...     plt.plot(ordered_x, ordered_y)
    >>> plot_tour(x=x, y=y, tour=tour)

This is great but it's code that works and it is not straightforward to see
how or why it works. Let us fix that::

    >>> def get_tour(number_of_stops, seed=None):
    ...     internal_stops = list(range(1, number_of_stops))
    ...     if seed is not None:
    ...         np.random.seed(seed)
    ...         np.random.shuffle(internal_stops)
    ...     return [0] + internal_stops + [0]
    >>> def swap_cities(tour, steps):
    ...     i, j = sorted(steps)
    ...     new_tour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
    ...     return new_tour
    >>> def get_cost(tour, distance_matrix):
    ...     return sum(
    ...         distance_matrix[current_stop, next_stop]
    ...         for current_stop, next_stop in
    ...         zip(tour[:-1], tour[1:])
    ...     )

We can use this to for example get the cost of our tour::

    >>> get_cost(tour=tour, distance_matrix=distance_matrix)
    133.40828432465426

Show how the code is much cleaner now::

    >>> def run_2_opt_algorithm(
    ...     number_of_stops,
    ...     distance_matrix,
    ...     iterations,
    ...     filename=None,
    ...     seed=None,
    ... ):
    ...     tour = get_tour(number_of_stops=number_of_stops, seed=seed)
    ...     best_cost = get_cost(tour=tour, distance_matrix=distance_matrix)
    ...     for _ in range(iterations):
    ...         two_indices = np.random.choice(range(1, number_of_stops), 2)
    ...         candidate_tour = swap_cities(tour=tour, steps=two_indices)
    ...         if (cost:=get_cost(tour=candidate_tour, distance_matrix=distance_matrix)) <= best_cost:
    ...             best_cost = cost
    ...             tour = candidate_tour
    ...     return tour
    >>> tour = run_2_opt_algorithm(number_of_stops=25, distance_matrix=distance_matrix, iterations=500, seed=0)
    >>> tour
    [0, 17, 14, 20, 7, 8, 21, 12, 6, 19, 3, 4, 11, 23, 1, 10, 13, 15, 24, 22, 5, 18, 16, 2, 9, 0]

Discuss the need for docstrings.

Then put the code in `tsp.py` and show how it can be imported.

## After class communication

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I went over modularising code which is an important foundation
    of software development.

    In class we used an example of solving the travelling salesagent problem and
    you can find a different example (studying snakes and ladders) here:
    https://vknight.org/pfm/building-tools/05-modularisation/tutorial/main.html

    Please get in touch if I can assist with anything,
    Vince
