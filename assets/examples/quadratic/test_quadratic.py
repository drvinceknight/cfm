import quadratic
import sympy


def test_discriminant_of_simple_quadratic():
    assert quadratic.discriminant(1, -3, 2) == 1


def test_discriminant_of_negative_case():
    assert quadratic.discriminant(1, 0, 1) == -4


def test_solutions_recovers_two_roots():
    x = sympy.Symbol("x")
    result = quadratic.solutions(1, -3, 2, x)
    assert result == sympy.FiniteSet(1, 2)


def test_solutions_of_repeated_root():
    x = sympy.Symbol("x")
    result = quadratic.solutions(1, -2, 1, x)
    assert result == sympy.FiniteSet(1)


def test_solutions_of_no_real_roots_is_empty():
    x = sympy.Symbol("x")
    result = quadratic.solutions(1, 0, 1, x)
    assert result == sympy.EmptySet


def test_number_of_real_roots_distinct():
    assert quadratic.number_of_real_roots(1, -3, 2) == 2


def test_number_of_real_roots_repeated():
    assert quadratic.number_of_real_roots(1, -2, 1) == 1


def test_number_of_real_roots_none():
    assert quadratic.number_of_real_roots(1, 0, 1) == 0


def test_vertex_of_canonical_parabola():
    x_vertex, y_vertex = quadratic.vertex(1, 0, 0)
    assert (x_vertex, y_vertex) == (0, 0)


def test_vertex_of_shifted_parabola():
    x_vertex, y_vertex = quadratic.vertex(1, -2, 1)
    assert (x_vertex, y_vertex) == (1, 0)


test_discriminant_of_simple_quadratic()
test_discriminant_of_negative_case()
test_solutions_recovers_two_roots()
test_solutions_of_repeated_root()
test_solutions_of_no_real_roots_is_empty()
test_number_of_real_roots_distinct()
test_number_of_real_roots_repeated()
test_number_of_real_roots_none()
test_vertex_of_canonical_parabola()
test_vertex_of_shifted_parabola()
