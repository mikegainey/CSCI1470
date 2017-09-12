############################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #2
#
# Algorithm:
#   Variable assignments
#   Draw M
#   Draw I
#   Draw K
#   Draw E
############################################################
# Due: to Blackboard by 11:59 pm Tuesday, September 19th

# Use turtle graphics to draw at least 4 different alphabetic characters of your choice across your output screen. Each
# character may be drawn using straight lines. Make sure that the characters are lined up in a row, not overlapping, and
# large enough to be read easily. Add a preface to your code that contains the following fields: Name, Course, Assignment,
# and Algorithm. Surround the preface with the '#' as shown in class. (10 points)

import turtle
import math

wn = turtle.Screen()   # make the window
wn.title("Mike")
wn.bgcolor('#d7edd5')

mike = turtle.Turtle() # make the turtle
mike.color('green')
mike.pensize(5)
mike.speed(10)

mike.penup()           # move the turtle to the starting point
mike.back(120)
mike.pendown()

# draw the "M"
mike.left(90)     # rotate before the first leg
mike.forward(120) # the left long leg
mike.right(90 + 60)
mike.forward(60)  # the left short segment
mike.left(60 + 60)
mike.forward(60)  # the right short segment
mike.right(60 + 90)
mike.forward(120) # the right long leg
mike.left(90)     # rotate for the next letter

# move to the next letter
mike.penup()
mike.forward(25)
mike.pendown()

# draw the "i"
mike.left(90) # rotate before the first leg
mike.forward(60) # the leg of the "i"
mike.penup()
mike.forward(10)
mike.pendown()
mike.forward(2) # the dot of the "i"
mike.penup()
mike.back(60 + 10 + 2)
mike.right(90) # rotate for the next letter

# move to the next letter
mike.penup()
mike.forward(25)
mike.pendown()

# draw the "k"
mike.left(90)     # rotate before the first leg
mike.forward(120) # the leg of the "k"
mike.back(70)
mike.right(40)
mike.forward(60)  # the top segment of the "k"
mike.back(60)
mike.right(50 + 45)
mike.forward(math.sqrt(50**2 + 50**2)) # the second leg of the "k"
mike.left(45)     # rotate for the next letter

# move to the next letter
mike.penup()
mike.forward(20)
mike.pendown()

# draw the "E" (because the lowercase version is too hard)
mike.left(90)
mike.forward(70) # the spine of the "E"
mike.right(90)
mike.forward(40) # the top segment
mike.back(40)
mike.right(90)
mike.forward(35)
mike.left(90)
mike.forward(30) # the middle segment
mike.back(30)
mike.right(90)
mike.forward(35)
mike.left(90)
mike.forward(40) # the bottom segment

mike.hideturtle()

wn.mainloop()
