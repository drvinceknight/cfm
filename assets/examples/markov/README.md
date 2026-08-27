# markov

A small Python library for working with finite, discrete-time Markov
chains. The chain is described by its transition matrix, and the
library returns the distribution after a given number of steps and the
stationary distribution.

## Tutorial

We are going to study the two-state chain with transition matrix

\[
    P = \begin{pmatrix} 7/10 & 3/10 \\ 4/10 & 6/10 \end{pmatrix}.
\]

We start by importing the library and building the matrix:

```python
>>> import sympy as sym
>>> import markov
>>> transition = sym.Matrix([
...     [sym.Rational(7, 10), sym.Rational(3, 10)],
...     [sym.Rational(4, 10), sym.Rational(6, 10)],
... ])

```

We first check that the matrix is stochastic, that is, every row sums
to 1:

```python
>>> markov.is_stochastic(transition)
True

```

Starting deterministically in state 0, the distribution after one step
is the first row of \(P\):

```python
>>> initial = sym.Matrix([[1, 0]])
>>> markov.n_step_distribution(initial, transition, 1)
Matrix([[7/10, 3/10]])

```

The chain has a stationary distribution \(\pi = (4/7, 3/7)\):

```python
>>> markov.stationary_distribution(transition)
Matrix([[4/7, 3/7]])

```

## How to guide

### How to check that a matrix is row-stochastic

```python
>>> import sympy as sym
>>> import markov
>>> markov.is_stochastic(
...     sym.Matrix([[sym.Rational(1, 2), sym.Rational(1, 2)], [0, 1]])
... )
True

```

### How to apply the chain for several steps

```python
>>> import sympy as sym
>>> import markov
>>> initial = sym.Matrix([[1, 0]])
>>> transition = sym.Matrix([
...     [sym.Rational(7, 10), sym.Rational(3, 10)],
...     [sym.Rational(4, 10), sym.Rational(6, 10)],
... ])
>>> markov.n_step_distribution(initial, transition, 2)
Matrix([[61/100, 39/100]])

```

### How to compute the stationary distribution

```python
>>> import sympy as sym
>>> import markov
>>> transition = sym.Matrix([
...     [sym.Rational(7, 10), sym.Rational(3, 10)],
...     [sym.Rational(4, 10), sym.Rational(6, 10)],
... ])
>>> markov.stationary_distribution(transition)
Matrix([[4/7, 3/7]])

```

## Discussion

A discrete-time Markov chain on a finite state space is described by a
row-stochastic transition matrix \(P\), where \(P_{ij}\) is the
probability of moving from state \(i\) to state \(j\) in one step. The
key linear-algebraic fact is that if \(\pi_0\) is the row vector of
initial probabilities, then the distribution after \(n\) steps is
\(\pi_0 P^n\).

A stationary distribution is a row vector \(\pi\) such that
\(\pi P = \pi\), or equivalently \(\pi (P - I) = 0\). We compute it
as the (normalised) right null space of \(P^T - I\); since the columns
of \(P\) do not in general sum to 1, this is more direct than trying to
solve the linear system from scratch. The resulting vector is then
normalised so its entries sum to 1.

The more general theory of Markov chains, including the conditions
under which a stationary distribution exists and is unique, is covered
in [2].

### How we built this

We use `sympy.Matrix` rather than `numpy.ndarray` so that the
probabilities stay as exact rationals: for the two-state chain in the
Tutorial the stationary distribution is exactly \((4/7, 3/7)\), and the
library returns it in that form. A floating-point library would return
the same answer to within rounding.

The library follows the matrices chapter of *Python for Mathematics*
[1]: we use `sympy as sym` and reach for `sym.Matrix`, `sym.Rational`,
`sym.eye`, and `.nullspace()`. We compute the stationary distribution
as the null space of \(P^T - I\) and normalise.

## Reference

### List of functionality

A list of functionality in this library is:

- `is_stochastic(transition_matrix)`: check that the matrix is
  row-stochastic.
- `n_step_distribution(initial_distribution, transition_matrix,
  number_of_steps)`: return \(\pi_0 P^n\).
- `stationary_distribution(transition_matrix)`: return the row vector
  \(\pi\) satisfying \(\pi P = \pi\) with \(\sum_i \pi_i = 1\).

### Tests

The tests live in `test_markov.py` and can be run with:

```sh
python test_markov.py
```

They cover the stochastic check, the one-step and zero-step
distributions, the stationary distribution of the two-state chain, and
verify that \(P^{50}\) applied to a deterministic initial distribution
agrees with the stationary distribution to within \(10^{-10}\).

### Bibliography

[1] Knight, V. *Python for Mathematics*, vknight.org/pfm. Accessed 2026.

[2] Norris, J. R. *Markov Chains*. Cambridge University Press, 1998.
