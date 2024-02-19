# This is a program to claculate average rainfall in a given number of years based on user input

#Intialization of variables; usage outside the loop
total_rainfall = 0
total_months = 0

# Prompt the user for the number of years and get input
num_years = int(input("Enter the number of years: "))

# Outer loop for each year
for year in range(1, num_years + 1):
    # Inner loop for each month of the year
    for month in range(1, 13):
        # Ask user for rainfall for the month. Rainfall can be in decimals
        rainfall = float(input(f"Enter the rainfall (in inches) for year {year}, month {month}: "))
        # Add to total rainfall
        total_rainfall = total_rainfall + rainfall
        # Increment total months
        total_months =  total_months + 1

# Calculate average rainfall. Handle the scenario if user enter <=0 years for division by 0 problem

if(num_years > 0):
    average_rainfall = total_rainfall / total_months
    # Display the results
    print(f"Total number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")
else:
    print(f"Invalid number of years entered: {num_years}. Therefore no calculation performed")