import pytest

from functions.level_4.three_promocodes import generate_promocode


@pytest.mark.parametrize('code_length', [0, 1, 5, 8, 10])
def test__three_promocodes__return_promo_code_with_passed_len(code_length):
    code = generate_promocode(code_length)
    assert len(code) == code_length
    assert isinstance(code, str) is True


def test__three_promocodes__return_promo_code_if_no_len_passed():
    code = generate_promocode()
    assert len(code) == 8
    assert isinstance(code, str) is True
    