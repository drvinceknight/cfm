"""Discrete-time Markov chains with exact arithmetic.

A discrete-time Markov chain is described by a transition matrix
$P$, where $P_{ij}$ is the probability of moving from state
$i$ to state $j$ in one step. We use ``sympy`` matrices so that
the probabilities and distributions stay exactly as rationals.
"""

import sympy as sym


def is_stochastic(transition_matrix):
    """Return ``True`` if every row of ``transition_matrix`` sums to 1.

    Parameters
    ----------
    transition_matrix : sympy.Matrix
        A square matrix of probabilities.

    Returns
    -------
    bool
        ``True`` if the matrix is row-stochastic.
    """
    for row_index in range(transition_matrix.rows):
        row_sum = sum(transition_matrix.row(row_index))
        if sym.simplify(row_sum - 1) != 0:
            return False
    return True


def n_step_distribution(initial_distribution, transition_matrix, number_of_steps):
    """Return the distribution after ``number_of_steps`` steps.

    If $\\pi_0$ is the row vector of initial probabilities and
    $P$ is the transition matrix, then the distribution after
    $n$ steps is $\\pi_0 P^n$.

    Parameters
    ----------
    initial_distribution : sympy.Matrix
        A row vector of probabilities summing to 1.
    transition_matrix : sympy.Matrix
        A square row-stochastic matrix.
    number_of_steps : int
        The number of one-step transitions to apply.

    Returns
    -------
    sympy.Matrix
        The row vector $\\pi_0 P^n$.
    """
    return initial_distribution * transition_matrix**number_of_steps


def stationary_distribution(transition_matrix):
    """Return the stationary distribution of a Markov chain.

    The stationary distribution is the row vector $\\pi$ satisfying
    $\\pi P = \\pi$ with $\\sum_i \\pi_i = 1$. We compute it as
    the (normalised) basis vector of the null space of
    $P^T - I$, which is equivalent to the left eigenvector of
    $P$ for eigenvalue $1$.

    Parameters
    ----------
    transition_matrix : sympy.Matrix
        A square row-stochastic matrix.

    Returns
    -------
    sympy.Matrix
        The stationary distribution as a row vector.
    """
    number_of_states = transition_matrix.rows
    identity_matrix = sym.eye(number_of_states)
    null_space_vectors = (transition_matrix.T - identity_matrix).nullspace()
    vector = null_space_vectors[0]
    total = sum(vector)
    normalised = vector / total
    return normalised.T
