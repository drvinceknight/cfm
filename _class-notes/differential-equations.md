---
layout: class-notes
title: "Differential Equations"
tags: differential-equations
---

# Differential equations week

## First meeting

After this meeting students should:

- Understand how to write a differential equation.
- Understand how to use the `sympy` library to solve differential equations to
  obtain both the general and particular solution.

### Problem

Explain to students that we will be solving the following problem:

```
Obtain the general solution to the following differential equation:

$$\frac{dy}{dx}=3y^2-5xy^2$$

Obtain the particular solution given that $y(3)=4$.

```

Set up the variable and the function:

    >>> import sympy as sym
    >>> x = sym.Symbol("x")
    >>> y = sym.Function("y")

Write the differential equation:

    >>> differential_equation = sym.Eq(lhs=sym.diff(y(x), x), rhs=3 * y(x) ** 2 - 5 * x * y(x) ** 2)
    >>> differential_equation
    Eq(Derivative(y(x), x), -5*x*y(x)**2 + 3*y(x)**2)

Use `sympy.dsolve` to obtain the general equation:

    >>> sym.dsolve(differential_equation, y(x))
    Eq(y(x), 2/(C1 + 5*x**2 - 6*x))

Create the boundary conditions:

    >>> condition = {y(3): 4}
    >>> sym.dsolve(differential_equation, y(x), ics=condition)
    Eq(y(x), 2/(5*x**2 - 6*x - 53/2))

Come back: with time take any questions.

Point at resources.
