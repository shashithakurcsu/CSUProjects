# Here are given tip and tax percenatage
tip_percentage = 18
tax_percentage = 7

# Ask the user to enter the charge for the food
food_charge = float(input("Enter the charge for the food: $"))

# Calculate the tip and tax
tip = food_charge * tip_percentage / 100
tax = food_charge * tax_percentage / 100

# Calculate the total amount
total_amount = food_charge + tip + tax

# Display the results
print(f"Original Food Charge: ${food_charge:.2f}")
print(f"Tip ({tip_percentage}%): ${tip:.2f}")
print(f"Sales Tax ({tax_percentage}%): ${tax:.2f}")
print(f"Total Amount: ${total_amount:.2f}")
