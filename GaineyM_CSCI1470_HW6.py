###############################################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #6
#
# Algorithm:
#     Import the turtle module to enable turtle graphics.
#
#     Define function make_window to make a turtle window of given color and title.
#         Instantiate a Screen object called newWindow.
#         Set newWindow's background color.
#         Set newWindow's title.
#         Return newWindow to the calling function/program.
#
#
#     Define function make_turtle to make a turtle of given color and pen size.
#         Instantiate a turtle object called newTurtle.
#         Set newTurtle's color.
#         Set newTurtle's pensize.
#         Return newTurtle to the calling function/program.
#
#
#     Define function draw_square to draw a square given a turtle and side length.
#         Begin a loop that repeats 4 times:
#             Have the turtle draw a line of length length.
#             Have the turtle turn 90 degrees to the left.
#
#
#     Instantiate a window called window with the make_window function.
#
#     Instantiate mirtle the turtle with the make_turtle function.
#     Set mirtle's speed to 0, the fastest speed.
#
#     Have mirtle lift her pen to preposition her for centered output.
#     Have mirtle back up 160 pixels.
#     Have mirtle lower her pen so she can draw.
#
#     Set the variable length to 20, the side length of subsequent squares.
#         Begin a loop that repeats 5 times (for 5 squares).
#
#             Call the draw_square function so mirtle will draw a square.
#
#             Have mirtle lift her pen to prepare to move.
#             Have mirtle move forward 40 pixels.
#             Have mirtle lower her pen to draw the next square.
#
#     Have mirtle lift her pen to prepare to move.
#     Have mirtle move forward 60 pixels to her next creation.
#     Have mirtle lower her pen to draw the next square.
#
#     Set the variable length to 20, the side length of her next square.
#     Begin a loop that repeats 5 times (for 5 squares).
#
#         Call the draw_square function so mirtle will draw a square of side-length length.
#
#         Have mirtle lift her pen to prepare to move.
#         Have mirtle move back 10 pixels.
#         Have mirtle turn right 90 degrees.
#         Have mirtle move forward 10 pixels.
#         Have mirtle turn left 90 degrees.
#         Have mirtle lower her pen to draw the next square.
#
#         Increase length by 20 so the next square will surround the previous one.
#
#     Enter the mainloop so the window will persist until the user closes it.
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


def draw_square(turtleObject, sideLength):
     """Make turtle turtleObject draw a square of sideLength."""

     for side in range(4):
         turtleObject.forward(sideLength) # draw a side
         turtleObject.left(90)            # turn left
         

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

    draw_square(turtleObject=mirtle, sideLength=length)

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

    draw_square(turtleObject=mirtle, sideLength=length)

    # move (back and down) to the next (larger) square
    mirtle.penup()
    mirtle.back(10)
    mirtle.right(90)
    mirtle.forward(10)
    mirtle.left(90)
    mirtle.pendown()

    length += 20 # the next square will be larger


window.mainloop() # so the window doesn't disappear
