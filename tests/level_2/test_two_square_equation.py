import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(('square_coeff', 'linear_coeff', 'const_coeff', 'result'),[
    (0.0, 0.1, 0.1, (-1.0, None)),
    (0.0, 0.0, 0.1, (None, None)),
    (0.0, 0.0, 0.0, (None, None)),
    (0.0, -0.1, 0.1, (1.0, None)),
    (0.0, 0.1, -0.1, (1.0, None)),
    (0.0, -0.1, -0.1, (-1.0, None))
])
def test_two_square_zero_data(square_coeff, linear_coeff, const_coeff, result):
    assert solve_square_equation(square_coeff, linear_coeff, const_coeff) == result


@pytest.mark.parametrize(('square_coeff', 'linear_coeff', 'const_coeff', 'result'), [
    (1.0, 2.0, 1.0, (-1.0, -1.0)),
    (1.0, -2.0, 1.0, (1.0, 1.0)),
    (0.9, 0.1, 0.1, (None, None)),
    (0.1, 0.1, 0.9, (None, None)),
    (0.1, 0.1, 0.1, (None, None)),
    (-1.0, 2.0, 1.0, (2.414213562373095, -0.41421356237309515)),
    (0.9, -0.1, 0.1, (None, None)),
    (-0.1, 0.1, -0.9, (None, None)),
    (-0.1, -0.1, -0.1, (None, None))
])
def test_two_square_some_equal_coefficients(square_coeff, linear_coeff, const_coeff, result):
    assert solve_square_equation(square_coeff, linear_coeff, const_coeff) == result


@pytest.mark.parametrize(('square_coeff', 'linear_coeff', 'const_coeff', 'result'), [
    (0.01, 0.09, 0.01, (-8.88748219369606, -0.11251780630393907)),
    (-0.01, -0.09, -0.01, (-0.11251780630393907, -8.88748219369606))
])
def test_two_square(square_coeff, linear_coeff, const_coeff, result):
    assert solve_square_equation(square_coeff, linear_coeff, const_coeff) == result
