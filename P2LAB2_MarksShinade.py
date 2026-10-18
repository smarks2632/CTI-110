# Shinade Marks
# 10/26
# P2LAB2
# Using dictionaries

cars = {'Camero': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}
print()

car_keys = cars.keys()

print(car_keys)

print(*car_keys, sep=', ')

# User input to get a car name and display the corresponding MPG value
car_name = input("Enter a car: ")

# Get the mpg value for the entered car name
car_mpg = cars.get(car_name)
print(f"The {car_name} gets {car_mpg} mpg.")

# User input to get the number of miles they will drive
miles = float(input(f"How many miles will you drive the {car_name}? "))

# Calculate the amount of gas needed for the trip
gas_needed = miles / car_mpg

# Display the total cost of gas for the trip
print(f"{gas_needed:.2f} gallon(s) of gas is needed to drive {car_name} {miles} miles.")