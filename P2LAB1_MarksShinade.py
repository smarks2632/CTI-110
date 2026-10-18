# Shinade Marks
# 10/26
# P2LAB1
# Calculates the diameter, circumference, and area of a circle


import math

# user inputs radius
radius = float(input("What is the radius of the circle? "))
print()

# calculate the diameter
diameter = 2 * radius

# calculate the circumference
circumference = 2 * math.pi * radius

# calculate the area
area = math.pi * radius ** 2

print(f"The diameter of the circle is {diameter:.1f}\n")
print(f"The circumference of the circle is {circumference:.2f}\n")
print(f"The area of the circle is {area:.3f}")