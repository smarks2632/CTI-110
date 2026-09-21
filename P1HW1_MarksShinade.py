# Shinade Marks
# 9/18/26
# P1HW1
# Calculating exponents and addition and subtraction

# Calculaeting exponents
print("-----Exponents-----")
print()

base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent number: "))
result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result} !")

# Calculating addition and subtraction
print("-----Addition and Subtraction-----")
print()

num1 = int(input("Enter a starting number: "))
num2 = int(input("Enter a number to add: "))
num3 = int(input("Enter a number to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3

print(f"num1 + num2 - num3 = {final_result}!")