class ShoppingCart:
    """
    A class to represent a shopping cart.

    Attributes
    ----------
    customer_name : str
        The name of the customer. Default is "none".
    current_date : str
        The current date. Default is "September 3, 2024".
    cart_items : list
        A list to store items in the shopping cart.

    Methods
    -------
    add_item(item):
        Adds an item to the shopping cart.
    remove_item(item_name):
        Removes an item from the shopping cart by its name.
    modify_item(item):
        Modifies an existing item's quantity, price, or description in the shopping cart.
    get_num_items_in_cart():
        Returns the total quantity of items in the shopping cart.
    get_cost_of_cart():
        Returns the total cost of all items in the shopping cart.
    print_total():
        Prints the total number of items, each item's cost, and the total cost of the cart.
    print_descriptions():
        Prints the descriptions of all items in the shopping cart.
    """

    def __init__(self, customer_name="none", current_date="September 3, 2024"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        """Adds an item to the shopping cart."""
        self.cart_items.append(item)

    def remove_item(self, item_name):
        """
        Removes an item from the shopping cart by its name.
        
        If the item is not found, prints a message indicating that nothing was removed.
        """
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        """
        Modifies an existing item's quantity, price, or description in the shopping cart.
        
        If the item is not found, prints a message indicating that nothing was modified.
        """
        item_found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                if item.item_quantity != 0:
                    self.cart_items[i].item_quantity = item.item_quantity
                if item.item_price != 0: 
                    self.cart_items[i].item_price = item.item_price
                if item.item_description != "": 
                    self.cart_items[i].item_description = item.item_description 
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        """Returns the total quantity of items in the shopping cart."""
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        """Returns the total cost of all items in the shopping cart."""
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        """
        Prints the total number of items, each item's cost, and the total cost of the cart.
        
        If the cart is empty, prints a message indicating that the shopping cart is empty.
        """
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        """
        Prints the descriptions of all items in the shopping cart.
        
        If the cart is empty, prints a message indicating that the shopping cart is empty.
        """
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("Item Descriptions")
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}")
