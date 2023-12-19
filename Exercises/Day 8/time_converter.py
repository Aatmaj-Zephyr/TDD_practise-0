"""Program to convert seconds into hours, minutes and seconds"""

def convert(input_seconds: int) -> list[int]:
    """
    The function `convert` takes an input of seconds and returns a list of hours, minutes, and seconds.

    :param input_seconds: An integer representing the total number of seconds that you want to convert
    :type input_seconds: int
    :return: a list of integers with the number of hours, minutes, and seconds in the input_seconds.
    """
    seconds: int = 0
    minutes: int = 0
    hours: int = 0
    hours, input_seconds = divmod(input_seconds, 3600)
    minutes, seconds = divmod(input_seconds, 60)
    return [hours, minutes, seconds]
