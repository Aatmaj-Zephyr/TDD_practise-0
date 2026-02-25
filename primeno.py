def is_prime(num: int) -> bool:
    """
    This Python function determines whether a given integer is a prime number or not.

    :param num: The `num` parameter in the `is_prime` function represents the integer number that we
    want to check for primality. The function will return `True` if the number is prime, and `False` if
    it is not prime
    :type num: int
    :return: The function `is_prime` returns a boolean value indicating whether the input number `num`
    is a prime number.
    """
    if num <= 1:
        return False

    flag = sum([num % i == 0 for i in range(2, int(num**0.5) + 1)])
    return flag < 1


print(is_prime(int(input("Please enter a number "))))
