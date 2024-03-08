import pytest

from functions.level_2.three_first import first


@pytest.mark.parametrize(('items', 'default', 'expected'), [
    ([1, 2], 4, 1),
    ([1, 2], None, 1),
    ([1, 2], 'NOT_SET', 1),
    ([], 5, 5),
    ([], None, None)
])
def test__three_first__with_return_value(items, default, expected):
    assert first(items, default) == expected


def test__three_first__attribute_error_if_default_equals_not_set_and_no_items():
    with pytest.raises(AttributeError):
        assert first([], 'NOT_SET') == 0
