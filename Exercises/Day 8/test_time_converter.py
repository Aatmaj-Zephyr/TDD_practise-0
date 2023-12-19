"""Testing of timeconverter"""
from time_converter import convert


def test_seconds():
    """
    The function `test_seconds()` tests the `convert()` function by asserting that it returns the
    expected output for different input values.
    """
    assert convert(2) == [0, 0, 2]
    assert convert(59) == [0, 0, 59]


def test_minutes():
    """
    The function `test_minutes` tests the `convert` function by asserting that certain inputs return the
    expected outputs.
    """
    assert convert(60) == [0, 1, 0]
    assert convert(61) == [0, 1, 1]
    assert convert(90) == [0, 1, 30]
    assert convert(60*60-1) == [0, 59, 59]


def test_hours():
    """
    The function `test_hours()` tests the `convert()` function by asserting that certain inputs return
    the expected outputs.
    """

    assert convert(60*60) == [1, 0, 0]
    assert convert(60*60+60) == [1, 1, 0]
    assert convert(60*60+60*2) == [1, 2, 0]
    assert convert(60*60+1) == [1, 0, 1]
    assert convert(60*60+60+1) == [1, 1, 1]
