# HTTLaCS Ch 3 -- turtle graphics
# Tk color list: http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
                         
colors = ["blue", "red", "green"]

import turtle            # allows us to use turtles

wn = turtle.Screen()     # creates a playground for turtles
wn.bgcolor("cornsilk")   # set the window background color
wn.title("Hello, Tess!") # set the window title

tess = turtle.Turtle()
tess.color("blue")       # set color
tess.pensize(10)         # set pen width

# We can speed up or slow down the turtle’s animation speed. (Animation controls how quickly the turtle turns and moves
# forward).  Speed settings can be set between 1 (slowest) to 10 (fastest). But if we set the speed to 0, it has a special
# meaning — turn off animation and go as fast as possible.
tess.speed(5)

sides = 5                # make a pentagon

for i in range(sides):
    color = colors[i % len(colors)]
    tess.color(color)
    tess.forward(100)
    tess.left(360/sides)

wn.mainloop()            # wait for user to close window
