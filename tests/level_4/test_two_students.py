from functions.level_4.two_students import get_student_by_tg_nickname, Student


def test__two_students__return_none_if_username_is_not_the_same_as_tg_account():
    student = Student(first_name='Vasya', last_name='Osipov', telegram_account='@pacman')
    assert get_student_by_tg_nickname('mouse', [student]) is None


def test__two_students__return_student_if_username_is_the_same_as_tg_account():
    student = Student(first_name='Vasya', last_name='Osipov', telegram_account='@pacman')
    assert get_student_by_tg_nickname('pacman', [student]) == student
