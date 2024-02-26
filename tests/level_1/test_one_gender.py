import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(("gender", 'verb'), [
    ('male', 'he'),
    ('male ', 'she'),
    (' male ', 'she'),
    ('ma le', 'she')
])
def test_genderalize_male(gender, verb):
    assert genderalize('he', 'she', gender) == verb


@pytest.mark.parametrize(("gender", 'verb'), [
    ('female', 'she'),
    ('fem', 'she'),
    ('female1', 'she'),
    ('mal', 'she'),
    ('male1', 'she'),
    ('123', 'she'),
    ('', 'she')
])
def test_genderalize_not_male(gender, verb):
    assert genderalize('he', 'she', gender) == verb
