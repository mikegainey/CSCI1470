# HTTLaCS Ch. 3, problem #12

import turtle

# 12. Write a program to draw a face of a clock that looks something like this:
# URL: http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

wn = turtle.Screen()   # initialize the window
wn.title("clock face")
wn.bgcolor('#c6e8c2')

tess = turtle.Turtle() # initialize the turtle
tess.color("blue")
tess.shape("turtle")
tess.pensize(5)

length1 = 120 # to the beginning of the tick mark
length2 = 10  # length of the tick mark
length3 = 20  # space after the tick mark

angle = 360 / 12
angle = int(angle)

for i in range(12):
    tess.penup()
    tess.forward(length1) # move to the tick mark
    tess.pendown()
    tess.forward(length2) # draw the tick mark
    tess.penup()
    tess.forward(length3) # move out a little further
    tess.stamp()          # and stamp
    tess.backward(length3 + length2 + length1) # move backwards to the center
    tess.right(angle)                          # and rotate for the next hour

wn.mainloop()
