import datetime

from functions.level_3.three_is_subscription import is_subscription


def test__three_is_subscription__return_true_if_month_not_the_same(create_expense):
    expense_1 = create_expense(spent_at=datetime.datetime(2024, 1, 1))
    expense_2 = create_expense(spent_at=datetime.datetime(2024, 2, 1))
    expense_3 = create_expense(spent_at=datetime.datetime(2024, 3, 1))
    expense_4 = create_expense(spent_at=datetime.datetime(2024, 4, 1))
    expense_5 = create_expense(spent_at=datetime.datetime(2024, 5, 1))
    assert is_subscription(expense_1, [expense_2, expense_3, expense_4, expense_5]) is True


def test__three_is_subscription__return_false_if_months_are_the_same(create_expense):
    expense_1 = create_expense(spent_at=datetime.datetime(2024, 1, 1))
    expense_2 = create_expense(spent_at=datetime.datetime(2024, 1, 1))
    expense_3 = create_expense(spent_at=datetime.datetime(2024, 1, 1))
    expense_4 = create_expense(spent_at=datetime.datetime(2024, 1, 1))
    expense_5 = create_expense(spent_at=datetime.datetime(2024, 1, 1))
    assert is_subscription(expense_1, [expense_2, expense_3, expense_4, expense_5]) is False


def test__three_is_subscription__return_false_if_expenses_list_less_than_three(create_expense):
    expense_1 = create_expense(spent_at=datetime.datetime(2024, 1, 1))
    expense_2 = create_expense(spent_at=datetime.datetime(2024, 2, 1))
    expense_3 = create_expense(spent_at=datetime.datetime(2024, 3, 1))
    assert is_subscription(expense_1, [expense_2, expense_3]) is False



