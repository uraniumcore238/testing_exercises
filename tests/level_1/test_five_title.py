import pytest

from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(('title', 'result'), [
    ('Title', 'Copy of Title'),
    ('Tit19'*19, f'Copy of {"Tit19"*19}'), # Failed
    ('Tit20'*20, 'Tit20'*20),
    ('TITLE', 'Copy of TITLE'),
    ('Tit18'*18, f'Copy of {"Tit18"*18}'),
    ('Copy of Tit18', f'Copy of Tit18 (2)'),
    ('Copy of Title (1)', f'Copy of Title (2)'),
    ('Copy of Title (2)', f'Copy of Title (3)')
])
def test_change_copy_item(title, result):
    assert change_copy_item(title) == result
