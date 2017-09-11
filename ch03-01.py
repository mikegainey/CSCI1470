# HTTLaCS Ch 3
# Tk color list: http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

backgndcolor = input("Input background color: ")
tesscolor = input("Input turtle color: ")
linewidth = input("Input line width: ")
linewidth = int(linewidth)

import turtle            # allows us to use turtles
wn = turtle.Screen()     # creates a playground for turtles
wn.bgcolor(backgndcolor) # set the window background color
wn.title("Hello, Tess!") # set the window title

tess = turtle.Turtle()
tess.color(tesscolor)    # set color
tess.pensize(linewidth)  # set pen width

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()            # wait for user to close window

