# quadratic

A small Python library for solving real quadratic equations. We return
the discriminant, the set of real roots, the number of real roots, and
the vertex of the parabola.

## Tutorial

We are going to solve the quadratic \(x^2 - 3 x + 2 = 0\). The
coefficients are \(a = 1\), \(b = -3\), \(c = 2\). We start by importing
the library:

```python
>>> import sympy
>>> import quadratic
>>> x = sympy.Symbol("x")

```

The discriminant is positive:

```python
>>> quadratic.discriminant(1, -3, 2)
1

```

so we expect two distinct real roots. Calling `solutions` returns a
`sympy` set containing them:

```python
>>> quadratic.solutions(1, -3, 2, x)
{1, 2}

```

The number of real roots is

```python
>>> quadratic.number_of_real_roots(1, -3, 2)
2

```

and the vertex of the parabola \(y = x^2 - 3 x + 2\) is at

```python
>>> quadratic.vertex(1, -3, 2)
(3/2, -1/4)

```

## How to guide

### How to compute the discriminant

To compute \(b^2 - 4 a c\) for a quadratic \(a x^2 + b x + c\):

```python
>>> import quadratic
>>> quadratic.discriminant(2, 4, 2)
0

```

### How to find the real roots

To find the real roots we need to pass a `sympy.Symbol` for the
unknown:

```python
>>> import sympy
>>> import quadratic
>>> x = sympy.Symbol("x")
>>> quadratic.solutions(1, -2, 1, x)
{1}

```

If there are no real roots the returned set is empty:

```python
>>> quadratic.solutions(1, 0, 1, x)
EmptySet

```

### How to classify by number of real roots

```python
>>> import quadratic
>>> quadratic.number_of_real_roots(1, -3, 2)
2
>>> quadratic.number_of_real_roots(1, -2, 1)
1
>>> quadratic.number_of_real_roots(1, 0, 1)
0

```

### How to find the vertex of the parabola

```python
>>> import quadratic
>>> quadratic.vertex(1, -2, 1)
(1, 0)

```

## Discussion

A quadratic equation has the form \(a x^2 + b x + c = 0\) with
\(a \ne 0\). The quadratic formula gives the two solutions as

\[
    x = \frac{-b \pm \sqrt{b^2 - 4 a c}}{2 a}.
\]

The quantity under the square root is the discriminant
\(\Delta = b^2 - 4 a c\). When \(\Delta > 0\) the equation has two
distinct real roots; when \(\Delta = 0\) the two roots collapse onto a
single repeated root; and when \(\Delta < 0\) there are no real roots
because the formula asks for the square root of a negative number.

The vertex of the parabola \(y = a x^2 + b x + c\) is at
\(x = -b / (2 a)\), which is also halfway between the two real roots
when they exist. We expose this as a separate function because it is
useful for sketching the parabola without having to solve the quadratic
first.

### How we built this

We could have implemented the quadratic formula by hand, but
`sympy.solveset` already handles every case, including the empty-set
case when there are no real roots. We pass the domain `sympy.S.Reals`
so that we only get real solutions back: the default domain would also
include complex roots, and the marking scheme of this module asks us
only about real roots.

The library is built on the conventions of the `pfm` algebra chapter
[1]: every input is treated symbolically by wrapping it in
`sympy.S(...)` before doing arithmetic, and the answer comes back as a
`sympy` expression rather than a `float`.

## Reference

### List of functionality

A list of functionality in this library is:

- `discriminant(quadratic_coefficient, linear_coefficient,
  constant_coefficient)`: return \(b^2 - 4 a c\).
- `solutions(quadratic_coefficient, linear_coefficient,
  constant_coefficient, variable)`: return the real roots as a
  `sympy.Set`.
- `number_of_real_roots(quadratic_coefficient, linear_coefficient,
  constant_coefficient)`: return 0, 1, or 2.
- `vertex(quadratic_coefficient, linear_coefficient,
  constant_coefficient)`: return the vertex of the parabola.

### Tests

The tests live in `test_quadratic.py` and can be run with:

```sh
python test_quadratic.py
```

They cover the three discriminant cases and check the vertex against
the known parabolas \(y = x^2\) and \(y = (x - 1)^2\).

### Bibliography

[1] Knight, V. *Python for Mathematics*, vknight.org/pfm. Accessed 2026.
