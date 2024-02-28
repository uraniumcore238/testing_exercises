import pytest

from functions.level_2.three_first import first


@pytest.mark.parametrize(('items', 'default', 'result'), [
    ([1, 2], 4, 1),
    ([1, 2], None, 1),
    ([1, 2], 'NOT_SET', 1),
    ([], 5, 5),
    ([], None, None)
])
def test_with_return_value(items, default, result):
    assert first(items, default) == result


def test_with_attribute_error():
    with pytest.raises(AttributeError):
        assert first([], 'NOT_SET') == 0
