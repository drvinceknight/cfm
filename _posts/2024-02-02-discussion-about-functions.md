---
layout: post
title: "Functions, docstrings and a mistake by me at the end"
tags:
  - functions-and-data-structures
---

In class today we spoke about group coursework a bit but mainly spent time
looking at docstrings.

You can see a recording of this here: [https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=7c020a93-9855-44f2-9f30-b1050118b4a9](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=53ced2ac-b8f5-4b07-9b3a-b10201087ba1)

We spoke about the numpy docstring format, which is specified here: [https://vknight.org/pfm/building-tools/02-functions-and-data-structures/how/main.html#how-to-write-a-docstring](https://vknight.org/pfm/building-tools/02-functions-and-data-structures/how/main.html#how-to-write-a-docstring)

I used the example of verifying the following identity to demonstrate this:

$$(a + b) ^ n = \sum_{i=0}^n\binom{n}{i} a ^ i b ^ {n - i}$$

You can find a notebook with all this [here]({{site.baseurl}}/assets/nbs/2023-2024/functions-and-data-structures.ipynb)

**I'm really sorry about how confusing the ending of class today must have been
I made a mistake (my fault entirely)**.

The notebook linked to above does not contain the error.

When it came to fixing the floating point error I wrote:

```python
sum(int(scipy.special.binom(n, i) * a ** i * b ** (n - i)) for i in range(n + 1))
```

But the mistake I made here (and again I apologise for the crash and burn at the
end of the class) is that the closing bracket of `int` should have been after
the `binom` and not after the entire calculation.

```python
sum(int(scipy.special.binom(n, i)) * a ** i * b ** (n - i) for i in range(n + 1))
```

The difference is subtle but it is important as `scipy.special.binom(n, i)`
will always be a float with 0 fractional part. So taking the `int` of it will
give what we need.

I'll happily go over this again on Tuesday if I can clarify things. The
important thing to take from today is the approach and the docstrings.
