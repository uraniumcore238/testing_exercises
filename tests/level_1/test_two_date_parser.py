from datetime import datetime
import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize('date_str', ['today', 'yesterday'])
def test_compose_datetime_today_or_yesterday(date_str):
    assert compose_datetime_from(date_str, '11:22') == datetime(datetime.now().year, datetime.now().month, datetime.now().day, 11, 22)


def test_compose_datetime_tomorrow():
    assert compose_datetime_from('tomorrow', '11:22') == datetime(datetime.now().year, datetime.now().month, datetime.now().day+1, 11, 22)


@pytest.mark.parametrize('date_str', ['123', '', ' '])
def test_compose_datetime_from_improper_date_value(date_str):
    assert compose_datetime_from(date_str, '11:22') == datetime(datetime.now().year, datetime.now().month, datetime.now().day, 11, 22)


@pytest.mark.parametrize(('time_str', 'hour', 'minute'), [
    ('123', 1, 23),
    ('', 0, 0),
    ('12:77', 12, 77),
    ('77:12', 77, 12),
    (' : ', 0, 0)
])
def test_compose_datetime_from_improper_time_value(time_str, hour, minute):
    with pytest.raises(ValueError):
        assert compose_datetime_from('today', time_str) == datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour, minute)
