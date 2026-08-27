# newton

A small Python library for finding roots of single-variable expressions with
Newton-Raphson iteration.

## Tutorial

We are going to approximate \(\sqrt{2}\) by finding the positive root of
\(f(x) = x^2 - 2\). We start by declaring a symbol and importing the
library:

```python
>>> import sympy as sym
>>> import newton
>>> x = sym.Symbol("x")

```

A single Newton step from \(x_0 = 1\) gives

\[
    x_1 = x_0 - \frac{f(x_0)}{f'(x_0)} = 1 - \frac{-1}{2} = \frac{3}{2}.
\]

We can confirm this with the library:

```python
>>> newton.newton_step(x ** 2 - 2, x, sym.S(1))
3/2

```

To collect a list of successive iterates, we call `iterate`:

```python
>>> iterates = newton.iterate(x ** 2 - 2, x, sym.S(1), number_of_iterations=4)
>>> iterates
[1, 3/2, 17/12, 577/408, 665857/470832]

```

Each iterate is held as an exact rational. To get a closed answer we use
`find_root`, which stops as soon as two successive iterates agree to within
a tolerance:

```python
>>> root, iterations = newton.find_root(
...     x ** 2 - 2,
...     x,
...     sym.S(1),
...     tolerance=10 ** -10,
...     maximum_iterations=50,
... )
>>> round(float(root), 8)
1.41421356

```

The number of iterations taken is small:

```python
>>> iterations
5

```

## How to guide

### How to take a single Newton step

To take one Newton step from `current_value` on the expression `expression`
in the symbol `variable`:

```python
>>> import sympy as sym
>>> import newton
>>> x = sym.Symbol("x")
>>> newton.newton_step(x ** 3 - 8, x, sym.S(1))
10/3

```

### How to collect a sequence of iterates

To collect the first `number_of_iterations + 1` iterates of Newton-Raphson:

```python
>>> import sympy as sym
>>> import newton
>>> x = sym.Symbol("x")
>>> newton.iterate(x ** 2 - 2, x, sym.S(2), number_of_iterations=3)
[2, 3/2, 17/12, 577/408]

```

### How to find a root to a given tolerance

To iterate until two successive iterates agree to within `tolerance`, or
until `maximum_iterations` steps have been taken:

```python
>>> import sympy as sym
>>> import newton
>>> x = sym.Symbol("x")
>>> root, iterations = newton.find_root(
...     x ** 3 - 8,
...     x,
...     sym.S(1),
...     tolerance=10 ** -8,
...     maximum_iterations=50,
... )
>>> round(float(root), 6)
2.0

```

## Discussion

Newton-Raphson is a method for finding a root of a differentiable function
\(f\). Starting from an initial guess \(x_0\) close to a root, the method
updates the iterate by

\[
    x_{n + 1} = x_n - \frac{f(x_n)}{f'(x_n)}.
\]

Geometrically each step replaces \(f\) by its tangent line at \(x_n\) and
takes the root of that line as the new iterate. When the method converges
to a simple root the error is squared at each step: this is the
quadratic-convergence property that makes Newton-Raphson the standard
choice when a derivative is available.

The method can fail to converge: a poor initial guess can land the iterate
in a region where the derivative is small, and the next step can overshoot.
A `maximum_iterations` cap protects against this. We return both the final
iterate and the number of iterations taken so the caller can detect that
the cap was reached.

### How we built this

We keep the iterates symbolic by using `sympy` because this avoids
floating-point drift in the early steps; we only call `float` when we
report the final answer. The derivative is computed inside `newton_step`
with `sympy.diff`, and the substitution at the current value uses the
dict form `expression.subs({variable: current_value})`. The library
accepts both symbolic and numeric inputs, but a symbolic `current_value`
(using `sympy.S`) gives the cleanest trail of iterates [1].

## Reference

### List of functionality

A list of functionality in this library is:

- `newton_step(expression, variable, current_value)`: apply one
  Newton-Raphson step.
- `iterate(expression, variable, initial_value, number_of_iterations)`:
  collect the first `number_of_iterations + 1` iterates.
- `find_root(expression, variable, initial_value, tolerance,
  maximum_iterations)`: iterate to a tolerance.

### Tests

The tests live in `test_newton.py` and can be run with:

```sh
python test_newton.py
```

The tests cover all three functions, check that the iterates have the
expected exact rational form, and check that `find_root` recovers
\(\sqrt{2}\) and \(2\) (as the real root of \(x^3 - 8\)) to within
tolerance.

### Bibliography

[1] Knight, V. *Python for Mathematics*, vknight.org/pfm. Accessed 2026.
