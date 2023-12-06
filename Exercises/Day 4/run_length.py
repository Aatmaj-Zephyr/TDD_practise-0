"""Run length encoding
eg 1111000000 becomes 1406"""


def rle(input_string: str) -> str:
    """
    The function `rle` takes an input string, validates it, and then processes it using the RLE
    (Run-Length Encoding) algorithm, returning the encoded output.

    :param input_string: Input for the RLE (Run-Length Encoding) algorithm
    :type input_string: str
    :return: The function `rle` is returning the variable `output`, which is a string.
    """
    if input_string_validate(input_string) is not True:
        raise ValueError("input provided is not a correct")
    output = process(input_string)

    return output


def process(input_string: str) -> str:
    """
    The function takes an input string, finds the unique characters in the string, and returns a string
    where each character is followed by the number of times it appears consecutively in the input
    string.

    :param input_string: The input_string parameter is a string that contains a sequence of characters
    :type input_string: str
    :return: a processed version of the input string.
    """
    output: str = ""
    unique_number_string: list[str] = make_list_of_continuouse_same_numbers(
        input_string)  # eg. ['1111','22222']
    for string in unique_number_string:
        output += string[0]+str(len(string))
    return output


def make_list_of_continuouse_same_numbers(input_string: str) -> list[str]:
    """
    The function `make_list_of_continuous_same_numbers` takes an input string and returns a list of
    strings, where each string represents a sequence of continuous same numbers in the input string.
    
    :param input_string: The input_string parameter is a string that contains a sequence of numbers
    :type input_string: str
    :return: The function `make_list_of_continuouse_same_numbers` returns a list of strings.
    """

    previous_number_string: str = "_"
    strings_of_unique_nums: list[str] = []  # eg ['1111','22222']

    for number in input_string:
        if number not in previous_number_string:   # unique number
            strings_of_unique_nums.append(previous_number_string)
            previous_number_string = ""  # clear prev_number_string
        previous_number_string += number

    strings_of_unique_nums.append(previous_number_string)  # append last one
    return strings_of_unique_nums[1:]  # initial blank ["_"] must be removed


def input_string_validate(input_string: str) -> bool:
    """
    The function `input_string_validate` checks if all characters in the input string are digits and
    returns True if they are, and False otherwise.

    :param input_string: The input_string parameter is a string that you want to validate
    :type input_string: str
    :return: A boolean value returns true if all characters in the input string are digits, and False otherwise.
    """
    for i in input_string:
        if i.isdigit() is not True:
            return False
    return True
