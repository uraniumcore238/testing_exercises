import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(('text', 'replace_from', 'replace_to'), [
    ('one two three four five six', 'seven', 'seven'),
    ('one two three four five six', 'seven', 'one'),
    ('one two three four five six', '', 'one'),
    ('one two three four five six', '', ''),
    ('one two three four five six', ' ', ' ')
])
def test____five_replace_word____no_replacement_if_no_replace_from_in_the_text(text, replace_from, replace_to):
    assert replace_word(text, replace_from, replace_to) == text


@pytest.mark.parametrize(('text', 'replace_from', 'replace_to'), [
    ('one two three four five six', 'one', 'seven'),
    ('one two three four five six', 'one', 'two'),
    ('one two three four five six', 'one', ''),
    ('one two three four five six', 'one', ' ')
])
def test__five_replace_word__replacement_if_replace_from_is_in_the_text(text, replace_from, replace_to):
    removed_first_word = text.split(' ', 1)[1]
    assert replace_word(text, replace_from, replace_to) == f"{replace_to} {removed_first_word}"


def test__five_replace_word__replacement_without_changes_if_the_same_words_in_all_parameters():
    assert replace_word('one two three four five six', 'one', 'one') == 'one two three four five six'


@pytest.mark.parametrize(('text', 'replace_from', 'replace_to'), [
    ('one two three four five six', 'ONE', 'seven'),
    ('one two three four five six', 'one', 'TWO'),
    ('one two three four five six', 'ONE', ''),
    ('one two three four five six', 'ONE', ' '),
    ('ONE two three four five six', 'one', 'seven'),
])
def test__five_replace_word__replacement_if_replace_from_is_in_the_text_ignore_case(text, replace_from, replace_to):
    removed_first_word = text.split(' ', 1)[1]
    assert replace_word(text, replace_from, replace_to) == f"{replace_to} {removed_first_word}"