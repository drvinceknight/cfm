Documentation
=============

First meeting
-------------

After this meeting students should:

- Understand the general structure required for documentation
- Understand how to write further markdown


Writing documentation
---------------------

Discuss how we will write documentation for the `tsp` library we wrote in the
first section.

There are 4 components for documentation:

1. Tutorial
2. How to guide
3. Reference
4. Discussion

Ask students what they think the purpose of each of these are. Ask them to
discuss amongst themselves.

Say that we will address this after writing the documentation.

Writing the tutorial
********************

Open a markdown file (in the same location as the :code:`tsp.py` file) and call it
:code:`README.md`.

Write the following::

    # TSP

    A library for solving instances of the travelling sales agent problem

    ## Tutorial

    In this tutorial we will see how to use `tsp` to solve instances of the
    [Travelling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

    Assuming we have the following distance matrix:

    ```python
    import numpy as np

    distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))
    ```

    We can obtain a tour using the following:

    ```python
    import tsp

    tour = tsp.run_2_opt_algorithm(number_of_stops=4, distance_matrix=distance_matrix, iterations=1000, seed=0)
    ```

    We can see the tour here:

    ```python
    tour
    ```

    This gives:

    ```
    [0, 3, 1, 2, 0]
    ```

    The `tsp` library includes further functionality which you can read in the
    How To guides.

    ## How to guides

    ### How to obtain a basic tour

    To obtain a basic tour, we use the `tsp.get_tour` function:

    ```python
    import tsp

    tsp.get_tour(number_of_stops=5)
    ```

    This gives

    ```
    [0, 1, 2, 3, 4, 0]
    ```

    If we pass a random seed this will also shuffle the interior stops (in a
    reproducible manner):

    ```python
    tsp.get_tour(number_of_stops=5, seed=0)
    ```

    This gives:

    ```
    [0, 3, 4, 2, 1, 0]
    ```

    ### How to swap two spots

    To swap two cities for a given tour, we use the `tsp.swap_cities` function:

    ```python
    tour = [0, 1, 2, 3, 4, 5, 0]
    tsp_swap_cities(tour=tour, indices=(2, 4))
    ```

    This gives:

    ```
    [0, 1, 4, 3, 2, 5, 0]
    ```

    ### How to get the cost of a tour

    To calculate the cost of a given tour, we use the `tsp.get_cost` function:

    ```python
    distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))
    tour = [0, 1, 2, 3, 0]
    tsp.get_cost(tour=tour, distance_matrix=distance_matrix)
    ```

    which gives:

    ```
    24
    ```

    ### How to plot a tour

    To plot a tour we use the `tsp.plot_tour` function:

    ```python
    xs = (0, 1, 1, 2.5)
    ys = (0, 5, 1, 3)
    tour = [0, 1, 3, 2, 0]
    tsp.plot_tour(x=xs, y=ys, tour=tour)
    ```

    This gives the following image:

    ![](./how-to.svg)

    ### How to use the 2-opt algorithm

    To run the full algorithm, we use the
    `tsp.run_2_opt_algorithm` function:

    ```python
    distance_matrix = np.array(((0, 5, 2, 9), (5, 0, 3, 1), (2, 3, 0, 7), (9, 1, 7, 0)))
    tour = tsp.run_2_opt_algorithm(number_of_stops=4, distance_matrix=distance_matrix, iterations=1000, seed=0)
    tour
    ```

    This gives:

    ```
    [0, 3, 1, 2, 0]
    ```

    ## Explanations

    This software implements the 2-opt algorithm for the travelling sales agent
    problem.

    ### The TSP

    As an example, if we consider three cities with the following matrix
    defining their distances between them:

    $$
        \begin{pmatrix}
            0 & 4 & 1\\
            4 & 0 & 2\\
            9 & 2 & 0
        \end{pmatrix}
    $$

    Note that the distance matrix is not symmetric, it is a lot further to go
    from the 3rd to the 1st city (9) than to go from the 1st to the 3rd (1)

    If a tour starts **and** finishes at the first city there are in fact 2
    possibilities:

    $$T \in \{(0, 1, 2, 0), (0, 2, 1, 0)\}$$

    The cost $c(t)$ for $t\in T$ of these tour tours is taken to be the total
    distance travelled:

    1. For $t=(0, 1, 2, 0)$ we have $c(t)=4 + 2 + 9=15$
    2. For $t=(0, 2, 1, 0)$ we have $c(t)=1 + 2 + 2=5$

    As the size of our problem grows the complexity of finding the optimal tour
    grows in complexity. In fact this problem is NP-hard, which puts it in a
    class of problems for which a general solution cannot be obtained
    efficiently for any given sized problem.

    ## The 2-opt algorithm

    One solution approach of this is the 2-opt algorithm which is what is
    implemented in this software.

    The 2-opt algorithm is an example of a neighbourhood search algorithm which
    means that it iteratively improves a given solution by looking in
    at other candidates near it.

    The 2-opt algorithm does this by randomly choosing two stops in a tour, and
    swapping the order between them. Essentially picking stop $n$ and stop $n +
    k$ and reversing the order. Thus the new candidate would visit the same
    stops as the original tour, until it got to stop $n$, when it would instead
    go to stop $n + k$ and reverse its way back to stop $n$.

    Once this candidate tour is obtained the cost is evaluated and if it is good
    it is accepted as the new solution.

    This has the effect of essentially untangling a given tour.

    ## Reference

    ### List of functionality

    This software implements 5 functions:

    1. `plot_tour`
    2. `get_tour`
    3. `swap_cities`
    4. `get_cost`
    5. `run_2_opt_algorithm`

    ### Bibliography

    The wikipedia page on the TSP offers good background reading:
    https://en.wikipedia.org/wiki/Travelling_salesman_problem

    The following text is a recommended text on neighbourhood search algorithms:

    > Aarts, Emile, Emile HL Aarts, and Jan Karel Lenstra, eds. Local search in
    > combinatorial optimization. Princeton University Press, 2003.



After class email
-----------------

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I went over documenting code.

    In class we documented the travelling salesagent problem code
    you can find a different example (studying snakes and ladders) here:
    https://vknight.org/pfm/building-tools/06-documentation/tutorial/main.html

    Please get in touch if I can assist with anything,
    Vince
