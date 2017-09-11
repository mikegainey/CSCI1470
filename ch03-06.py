# Every turtle can have its own shape. The ones available “out of the box” are
#   arrow, blank, circle, classic, square, triangle, turtle.


import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()                # This is new
size = 20
for i in range(30):
   tess.stamp()             # Leave an impression on the canvas
   size = size + 3          # Increase the size on every iteration
   tess.forward(size)       # Move tess along
   tess.right(24)           #  ...  and turn her

tess.right(360*10)

wn.mainloop()
