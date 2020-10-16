Algebra week
============

First meeting
-------------

After this meeting students should:

- Understand how to use the Sympy library to carry out basic Algebraic tasks.
- Know what they need to do to prepare for their second tutorial.

Problem
*******

Explain to students that we will be solving the following problem:

1. Rationalise the following expression: :math:`\frac{1}{\sqrt{3} + 1}`.
2. Consider the quadratic :math:`f(x) = -x ^ 2 + 8 x - 18`.

    1. Calculate the discriminant of the quadratic equation :math:`f(x)=0`. What
       does this tell us about the graph of :math:`f(x)`.
    2. By completing the square, confirm that :math:`(4, -2)` is the maximum of
       point of :math:`f(x)`.

Solution
********

Group exercise (breakout rooms of 3): ask students to spend 5 minutes writing a
plan to tackle that problem (not necessarily carrying out each step).

Clearly write down these steps:


1. For first question: multiply by :math:`\sqrt{3} - 1`.
2. Calculate discriminant: compare to 0. If negative: no roots.
3. Complete the square to make :math:`f(x) = a (x - b ) ^2 + c`. Do this by
   expending that formula and comparing coefficients.

Now show how to get code to do this::

    >>> import sympy
    >>> expression = 1 / (sympy.sqrt(3) + 1)
    >>> expression
    1/(1 + sqrt(3))
    >>> sympy.simplify(expression)
    -1/2 + sqrt(3)/2

Discuss here how this differs if we used :code:`math.sqrt`. Explain that
:code:`sympy.simplify` is essentially acting as a black box here.

Now to carry out the rest of the problem::

    >>> x = sympy.Symbol("x")
    >>> expression = - x ** 2 + 8 * x - 18
    >>> expression
    -x**2 + 8*x - 18
    >>> sympy.discriminant(expression)
    -8

Confirm results by hand.

Discuss what this implies:

- Quadratic equation has no real roots.
- Graph does not intersect the :math:`y=0` line.
- Concave parabola (sign of leading coefficient of quadratic).

Confirm by solving the quadratic equation::

    >>> equation = sympy.Eq(lhs=expression, rhs=0)
    >>> equation
    Eq(-x**2 + 8*x - 18, 0)

    >>> sympy.solveset(expression, x)
    FiniteSet(4 + sqrt(2)*I, 4 - sqrt(2)*I)

Now to move on to next part of the problem: completing the square::

    >>> a, b, c = sympy.Symbol("a"), sympy.Symbol("b"), sympy.Symbol("c")
    >>> completed_square = a * (x - b) ** 2 + c
    >>> completed_square
    a*(-b + x)**2 + c

Let us expand and compare the coefficients::

    >>> sympy.expand(completed_square)
    a*b**2 - 2*a*b*x + a*x**2 + c

We see that :math:`a` is :math:`-1`. Let us substitute this value in to the
expression::

    >>> completed_square.subs({a: -1})
    c - (-b + x)**2

We can in fact overwrite the expression::

    >>> completed_square = completed_square.subs({a: -1})
    >>> completed_square
    c - (-b + x)**2

If we now expand again and compare coefficients::

    >>> sympy.expand(completed_square)
    -b**2 + 2*b*x + c - x**2

We see that :math:`2b=8`. Despite the fact that this equation is relatively
straightforward, let us solve it using :code:`sympy`::

    >>> equation = sympy.Eq(lhs=2 * b, rhs=8)
    >>> sympy.solveset(equation, b)
    FiniteSet(4)

We will substitute this value for :math:`b` back in to the completed square, and
expand again::

    >>> completed_square = completed_square.subs({b: 4})
    >>> completed_square
    c - (x - 4)**2
    >>> sympy.expand(completed_square)
    c - x**2 + 8*x - 16

We see that :math:`c - 16=-18`. Let us again solve that equation using
:math:`sympy`::

    >>> equation = sympy.Eq(lhs=c - 16, rhs= -18)
    >>> sympy.solveset(equation, c)
    FiniteSet(-2)

We will substitute this value back in::

    >>> completed_square = completed_square.subs({c: -2})
    >>> completed_square
    -(x - 4)**2 - 2
    >>> sympy.expand(completed_square)
    -x**2 + 8*x - 18

Ask students to break out in to groups of 3 and do the following:

1. Confirm that this answers the question.
2. Explain to each other what we did using code.

Come back: with time take any questions.

Point at resources.

After class email
-----------------

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I went over a demonstration of using Python to solve an
    algebraic problem. I did the following mathematical techniques:

    - Simplifying an exact numerical expression.
    - Calculating the discriminant of a quadratic.
    - Solving a symbolic equation.
    - Substitute values in to a symbolic expression.

    In preparation for your tutorial tomorrow please work through the second
    chapter of the Python for mathematics book:
    https://vknight.org/pfm/tools-for-mathematics/02-algebra/introduction/main.html

    Please get in touch if I can assist with anything,
    Vince


Second meeting
--------------

- Give brief review of the contents of the chapter. Do this by browsing
  through: https://vknight.org/pfm/tools-for-mathematics/01-using-notebooks/how/main.html
- Ask if anyone has any questions/comments/feedback.
- Remind everyone about the resources available to them (videos both on youtube
  and LC, chapters, plan, discord etc...).
- Explain that the following things seemed to be the main ones to come up:
    1. Finding files on computer.
    2. Difference between markdown and code cell.
    3. Using brackets when doing computations.

For each of those do a small walk-through showing the concepts again.
