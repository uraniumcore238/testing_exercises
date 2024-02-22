import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(("gender", 'verb'), [
    ('male', 'he'),
    ('female', 'she'),
    ('123', 'she'),
    (123, 'she'),
    (None, 'she'),
    (True, 'she'),
    (('male'), 'he'),
    (['male'], 'she'),
    (['male', 'female'], 'she'),
    (('female'), 'she'),
    (['female'], 'she'),
    (['female', 'male'], 'she')
])
def test_genderalize(gender, verb):
    assert genderalize('he', 'she', gender) == verb
