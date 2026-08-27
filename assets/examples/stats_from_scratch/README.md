# stats_from_scratch

A small Python library that implements the mean, the median, the
population and sample standard deviations, and the three quartiles
directly from their definitions.

## Tutorial

We are going to compute the summary statistics of the sequence
\(1, 2, 3, 4, 5\). We start by importing the library:

```python
>>> import stats_from_scratch

```

The mean and median are

```python
>>> stats_from_scratch.mean([1, 2, 3, 4, 5])
3.0
>>> stats_from_scratch.median([1, 2, 3, 4, 5])
3

```

The population standard deviation (divisor \(n\)) is
\(\sqrt{2} \approx 1.414\), and the sample standard deviation
(divisor \(n - 1\)) is \(\sqrt{2.5} \approx 1.581\):

```python
>>> round(stats_from_scratch.population_standard_deviation([1, 2, 3, 4, 5]), 6)
1.414214
>>> round(stats_from_scratch.sample_standard_deviation([1, 2, 3, 4, 5]), 6)
1.581139

```

The three quartiles are

```python
>>> stats_from_scratch.quartiles([1, 2, 3, 4, 5])
(1.5, 3.0, 4.5)

```

## How to guide

### How to compute the mean

```python
>>> import stats_from_scratch
>>> stats_from_scratch.mean([10, 20, 30, 40])
25.0

```

### How to compute the median

```python
>>> import stats_from_scratch
>>> stats_from_scratch.median([1, 2, 3, 4])
2.5
>>> stats_from_scratch.median([1, 2, 3, 4, 5])
3

```

### How to compute the standard deviations

The two versions differ in the divisor: the population variance uses
\(n\) and the sample variance uses \(n - 1\).

```python
>>> import stats_from_scratch
>>> round(stats_from_scratch.population_standard_deviation([2, 4, 4, 4, 5, 5, 7, 9]), 6)
2.0
>>> round(stats_from_scratch.sample_standard_deviation([2, 4, 4, 4, 5, 5, 7, 9]), 6)
2.13809

```

### How to compute the three quartiles

```python
>>> import stats_from_scratch
>>> stats_from_scratch.quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
(2.75, 5.5, 8.25)

```

## Discussion

The summary statistics of a sample are the standard way to describe
its location and spread. The mean and the population standard
deviation describe the centre and the spread of a fixed sample; the
sample standard deviation is the unbiased estimator of the standard
deviation of the underlying distribution and so uses the divisor
\(n - 1\) instead of \(n\). The three quartiles divide the sorted
sample into four equally sized groups.

For the quartiles we have to pick a method. There are several in use
in the literature and in software; the standard library's
`statistics.quantiles(data, n=4)` uses the so-called 'exclusive'
method, in which the \(k\)-th quartile is at the fractional
1-indexed position \(k (n + 1)/4\). We picked this method so that
our implementation could be compared directly against the
`statistics` module in the tests; on a sample of size five our
quartiles are exactly \((1.5, 3, 4.5)\), as expected.

### How we built this

Every function is written from its definition without using the
`statistics` module. The mean is the sum divided by the count; the
median is the middle of the sorted sample, averaging two values for
an even count; the standard deviations are square roots of mean
squared deviations from the mean; and the quartiles are computed by
linear interpolation at the fractional positions described above.

We use the `statistics` module only in the tests, where it serves as
a reference implementation. Each function is checked against the
matching `statistics` function on at least one sample, and the
quartiles are also checked against the known small example
\((1.5, 3, 4.5)\) for the sequence \(1, 2, 3, 4, 5\).

We follow the statistics chapter of *Python for Mathematics* [1]:
we reach for `statistics.mean`, `statistics.median`,
`statistics.pstdev`, `statistics.stdev`, and `statistics.quantiles`
when we want a quick answer, and we drop down to the definitions
when we want to know what the answer means.

## Reference

### List of functionality

A list of functionality in this library is:

- `mean(values)`: arithmetic mean.
- `median(values)`: median.
- `population_standard_deviation(values)`: standard deviation with
  divisor \(n\).
- `sample_standard_deviation(values)`: standard deviation with
  divisor \(n - 1\).
- `quartiles(values)`: the three quartiles
  \((Q_1, Q_2, Q_3)\), computed with the 'exclusive' method.

### Tests

The tests live in `test_stats_from_scratch.py` and can be run with:

```sh
python test_stats_from_scratch.py
```

They compare every function with the matching function in the
standard library `statistics` module, and they check the quartiles
against the known small example \([1, 2, 3, 4, 5]\), which gives
\((1.5, 3, 4.5)\).

### Bibliography

[1] Knight, V. *Python for Mathematics*, vknight.org/pfm. Accessed 2026.

[2] Rice, J. A. *Mathematical Statistics and Data Analysis*. Cengage,
3rd edition, 2007.
