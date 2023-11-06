"""Collatz conjectiure - cleaned up code. may look verbose but it is for practise"""
def collatz(input_number: int)->int:
    """
    The function collatz takes an input number and returns a new number based on the Collatz conjecture.
    
    :param input_number: The input_number parameter is an integer that represents the starting number
    for the Collatz sequence
    :type input_number: int
    :return: The function `collatz` is returning an integer value.
    """
    check_input_is_greater_than_0_else_error(input_number)
    output:int = -1
    if input_number%2==0:
        output = handel_even(input_number)
    else:
        output = handel_odd(input_number)
    return output

def check_input_is_greater_than_0_else_error(input_number:int)->None:
    """
    The function checks if the input number is greater than 0, otherwise it raises a ValueError.
    
    :param input_number: The input_number parameter is an integer that represents the number to be
    checked
    :type input_number: int
    """
    if input_number <= 0:
        raise ValueError("input provided is not a correct")

def handel_odd(input_number:int)->int:
    """
    The function `handel_odd` takes an input number and returns the result of multiplying it by 3 and
    adding 1.
    
    :param input_number: The input_number parameter is an integer that represents the number you want to
    handle
    :type input_number: int
    :return: the result of multiplying the input number by 3 and then adding 1.
    """
    return input_number*3 + 1

def handel_even(input_number:int)->int:
    """
    The function "handel_even" takes an input number and returns its integer division by 2.
    
    :param input_number: An integer number that needs to be divided by 2
    :type input_number: int
    :return: the input number divided by 2, rounded down to the nearest integer.
    """
    return input_number//2  # //2 to ensure that it will always equal integer (for type safety)
    