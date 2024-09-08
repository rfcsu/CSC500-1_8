class ItemToPurchase:
    """
    A class to represent an item to be purchased.

    Attributes
    ----------
    item_name : str
        The name of the item. Default is "none".
    item_price : float or int
        The price of a single item. Default is 0.
    item_quantity : int
        The quantity of the item to be purchased. Default is 0.
    item_description : str
        A brief description of the item. Default is an empty string.

    Methods
    -------
    print_item_cost():
        Prints the total cost of the item based on its price and quantity.
    """

    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description=""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description 

    def print_item_cost(self):
        """
        Prints the cost of the item based on its price and quantity in the format:
        'item_name item_quantity @ $item_price = $total_cost'
        """
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
