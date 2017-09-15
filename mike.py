# convert a list of (x, y, 'm'|'d') tuples into turtle commands
# 'm' means move to (without drawing) (penup)
# 'd' means draw (pendown)

import turtle
import math

M = [ (31, 130, 'm'), (63, 92, 'd'), (80, 59, 'd'), (90, 30, 'd'), (86, 25, 'd'), (57, 27, 'd'),
      (68, 88, 'm'), (115, 42, 'd'), (145, 24, 'd'), (135, 42, 'd'), (101, 78, 'd'),
      (136, 48, 'd'), (169, 25, 'd'), (168, 36, 'd'), (145, 74, 'd'), (122, 106, 'd'),
      (120, 113, 'd'), (128, 120, 'd') ]

turtleAngle = 0 # initial direction the turtle is pointing (where 0 = pointing to the right)

turtleXY1 = M.pop(0) # initial coords of the turtle

wn = turtle.Screen()
wn.bgcolor('#adc3d6')
wn.title('Mike')

t = turtle.Turtle()
t.pensize(5)

while len(M) > 0:
    turtleXY2 = M.pop(0) # get a new destination point
    distance = math.sqrt( (turtleXY1[0] - turtleXY2[0])**2 + (turtleXY1[1] - turtleXY2[1])**2 ) # Pythagorean thm
    angle = math.atan((turtleXY1[1] - turtleXY2[1]) / (turtleXY1[0] - turtleXY2[0]))
    angle = math.degrees(angle)
    # so far, this should only work for angles between 0 and 90 degrees
    


wn.mainloop()




