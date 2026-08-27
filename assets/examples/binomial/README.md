# binomial

A small Python library for the binomial distribution: the probability
mass function, the cumulative distribution function, the mean, the
variance, and a simulator.

## Tutorial

We are going to look at the number of heads in 10 tosses of a fair
coin. The number of heads is a binomial random variable
\(X \sim \text{Bin}(10, 1/2)\). The most likely outcome is 5 heads,
with probability \(252 / 1024\). We start by importing the library:

```python
>>> import binomial

```

The probability of exactly five heads is

```python
>>> round(binomial.pmf(5, 10, 0.5), 6)
0.246094

```

The probability of at most three heads is

```python
>>> round(binomial.cdf(3, 10, 0.5), 6)
0.171875

```

The mean and variance are

```python
>>> binomial.mean(10, 0.5)
5.0
>>> binomial.variance(10, 0.5)
2.5

```

To simulate the experiment we can also draw samples from the
distribution:

```python
>>> samples = binomial.simulate(10, 0.5, 1000, seed=0)
>>> len(samples)
1000

```

## How to guide

### How to compute the probability of a specific number of successes

```python
>>> import binomial
>>> round(binomial.pmf(2, 5, 0.3), 6)
0.3087

```

### How to compute the cumulative probability up to a value

```python
>>> import binomial
>>> round(binomial.cdf(2, 5, 0.3), 6)
0.83692

```

### How to compute the mean and variance

```python
>>> import binomial
>>> binomial.mean(20, 0.4)
8.0
>>> round(binomial.variance(20, 0.4), 6)
4.8

```

### How to simulate from the distribution

```python
>>> import binomial
>>> samples = binomial.simulate(10, 0.5, 100, seed=42)
>>> all(0 <= value <= 10 for value in samples)
True

```

## Discussion

The binomial distribution describes the number of successes in
\(n\) independent Bernoulli trials, each with success probability
\(p\). Writing \(X \sim \text{Bin}(n, p)\) the probability mass
function is

\[
    P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k},
    \qquad k = 0, 1, \dots, n,
\]

and the cumulative distribution function is the partial sum

\[
    P(X \le k) = \sum_{j = 0}^{k} \binom{n}{j} p^j (1 - p)^{n - j}.
\]

The mean and variance have the clean forms \(\mathbb{E}[X] = n p\) and
\(\text{Var}(X) = n p (1 - p)\). These can be derived directly from
the moment generating function, or by writing \(X = \sum_{i = 1}^{n}
X_i\) for independent Bernoulli summands.

The binomial distribution is a standard reference distribution in
introductory probability [2]. It also appears in many other places:
it is the discrete analogue of the normal distribution for fixed
\(p\) and large \(n\), and it underpins the binomial test in
statistics.

### How we built this

For the binomial coefficient \(\binom{n}{k}\) we use
`scipy.special.comb(..., exact=True)`. The exact form returns a
Python `int` instead of a `float`, which keeps the integer
factor honest before we multiply by the probabilities. This is also
the function recommended by the combinatorics chapter of *Python for
Mathematics* [1].

The simulator uses the `random` module from the standard library:
for each draw, we count how many of `number_of_trials` uniform
draws fall below `success_probability`. This is the most direct
simulation of the underlying Bernoulli trials, and it lets us seed
the generator for reproducibility.

The CDF is computed by summing the PMF rather than by calling a
ready-made `scipy.stats.binom.cdf`. We did this because the project
focuses on understanding the distribution rather than on speed, and
because summing eleven floats for a small \(n\) is cheap.

## Reference

### List of functionality

A list of functionality in this library is:

- `pmf(number_of_successes, number_of_trials, success_probability)`:
  the probability mass function \(P(X = k)\).
- `cdf(number_of_successes, number_of_trials, success_probability)`:
  the cumulative distribution function \(P(X \le k)\).
- `mean(number_of_trials, success_probability)`: the mean \(n p\).
- `variance(number_of_trials, success_probability)`: the variance
  \(n p (1 - p)\).
- `simulate(number_of_trials, success_probability,
  number_of_simulations, seed=None)`: simulate draws from the
  distribution.

### Tests

The tests live in `test_binomial.py` and can be run with:

```sh
python test_binomial.py
```

They cover the PMF at \(k = 0\) and the mode \(k = n / 2\) of a fair
coin, check that the PMF sums to 1, that the CDF is monotone and
reaches 1, and that the empirical mean of 5000 simulated draws of
\(\text{Bin}(20, 1/2)\) lies within 0.3 of the theoretical mean of 10.

### Bibliography

[1] Knight, V. *Python for Mathematics*, vknight.org/pfm. Accessed 2026.

[2] Ross, S. M. *A First Course in Probability*. Pearson, 9th edition,
2014.

[3] Virtanen, P. et al. *SciPy 1.0: fundamental algorithms for
scientific computing in Python.* Nature Methods 17, 261-272, 2020.
