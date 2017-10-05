############################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #
#
# Algorithm:
#   Variable assignments
#   Prompt user for dayOfWeek
#   Get dayOfWeek
#   if dayOfWeek is Tuesday
#    ...
############################################################

import turtle

def make_window(colr, ttle):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, sz):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

def draw_square(t, sz):
     """Make turtle t draw a square of sz."""
     for i in range(4):
         t.forward(sz)
         t.left(90)
         

w = make_window("lightgreen", "HW6 (part 1)")
t = make_turtle("hotpink", 5)
t.speed(0)

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
