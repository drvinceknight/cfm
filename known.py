words = set(
    (
        "scipy",
        "Combinatorics",
        "rhs",
        "lhs",
        "df",
        "AttributeError",
        "Cymru",
        "FiniteSet",
        "Jupyter",
        "LaTeX",
        "Modularisation",
        "NameError",
        "PyCons",
        "allclose",
        "ax",
        "bc",
        "boolean",
        "docstring",
        "dtype",
        "dx",
        "dy",
        "expr",
        "frisbee",
        "inv",
        "ipynb",
        "isclose",
        "itertools",
        "jupyter",
        "len",
        "nbs",
        "nd",
        "np",
        "numpy",
        "solveset",
        "sqrt",
        "sym",
        "sympy",
        "th",
    )
)

prose_exceptions = {
    "assets/nbs/assessment/mock/main.ipynb": set(
        (
            r"The matrix \\(D\\) is given by \\(D = \begin{pmatrix} a & 2 & 0\\ 3 & 1 & 2\\ 0 & -1 & 1\end{pmatrix}\\) where \\(a\ne 2\\).",
        ),
    ),
    "assets/nbs/assessment/mock/assignment.ipynb": set(
        (
            r"The matrix \\(D\\) is given by \\(D = \begin{pmatrix} a & 2 & 0\\ 3 & 1 & 2\\ 0 & -1 & 1\end{pmatrix}\\) where \\(a\ne 2\\).",
        )
    ),
    "assets/nbs/assessment/mock/solution.ipynb": set(
        (
            r"The matrix \\(D\\) is given by \\(D = \begin{pmatrix} a & 2 & 0\\ 3 & 1 & 2\\ 0 & -1 & 1\end{pmatrix}\\) where \\(a\ne 2\\).",
        )
    ),
}
prose_suggestions_to_ignore = {
    "assets/nbs/assessment/2020/main.ipynb": set(
        ("typography.symbols.curly_quotes", "garner.preferred_forms")
    ),
    "assets/nbs/assessment/2020/solution.ipynb": set(
        ("typography.symbols.curly_quotes", "garner.preferred_forms")
    ),
    "assets/nbs/assessment/mock/main.ipynb": set(
        ("typography.symbols.curly_quotes", "garner.preferred_forms")
    ),
    "assets/nbs/assessment/mock/assignment.ipynb": set(
        ("typography.symbols.curly_quotes", "garner.preferred_forms")
    ),
    "assets/nbs/assessment/mock/solution.ipynb": set(
        ("typography.symbols.curly_quotes", "garner.preferred_forms")
    ),
    "assets/nbs/assessment/example/main.ipynb": set(
        (
            "typography.symbols.curly_quotes",
            "typography.symbols.ellipsis",
            "garner.preferred_forms",
        )
    ),
}
