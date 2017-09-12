# HTTLaCS Ch. 3, problem #6

import turtle

# 6. Use for loops to make a turtle draw these regular polygons
# (regular means all sides the same lengths, all angles the same):
#     An equilateral triangle
#     A square
#     A hexagon (six sides)
#     An octagon (eight sides)

wn = turtle.Screen()   # initialize the window
wn.title("regular polygons")
wn.bgcolor("cornsilk")

tess = turtle.Turtle() # initialize the turtle
tess.color("brown")
tess.pensize(5)

tess.penup()           # move the start point to the left of the screen
tess.setpos(-400,0)
tess.pendown()

moveover = 30          # distance to move over for the next shape

#################
# draw a triangle
#################

sides = 3              # set variables for a triangle
angle = int(360 / sides)
length = 100

for i in range(sides): # draw the triangle
    tess.forward(length)
    tess.left(angle)

tess.penup()           # move over to draw a new shape
tess.forward(length + moveover)
tess.pendown()

###############
# draw a square
###############

sides = 4              # set variables for a square
angle = int(360 / sides)
length = 100

for i in range(sides): # draw the square
    tess.forward(length)
    tess.left(angle)

tess.penup()           # move over to draw a new shape
tess.forward(length + moveover)
tess.pendown()

################
# draw a hexagon
################

sides = 6              # set variables for a hexagon
angle = int(360 / sides)
length = 100

for i in range(sides): # draw the hexagon
    tess.forward(length)
    tess.left(angle)

tess.penup()           # move over to draw a new shape
tess.forward(length + moveover)
tess.pendown()

################
# draw a octagon
################

sides = 8              # set variables for a octagon
angle = int(360 / sides)
length = 100

for i in range(sides): # draw the octagon
    tess.forward(length)
    tess.left(angle)

wn.mainloop()

