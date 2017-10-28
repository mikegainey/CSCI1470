###############################################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #9
#
# Algorithm:
#
###############################################################################

import turtle
import random

def found_treasure(turtle_xpos, turtle_ypos):
    '''If the turtle is within the treasure square, return True.
       found_treasure(turtle_xpos : float, turtle_ypos : float) -> bool
       note: Numbers in the turtle world are floats! (therefore, the a <= b <= c)
    '''
    within_xbound = treasure_xpos <= turtle_xpos <= (treasure_xpos + TREASURESIZE)
    within_ybound = treasure_ypos <= turtle_ypos <= (treasure_ypos + TREASURESIZE)
    found = within_xbound and within_ybound
    return found


def draw_rectangle(start_xpos, start_ypos, width, height, size, color):
    '''Draw a rectangle starting from the bottom left corner, proceding clockwise.
       draw_rectangle(start_xpos : float, start_ypos : float, width : float, height : float,
                      size : float, color : str) -> NoneType (+ desired side effects)
    '''
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(start_xpos, start_ypos) # the bottom left corner
    turtle.pendown()
    turtle.pensize(size)
    turtle.color(color)
    turtle.setheading(90) # make the turtle point up
    for side in range(2):
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)


def reveal_treasure_square(color='red'): # default color is 'red'
    '''Reveal the treasure square after it has been found.
       reveal_treasure_square(color : str) -> NoneType (+ desired side effects)
    '''
    pensize = 5
    draw_rectangle(treasure_xpos, treasure_ypos, TREASURESIZE, TREASURESIZE, pensize, color)


# set the game area and window dimensions
FIELD_WIDTH = 800
FIELD_HEIGHT = 600
# set the window dimensions a bit bigger than the game area
turtle.setup(width=FIELD_WIDTH + 20, height=FIELD_HEIGHT + 20)

# create the screen
window = turtle.Screen()
window.bgcolor('#10b56d') # a nice green background
# window.screensize(FIELD_WIDTH, FIELD_HEIGHT) # this doesn't affect the windowsize (on my computer)!
# print("window width and height = {} x {}".format(window.window_width(), window.window_height()))

# set variables to define the limits of the game area
# note: (0, 0) is the middle of the screen
# (field_min_x, field_min_y) is the lower-left corner; (field_max_x, field_max_y) is the upper-right
field_min_x = 0 - (FIELD_WIDTH / 2)  # left boundary
field_max_x = (FIELD_WIDTH / 2)      # right boundary
field_min_y = 0 - (FIELD_HEIGHT / 2) # bottom boundary
field_max_y = (FIELD_HEIGHT /2)      # top boundary

# draw a border around the game area
draw_rectangle(field_min_x, field_min_y, FIELD_WIDTH, FIELD_HEIGHT, size=1, color='black')

# set the side length of the treasure square
TREASURESIZE = 300

# define the lower-left corner of the treasure square (TREASURESIZE = side length)
treasure_xpos = random.randint(field_min_x, field_max_x - TREASURESIZE)
treasure_ypos = random.randint(field_min_y, field_max_y - TREASURESIZE)

# show the treasure square for testing
# reveal_treasure_square('blue')

# create the turtle
tuttle = turtle.Turtle()
tuttle.speed(10) # make a fast turtle

# put the turtle in a random starting position
random_x = random.randint(field_min_x, field_max_x)
random_y = random.randint(field_min_y, field_max_y)
random_angle = random.randint(0,359)
tuttle.penup()
tuttle.setx(random_x)
tuttle.sety(random_y)
tuttle.pendown()
tuttle.color('black')
tuttle.right(360 * 10 + random_angle) # spin around 10 times plus a little more

print()
print("Enter commands for the turtle and find the treasure!")
print("(fd=forward, bk=back, rt=right, lt=left, plus a distance or angle as appropriate.)")
print()

move_count = 0 # to count the number of steps to find the treasure

# the game loop
while True:

    command = input("Turtle command: ")
    command = command.split() # command is a list: [two-letter command, distance or angle]

    # command should be a list of length 2
    if len(command) != 2:
        print("--Enter a command and a numeric argument separated by a space.\n")
        continue # if not, ask again

    # catch unrecognized commands
    cmd = command[0]
    if cmd not in ['fd', 'bk', 'rt', 'lt']:
        print("--You entered an unrecognized command.\n")
        continue # on unrecognized command, ask again

    # catch invalid arguments
    arg = command[1]
    if arg.isdecimal() != True:
        print("--Your argument contained non-numeric characters.\n")
        continue # arg had characters other than decimal digits, ask again
    arg = int(arg)

    # execute the command
    if cmd == 'fd':
        tuttle.fd(arg)
    elif cmd == 'bk':
        tuttle.bk(arg)
    elif cmd == 'rt':
        tuttle.rt(arg)
    elif cmd == 'lt':
        tuttle.lt(arg)

    move_count += 1 # counting the number of moves to find the treasure
    
    # check to see if the treasure was found
    turtle_xpos = tuttle.xcor()
    turtle_ypos = tuttle.ycor()
    if found_treasure(turtle_xpos, turtle_ypos):
        print("\nYou found the treasure in {} moves!".format(move_count))
        break # exit the loop and celebrate


# save the turtle position
saved_position = tuttle.pos() # returns a tuple
saved_heading = tuttle.heading()

# reveal the treasure square
reveal_treasure_square('red')

# restore the turtle position
tuttle.penup()
tuttle.setpos(saved_position)
tuttle.setheading(saved_heading)

# show the celebration picture
window.bgpic("treasure.png")

# the window persists until the user presses <Enter>
input("\nPress <Enter> to quit ")

# window.mainloop() # this doesn't seem to be needed
