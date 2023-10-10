---
layout: post
title: "Introduction to algebra with Sympy"
tags: algebra
---

In class today I gave an introduction to using [Sympy](https://www.sympy.org/en/index.html) to study algebra.

You can see a recording of the class [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=e9ce2ff1-c853-46ed-ac16-b09100f7d23c)

In class I used Sympy to solve the following problem:

1. Rationalise the following expression: \\(\frac{1}{\sqrt{3} + 1}\\).
2. Consider the quadratic \\(f(x) = -x ^ 2 + 8 x - 18\\).

   1. Calculate the discriminant of the quadratic equation $f(x)=0$. What
      does this tell us about the graph of \\(f(x)\\).
   2. By completing the square, confirm that \\((4, -2)\\) is the maximum
      point of \\(f(x)\\).

This is similar to the tutorial in the python for mathematics chapter which is
what your lab tutor will be taking you through in labs.

Here the notebook I used in class:
[algebra.ipynb]({{site.baseurl}}/assets/nbs/2023-2024/algebra.ipynb)

### Following along in class

A few students asked how to follow along in class when they are typing commands
in to their computer at the same time (especially when a command doesn't quite
work: for example a student wrote `sympy.symbol` instead of `sympy.Symbol` which
is easily done).

My advice is essentially to follow along in the same way you would any other
mathematics class. Perhaps in a calculus lecture you attempt to carry out the
same calculations at the same time but at some point you do not fully follow. In
this case I'd suggest making a note to ask what went wrong there and continue to
follow along as best is possible (even if it means no longer carrying out the
calculations). The only difference in this example and with computing is that
perhaps at some stage you do not get the expected output. If you can type the
next command and carry on but if that's not possible follow as best you can and
make a note to come back to it and work through it.

**BUT** Just like many of you did yesterday: please do ask me questions as we
go. If a quick scroll back to a specific point in the code fixes the problem
then I will super happily do that, if it's a more involved problem that might
need me to take a look at it we will find some time to do that.
