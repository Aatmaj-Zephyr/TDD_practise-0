"""
Check if a date is valid or invalid. 
Use a class for a date. A new date can be made by making a new date object. 
If the value in the constructor is invalid, raise an exception.
"""


class Date:
    """Class representing date"""

    def __init__(self, day: int, month: int, year: int):
        self.check_if_input_values_are_positive_integers(day, month, year)
        self.check_if_valid_date(day, month, year)
        self.day = day
        self.month = month
        self.year = year

    def check_if_valid_date(self, day: int, month: int, year: int) -> None:
        """
        The function checks if a given date is valid by checking upper bounds, last day of the month, and
        specific rules for February.
        
        :param day: The `day` parameter represents the day of the month
        :type day: int
        :param month: The "month" parameter represents the month of a date. It is an integer value
        :type month: int
        :param year: The "year" parameter represents the year of the date being checked
        :type year: int
        """
        self.check_upper_bounds(day, month, year)
        self.check_last_day_of_month(day, month)
        if month == 2:
            self.check_feburary(day, month, year)

    def check_last_day_of_month(self, day: int, month: int) -> None:
        """
        The function checks if the given day is valid for the given month, and raises a ValueError if it
        is not.
        
        :param day: The `day` parameter represents the day of the month. It should be an integer value
        :type day: int
        :param month: The `month` parameter represents the month where January is 1, February is 2, etc
        :type month: int
        """
        months_with_31 = [1, 3, 5, 7, 8, 10, 12]
        if month not in months_with_31:
            if day == 31:
                raise ValueError("The month does not have 31 days")

    def check_feburary(self, day: int, month: int, year: int) -> None:
        """
        The function checks if a given date in February is valid, raising an error if the day is greater
        than 29 or if it is the 29th and the year is not a leap year.
        
        :param day: An integer representing the day of the month
        :type day: int
        :param month: The month parameter represents the month of the year. must be 2
        :type month: int
        :param year: The "year" parameter represents the year
        :type year: int
        """
        assert month == 2
        if day > 29:
            raise ValueError("February cannot have more than 29 days")
        if day == 29 and not self.is_leap_year(year):
            raise ValueError(f"Year {year} is not a leap year")

    def is_leap_year(self, year: int) -> bool:
        """
        The function checks if a given year is a leap year according to the rules.
        1) Check if the year is divisible by 4 and not divisible by 100
        2) Check if the year is divisible by 400 and not divisible by 100
        3) If any of the above conditions are true, the year is a leap year
        :param year: The "year" parameter is an integer representing the year.
        :type year: int
        :return: a boolean value indicating whether the given year is a leap year or not.
        """
        is_leap = False
        if year % 4 == 0:  # first check
            if year % 100 == 0 and year % 400 != 0:  # second check
                is_leap = False
            else:
                is_leap = True
        else:
            is_leap = False
        return is_leap

    def check_upper_bounds(self, day: int, month: int, year: int) -> None:
        """
        The function checks if the given day, month, and year values are within their respective upper
        bounds.

        :param day: An integer representing the day of the month
        :type day: int
        :param month: The "month" parameter represents the month of a date.
        :type month: int
        :param year: The "year" parameter represents the year value that needs to be checked for an
        :type year: int
        """
        self.check_day_upper_bound(day)
        self.check_month_upper_bound(month)
        self.check_year_upper_bound(year)

    def check_day_upper_bound(self, day: int) -> None:
        """
        The function `check_day_upper_bound` checks if the given day is greater than 31 and raises a
        `ValueError` if it is.

        :param day: The parameter "day" is an integer representing the day of the month
        :type day: int
        """
        if day > 31:
            raise ValueError("Day is out of range")

    def check_month_upper_bound(self, month: int) -> None:
        """
        The function `check_month_upper_bound` checks if the given month is greater than 12 and
        raises a `ValueError` if it is.

        :param month: The parameter "month" is an integer representing the month of a date
        :type month: int
        """
        if month > 12:
            raise ValueError("Month is out of range")

    def check_year_upper_bound(self, year: int) -> None:
        """
        The function checks if a given year is greater than 20000 and raises a ValueError if it is.

        :param year: The "year" parameter is an integer that represents a year
        :type year: int
        """
        if year > 20000:
            raise ValueError("Year is out of range")

    def check_if_input_values_are_positive_integers(self, day: int, month: int, year: int) -> None:
        """
        The function checks if the inputs for day, month, and year are positive integers else 
        raises typeerror (if not integer) or valueerror (if not positive)

        :param day: An integer representing the day of the month
        :type day: int
        :param month: The parameter "month" represents the month of a date. It should be an integer
        :type month: int
        :param year: The "year" parameter is an integer representing a year
        :type year: int
        """
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError("Inputs must be integers")
        if day < 1 or month < 1 or year < 1:
            raise ValueError("Input must be positive integer")
