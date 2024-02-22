import datetime
from decimal import Decimal

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense():
    assert (parse_ineco_expense(
    SmsMessage(
        text='7777.55 EUR, '
             '8888 12.02.24 10:47 London authcode 123456',
        author='Alice', sent_at=datetime.datetime(2024, 2, 22, 12, 34, 56)

    ),
    [BankCard(last_digits='8888', owner='John Doe')]) ==
            Expense(amount=Decimal('7777.55'), card=BankCard(last_digits='8888', owner='John Doe'),
                    spent_in='London', spent_at=datetime.datetime(2024, 2, 12, 10, 47)))
