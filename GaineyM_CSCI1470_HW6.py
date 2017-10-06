###############################################################################
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
###############################################################################

import turtle

def make_window(backgroundColor, windowTitle):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    window = turtle.Screen()        # make a new window
    window.bgcolor(backgroundColor) # set the background color
    window.title(windowTitle)       # set the title
    return window                   # give it back to the calling program


def make_turtle(turtleColor, penWidth):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    newTurtle = turtle.Turtle()  # make a new turtle
    newTurtle.color(turtleColor) # set the color
    newTurtle.pensize(penWidth)  # set the pen size
    return newTurtle             # give it back to the calling program


def draw_square(theTurtle, sideLength):
     """Make turtle theTurtle draw a square of sideLength."""

     for side in range(4):
         theTurtle.forward(sideLength) # draw a side
         theTurtle.left(90)            # turn left
         

window = make_window("lightgreen", "GaineyM_CSCI1470_HW6")

# Introducing Mirtle, the turtle!
mirtle = make_turtle("hotpink", 5)
mirtle.speed(0)

# pre-position the turtle so the output will be centered on the screen
mirtle.penup()
mirtle.backward(160)
mirtle.pendown()

# Part 1: Five little squares in a row
for square in range(5):

    draw_square(mirtle, 20)

    # move to the next square
    mirtle.penup()
    mirtle.forward(40)
    mirtle.pendown()


# Separate the output from Part 1 and Part 2
mirtle.penup()
mirtle.forward(60)
mirtle.pendown()


# Part 2: Concentric squares
    
sideLength = 20

for square in range(5):

    draw_square(mirtle, sideLength)

    # move (back and down) to the next (larger) square
    mirtle.penup()
    mirtle.back(10)
    mirtle.right(90)
    mirtle.forward(10)
    mirtle.left(90)
    mirtle.pendown()

    sideLength += 20 # the next square will be larger


window.mainloop() # so the window doesn't disappear
