Calculus week
=============

First meeting
-------------

After this meeting students should:

- Understand how to use the Sympy library to carry out basic Calculus tasks
- Know what they need to do to prepare for their third tutorial.

Problem
*******

Explain to students that we will be solving the following problem:

Consider the function :math:`f(x)= x ^ 3 - ax ^ 2 + bx - 5`

1. Given that :math:`\frac{df}{dx}|_{x=0}=0$, $\frac{d^2f}{dx^2}|_{x=0}=5` and that :math:`b>0` find the values of :math:`a` and :math:`b`.
2. For the specific values of :math:`a` and :math:`b` find:
    1. :math:`\lim_{x\to 0}f(x)`;
    2. :math:`\lim_{x\to \infty}f(x)`;
    3. :math:`\int f(x) dx`;
    4. :math:`\int_{5}^{\pi} f(x) dx`.


Solution
********

Group exercise (breakout rooms of 3): ask students to spend 5 minutes writing a
plan to tackle that problem (not necessarily carrying out each step).

Clearly write down these steps:

1. Differentiate and write system of equations and solve them for :math:`a` and :math:`b`.
2. Take the limits and calculate the integrals.

Now show how to get code to do this::

    >>> import sympy as sym  # Note that we are using an alias
    >>> x = sym.Symbol("x")
    >>> a = sym.Symbol("a")
    >>> b = sym.Symbol("b")
    >>> expression = x ** 3 - a * x ** 2 + b * x - 5
    >>> expression
    -a*x**2 + b*x + x**3 - 5

So far we have not done anything different to what we saw in the Algebra
chapter.
Now to differentiate::

    >>> derivative = sym.diff(expression, x)
    >>> derivative
    -2*a*x + b + 3*x**2

This can now be used to give us our first equation::

    >>> first_equation = sym.Eq(derivative.subs({x: 0}), 0)
    >>> first_equation
    Eq(b, 0)

Now let us get the second derivative::

    >>> second_derivative = sym.diff(expression, x, 2)
    >>> second_derivative
    2*(-a + 3*x)

and get the second equation::

    >>> second_equation = sym.Eq(second_derivative.subs({x: 0}), 5)
    >>> second_equation
    Eq(-2*a, 5)

Now to solve the first equation to obtain a value for :math:`b`::

    >>> sym.solveset(first_equation, b)
    FiniteSet(0)

Now to substitute that value for $a$ (note that this is not necessary) and solve
the second equation for $a$::

    >>> second_equation = second_equation.subs({b: 0})
    >>> second_equation
    Eq(-2*a, 5)

We can solve this::

    >>> sym.solveset(second_equation, a)
    FiniteSet(-5/2)

Substituting these back::

    >>> expression = expression.subs({b: 0, a: - sym.S(5) / 2})
    >>> expression
    x**3 + 5*x**2/2 - 5

We can confirm our findings::

    >>> sym.diff(expression, x).subs({x: 0})
    0
    >>> sym.diff(expression, x, 2).subs({x: 0})
    5

Now we can compute the limits and integrals::

    >>> sym.limit(expression, x, 0)
    -5
    >>> sym.limit(expression, x, sym.oo)
    oo
    >>> sym.integrate(expression, x)
    x**4/4 + 5*x**3/6 - 5*x
    >>> sym.factor(sym.integrate(expression, (x, 5, sym.pi)))
    (-5 + pi)*(3*pi**3 + 25*pi**2 + 125*pi + 565)/12


Come back: with time take any questions.

Point at resources.

After class email
-----------------

Send the following email after class::

    Hi all,

    A recording of today's class is available at <>.

    In this class I went over a demonstration of using Python to solve a
    calculus problem. I carried out the following mathematical techniques:

    - Differentiation
    - Limits
    - Integrations

    In preparation for your tutorial tomorrow please work through the third
    chapter of the Python for mathematics book:
    https://vknight.org/pfm/tools-for-mathematics/03-calculus/introduction/main.html

    Please get in touch if I can assist with anything,
    Vince
