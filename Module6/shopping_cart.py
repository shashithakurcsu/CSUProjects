# Define class here with constructor to iniatlalize the attributes. Build it on top of Module 4 assignement
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

# Define ShoppingCart class. It should have a parametrized constructor

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        item_found = False
        # Iterate through the items in the cart to find a match by name
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                item_found = True  # Mark as found

                # Check for non-default values and modify the item accordingly
                # Assuming default for description is "none", price is 0.0, and quantity is 0
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0.0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity

                break  # Exit the loop as we've found and processed the item

        if not item_found:
            print("Item not found in cart. Nothing modified.")


    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity
    
    def get_cost_of_cart(self):
        total_cost = 0  # Initialize total cost
        # Iterate over each item in the cart
        for item in self.cart_items:
            # Calculate the cost of the current item (price * quantity)
            item_cost = item.item_price * item.item_quantity
            # Add the cost of the current item to the total cost
            total_cost += item_cost
        # Return the total cost of the cart
        return total_cost
    
    def print_total(self):
        if len(self.cart_items) == 0:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            total_cost = 0
            for item in self.cart_items:
                total_cost += item.item_price * item.item_quantity
                item.print_item_cost()
            print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}")

# Here is teh  menu Shopping cart menu fucntionality for users
            
def print_menu(shopping_cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    option = ''
    while option != 'q':
        print(menu)
        option = input("Choose an option:\n")
        
        if option == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item_to_purchase = ItemToPurchase(item_name, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)
        
        elif option == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            shopping_cart.remove_item(item_name)
        
        elif option == 'c':
            print("CHANGE ITEM QUANTITY")
            # This functionality requires further specifics on how to implement.
            # Placeholder for implementation.
        
        elif option == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()
        
        elif option == 'o':
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    new_cart = ShoppingCart(customer_name, current_date)
    print_menu(new_cart)

if __name__ == "__main__":
    main()
