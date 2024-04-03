from functions.level_4.four_lines_counter import count_lines_in


def test__four_line_counter__return_lines_quantity_in_the_file(file_path):
    assert count_lines_in(file_path) == 3


def test__four_line_counter__return_none_if_there_is_no_file():
    assert count_lines_in('') is None
    