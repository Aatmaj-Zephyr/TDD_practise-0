"""
Testing of everything
"""


def calculate_power(base: int, exponent: int) -> int:
    """
    The function calculates the power of a given base raised to a given exponent.
    :param base: The base parameter represents the base number in a power operation. It is an integer
    value
    :type base: int
    :param exponent: The exponent parameter represents the power to which the base number will be raised
    :type exponent: int
    :return: the result of raising the base to the power of the exponent.
    """
    return base ** exponent


def calculate_sum(num1: int, num2: int) -> int:
    """
    Calculates the sum of two numbers.

    :param num1: The first number to be added in the sum.
    :param num2: The second number to be added in the sum.

    :return: The sum of num1 and num2.
    """
    return num1 + num2


def calculate_difference(num1: int, num2: int) -> int:
    """
    The function `calculate_difference` takes two integer inputs and returns the difference between
    them.

    :param num1: The `num1` parameter is an integer that represents the first number in the subtraction
    operation
    :type num1: int
    :param num2: The `num2` parameter is the second integer value that will be used to calculate the
    difference in the `calculate_difference` function
    :type num2: int
    :return: The function `calculate_difference` returns the difference between `num1` and `num2`.
    """
    
    return num2 - num1

def calculate_ratio(num1: int, num2: int) -> float:
    """
    Calculates the ratio of two numbers.
    """
    return num1 / num2

def fibonacci(n):
    """
    Generates a Fibonacci sequence up to n.
    """
    a = 0
    b = 1
    sequence = []
    while b < n:
        
        a, b = b, a + b
        sequence.append(a)
    return sequence

def fibonacii_of_prime(n):
    #this calculates the fibonacii number sequence upto the nth prime number

    #calculate the nth prime number
    i = 0
    num = 0
    while i < n:
        num +=1
        if isPrime(i):
            i += 1
    
    return fibonacci(num)

def isPrime(n):
    #this function checks whether a number is prime or not
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    else : 
        return True




