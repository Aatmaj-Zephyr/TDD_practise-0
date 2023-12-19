"""Testing of the shopping list class"""

import pytest
from tdd_shopping_list import ShoppingList



@pytest.fixture(name="my_fruit_shopping_list")
def fixture_my_fruit_shopping_list():
    """
    The function `fixture_my_fruit_shopping_list` returns a `ShoppingList` object with the name "Fruits"
    and owner "Aatmaj".
    :return: R `ShoppingList` object with the name "Fruits" and owner "Aatmaj".
    """
    return ShoppingList("Fruits", "Aatmaj")

def test_for_inititialization_of_shopping_list(my_fruit_shopping_list):
    """
    The function is testing the initialization of a shopping list object and checking if it is none or not
    """


    assert my_fruit_shopping_list is not None


def test_adding_an_item_and_checking_length_of_shopping_list(my_fruit_shopping_list):
    """
    The function adds a banana to the shopping list with a values and checking its length
    """

    my_fruit_shopping_list.add("banana", 5, "Units")
    assert my_fruit_shopping_list.get_length() == 1


def test_adding_repeative_items_raises_error(my_fruit_shopping_list):
    """
    The function tests whether adding repetitive items to a shopping list raises a ValueError.
    """

    with pytest.raises(ValueError) as error_info:
        my_fruit_shopping_list.add("banana", 5, "Units")
        my_fruit_shopping_list.add("banana", 5, "Units")
    assert error_info is not None


def test_is_in_list(my_fruit_shopping_list):
    """
    The function `test_is_in_list` tests whether the item is already in the shopping list by invoking function 
    of the class correctly done by function or not
    """
    my_fruit_shopping_list.add("banana", 5, "Units")
    assert my_fruit_shopping_list.already_in_list("banana") is True



def test_get_list_many_items(my_fruit_shopping_list):
    """
    The function `test_get_list_many_items` tests the `get_items` method of the `my_fruit_shopping_list`
    object by adding two items to the list and checking if the returned item and quantity lists match
    the expected values.
    """
    my_fruit_shopping_list.add("banana", 5, "Units")
    my_fruit_shopping_list.add("apple", 1, "kg")
    item:list[str]
    quantity:list[str]
    item, quantity = my_fruit_shopping_list.get_items()
    assert item == ["banana", "apple"] and quantity == ["5 Units", "1 kg"]
