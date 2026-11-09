# Shinade Marks
# 11/26
# P4LAB2
# Use while loop and for loop togther

'''
Get integer from user
Determines if the integer is even or odd
if positive, display mutiplication table
if negative, tell user to enter a positive integer
Ask user if they want to run the program again
if yes, repeat the program
if no, exit the program
'''

run_again = 'yes'

while run_again != 'no':

    user_num = int(input("Enter an integer: "))
    if user_num >= 0:
        for item in range(1, 13):
            print(f"{user_num} x {item} = {user_num * item}")
    else:
        print("Please enter a positive integer.")

    run_again = input("Do you want to run the program again? (yes/no): ")