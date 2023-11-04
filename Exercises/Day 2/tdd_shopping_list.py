"""Making of class shopping cart for the backend of the shopping cart"""


class ShoppingList():
    """The `ShoppingList` class represents a shopping list object that allows users to add items with their
        quantities and units, and retrieve the items and their corresponding quantities with units."""

    def __init__(self, name: str, owner_name: str) -> None:
        """
        The function initializes an object with a name and owner name attribute.

        :param name: The name parameter is a string that represents the name of an object
        :type name: str
        :param owner_name: The `owner_name` parameter is a string that represents the name of the owner of
        an object
        :type owner_name: str
        """
        self.name = name
        self.owner_name = owner_name
        self.shopping_dictionary: dict = {}

    def add(self, item: str, quantity: int, unit: str) -> None:
        """
        The add function adds an item, its quantity, and unit to a shopping dictionary, but raises an error
        if the item is already in the list.

        :param item: The `item` parameter is a string that represents the name or description of the item
        being added to the shopping list
        :type item: str
        :param quantity: The parameter `quantity` represents the number of units of the item that you want
        to add to the shopping list
        :type quantity: int
        :param unit: The "unit" parameter in the "add" method represents the unit of measurement for the
        quantity of the item being added to the shopping list. It could be something like "kg", "lbs",
        "pieces", "liters", etc
        :type unit: str
        """
        if self.already_in_list(item):
            raise ValueError("Item is already in the list")

        self.shopping_dictionary[item] = str(quantity) + ":" + unit

    def get_length(self,) -> int:
        """
        The function `get_length` returns the length of the `shopping_dictionary`.
        :return: The length of the shopping dictionary.
        """
        return len(self.shopping_dictionary)

    def already_in_list(self, item: str) -> bool:
        """
        The function checks if an item is already in a shopping list dictionary.

        :param item: A string representing the item that we want to check if it is already in the shopping
        list
        :type item: str
        :return: a boolean value. It returns True if the item is already in the shopping_dictionary, and
        False otherwise.
        """
        return self.shopping_dictionary.get(item) is not None

    def get_items(self,) -> tuple[list[str], list[str]]:
        """
        The function "get_items" takes a shopping dictionary as input and returns two lists - one containing
        the items and another containing the quantity with unit for each item.
        :return: two lists: "items" and "quantity_with_unit".
        """
        items: list[str] = []
        quantity_with_unit: list[str] = []
        for key, value in self.shopping_dictionary.items():
            self.format_quantity_with_unit(quantity_with_unit, value)
            items.append(key)
        return (items, quantity_with_unit)

    def format_quantity_with_unit(self, quantity_with_unit: list[str], value: str) -> None:
        """
        The function `format_quantity_with_unit` takes a list `quantity_with_unit` and a string `value`,
        splits the string into `quantity` and `unit`, and appends the formatted quantity with unit to the
        list.

        :param quantity_with_unit: A list that will store the formatted quantity with unit values
        :param value: The `value` parameter is a string that contains a quantity and a unit separated by a
        colon. For example, it could be "5:kg" or "10:m"
        """
        quantity: str
        unit: str
        quantity, unit = value.split(":")
        quantity_with_unit.append(quantity + " " + unit)
