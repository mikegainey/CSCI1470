############################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #6
#
# Algorithm:
#     blah, blah, blah, ...
#
############################################################

import turtle

def make_window(backgndColor, windowTitle):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    window = turtle.Screen()
    window.bgcolor(backgndColor)
    window.title(windowTitle)
    return window


def make_turtle(turtleColor, penWidth):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    newTurtle = turtle.Turtle()
    newTurtle.color(turtleColor)
    newTurtle.pensize(penWidth)
    return newTurtle


def draw_square(t, sideLength):
     """Make turtle t draw a square of sideLength."""
     for i in range(4):
         t.forward(sideLength)
         t.left(90)
         

w = make_window("lightgreen", "GaineyM_CSCI1470_HW6")
t = make_turtle("hotpink", 5)
t.speed(0)

# pre-position the turtle so the output will be centered on the screen
t.penup()
t.backward(160)
t.pendown()

# Part 1: Five little squares in a row

for square in range(5):
    draw_square(t, 20)
    t.penup()
    t.forward(40)
    t.pendown()


# Separate output from Part 1 and Part 2
t.penup()
t.forward(60)
t.pendown()


# Part 2
    
side = 20
for square in range(5):
    draw_square(t, side)
    
    t.penup()
    t.back(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()

    side += 20

    
w.mainloop()
