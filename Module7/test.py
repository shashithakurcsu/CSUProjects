def find_sqrt_custom(number):
    if not isinstance(number, int) or number < 0:
        return "Input must be a non-negative integer."
    return number ** 0.5

print(find_sqrt_custom(9))  # Example usage

def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity