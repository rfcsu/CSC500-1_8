# Shopping Cart Application

This Python application simulates a basic shopping cart experience, allowing users to add, remove, and modify items, as well as view the cart's contents and total cost.

## How to Run

1. Change directory to `src`.
2. Run the script from your terminal: `python main.py`

## Implementation Choices

- **List for Cart Items:** The `cart_items` attribute within `ShoppingCart` is implemented as a Python list. This provides flexibility for adding, removing, and iterating through items efficiently.
- **Linear Search for Item Modification/Removal:**  When modifying or removing items, a linear search is performed through the `cart_items` list. While not the most optimal for large carts, it's suitable for this application's scale and keeps the implementation straightforward.
- **Object-Oriented Design:** The use of classes (`ItemToPurchase`, `ShoppingCart`) promotes code organization, encapsulation, and reusability, making the codebase easier to maintain and extend.
- **Input Validation:** Basic input validation is incorporated (e.g., checking for valid menu choices) to enhance the user experience and prevent potential errors.
- **Clear Output Formatting:** The `print_total()` and `print_descriptions()` methods employ formatted output to present information in a user-friendly manner.

## Program Details

- **`ItemToPurchase` Class:**
    - Represents individual items in the cart with attributes for name, price, quantity, and description.
    - `print_item_cost()` method neatly displays the item's cost breakdown.

- **`ShoppingCart` Class:**
    - Manages the overall shopping cart with attributes for customer name, date, and a list to store `ItemToPurchase` objects.
    - Key methods include:
        - `add_item()`: Appends an item to the cart.
        - `remove_item()`: Removes an item by name, handling potential "not found" scenarios.
        - `modify_item()`: Updates an item's quantity, price, or description if found.
        - `get_num_items_in_cart()`: Calculates the total quantity of items.
        - `get_cost_of_cart()`: Computes the total cost of items in the cart.
        - `print_total()`: Displays a formatted summary of the cart, including individual item costs and the grand total.
        - `print_descriptions()`: Lists item descriptions.

- **`print_menu()` Function:**
    - Presents a user-friendly menu with options to interact with the shopping cart.
    - Handles user input and calls appropriate `ShoppingCart` methods.
    - Employs a loop to continuously display the menu until the user chooses to quit.

- **`main()` Function:**
    - Initializes the program by:
        - Prompting for initial items and calculating their total cost (demonstrating `ItemToPurchase` usage).
        - Getting customer name and date.
        - Creating a `ShoppingCart` object.
        - Entering the main menu loop by calling `print_menu()`.

## Future Enhancements

- **Persistent Storage:** Implement saving and loading cart data to/from a file or database for a more realistic shopping experience.
- **Advanced Search:** Consider using a dictionary or a more efficient data structure for faster item lookup in larger carts.
- **Error Handling:** Add more robust error handling to gracefully manage unexpected user input or other potential issues.
- **Graphical User Interface (GUI):** Develop a GUI using a library like Tkinter or PyQt for a visually appealing and interactive shopping cart experience.
