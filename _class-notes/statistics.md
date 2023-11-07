---
layout: class-notes
title: "Statistics"
tags: statistics
---

# Statistics week

## First meeting

After this meeting students should:

- Understand how to use the `statsmodels` library to fit a line to data.

### Problem

Explain to students that we will be solving the following problem:

```
I want to know if there is a relationship between distance from home and
expectation of grade in first year mathematics students.

The variables:

- $x$ is the self reported expectation (between 0 and 100)
- $y$ is the distance from home (as a percentage of 13,000 miles which is how far New
Zealand is).

1. Obtain the following summary statistics for both $x$ and $y$:
    - The mean;
    - The median;
    - The quartiles;
    - The standard deviation;
2. Obtain the Pearson correlation coefficient between $x$ and $y$.
3. Obtain a line of best fit $y=ax + b$.

```

If possible, use a web form to get students to input their own data. A quick
script like the following can be used to transform the data in to tuples:

```
import pandas as pd

df = pd.read_excel(
    "/Users/smavak/Downloads/Relationship between distance from home and
grade?(1-3).xlsx"
)
x = tuple(df["What year 1 average do you think you will get this year?"])
y = tuple(df["How far is home? (Miles)"])

```

Here is some data that would work if not:

    >>> x = (44,
    ...      47,
    ...      64,
    ...      67,
    ...      67,
    ...      9,
    ...      83,
    ...      21,
    ...      36,
    ...      87,
    ...      70,
    ...      88,
    ...      88,
    ...      12,
    ...      58,
    ...      65,
    ...      39,
    ...      87,
    ...      46,
    ...      88,
    ...      81,
    ...      37,
    ...      25,
    ...      77,
    ...      72,
    ...      9,
    ...      20,
    ...      80,
    ...      69,
    ...      79,
    ...      47,
    ...      64,
    ...      82,
    ...      99,
    ...      88,
    ...      49,
    ...      29,
    ...      19,
    ...      19,
    ...      14,
    ...      39,
    ...      32,
    ...      65,
    ...      9,
    ...      57,
    ...      32,
    ...      31,
    ...      74,
    ...      23,
    ...      35,
    ...      75,
    ...      55,
    ...      28,
    ...      34,
    ...      0,
    ...      0,
    ...      36,
    ...      53,
    ...      5,
    ...      38,
    ... )
    >>> y = (17,
    ...      79,
    ...      4,
    ...      42,
    ...      58,
    ...      31,
    ...      1,
    ...      65,
    ...      41,
    ...      57,
    ...      35,
    ...      11,
    ...      46,
    ...      82,
    ...      91,
    ...      0,
    ...      14,
    ...      99,
    ...      53,
    ...      12,
    ...      42,
    ...      84,
    ...      75,
    ...      68,
    ...      6,
    ...      68,
    ...      47,
    ...      3,
    ...      76,
    ...      52,
    ...      78,
    ...      15,
    ...      20,
    ...      99,
    ...      58,
    ...      23,
    ...      79,
    ...      13,
    ...      85,
    ...      48,
    ...      49,
    ...      69,
    ...      41,
    ...      35,
    ...      64,
    ...      95,
    ...      69,
    ...      94,
    ...      0,
    ...      50,
    ...      36,
    ...      34,
    ...      48,
    ...      93,
    ...      3,
    ...      98,
    ...      42,
    ...      77,
    ...      21,
    ...      73,
    ... )

Here is what this looks like (highlight that plotting is not part of this
chapter -- point students at pfm chapter on matplotlib):

    import matplotlib.pyplot as plt
    plt.figure()
    plt.scatter(x, y)
    plt.xlabel("Expected grade")
    plt.ylabel("Distance from home")

Compute the summary statistics:

    >>> import statistics as st
    >>> st.mean(x)
    49.1
    >>> st.median(x)
    47.0
    >>> st.quantiles(x, n=4)
    [28.25, 47.0, 73.5]
    >>> st.stdev(x) # doctest: +ELLIPSIS
    27.2096...
    >>> st.mean(y) # doctest: +ELLIPSIS
    49.4666...
    >>> st.median(y)
    48.5
    >>> st.quantiles(y, n=4)
    [21.5, 48.5, 75.75]
    >>> st.stdev(y) # doctest: +ELLIPSIS
    29.9510...

Compute the Pearson coefficient of correlation:

    >>> st.correlation(x, y) # doctest: +ELLIPSIS
    -0.10957...

This low but negative coefficient indicates that students who are further away
expect to do worst. (Note the data here is just random noise.)

Let us fit a line:

    >>> slope, intercept = st.linear_regression(x, y)
    >>> slope # doctest: +ELLIPSIS
    -0.1206...
    >>> intercept # doctest: +ELLIPSIS
    55.3890...

Highlight here that we are not doing any analysis of whether or not this is a
GOOD fit.

Here is what this looks like (highlight that plotting is not part of this
chapter -- point students at pfm chapter on matplotlib):

    plt.figure()
    plt.scatter(x, y)
    plt.plot((0, 100), (intercept, 100 * slope + intercept), color="black")
    plt.xlabel("Expected grade")
    plt.ylabel("Distance from home")

Come back: with time take any questions.

Point at resources.
