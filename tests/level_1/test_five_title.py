import pytest

from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(('title', 'result'), [
    ('Title', 'Copy of Title'),
    ('TitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitle6789',
     'Copy of TitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitle6789'), # Failed
    ('TITLE', 'Copy of TITLE'),
    ('TITLE ', 'Copy of TITLE '),
    (' TITLE ', 'Copy of  TITLE '),
    ('Title /!@# $%^&*()_+=- 098765432 1]\};`', 'Copy of Title /!@# $%^&*()_+=- 098765432 1]\};`')
])
def test_title_length_less_one_hundred(title, result):
    assert change_copy_item(title) == result


@pytest.mark.parametrize(('title', 'result'), [
    ('TitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitle',
     'TitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitle'),
    ('TitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitle1',
     'TitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitle1')
    ])
def test_title_length_more_or_equal_one_hundred(title, result):
    assert change_copy_item(title) == result


@pytest.mark.parametrize(('title', 'result'), [
    ('Copy of Title', 'Copy of Title (2)'),
    ('COPY OF Title', 'Copy of COPY OF Title'),
    ('Copy of Title (2)', f'Copy of Title (3)'),
    ('Copy Title', 'Copy of Copy Title'),
    ('Copy of Title (0)', f'Copy of Title (1)'),
    ('Copy of Title (-1)', f'Copy of Title (-1) (2)')
    ])
def test_title_contains_copy(title, result):
    assert change_copy_item(title) == result
