# Shinade Marks
# 9/18/26
# P1HW2
# Calculating Travel Expenses

# Calculates the total expenses and remaining budget for a trip based on user input
print("This program calculates and displays travel expenses")
print()

budget=int(input("Enter your travel budget: "))
destination=input("Enter your travel destination: ")
gas=int(input("How much do you think you will spend on gas: "))
hotel=int(input("How much do you think you will spend on hotel accomodations: "))
food=int(input("How much do you think you will spend on food: "))

total_expenses = gas + hotel + food
remaining_budget = budget - total_expenses

print("-----Travel Expenses-----")
print()

print(f"Destination: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Total Expenses: {total_expenses}")
print(f"Remaining Budget: {remaining_budget}")