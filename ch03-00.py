import turtle            # allows us to use turtles
wn = turtle.Screen()     # creates a playground for turtles
wn.bgcolor("lightgreen") # set the window background color
wn.title("Hello, Tess!") # set the window title

alex = turtle.Turtle()   # creates a turtle; assign to alex

alex.forward(50)         # tell alex to move forward by 50 units
alex.left(90)            # tell alex to turn left 90 degrees
alex.forward(30)         # move forward 30 units

wn.mainloop()            # wait for user to close window

