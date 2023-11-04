"""Testing of fizzbuzz function"""

from fizz_buzz import fizz, buzz, fizz_buzz



def test_fizz():
    """
    The function `test_fizz` tests the `fizz` function by asserting that it returns the correct output
    for different input values.
    """
    assert fizz(3) == "Fizz"
    assert fizz(4) == ""


def test_buzz():
    """
    The function `test_buzz()` tests the `buzz()` function by asserting that it returns "Buzz" when the
    input is 5 and returns an empty string when the input is 1.
    """
    assert buzz(5) == "Buzz"
    assert buzz(1) == ""

def test_fizz_buzz():
    """
    The function `test_fizz_buzz` tests the `fizz_buzz` function by asserting the expected output for
    different input values.
    """
    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(2) == ""
