# dice

A small Python library for simulating and analysing sums of fair dice.
We provide a simulator, the empirical distribution of simulated sums,
the exact theoretical distribution, and a small set of summary
statistics.

## Tutorial

We are going to look at the sum of two six-sided dice. The classical
result is that there are 36 equally likely outcomes, the sum
\(s = 7\) is the most likely, and the sums \(s = 2\) and \(s = 12\)
are the least likely. We start by importing the library:

```python
>>> import dice

```

The exact theoretical distribution is

```python
>>> from fractions import Fraction
>>> distribution = dice.theoretical_distribution(2, sides=6)
>>> distribution[2]
Fraction(1, 36)
>>> distribution[7]
Fraction(1, 6)
>>> distribution[12]
Fraction(1, 36)

```

The probabilities sum to one:

```python
>>> sum(distribution.values())
Fraction(1, 1)

```

To simulate \(N\) rolls of two dice and look at the empirical
distribution, we pass a seed for reproducibility:

```python
>>> sums = dice.simulate_sums(2, 10_000, sides=6, seed=0)
>>> empirical = dice.empirical_distribution(sums)
>>> 0.13 < empirical[7] < 0.20
True

```

The empirical probability of rolling a 7 is close to the theoretical
\(1/6 \approx 0.167\).

## How to guide

### How to roll a fixed number of dice

```python
>>> import dice
>>> result = dice.roll(3, sides=6, seed=42)
>>> len(result)
3
>>> all(1 <= face <= 6 for face in result)
True

```

### How to simulate many sums of dice

```python
>>> import dice
>>> sums = dice.simulate_sums(2, 100, sides=6, seed=0)
>>> len(sums)
100

```

### How to compute the empirical distribution from samples

```python
>>> import dice
>>> samples = [2, 3, 3, 4, 4, 4, 5]
>>> dice.empirical_distribution(samples) == {
...     2: 1 / 7, 3: 2 / 7, 4: 3 / 7, 5: 1 / 7,
... }
True

```

### How to get the exact theoretical distribution

```python
>>> import dice
>>> from fractions import Fraction
>>> dice.theoretical_distribution(1, sides=6) == {
...     face: Fraction(1, 6) for face in range(1, 7)
... }
True

```

### How to compute summary statistics

```python
>>> import dice
>>> dice.summary_statistics([2, 3, 4, 5, 6])
(4, 4, 1.5811388300841898)

```

## Discussion

The sum of \(n\) fair \(s\)-sided dice has a known distribution that
can be computed by hand for small \(n\). For \(n = 2\) and \(s = 6\)
the well-known triangular distribution gives \(P(s = 2) = 1/36\),
\(P(s = 7) = 6/36 = 1/6\), and \(P(s = 12) = 1/36\). For larger \(n\)
the formula in closed form involves an alternating sum of binomial
coefficients, which is awkward to write out by hand. We use repeated
convolution instead: starting from the uniform distribution of one
die, we convolve with itself \(n - 1\) times to get the distribution
of the sum. This is short to implement and easy to test.

For 10 000 rolls of two dice the empirical probability of a 7 is
reliably between 0.13 and 0.20, which spans the theoretical
\(1/6 \approx 0.167\) by a comfortable margin.

### How we built this

We keep the probabilities exact using `fractions.Fraction` from the
standard library, which means that the sum of all probabilities is
exactly \(1\) (not just approximately). This matches the convention
of the textbook chapter on probability [1], where the worked examples
use rationals rather than decimals.

The empirical distribution is computed from a simulation: we use
`random.randint` to generate face values and count how often each sum
occurs. The `summary_statistics` function uses the `statistics`
module from the standard library: `statistics.mean`,
`statistics.median`, and the sample standard deviation
`statistics.stdev` (with a divisor of \(n - 1\)).

## Reference

### List of functionality

A list of functionality in this library is:

- `roll(number_of_dice, sides=6, seed=None)`: roll dice once.
- `simulate_sums(number_of_dice, number_of_rolls, sides=6, seed=None)`:
  simulate many rolls of a fixed number of dice and return the sums.
- `empirical_distribution(samples)`: relative-frequency distribution.
- `theoretical_distribution(number_of_dice, sides=6)`: exact
  distribution as a dictionary of `Fraction` values.
- `summary_statistics(samples)`: mean, median, and sample standard
  deviation.

### Tests

The tests live in `test_dice.py` and can be run with:

```sh
python test_dice.py
```

They check that `roll` returns values in range, that
`theoretical_distribution` agrees with the textbook values for two
six-sided dice, and that the empirical distribution from a
seeded simulation lies within a wide interval around the theoretical
probability of rolling a 7.

### Bibliography

[1] Knight, V. *Python for Mathematics*, vknight.org/pfm. Accessed 2026.

[2] Ross, S. M. *A First Course in Probability*. Pearson, 9th edition,
2014.
