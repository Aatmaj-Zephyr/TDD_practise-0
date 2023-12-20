"""Program to convert seconds into hours, minutes and seconds"""


def convert_seconds_to_days_hours_minutes_seconds(input_seconds: int) -> list[int]:
    """
    The function `convert` takes an input of seconds and returns a list of days, hours, minutes, and seconds.

    :param input_seconds: An integer representing the total number of seconds that you want to convert
    :type input_seconds: int
    :return: a list of integers as [days, hours, minutes, seconds]
    """
    seconds: int = 0
    minutes: int = 0
    hours: int = 0
    days: int = 0
    days, input_seconds = divmod(input_seconds, 24*3600)
    hours, input_seconds = divmod(input_seconds, 3600)
    minutes, seconds = divmod(input_seconds, 60)
    return [days, hours, minutes, seconds]
