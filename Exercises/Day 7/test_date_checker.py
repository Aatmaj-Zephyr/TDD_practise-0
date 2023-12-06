"""Testing date checker"""
from date_checker import Date
import pytest


def test_new_date():
    """
    The function `test_new_date` creates a new instance of the `Date` class and asserts that it is an
    instance of the `Date` class.
    """
    date = Date(1, 1, 1)
    assert isinstance(date, Date)


# trunk-ignore(pylint/R0915)
def test_invalid_type_inputs_string_type():
    """
    The function `test_invalid_type_inputs_string_type()` tests for invalid type inputs in the `Date`
    class constructor.
    """
    with pytest.raises(TypeError) as error_info:
        Date("a", 1, 1)   # type: ignore
    assert error_info is not None

    with pytest.raises(TypeError) as error_info:
        Date(1, "a", 1)  # type: ignore
    assert error_info is not None

    with pytest.raises(TypeError) as error_info:
        Date(1, 1, "a")  # type: ignore
    assert error_info is not None


# trunk-ignore(pylint/R0915)
def test_negative_inputs():
    """
    The function `test_negative_inputs` tests if the `Date` class raises a `ValueError` when negative
    inputs are provided for the year, month, or day.
    """
    with pytest.raises(ValueError) as error_info:
        Date(-1, 1, 1)
    assert error_info is not None

    with pytest.raises(ValueError) as error_info:
        Date(1, -1, 1)
    assert error_info is not None

    with pytest.raises(ValueError) as error_info:
        Date(1, 1, -1)
    assert error_info is not None



# trunk-ignore(pylint/R0915)
def test_zero_inputs():
    """
    The function `test_zero_inputs` tests if the `Date` class raises a `ValueError` when any of the
    input arguments are zero.
    """
    with pytest.raises(ValueError) as error_info:
        Date(0, 1, 1)
    assert error_info is not None

    with pytest.raises(ValueError) as error_info:
        Date(1, 0, 1)
    assert error_info is not None

    with pytest.raises(ValueError) as error_info:
        Date(1, 1, 0)
    assert error_info is not None


def test_day_exceed_31():
    """
    The function `test_day_exceed_31` tests whether a `ValueError` is raised when creating a `Date`
    object with a day value greater than 31.
    """
    with pytest.raises(ValueError) as error_info:
        Date(32, 1, 1)
    assert error_info is not None


def test_month_exceed_12():
    """
    The function `test_month_exceed_12` tests whether a `ValueError` is raised when creating a `Date`
    object with a month value greater than 12.
    """
    with pytest.raises(ValueError) as error_info:
        Date(1, 13, 1)
    assert error_info is not None


def test_year_exceed():
    """
    The function `test_year_exceed` tests whether a `ValueError` is raised when trying to create a
    `Date` object with a year exceeding 20000.
    """
    with pytest.raises(ValueError) as error_info:
        Date(1, 1, 20001)
    assert error_info is not None


def test_at_upper_boundary_values():
    """
    The function tests if the Date class can handle upper boundary values for the day, month, and year.
    """

    date = Date(31, 12, 20000)
    assert isinstance(date, Date)


def test_month_with_30_days():
    """
    The function tests if the Date class can handle months with 30 days. Correct and incorrect values.
    """
    with pytest.raises(ValueError) as error_info:
        Date(31, 4, 1)
    assert error_info is not None

    date = Date(31, 1, 20000)
    assert isinstance(date, Date)

    date = Date(30, 1, 20000)
    assert isinstance(date, Date)


def test_feburary_for_31_and_30():
    """
    The function tests if an error is raised when trying to create a Date object with a day value of 31
    or 30 in the month of February.
    """
    with pytest.raises(ValueError) as error_info:
        Date(31, 2, 1)
    assert error_info is not None

    with pytest.raises(ValueError) as error_info:
        Date(30, 2, 1)
    assert error_info is not None


# trunk-ignore(pylint/R0915)
def test_feburary_for_non_leap_years():
    """
    The function tests that the Date class correctly raises a ValueError when trying to create a date
    with February 29th on a non-leap year, and that it successfully creates a Date object when given a
    valid date on a leap year.
    """
    with pytest.raises(ValueError) as error_info:
        Date(29, 2, 1)  # non leap
    assert error_info is not None

    with pytest.raises(ValueError) as error_info:
        Date(29, 2, 3)  # non leap
    assert error_info is not None

    with pytest.raises(ValueError) as error_info:
        Date(29, 2, 1990)  # non leap
    assert error_info is not None

    date = Date(29, 2, 4)  # leap
    assert isinstance(date, Date)


# trunk-ignore(pylint/R0915)
def test_feb_for_leap_year_atend_of_century():
    """
    The function `test_feb_for_leap_year_atend_of_century()` tests whether the `Date` class correctly
    handles leap years at the end of a century.
    """

    date = Date(29, 2, 400)  # leap
    assert isinstance(date, Date)

    date = Date(29, 2, 2000)  # leap
    assert isinstance(date, Date)

    with pytest.raises(ValueError) as error_info:
        Date(29, 2, 300)  # non leap
    assert error_info is not None

    with pytest.raises(ValueError) as error_info:
        Date(29, 2, 1900)  # non leap
    assert error_info is not None
