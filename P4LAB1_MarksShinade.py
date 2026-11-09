# Shinade Marks
# 11/26
# P4LAB1
# Use turtle and loops to draw a shape

import turtle

# Set up the turtle
pen = turtle.Turtle()
win = turtle.Screen()

# Set turtle options
pen.pensize(5)
pen.color("magenta")
pen.shape("arrow")

# square
for side in range(4):
    pen.forward(100)
    pen.right(90)

# triangle
sides = 3
while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

win.mainloop()