# HTTLaCS Ch. 3, problem #11

import turtle

# 11. Write a program to draw a 5-pointed star (with inner lines showing)

wn = turtle.Screen()   # initialize the window
wn.title("Star")
wn.bgcolor("cornsilk")

tess = turtle.Turtle() # initialize the turtle
tess.color("brown")
tess.pensize(5)

angle = (360 * 2) / 5
angle = int(angle)

length = 200

for i in range(5):
    tess.forward(length)
    tess.right(angle)

tess.hideturtle()

wn.mainloop()
