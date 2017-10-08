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

def make_window(color, title):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    newWindow = turtle.Screen() # make a new window
    newWindow.bgcolor(color)    # set the background color
    newWindow.title(title)      # set the title
    return newWindow            # give it back to the calling program


def make_turtle(color, size):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    newTurtle = turtle.Turtle() # make a new turtle
    newTurtle.color(color)      # set the color
    newTurtle.pensize(size)     # set the pen size
    return newTurtle            # give it back to the calling program


def draw_square(turtle, sideLength):
     """Make turtle turtle draw a square of sideLength."""

     for side in range(4):
         turtle.forward(sideLength) # draw a side
         turtle.left(90)            # turn left
         

# keyword arguments are clearer than positional arguments
window = make_window(color="lightgreen", title="GaineyM_CSCI1470_HW6")

# Introducing Mirtle, the turtle!
mirtle = make_turtle(color="hotpink", size=5)
mirtle.speed(0)

# pre-position mirtle so the output will be centered on the screen
mirtle.penup()
mirtle.backward(160)
mirtle.pendown()


######################################
# Part 1: Five little squares in a row
######################################

length = 20

for square in range(5):

    draw_square(turtle=mirtle, sideLength=length)

    # move to the next square
    mirtle.penup()
    mirtle.forward(40)
    mirtle.pendown()


# Separate the output from Part 1 and Part 2
mirtle.penup()
mirtle.forward(60)
mirtle.pendown()


############################
# Part 2: Concentric squares
############################

length = 20

for square in range(5):

    draw_square(turtle=mirtle, sideLength=length)

    # move (back and down) to the next (larger) square
    mirtle.penup()
    mirtle.back(10)
    mirtle.right(90)
    mirtle.forward(10)
    mirtle.left(90)
    mirtle.pendown()

    length += 20 # the next square will be larger


window.mainloop() # so the window doesn't disappear
