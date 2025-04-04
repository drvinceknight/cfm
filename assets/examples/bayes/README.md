# Bayes

A python library for studying Bayes' theorem.

## Tutorial

Let us assume that a child has fallen over. This happens with probability .2.

If they have fallen over, they might have hurt themselves seriously. The probability of hurting themselves seriously when they have fallen over is .1.

We know that the probability of them hurting themselves seriously is 0.05.

We would like to wort out the probability that they have fallen if they hurt themselves seriously.

We can use Bayes' theorem for this, and indeed use the bayes python library for this. First let us define the various parameters:

```python
>>> import bayes
>>> conditional_probability = 0.1
>>> marginal_probability = 0.05
>>> prior_probability = .2

```

Having done this we can now calculate the probability:

```python
>>> posterior = bayes.compute_posterior(marginal=marginal_probability, prior=prior_probability, conditional=conditional_probability)
>>> round(posterior, 1)
0.4

```

## How to guide

### How to compute the posterior

To compute the posterior probability given a `marginal`, `prior` and `conditional` you use:

```python
>>> import bayes
>>> bayes.compute_posterior(conditional=1 / 2, prior=1 / 4, marginal=1 / 3)
0.375

```

## Discussion

Bayes' theorem is credited to Thomas Bayes who published the following result in 1763:

$$
    P(A | B) = \frac{P(B | A) P(A)}{P(B)}
$$

Proofs of this and examples can be found in [1]. A good way of presenting the relationship is as so:

$$
    P(A | B)P(B) = P(B | A) P(A)
$$

As both the right hand side and the left hand side are equivalent to $P(A \cap B)$.

## Reference

### List of functionality

A list of functionality in this library is:

- `compute_posterior`

### Bibliography

[1] Starnes, Daren S., Josh Tabor, and Luke Wilcox. Statistics and probability with applications. Bedford, Freeman & Worth High School Publishers, 2017.