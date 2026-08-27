# continued_fractions

A small Python library for computing the continued fraction expansion of a
rational number and the resulting list of convergents.

## Tutorial

We are going to expand \(22/7\), a common approximation of \(\pi\), as a
continued fraction. We start by importing the library:

```python
>>> import sympy
>>> import continued_fractions

```

The expansion of \(22/7\) is computed with `continued_fraction`:

```python
>>> continued_fractions.continued_fraction(sympy.Rational(22, 7), 10)
[3, 7]

```

The loop terminates as soon as the remainder is zero, so we get the two
coefficients \([3; 7]\) even though we asked for up to ten.

We can then turn those coefficients back into the corresponding rationals
with `convergents`:

```python
>>> continued_fractions.convergents([3, 7])
[3, 22/7]

```

The first convergent is \(3\) and the second is \(22/7\), which is the
original number.

## How to guide

### How to get the continued fraction expansion of a rational

To compute the expansion of a rational number we pass a `sympy.Rational` and
a cap on the number of terms:

```python
>>> import sympy
>>> import continued_fractions
>>> continued_fractions.continued_fraction(sympy.Rational(355, 113), 20)
[3, 7, 16]

```

### How to get the convergents from a list of coefficients

To turn a list of integer coefficients into the corresponding convergents:

```python
>>> import continued_fractions
>>> continued_fractions.convergents([3, 7, 16])
[3, 22/7, 355/113]

```

### How to get the Fibonacci-ratio approximation of the golden ratio

The golden ratio has continued fraction \([1; 1, 1, 1, \dots]\). We expose a
helper that returns its first convergents:

```python
>>> import continued_fractions
>>> continued_fractions.golden_ratio_convergents(6)
[1, 2, 3/2, 5/3, 8/5, 13/8]

```

## Discussion

Continued fractions are a way of writing a real number as a (possibly
infinite) nested sequence

\[
    r = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cdots}}
\]

with integer coefficients. For a rational number the expansion terminates
after finitely many steps; for an irrational number it is infinite. The
convergents are the rational numbers obtained by truncating the expansion
after each step, and they are known to give the best rational
approximations to the original number in the sense that no fraction with a
smaller denominator is closer.

The golden ratio is the simplest irrational number to expand: every
coefficient is \(1\), so its convergents are ratios of consecutive
Fibonacci numbers. We expose a convenience function for this case because
it is a good worked example to test against.

### How we built this

We compute the expansion with the Euclidean algorithm: at each step we
take the integer part of the remaining number, subtract it, and invert the
fractional part. Keeping the arithmetic symbolic with `sympy.Rational`
means that we never lose precision, which matters for known approximations
such as \(355 / 113\), where any floating-point detour would round.

For the convergents we use the standard recursion
\(p_n = a_n p_{n - 1} + p_{n - 2}\) and
\(q_n = a_n q_{n - 1} + q_{n - 2}\). This avoids reconstructing the
nested fractions from scratch at each step.

## Reference

### List of functionality

A list of functionality in this library is:

- `continued_fraction(rational_number, maximum_terms)`: return the
  continued fraction expansion of a rational.
- `convergents(coefficients)`: return the list of convergent rationals.
- `golden_ratio_convergents(number_of_terms)`: return the first
  convergents of the golden ratio.

### Tests

The tests live in `test_continued_fractions.py` and can be run with:

```sh
python test_continued_fractions.py
```

They check the expansion of \(3/2\), \(22/7\), \(355/113\), confirm that
the convergents of the golden ratio give Fibonacci ratios, and that the
twentieth convergent agrees with \(\varphi\) to within \(10^{-8}\).

### Bibliography

[1] Knight, V. *Python for Mathematics*, vknight.org/pfm. Accessed 2026.

[2] Khinchin, A. Y. *Continued Fractions*. University of Chicago Press,
1964.
