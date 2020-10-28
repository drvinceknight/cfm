Matrices week
=============

First meeting
-------------

After this meeting students should:

- Understand how to use the Sympy library to carry out basic Matrix related tasks
- Know what they need to do to prepare for their fourth tutorial.

Problem
*******

Explain to students that we will be solving the following problem:

The matrix :math:`A` is given by :math:`A=\begin{pmatrix}1 & 1 & a\\ 2 & a & 1\\ a & 1 & 2 a\end{pmatrix}`.

1. Find the determinant of :math:`A`
2. Hence find the values of :math:`a` for which :math:`A` is singular.
3. For the following values of :math:`a`, when possible obtain :math:`A ^ {- 1}`
   and confirm the result by computing :math:`AA^{-1}`:

    1. :math:`a = 0`;
    2. :math:`a = 1`;
    3. :math:`a = 2`;
    4. :math:`a = 3`.


Solution
********

Group exercise (breakout rooms of 3): ask students to spend 5 minutes writing a
plan to tackle that problem (not necessarily carrying out each step). Some
students might not be familiar with matrices so this is an opportunity

Now show how to get code to do this::

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

After class email
-----------------

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I went over a demonstration of using Python to solve a
    matrix problem. I carried out the following mathematical techniques:

    - Calculating a determinant
    - Computing a matrix inverse
    - Doing matrix multiplication

    One thing I did not cover explicitly is solving a linear system. However
    this is implicitely covered by calculating a matrix inverse. You can see
    this here:
    https://vknight.org/pfm/tools-for-mathematics/04-matrices/how/main.html#how-to-solve-a-linear-system

    In preparation for your tutorial tomorrow please work through the fourth
    chapter of the Python for mathematics book:
    https://vknight.org/pfm/tools-for-mathematics/04-matrices/introduction/main.html

    Please get in touch if I can assist with anything,
    Vince
