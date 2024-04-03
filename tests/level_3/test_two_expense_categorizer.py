import pytest

from functions.level_3.models import ExpenseCategory
from functions.level_3.two_expense_categorizer import guess_expense_category, is_string_contains_trigger


@pytest.mark.parametrize('spent_in', ('asador', 'julis', 'doc', 'set', 'bastard'))
def test__guess_expense_category__bar_restaurant(create_expense, spent_in):
    expense_one = create_expense(spent_in=spent_in)
    assert guess_expense_category(expense_one) == ExpenseCategory.BAR_RESTAURANT


@pytest.mark.parametrize('spent_in', ('chinar', 'sas', 'green apple', 'meat house', 'clean house'))
def test__guess_expense_category__supermarket(create_expense, spent_in):
    expense_one = create_expense(spent_in=spent_in)
    assert guess_expense_category(expense_one) == ExpenseCategory.SUPERMARKET


@pytest.mark.parametrize('spent_in', ('apple.com/bill', 'leetcode.com', 'zoom.us', 'netflix'))
def test__guess_expense_category__online_subscription(create_expense, spent_in):
    expense_one = create_expense(spent_in=spent_in)
    assert guess_expense_category(expense_one) == ExpenseCategory.ONLINE_SUBSCRIPTIONS


@pytest.mark.parametrize('spent_in', ('farm', 'pharm', 'alfa-pharm', 'maname'))
def test__guess_expense_category__medicine_pharmacy(create_expense, spent_in):
    expense_one = create_expense(spent_in=spent_in)
    assert guess_expense_category(expense_one) == ExpenseCategory.MEDICINE_PHARMACY


@pytest.mark.parametrize('spent_in', ('tomsarkgh', 'moscow cinema', 'kino park', 'cinema galleria'))
def test__guess_expense_category__theatres_movies_culture(create_expense, spent_in):
    expense_one = create_expense(spent_in=spent_in)
    assert guess_expense_category(expense_one) == ExpenseCategory.THEATRES_MOVIES_CULTURE


@pytest.mark.parametrize('spent_in', ('gg platform', 'www.taxi.yandex.ru', 'bolt.eu', 'yandex go'))
def test__guess_expense_category__transport(create_expense, spent_in):
    expense_one = create_expense(spent_in=spent_in)
    assert guess_expense_category(expense_one) == ExpenseCategory.TRANSPORT


@pytest.mark.parametrize('spent_in', ('asado', 'hinar', 'apple.com', 'farmmmm', 'tomsarkg', 'www.taxi.yandex'))
def test__guess_expense_category__not_expecting_item(create_expense, spent_in):
    expense_one = create_expense(spent_in=spent_in)
    assert guess_expense_category(expense_one) is None


@pytest.mark.parametrize('original_string', (' Test', 'T est', 'Test ', ' Test ', '  Test  '))
def test__is_string_contains_trigger_delimeter_space(original_string):
    assert is_string_contains_trigger(original_string, 't') is True


@pytest.mark.parametrize('original_string', (',Test', 'T,est', 'Test,', ',Test,', ',,Test,,'))
def test__is_string_contains_trigger_delimeter_comma(original_string):
    assert is_string_contains_trigger(original_string, 't') is True


@pytest.mark.parametrize('original_string', ('.Test', 'T.est', 'Test.', '.Test.', '..Test..'))
def test__is_string_contains_trigger_delimeter_dot(original_string):
    assert is_string_contains_trigger(original_string, 't') is True


@pytest.mark.parametrize('original_string', ('-Test', 'T-est', 'Test-', '-Test-', '--Test--'))
def test__is_string_contains_trigger_delimeter_dash(original_string):
    assert is_string_contains_trigger(original_string, 't') is True


@pytest.mark.parametrize('original_string', ('/Test', 'T/est', 'Test/', '/Test/', '//Test//'))
def test__is_string_contains_trigger_delimeter_slash(original_string):
    assert is_string_contains_trigger(original_string, 't') is True


@pytest.mark.parametrize('original_string', (r'\Test', r'T\est', r'Test\\', r'\Test\\', r'\\Test\\'))
def test__is_string_contains_trigger_delimeter_back_slash(original_string):
    assert is_string_contains_trigger(original_string, 't') is True


def test__is_string_contains_trigger_equals_string():
    assert is_string_contains_trigger('t', 't') is True


def test__is_string_contains_trigger_no_trigger():
    assert is_string_contains_trigger('test', 'o') is False
    