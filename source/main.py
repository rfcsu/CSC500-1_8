from item_to_purchase import ItemToPurchase
from shopping_cart import ShoppingCart

def print_menu(cart):
    """
    Displays a menu of options for the user to interact with the shopping cart.
    
    The menu includes options to add items, remove items, modify item quantities,
    output item descriptions, output the entire shopping cart, and quit the menu.

    Parameters
    ----------
    cart : ShoppingCart
        The shopping cart instance that the user is interacting with.
    
    User Input
    ----------
    a : str
        Adds an item to the shopping cart.
    r : str
        Removes an item from the shopping cart by item name.
    c : str
        Changes the quantity of an item in the shopping cart.
    i : str
        Outputs the descriptions of all items in the shopping cart.
    o : str
        Outputs the entire shopping cart including item costs and total cost.
    q : str
        Quits the menu and exits the program.
    """
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        choice = input("Choose an option:\n")

        if choice == 'q':
            break
        elif choice == 'o':
            cart.print_total()
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(new_item)
        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)
        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            modified_item = ItemToPurchase(item_name, 0, new_quantity) 
            cart.modify_item(modified_item)
        else:
            print("Invalid choice. Please try again.")


def main():
    """
    Main function to initialize a shopping cart and interact with it via the menu.
    
    Prompts the user to input the customer's name and the current date to create a
    ShoppingCart instance. Then, calls `print_menu` to allow the user to manage the
    shopping cart.
    """
    customer_name = input("\nEnter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)


if __name__ == "__main__":
    main()
