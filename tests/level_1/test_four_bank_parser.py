import datetime
import pytest
from decimal import Decimal
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense_correct_data():
    assert (parse_ineco_expense(
    SmsMessage(
        text='7777.55 EUR, 8888 12.02.24 10:47 London authcode 123456',
        author='Alice', sent_at=datetime.datetime(2024, 2, 22, 12, 34, 56)),
    [BankCard(last_digits='8888', owner='John Doe')]) ==
            Expense(amount=Decimal('7777.55'), card=BankCard(last_digits='8888', owner='John Doe'),
                    spent_in='London', spent_at=datetime.datetime(2024, 2, 12, 10, 47)))



def test_parse_ineco_expense_int_sms_money_amount():
    assert (parse_ineco_expense(SmsMessage(
        text='777755 EUR, 8888 12.02.30 10:47 London authcode 123456',
        author='Alice', sent_at=datetime.datetime(2024, 2, 22, 12, 34, 56)),
    [BankCard(last_digits='8888', owner='John Doe')]) ==

            Expense(amount=Decimal('777755'), card=BankCard(last_digits='8888', owner='John Doe'),
                    spent_in='London', spent_at=datetime.datetime(2030, 2, 12, 10, 47)))


def test_parse_ineco_expense_sms_no_currency():
    with pytest.raises(IndexError):
        assert (parse_ineco_expense(SmsMessage(
            text='7777.55, 8888 12.02.30 10:47 London authcode 123456',
            author='Alice', sent_at=datetime.datetime(2024, 2, 22, 12, 34, 56)),
        [BankCard(last_digits='8888', owner='John Doe')]) ==

                Expense(amount=Decimal('7777.55'), card=BankCard(last_digits='8888', owner='John Doe'),
                        spent_in='London', spent_at=datetime.datetime(2030, 2, 12, 10, 47)))


def test_parse_ineco_expense_sms_no_auth_code():
    assert (parse_ineco_expense(SmsMessage(
        text='7777.55 EUR, 8888 12.02.30 10:47 London',
        author='Alice', sent_at=datetime.datetime(2024, 2, 22, 12, 34, 56)),
    [BankCard(last_digits='8888', owner='John Doe')]) ==

            Expense(amount=Decimal('7777.55'), card=BankCard(last_digits='8888', owner='John Doe'),
                    spent_in='London', spent_at=datetime.datetime(2030, 2, 12, 10, 47)))


def test_parse_ineco_expense_sms_no_card_last_digits():
    with pytest.raises(ValueError):
        assert (parse_ineco_expense(SmsMessage(
            text='7777.55 EUR, 12.02.30 10:47 London authcode 123456',
            author='Alice', sent_at=datetime.datetime(2024, 2, 22, 12, 34, 56)),
        [BankCard(last_digits='', owner='John Doe')]) ==

                Expense(amount=Decimal('7777.55'), card=BankCard(last_digits='', owner='John Doe'),
                        spent_in='London', spent_at=datetime.datetime(2030, 2, 12, 10, 47)))


def test_parse_ineco_expense_sms_wrong_date():
    with pytest.raises(ValueError):
        assert (parse_ineco_expense(
            SmsMessage(
                text='7777.55 EUR, 8888 40.02.24 10:47 London authcode 123456',
                author='Alice', sent_at=datetime.datetime(2024, 2, 22, 12, 34, 56)),
            [BankCard(last_digits='8888', owner='John Doe')]) ==
                Expense(amount=Decimal('7777.55'), card=BankCard(last_digits='8888', owner='John Doe'),
                        spent_in='London', spent_at=datetime.datetime(2024, 2, 40, 10, 47)))


def test_parse_ineco_expense_sms_wrong_time():
    with pytest.raises(ValueError):
        assert (parse_ineco_expense(
            SmsMessage(
                text='7777.55 EUR, 8888 20.02.24 50:47 London authcode 123456',
                author='Alice', sent_at=datetime.datetime(2024, 2, 22, 12, 34, 56)),
            [BankCard(last_digits='8888', owner='John Doe')]) ==
                Expense(amount=Decimal('7777.55'), card=BankCard(last_digits='8888', owner='John Doe'),
                        spent_in='London', spent_at=datetime.datetime(2024, 2, 20, 50, 47)))


def test_parse_ineco_expense_sms_empty_owner():
    assert (parse_ineco_expense(
        SmsMessage(
            text='7777.55 EUR, 8888 20.02.24 10:47 London authcode 123456',
            author='Alice', sent_at=datetime.datetime(2024, 2, 22, 12, 34, 56)),
        [BankCard(last_digits='8888', owner='')]) ==
            Expense(amount=Decimal('7777.55'), card=BankCard(last_digits='8888', owner=''),
                    spent_in='London', spent_at=datetime.datetime(2024, 2, 20, 10, 47)))