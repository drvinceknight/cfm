---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region -->
## Calculus

### Introduction

As of 2020, the A-level syllabus includes Calculus which
https://www.cambridgeinternational.org/Images/415060-2020-2022-syllabus.pdf
describes as:

> Calculus: this is a fundamental element which describes change in dynamic situations and underlines the links between functions and graphs.

In practice this often means:

- taking limits of functions;
- differentiating functions;
- integrating functions.

Here we will see how to instruct a computer to carry out these techniques.

## Tutorial

We will solve the following problem using a computer to assist with the technical aspects:


---

Consider the function \\(f(x)= \frac{24 x \left(a - 4 x\right) + 2 \left(a - 8 x\right) \left(b - 4 x\right)}{\left(b - 4 x\right)^{4}}\\)

1. Given that \\(\frac{df}{dx}|_{x=0}=0\\), \\(\frac{d^2f}{dx^2}|_{x=0}=-1\\) and that \\(b>0\\) find the values of \\(a\\) and \\(b\\).
2. For the specific values of \\(a\\) and \\(b\\) find:
    1. \\(\lim_{x\to 0}f(x)\\);
    2. \\(\lim_{x\to \infty}f(x)\\);
    3. \\(\int f(x) dx\\);
    4. \\(\int_{5}^{20} f(x) dx\\).

---

Sympy is once again the library we will use for this.

We will start by creating a variable `expression` that has the value of the expression of \\(f(x)\\):
<!-- #endregion -->

```python
import sympy as sym
x = sym.Symbol("x")
a = sym.Symbol("a")
b = sym.Symbol("b")
expression = (2 * (12 * x * (a - 4 * x) + (a-8 * x) * (b-4 * x))) / ((b - 4 * x) ** 4)
expression
```

now we can will use `sympy.diff` to calculate the derivative. This tool takes two inputs: 

- the first is the expression we are differentiating. Essentially this is the numerator of \\(\frac{df}{dx}\\).
- the first is the variable we are differentiating for. Essentially this is the denominator of \\(\frac{df}{dx}\\).

**Note** that we have imported `import sympy as sym` so we are going to write `sym.diff`:

```python
derivative = sym.diff(expression, x)
derivative
```

Let us factorise that to make it slightly clearer:

```python
sym.factor(derivative)
```

We will now create the first equation, which is obtained by substituting \\(x=0\\) in to the value of the derivative and equating that to \\(\pi\\):

```python
first_equation = sym.Eq(derivative.subs({x: 0}), 0)
first_equation
```

We will factor that equation:

```python
sym.factor(first_equation)
```

Now we are going to create the second equation, subsituting \\(x=0\\) in to the value of the second derivative. We calculate the second derivative by passing a third (optional) input to `sym.diff`:

```python
second_derivative = sym.diff(expression, x, 2)
second_derivative
```

We equate this expression to \\(-1\\):

```python
second_equation = sym.Eq(second_derivative.subs({x: 0}), -1)
second_equation
```

Now to solve the first equation to obtain a value for \\(a\\):

```python
sym.solveset(first_equation, a)
```

Now to subsitute that value for \\(a\\) and solve the second equation for \\(b\\):

```python
second_equation = second_equation.subs({a: b / 3})
second_equation
```

```python
sym.solveset(second_equation, b)
```

```python
sym.root(192, 4)
```

Recalling the question we know that \\(b>0\\) thus: \\(b = 2\sqrt{2}\sqrt[4]{3}\\) and \\(a=\frac{2\sqrt{2}\sqrt[4]{3}}{3}\\).

We will substitue these values back and finish the question:

```python
expression = expression.subs({a: 2 * sym.sqrt(2) * sym.root(3, 4) / 3, b: 2 * sym.sqrt(2) * sym.root(3, 4)})
expression
```

**Note** that we are using the `sym.root` command for the generic \\(n\\)th root. 

We can confirm our findings:

```python
sym.diff(expression, x).subs({x: 0})
```

```python
sym.diff(expression, x, 2).subs({x: 0})
```

Now we will calculate the limits using `sym.limit`, these takes 3 inputs:

- The expression we are taking the limit of.
- The variable that is changing.
- The value that the variable is tending towards.

```python
sym.limit(expression, x, 0)
```

```python
sym.limit(expression, x, sym.oo)
```

Now we are going to calculate the **indefinite** integral using `sympy.integrate`. This tool takes 2 inputs as:

- the first is the expression we're integrating. This is the \\(f\\) in \\(\int_a^b f dx\\).
- the second is the remaining information needed to calculate the integral: \\(x\\).

```python
sym.factor(sym.integrate(expression, x))
```

If we want to calculate a **definite** integral then instead of passing the single variable we pass a tuple which contains the variable as well as the bounds of integration:

```python
sym.factor(sym.integrate(expression, (x, 5, 20)))
```

### How to


### Exercises


### References
