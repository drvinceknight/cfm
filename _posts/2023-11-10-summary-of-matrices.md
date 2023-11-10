---
layout: post
title: "Summary of Matrices"
tags:
  - matrices
---

In class today I we went over the Matrices chapter.

You can see a recording of the class [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=d25d81fb-4cbc-4dde-be40-b0b100c647e1)

Here is the notebook I used in class:
[matrices.ipynb]({{site.baseurl}}/assets/nbs/2023-2024/matrices.ipynb)

We started with the quiz (won by Tom who has 1 win):

4 people have a single win:

- Daf: 2 wins
- Anthony: 1 win
- Ben: 1 win
- Joe: 1 win
- Millie: 1 win
- Tom: 1 win

After this we covered a couple of great questions:

- Using `sym.solve` to solve systems of equations (and why not to do it).
- Writing your own errors (which might be of interest to some of you next Semester)

Following this we spent some time looking at the coursework like question from
the handout. We ended briefly by looking at the fact that we can constrain the
domain of `solveset`. For example:

```
>>> import sympy as sym
>>> x = sym.Symbol("x")
>>> equation = sym.Eq(x ** 2, -1)
>>> sym.solveset(equation, x, domain=sym.S.Reals)
EmptySet
```
