from datetime import datetime
import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(('date_str', 'time_str', 'year', 'month', 'day', 'hours', 'minutes'), [
    ('today', '11:22', datetime.now().year, datetime.now().month, datetime.now().day, 11, 22),
    ('tomorrow', '11:22', datetime.now().year, datetime.now().month, datetime.now().day+1, 11, 22),
    ('yesterday', '11:22', datetime.now().year, datetime.now().month, datetime.now().day, 11, 22),
    ('123', '11:22', datetime.now().year, datetime.now().month, datetime.now().day, 11, 22),
    (123, '11:22', datetime.now().year, datetime.now().month, datetime.now().day, 11, 22),
    (True, '11:22', datetime.now().year, datetime.now().month, datetime.now().day, 11, 22),
    ('today', '00:01', datetime.now().year, datetime.now().month, datetime.now().day, 0, 1),
    ('tomorrow', '01:59', datetime.now().year, datetime.now().month, datetime.now().day+1, 1, 59),
    pytest.param('today', '99:99', datetime.now().year, datetime.now().month, datetime.now().day, 99, 99,
                 marks=pytest.mark.xfail(reason="Expected to fail", strict=True))
])
def test_compose_datetime_from(date_str, time_str, year, month, day, hours, minutes):
    assert compose_datetime_from(date_str, time_str) == datetime(year, month, day, hours, minutes)


