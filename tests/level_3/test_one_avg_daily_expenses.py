import decimal
import allure

from functions.level_3.models import Currency
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


@allure.id('id-1')
@allure.title('Assert that daily expenses amounts are sum correctly')
def test__one_avg_daily_expenses__sum_amount(create_expense):
    amount_1 = decimal.Decimal('10.3')
    amount_2 = decimal.Decimal('10.2')
    expense_one = create_expense(amount=amount_1)
    expense_two = create_expense(amount=amount_2)
    with allure.step(f'Assert that daily expense {amount_1} + daily expense {amount_2} =  total {amount_1+amount_2}'):
        assert calculate_average_daily_expenses([expense_one, expense_two]) == amount_1+amount_2


@allure.id('id-2')
@allure.title('Assert that daily expenses amounts are sum correctly with different currency')
def test__one_avg_daily_expenses__sum_amount_with_different_currency(create_expense):
    expense = create_expense()
    eur = Currency.EUR
    amd = Currency.AMD
    expense_one = create_expense(currency=eur)
    expense_two = create_expense(currency=amd)
    with allure.step(f'Assert that daily expense in {eur} + expense in {amd} = total {expense.amount*2}'):
        assert calculate_average_daily_expenses([expense_one, expense_two]) == expense.amount*2
