import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex and Tess")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()

tess.forward(80) # tess draws an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)              # Turn tess around
tess.forward(80)             # Move her away from the origin

alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.mainloop()
