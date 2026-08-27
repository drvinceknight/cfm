import continued_fractions
import sympy


def test_continued_fraction_of_three_halves():
    result = continued_fractions.continued_fraction(sympy.Rational(3, 2), 10)
    assert result == [1, 2]


def test_continued_fraction_of_twenty_two_sevenths():
    result = continued_fractions.continued_fraction(sympy.Rational(22, 7), 10)
    assert result == [3, 7]


def test_continued_fraction_terminates_for_rationals():
    coefficients = continued_fractions.continued_fraction(sympy.Rational(355, 113), 20)
    assert len(coefficients) < 20
    reconstructed = continued_fractions.convergents(coefficients)[-1]
    assert reconstructed == sympy.Rational(355, 113)


def test_convergents_of_golden_ratio_give_fibonacci_ratios():
    golden_convergents = continued_fractions.golden_ratio_convergents(6)
    expected = [
        sympy.Rational(1, 1),
        sympy.Rational(2, 1),
        sympy.Rational(3, 2),
        sympy.Rational(5, 3),
        sympy.Rational(8, 5),
        sympy.Rational(13, 8),
    ]
    assert golden_convergents == expected


def test_convergents_approach_golden_ratio():
    last = continued_fractions.golden_ratio_convergents(20)[-1]
    golden_ratio_value = (1 + 5**0.5) / 2
    error = abs(float(last) - golden_ratio_value)
    assert error < 1e-8


def test_convergents_of_finite_list():
    result = continued_fractions.convergents([3, 7])
    assert result == [sympy.Rational(3), sympy.Rational(22, 7)]


test_continued_fraction_of_three_halves()
test_continued_fraction_of_twenty_two_sevenths()
test_continued_fraction_terminates_for_rationals()
test_convergents_of_golden_ratio_give_fibonacci_ratios()
test_convergents_approach_golden_ratio()
test_convergents_of_finite_list()
