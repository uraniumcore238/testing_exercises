from functions.level_4.one_brackets import delete_remove_brackets_quotes


def test__one_brackets__return_the_same_string_if_there_is_no_brackets():
    assert delete_remove_brackets_quotes('Hello') == 'Hello'


def test__one_brackets__return_string_without_two_symbols_if_there_is_brackets_in_the_string():
    assert delete_remove_brackets_quotes('{{{Hello') == '{Hel'
