import datetime
import decimal
import pytest

from functions.level_3.models import Currency, Expense, ExpenseCategory, BankCard


@pytest.fixture
def create_expense():
    def inner(
            amount=decimal.Decimal('10.1'),
            currency=Currency.EUR,
            card=('1234', 'Owner'),
            spent_in='Magnit',
            spent_at=datetime.datetime.now(),
            category=ExpenseCategory.TRANSPORT):
        return Expense(
            amount=decimal.Decimal(amount),
            currency=currency,
            card=card,
            spent_in=spent_in,
            spent_at=spent_at,
            category=category
        )
    return inner
