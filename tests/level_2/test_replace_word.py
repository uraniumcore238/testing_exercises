import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(('replace_from', 'replace_to'), [
    ('seven', 'seven'),
    ('one', 'one'),
    ('seven', 'one')
])
def test_five_replace_word_no_replacement(replace_from, replace_to):
    assert replace_word('one two three four five six', replace_from, replace_to) == 'one two three four five six'


@pytest.mark.parametrize(('replace_from', 'replace_to'), [
    ('one', 'seven'),
    ('one', 'two')
])
def test_five_replace_word_with_replacement(replace_from, replace_to):
    removed_first_word = 'two three four five six'
    assert replace_word('one two three four five six', replace_from, replace_to) == f"{replace_to} {removed_first_word}"