words = set(
    (
        "AttributeError",
        "Jupyter",
        "NameError",
        "ax",
        "bc",
        "docstring",
        "inv",
        "jupyter",
        "sym",
        "sympy",
    )
)

prose_exceptions = {
    "assets/nbs/assessment/mock/main.ipynb": set(
        (
            r"The matrix \\(D\\) is given by \\(D = \begin{pmatrix} a & 2 & 0\\ 3 & 1 & 2\\ 0 & -1 & 1\end{pmatrix}\\) where \\(a\ne 2\\).",
        )
    )
}
prose_suggestions_to_ignore = {
    "assets/nbs/assessment/mock/main.ipynb": set(("typography.symbols.curly_quotes",)),
}
