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

1. Given that :math:`\frac{df}{dx}|_{x=0}=0`, :math:`\frac{d^2f}{dx^2}|_{x=0}=5` and that :math:`b>0` find the values of :math:`a` and :math:`b`.
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


Second meeting
--------------

- Give brief review of the contents of the chapter. Do this by browsing
  through: https://vknight.org/pfm/tools-for-mathematics/03-calculus/how/main.html
- Mention that no specific query arose so I will do a coursework type question
  but also demonstrate some difficulties that might arise with the Kernel.

I will work through the following problem:

Consider the functions :math:`f(x) = x ^ 3 + 3x - 3` and :math:`g(x) = \cos(x)
\sin(x)`.`

1. Create a variable `turning_points_of_f` which has value the turning points of
   :math:`f(X)`.
2. Create a variable `turning_points_of_g` which has value the turning points of
   :math:`g(X)`.
3. Create a variable `max_of_f_on_unit_circle` which has the maximum value of
   :math:`f` for :math:`x\in\[0, 2\pi\]`.
4. Create a variable `max_of_g_on_unit_circle` which has the maximum value of
   :math:`g` for :math:`x\in\[0, 2\pi\]`.
5. Which function has the maximum value?


The solution approach::

    >>> import sympy as sym
    >>> x = sym.Symbol("x")
    >>> f = x ** 3 + 3 * x - 3
    >>> g = sym.cos(x) * sym.sin(x)
    >>> turning_points_of_f = sym.solveset(sym.diff(f, x), x)
    >>> turning_points_of_f
    FiniteSet(I, -I)
    >>> turning_points_of_g = sym.solveset(sym.diff(g, x), x)
    >>> turning_points_of_g
    Union(ImageSet(Lambda(_n, 2*_n*pi + 5*pi/4), Integers), ImageSet(Lambda(_n, 2*_n*pi + 3*pi/4), Integers), ImageSet(Lambda(_n, 2*_n*pi + 7*pi/4), Integers), ImageSet(Lambda(_n, 2*_n*pi + pi/4), Integers))
    >>> max_of_f_on_unit_circle = max(f.subs({x: 0}), f.subs({x: 2 * sym.pi}))
    >>> max_of_f_on_unit_circle
    -3 + 6*pi + 8*pi**3
    >>> max_of_g_on_unit_circle = max(g.subs({x: 5 * sym.pi / 4}), g.subs({x: 3 * sym.pi / 4}), g.subs({x: 7 * sym.pi / 4}), g.subs({x: sym.pi / 4}))
    >>> max_of_g_on_unit_circle
    1/2
    >>> float(max_of_f_on_unit_circle)
    263.8997...


Highlight that the answer to the final question is thus :math:`f`.

Note that `max` is not a function that has been specifically been seen before
but that's not unexpected.

Now explain what the kernel is. Draw a picture showing the notebook separated
from the terminal. Analogy of a brain.

Restart the kernel, show that the last command does not work.

Rerun the cells but include a mistake::

    sym.solveset = (sym.diff(f, x), x)

Note the type of error we then get. And show that here we want the kernel to
forget everything.
