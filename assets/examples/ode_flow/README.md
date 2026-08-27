# ode_flow

A small Python library for solving and sampling first-order initial
value problems. The solver returns a symbolic solution, a helper
evaluates that solution at a list of sample times, and a verifier
checks that a candidate expression satisfies the equation.

## Tutorial

We are going to solve the exponential-growth problem
\(y'(t) = y(t)\) with \(y(0) = 1\). The exact solution is
\(y(t) = e^t\). We start by importing the library and declaring the
symbols:

```python
>>> import sympy as sym
>>> import ode_flow
>>> t = sym.Symbol("t")
>>> y = sym.Function("y")

```

The right-hand side of the ODE is the expression `y(t)`:

```python
>>> solution = ode_flow.solve_initial_value_problem(y(t), t, y, 0, 1)
>>> solution
exp(t)

```

We can sample the solution at a list of times:

```python
>>> ode_flow.trajectory(solution, t, [0, 1, 2])
[1.0, 2.718281828459045, 7.38905609893065]

```

We can also check that the candidate solution satisfies the ODE:

```python
>>> ode_flow.verify_solution(solution, y(t), t, y)
True

```

## How to guide

### How to solve a first-order initial value problem

The right-hand side is a `sympy` expression in the time variable and
the unknown function. The initial time and value can be either
symbolic or numeric.

```python
>>> import sympy as sym
>>> import ode_flow
>>> t = sym.Symbol("t")
>>> y = sym.Function("y")
>>> ode_flow.solve_initial_value_problem(2 * t, t, y, 0, 0)
t**2

```

### How to sample a symbolic solution at a list of times

```python
>>> import sympy as sym
>>> import ode_flow
>>> t = sym.Symbol("t")
>>> ode_flow.trajectory(t**2, t, [0, 1, 2, 3])
[0.0, 1.0, 4.0, 9.0]

```

### How to verify that an expression satisfies an ODE

```python
>>> import sympy as sym
>>> import ode_flow
>>> t = sym.Symbol("t")
>>> y = sym.Function("y")
>>> ode_flow.verify_solution(sym.exp(t), y(t), t, y)
True
>>> ode_flow.verify_solution(t, y(t), t, y)
False

```

## Discussion

A first-order initial value problem has the form
\(y'(t) = f(t, y(t))\) with \(y(t_0) = y_0\). For many right-hand
sides \(f\), the solution can be written down in closed form by
recognising one of the standard cases (separable, linear, exact). The
solver `sympy.dsolve` already implements these cases, and a great deal
more, so we treat it as the engine and focus on the interface.

The `trajectory` helper exists because the natural next step after
finding a symbolic solution is to plot it. The `verify_solution`
helper exists for tests: given a candidate symbolic solution, it
substitutes the candidate into the right-hand side and compares
against the derivative of the candidate. The general theory of ODEs
is covered in [2].

### How we built this

We pass the right-hand side and the initial condition through
`sym.Eq` and the `ics=` keyword of `sym.dsolve`. The return value of
`sym.dsolve` is an `Eq` of the form \(y(t) = \text{expression}\); we
take `.rhs` to return the expression itself, which is easier to
substitute into. Inside `trajectory` we convert each substitution to
`float` so that the output is small and plottable; the symbolic
solution remains available if exactness is needed.

We follow the differential equations chapter of *Python for
Mathematics* [1]: we use `sym.Function` for the unknown, `sym.Eq`
for the equation, and `sym.dsolve` with the `ics` keyword for the
initial condition.

## Reference

### List of functionality

A list of functionality in this library is:

- `solve_initial_value_problem(right_hand_side, time_variable,
  function, initial_time, initial_value)`: return the symbolic
  solution to a first-order initial value problem.
- `trajectory(solution_expression, time_variable, sample_times)`:
  evaluate the solution at a list of times.
- `verify_solution(solution_expression, right_hand_side,
  time_variable, function)`: check that a candidate solves the ODE.

### Tests

The tests live in `test_ode_flow.py` and can be run with:

```sh
python test_ode_flow.py
```

They check the solver on the exponential-growth problem
\(y' = y\), the constant-growth problem \(y' = 1\), the explicit
time-dependent problem \(y' = 2t\), and the same exponential-growth
problem with a non-zero initial time. They also check that
`trajectory` returns the correct length and known values, and that
`verify_solution` accepts a correct candidate and rejects an
incorrect one.

### Bibliography

[1] Knight, V. *Python for Mathematics*, vknight.org/pfm. Accessed 2026.

[2] Boyce, W. E. and DiPrima, R. C. *Elementary Differential Equations
and Boundary Value Problems*. Wiley, 11th edition, 2017.
