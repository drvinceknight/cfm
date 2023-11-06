---
layout: class-notes
title: "Sequences"
tags: sequences
---

# Sequences week

## First meeting

After this meeting students should:

- Understand how to use define function recursively
- Know what they need to do to prepare for their seventh tutorial.

### Problem

Explain to students that we will be solving the following problem:

```

A sequence $a_1, a_2, a_3, …$ is defined by:

$$\begin{aligned}
\left\{
\begin{array}{l}
    a_1 = k,\\
    a_{n + 1} = 3a_n – 4, n \geq 1,
\end{array}
\right.
\end{aligned}$$

where $k$ is a constant.

1.  Write down an expression for $a_2$ in terms of $k$.
2.  Show that $a_3 = 9k - 16$
3.  Given that $\sum_{r=1}^{12} a_r = 50$ find the value of $k$.

```

Now explain that we essentially need to add to our tools the ability to
define a function recursively which we can do:

    >>> def generate_a(k_value, n):
    ...     """
    ...     Uses recursion to return a_n for a given value of k:
    ...     a_1 = k
    ...     a_n = 3a_n - 4
    ...     """
    ...     if n == 1:
    ...         return k_value
    ...     return 3 * generate_a(k_value, n - 1) - 4

Spend some time explaining what is happening here. Specifically
highlighting that the programming recursion matches the mathematical
definition.

Show how we can make some calls of the function:

    >>> k = 5
    >>> generate_a(k_value=k, n=1)
    5
    >>> generate_a(k_value=k, n=2)
    11
    >>> generate_a(k_value=k, n=3)
    29
    >>> generate_a(k_value=k, n=4)
    83
    >>> generate_a(k_value=k, n=5)
    245

To be able to answer the questions we need $k$ as a symbol:

    >>> import sympy as sym
    >>> k = sym.Symbol("k")
    >>> generate_a(k_value=k, n=2)
    3*k - 4

To find $a_3$:

    >>> generate_a(k_value=k, n=3)
    9*k - 16

We now compute the sum of the first 12 terms:

    >>> sum_of_first_12_terms = sum(generate_a(k_value=k, n=r) for r in range(1, 13))
    >>> sum_of_first_12_terms
    265720*k - 531416

Our equation is thus:

    >>> equation = sym.Eq(sum_of_first_12_terms, 50)
    >>> equation
    Eq(265720*k - 531416, 50)
    >>> sym.solveset(equation, k)
    {20441/10220}

Come back: with time take any questions.

Point at resources.
