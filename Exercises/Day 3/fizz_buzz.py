"""
FizzBuzz is one of the most famous coding exercises for beginners. 
It is a simple exercise but an excellent one to start learning the TDD flow with.

Source https://tddmanifesto.com/exercises/
 
1. Write a “fizzBuzz” method that accepts a number as input and returns it as a String.

2. For multiples of three return “Fizz” instead of the number

3. For the multiples of five return “Buzz”

4. For numbers that are multiples of both three and five return “FizzBuzz”.
"""

def fizz(input_num:int)->str:
    """
    The function checks if the input number is divisible by 3 and returns "Fizz" if it is, otherwise it
    returns an empty string.
    
    :param input_num: An integer representing the input number
    :type input_num: int
    :return: the string "Fizz" if the input number is divisible by 3, otherwise it returns an empty
    string.
    """
    if input_num % 3 == 0:
        return "Fizz"
    return ""

def buzz(input_num:int)->str:
    """
    The function "buzz" returns the string "Buzz" if the input number is divisible by 5, otherwise it
    returns an empty string.
    
    :param input_num: An integer representing the input number
    :type input_num: int
    :return: the string "Buzz" if the input number is divisible by 5, otherwise it returns an empty
    string.
    """
    if input_num % 5 == 0:
        return "Buzz"
    return ""

def fizz_buzz(input_num:int)->str:
    """
    The function `fizz_buzz` takes an input number and returns a string that combines the results of the
    `fizz` and `buzz` functions.
    
    :param input_num: The input_num parameter is an integer that represents the number for which we want
    to determine if it is divisible by 3, 5, or both
    :type input_num: int
    :return: the result of calling the `fizz` function with the `input_num` argument, concatenated with
    a space, and then concatenated with the result of calling the `buzz` function with the `input_num`
    argument.
    """
    return fizz(input_num) + buzz(input_num)
