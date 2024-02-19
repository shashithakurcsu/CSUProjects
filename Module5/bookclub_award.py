# A program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.
#C Obtain user input for numbet of books

num_books_purchased = int(input("Enter the number of books you have purchased this month: "))

# Initialize the awards point variable
awards_point = 0

# Determine the awards point based on the number of books purchased
if num_books_purchased == 0 or num_books_purchased == 1:
    awards_point = 0
elif num_books_purchased == 2 or num_books_purchased == 3:
    awards_point = 5
elif num_books_purchased == 4 or num_books_purchased == 5:
    awards_point = 15
elif num_books_purchased == 6 or num_books_purchased == 7:
    awards_point = 30
elif num_books_purchased >= 8:
    awards_point = 60

# Display the number of points awarded
print(f"You have been awarded {awards_point} points.")

# End of the program