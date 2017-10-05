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

for square in range(5):
    draw_square(t, 20)
    t.penup()
    t.forward(40)
    t.pendown()

w.mainloop()
