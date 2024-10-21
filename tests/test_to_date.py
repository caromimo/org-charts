from automatedorgcharts import convert_to_date
import datetime


def test_creates_datetime_object():
    date = convert_to_date("2024-08-30")
    assert isinstance(date, datetime.date)
