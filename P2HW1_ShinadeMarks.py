# Shinade Marks
#>/26
# P2HW1
# Calculating Travel Expenses (now with nice formatting)

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

print("---------Travel Expenses--------")

print(f'{"Destination: ":<15s} {destination:>}')
print(f'{"Initial Budget: ":<15s} ${budget:>.2f}')
print(f'{"Gas: ":<15s} ${gas:>.2f}')
print(f'{"Hotel: ":<15s} ${hotel:>.2f}')
print(f'{"Food: ":<15s} ${food:>.2f}')
print('-'*30)
print(f'{"Total Expenses: ":<15s} ${total_expenses:>.2f}')
print(f'{"Remaining Budget: ":<15s} ${remaining_budget:>.2f}')

print()