Testing
=======

First meeting
-------------

After this meeting students should:

- Understand how assertion statements work
- Understand how to write unit tests using assert statements
- Understand how to write tests for documentation


Testing software
----------------

Discuss how we will write automated tests for the `tsp` library we wrote in the
first section.

Writing the unit tests
**********************

Write the following in a `test_tsp.py` file::

    import numpy as np
    import matplotlib.pyplot as plt

    import tsp

    def test_get_tour_with_no_seed():
        number_of_stops = 4
        tour = tsp.get_tour(number_of_stops=number_of_stops)
        assert np.array_equal(tour, np.array([0, 1, 2, 3, 0]))

    def test_get_tour_with_seed_0():
        number_of_stops = 4
        seed = 0
        tour = tsp.get_tour(number_of_stops=number_of_stops, seed=seed)
        assert np.array_equal(tour, np.array([0, 3, 2, 1, 0])), f"Obtained output is {tour}"

    def test_get_tour_with_seed_1():
        number_of_stops = 4
        seed = 1
        tour = tsp.get_tour(number_of_stops=number_of_stops, seed=seed)
        assert np.array_equal(tour, np.array([0, 1, 3, 2, 0])), f"Obtained output is {tour}"


    def test_swap_cities():
        tour = [0, 1, 3, 2, 4, 0]
        steps = (4, 1)
        new_tour = tsp.swap_cities(tour=tour, steps=steps)
        assert new_tour == [0, 4, 2, 3, 1, 0], f"Obtained output is {new_tour}"


    def test_get_cost():
        distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))
        tour = [0, 1, 2, 3, 0]
        cost = tsp.get_cost(tour=tour, distance_matrix=distance_matrix)
        assert cost == 24


    def test_run_2_opt_algorithm_with_seed_0():
        distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))
        number_of_stops = 4
        seed = 0
        iterations = 50
        tour = tsp.run_2_opt_algorithm(number_of_stops=number_of_stops,
                distance_matrix=distance_matrix, seed=seed, iterations=iterations)
        assert tour == [0, 2, 3, 1, 0], f"Obtained output is {tour}"

    def test_run_2_opt_algorithm_with_seed_1():
        distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))
        number_of_stops = 4
        seed = 1
        iterations = 50
        tour = tsp.run_2_opt_algorithm(number_of_stops=number_of_stops,
                distance_matrix=distance_matrix, seed=seed, iterations=iterations)
        assert tour == [0, 2, 1, 3, 0], f"Obtained output is {tour}"

    def test_plot_tour():
        x = np.array([2, 3])
        y = np.array([2, 3])
        tour = np.array([0, 1, 0])
        plot = tsp.plot_tour(x=x, y=y, tour=tour)
        assert plot is None

    test_get_tour_with_no_seed()
    test_get_tour_with_seed_0()
    test_get_tour_with_seed_1()
    test_swap_cities()
    test_get_cost()
    test_run_2_opt_algorithm_with_seed_0()
    test_run_2_opt_algorithm_with_seed_1()
    test_plot_tour()


Run the above tests by running::

    $ python test_tsp.py

Depending on time now discuss refactoring some of the code. For example:

- Modify `swap_cities` to be called `swap_steps` as this name is more generic.
- Possibly modify `swap_cities`/`swap_steps` so that it can handle numpy array
  outputs.

At each step modify the source code and then modify the tests.

Discuss importance of tests as a debugging tool.

Testing the documentation
*************************

Modify the documentation in the `README.md` file to use doctests::


    # TSP

    A library for solving instances of the travelling sales agent problem

    ## Tutorial

    In this tutorial we will see how to use `tsp` to solve instances of the
    [Travelling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

    Assuming we have the following distance matrix:

    ```python
    >>> import numpy as np
    >>> distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))

    ```

    We can obtain a tour using the following:

    ```python
    >>> import tsp
    >>> tour = tsp.run_2_opt_algorithm(number_of_stops=4, distance_matrix=distance_matrix, iterations=1000, seed=0)
    >>> tour
    [0, 3, 1, 2, 0]

    ```

    The `tsp` library includes further functionality which you can read in the
    How To guides.

Run the doc tests by typing::

    $ python -m doctest README.md


Discussion around 3 pillars of software development
***************************************************

Specifically look at diagram in further information section:
https://vknight.org/pfm/building-tools/07-testing/why/main.html#how-are-modularisation-documentation-and-testing-related

After class email
-----------------

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I went over automated testing.

    In class we wrote unit and doctests for the Travelling Salesagent Problem.
    You can find a different example (studying snakes and ladders) here:
    https://vknight.org/pfm/building-tools/07-testing/tutorial/main.html

    Please get in touch if I can assist with anything,
    Vince
