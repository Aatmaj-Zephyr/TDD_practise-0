"""Testing of timeconverter"""
from time_converter import convert_seconds_to_days_hours_minutes_seconds


def test_seconds():
    """
    The function `test_seconds()` tests the `convert()` function by asserting that it returns the
    expected output for different input values.
    """
    assert convert_seconds_to_days_hours_minutes_seconds(2) == [0, 0, 0, 2]
    assert convert_seconds_to_days_hours_minutes_seconds(59) == [0, 0, 0, 59]


def test_minutes():
    """
    The function `test_minutes` tests the `convert` function by asserting that certain inputs return the
    expected outputs.
    """
    assert convert_seconds_to_days_hours_minutes_seconds(60) == [0, 0, 1, 0]
    assert convert_seconds_to_days_hours_minutes_seconds(61) == [0, 0, 1, 1]
    assert convert_seconds_to_days_hours_minutes_seconds(90) == [0, 0, 1, 30]
    assert convert_seconds_to_days_hours_minutes_seconds(
        60*60-1) == [0, 0, 59, 59]


def test_hours():
    """
    The function `test_hours()` tests the `convert()` function by asserting that certain inputs return
    the expected outputs.
    """

    assert convert_seconds_to_days_hours_minutes_seconds(60*60) == [0, 1, 0, 0]
    assert convert_seconds_to_days_hours_minutes_seconds(
        60*60+60) == [0, 1, 1, 0]
    assert convert_seconds_to_days_hours_minutes_seconds(
        60*60+60*2) == [0, 1, 2, 0]
    assert convert_seconds_to_days_hours_minutes_seconds(
        60*60+1) == [0, 1, 0, 1]
    assert convert_seconds_to_days_hours_minutes_seconds(
        60*60+60+1) == [0, 1, 1, 1]
    assert convert_seconds_to_days_hours_minutes_seconds(
        23*60*60+1) == [0, 23, 0, 1]
    assert convert_seconds_to_days_hours_minutes_seconds(
        24*60*60-1) == [0, 23, 59, 59]


def test_days():
    """
    The function `test_days()` tests the `convert()` function by asserting that certain inputs return
    the expected outputs.
    """
    assert convert_seconds_to_days_hours_minutes_seconds(
        24*60*60) == [1, 0, 0, 0]
    assert convert_seconds_to_days_hours_minutes_seconds(
        2*24*60*60) == [2, 0, 0, 0]
    assert convert_seconds_to_days_hours_minutes_seconds(
        24*60*60+60*60+60+1) == [1, 1, 1, 1]
    assert convert_seconds_to_days_hours_minutes_seconds(
        24*60*60+60+1) == [1, 0, 1, 1]
