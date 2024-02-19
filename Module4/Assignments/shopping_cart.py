# Define class here with constructor to iniatlalize the attributes
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

# Define main here. The step 2 of program gies here.
def main():
# Obtain item1 details from user
    print("Item 1")
    item1_name = input("Enter the item name:\n")
    item1_price = float(input("Enter the item price:\n"))
    item1_quantity = int(input("Enter the item quantity:\n"))
    item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)
    print() # Insert an empty line here

# Obtain item2 details from user
    print("Item 2")
    item2_name = input("Enter the item name:\n")
    item2_price = float(input("Enter the item price:\n"))
    item2_quantity = int(input("Enter the item quantity:\n"))
    item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

# Step 3: Calculate and Output the Total Cost
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    total_cost = (item1_price * item1_quantity) + (item2_price * item2_quantity)
    print(f"Total: ${total_cost}")

if __name__ == "__main__":
    main()
