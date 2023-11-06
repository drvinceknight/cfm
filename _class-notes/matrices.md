---
layout: class-notes
title: "Matrices"
tags: matrices
---

## First meeting

After this meeting students should:

- Understand how to use the Sympy library to carry out basic Matrix related tasks
- Know what they need to do to prepare for their fourth tutorial.

Explain to students that we will be solving the following problem:

```
The matrix $A$ is given by $A=\begin{pmatrix}1 & 1 & a\\ 2 & a & 1\\ a & 1 & 2 a\end{pmatrix}$

1. Find the determinant of $A$
2. Hence find the values of $a$ for which $A$ is singular.
3. For the following values of $a$, when possible obtain $A ^ {- 1}$
   and confirm the result by computing $AA^{-1}$:

   1. $a = 0$;
   2. $a = 1$;
   3. $a = 2$;
   4. $a = 3$.

```

Solution

    >>> import sympy as sym
    >>> a = sym.Symbol("a")
    >>> A = sym.Matrix([[1, 1, 3], [2, a, 1], [a, 1, 0]])
    >>> A
    Matrix([
    [1, 1, 3],
    [2, a, 1],
    [a, 1, 0]])

Now to calculate the determinant::

    >>> determinant = A.det()
    >>> determinant
    -3*a**2 + a + 5

This can now be used to give us our first equation::

    >>> sym.solveset(determinant, a)
    FiniteSet(1/6 - sqrt(61)/6, 1/6 + sqrt(61)/6)

Indeed we can substitute those values in to the matrix and compute the inverse::

    >>> A.subs({a: sym.S(1) / 6 - sym.sqrt(61) / 6})
    Matrix([
    [               1,                1, 3],
    [               2, 1/6 - sqrt(61)/6, 1],
    [1/6 - sqrt(61)/6,                1, 0]])
    >>> A.subs({a: sym.S(1) / 6 - sym.sqrt(61) / 6}).inv()
    Traceback (most recent call last):
    ...
    sympy.matrices.common.NonInvertibleMatrixError: Matrix det == 0; not invertible.

Now for each value of :math:`a` we can compute the inverse and confirm that
inverse acts as required::

    >>> A.subs({a: 0}).inv()
    Matrix([
    [-1/5,  3/5,  1/5],
    [   0,    0,    1],
    [ 2/5, -1/5, -2/5]])
    >>> A.subs({a: 0}).inv() @ A.subs({a: 0})
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])
    >>> A.subs({a: 1}).inv()
    Matrix([
    [-1/3,  1, -2/3],
    [ 1/3, -1,  5/3],
    [ 1/3,  0, -1/3]])
    >>> A.subs({a: 1}).inv() @ A.subs({a: 1})
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])
    >>> A.subs({a: 2}).inv()
    Matrix([
    [ 1/5, -3/5,  1],
    [-2/5,  6/5, -1],
    [ 2/5, -1/5,  0]])
    >>> A.subs({a: 2}).inv() @ A.subs({a: 2})
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])
    >>> A.subs({a: 3}).inv()
    Matrix([
    [ 1/19, -3/19,  8/19],
    [-3/19,  9/19, -5/19],
    [ 7/19, -2/19, -1/19]])
    >>> A.subs({a: 3}).inv() @ A.subs({a: 3})
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])

Come back: with time take any questions.

Point at resources.

Here is a video recording of a short review given in the 2020/2021 academic
year: https://www.youtube.com/watch?v=rq_2ZYKq904
