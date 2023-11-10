"""
Decimal to binary conversion for positive numbers. FOr negative numbers it returns an error


"""


def to_binary(input_number: int) -> int:
    """
    The function converts a decimal number to its binary representation.
    
    :param input_number: The `input_number` parameter is an integer that represents the decimal number
    that you want to convert to binary
    :type input_number: int
    :return: the binary representation of the input number as an integer.
    """
    validate_input(input_number)
    power_of_two:int = highest_power_of_two(input_number)
    answer:int = 0
    while power_of_two != 0:
        answer *= 10
        answer += input_number // power_of_two
        input_number = input_number % power_of_two
        power_of_two = power_of_two // 2

    return answer

def validate_input(input_number:int)->None:
    """
    The function `validate_input` checks if the input number is less than 0 and raises a ValueError if
    it is.
    
    :param input_number: The input_number parameter is an integer that represents the number to be
    validated
    :type input_number: int
    """
    if input_number < 0:
        raise ValueError("input provided is not a correct")


def highest_power_of_two(input_number:int)->int:
    """
    The function `highest_power_of_two` returns the highest power of two that is less than or equal to
    the input number.
    
    :param input_number: The input_number parameter is an integer that represents the number for which
    we want to find the highest power of two
    :type input_number: int
    :return: the highest power of two that is less than or equal to the input number.
    """
    power_of_two = 1
    while power_of_two*2 <= input_number:
        power_of_two = power_of_two*2
    return power_of_two
