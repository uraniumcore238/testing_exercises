from functions.level_2.two_square_equation import solve_square_equation


def test__two_square_equation__descriminant_less_than_zero():
    assert solve_square_equation(1.0, 0.1, 0.1) == (None, None)


def test__two_square_equation__no_square_coefficient():
    assert solve_square_equation(0.0, 0.1, 0.1) == (-1.0, None)


def test__two_square_equation__no_square_coefficient_and_no_linear_coefficient():
    assert solve_square_equation(0.0, 0.0, 0.1) == (None, None)


def test__two_square_equation__no_square_coefficient_and_no():
    assert solve_square_equation(0.1, 5.1, 0.1) == (-50.980384612481814, -0.019615387518183702)


def test__two_square_equation__descriminant_is_zero():  #
    assert solve_square_equation(2.0, 1.0, 1.0) == (None, None)

