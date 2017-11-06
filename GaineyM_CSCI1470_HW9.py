###############################################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #9
#
# YouTube video demonstration: https://youtu.be/0-jbnnvd0ZA
#
# Algorithm:
#
#   Import turtle to access turtle graphics.
#   Import random to access random numbers.
#
#   Define a function found_treasure that takes turtle_xpos and turtle_ypos as parameters.
#       Set within_xbound to True if turtle_xpos is between treasure_xpos and (treasure_xpos + TREASURESIZE).
#       Set within_ybound to True if turtle_ypos is between treasure_ypos and (treasure_ypos + TREASURESIZE).
#       Set found to True if within_xbound and within_ybound are True.
#       Return found to the calling function/program.
#
#
#   Define a function draw_rectangle that takes start_xpos, start_ypos, width, height, size, and color as parameters.
#       Set the turtle speed to 0 (fastest)
#       Make the turtle invisible
#       Raise the turtle's pen to prepare to move
#       Reposition the turtle to (start_xpos, start_ypos)
#       Lower the turtle's pen to prepare to write
#       Set the turtle's pen size to size
#       Set the turtle's color to color
#       Set the turtle's heading to 90 (facing north)
#       Start a loop that executes twice:
#           Have the turtle draw forward a distance of height
#           Have the turtle turn right 90 degrees
#           Have the turtle draw forward a distance of width
#           Have the turtle turn right 90 degrees
#
#
#   Define a function reveal_treasure_square that takes a parameter color
#       Set pensize to 5
#       Call the draw_rectangle function with aruments treasure_xpos, treasure_ypos,
#         TREASURESIZE, TREASURESIZE, pensize, and color
#
#
#   Set the constant FIELD_WIDTH to 800
#   Set the constant FIELD_HEIGHT to 600
#   Set the turtle window width to FIELD_WIDTH + 20 and window height to FIELD_HEIGHT + 20
#
#   Set window to an instance of the turtle object Screen
#   Set window's background color to a nice shade of green
#
#   Set field_min_x to 0 - (FIELD_WIDTH / 2)
#   Set field_max_x to (FIELD_WIDTH / 2)
#   Set field_min_y to 0 - (FIELD_HEIGHT / 2)
#   Set field_max_y to (FIELD_HEIGHT / 2)
#
#   Call draw_rectangle with arguments field_min_x, field_min_y, FIELD_WIDTH, FIELD_HEIGHT, 1, and 'black'
#
#   Set the constant TREASURESIZE to 300
#
#   Set treasure_xpos to a random integer from field_min_x to field_max_x - TREASURESIZE
#   Set treasure_ypos to a random integer from field_min_y to field_max_y - TREASURESIZE
#
#   Set mirtle to an instance of turtle object Turtle
#   Set mirtle's speed to 10 (really fast)
#
#   Set random_x to a random integer from field_min_x to field_max_x
#   Set random_y to a random integer from field_min_y to field_max_y
#   Set random_angle to a random integer from 0 to 359
#   Have mirtle raise her pen
#   Have mirtle move in the x direction to random_x
#   Have mirtle move in the y direction to random_y
#   Have mirtle lower per pen to prepare to write
#   Have mirtle spin around to the right 10 times + random_angle
#
#   Print instructions for the user
#
#   Set move_count to zero
#
#   Start the game loop
#
#       Set command to a string the user inputs
#       Set command to a list words in command
#
#       If the length of command is not 2, ...
#           Print an error message
#           and go back to the beginning of the loop
#
#       Set cmd to equal the first element of command
#       If cmd is not one of 'fd', 'bk', 'rt', or 'lt' ...
#           Print an error message
#           and go back to the beginning of the loop
#
#       Set arg to equal the second element of command
#       If arg contains anything other than only decimal characters, ...
#           Print an error message
#           and go back to the beginning of the loop
#       Set arg to the integer corresponding to the string arg
#
#       If cmd is 'fd' have mirtle draw forward a distance of arg
#       If cmd is 'bk' have mirtle draw backward a distance of arg
#       If cmd is 'rt' have mirtle turn to the right arg degrees
#       If cmd is 'lt' have mirtle turn to the left arg degrees
#
#       Increment move_count by 1
#
#       Set turtle_xpos to mirtle's x coordinate
#       Set turtle_ypos to mirtle's y coordinate
#       If a call to the found_treasure function with arguments turtle_xpos and turtle_ypos is True, ...
#
#           Print "You found the treasure in" move_count moves
#           Break out of the loop to celebrate
#
#   Set saved_position to mirtle's current position
#   Set saved_heading to mirtle's current heading
#
#   Call the reveal_treasure_square function with argument 'red'
#
#   Have mirtle raise her pen to prepare to move
#   Set mirtle's position to saved_position
#   Set mirtle's heading to saved_heading
#
#   Set the background picture to "treasure.png"
#
#   Get user input to wait until <Enter> is pressed
#   ... after which the program will end
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
field_max_y = (FIELD_HEIGHT / 2)     # top boundary

# draw a border around the game area
draw_rectangle(field_min_x, field_min_y, FIELD_WIDTH, FIELD_HEIGHT, size=1, color='black')

# set the side length of the treasure square
TREASURESIZE = 200

# define the lower-left corner of the treasure square (TREASURESIZE = side length)
treasure_xpos = random.randint(field_min_x, field_max_x - TREASURESIZE)
treasure_ypos = random.randint(field_min_y, field_max_y - TREASURESIZE)

# show the treasure square for testing
# reveal_treasure_square('blue')

# create the turtle
mirtle = turtle.Turtle()
mirtle.speed(10) # make a fast turtle

# put the turtle in a random starting position
random_x = random.randint(field_min_x, field_max_x)
random_y = random.randint(field_min_y, field_max_y)
random_angle = random.randint(0, 359)
mirtle.penup()
mirtle.setx(random_x)
mirtle.sety(random_y)
mirtle.pendown()
mirtle.right(360 * 10 + random_angle) # spin around 10 times plus a little more

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
        print("-- Enter a command and a numeric argument separated by a space.")
        continue # if not, ask again

    # catch unrecognized commands
    cmd = command[0]
    if cmd not in ['fd', 'bk', 'rt', 'lt']:
        print("-- You entered an unrecognized command.")
        continue # on unrecognized command, ask again

    # catch invalid arguments
    arg = command[1]
    if arg.isdecimal() != True:
        print("-- Your argument contained non-numeric characters.")
        continue # arg had characters other than decimal digits, ask again
    arg = int(arg)

    # execute the command
    if cmd == 'fd':
        mirtle.fd(arg)
    elif cmd == 'bk':
        mirtle.bk(arg)
    elif cmd == 'rt':
        mirtle.rt(arg)
    elif cmd == 'lt':
        mirtle.lt(arg)

    move_count += 1 # counting the number of moves to find the treasure

    # check to see if the treasure was found
    turtle_xpos = mirtle.xcor()
    turtle_ypos = mirtle.ycor()
    if found_treasure(turtle_xpos, turtle_ypos):

        print("\nYou found the treasure in {} move".format(move_count), end="")
        print("!") if move_count == 1 else print("s!")
        break # exit the loop and celebrate


# save the turtle position
saved_position = mirtle.pos() # returns a tuple
saved_heading = mirtle.heading()

# reveal the treasure square
reveal_treasure_square('red')

# restore the turtle position
mirtle.penup()
mirtle.setpos(saved_position)
mirtle.setheading(saved_heading)

# show the celebration picture
window.bgpic("treasure.png")

# the window persists until the user presses <Enter>
input("\nPress <Enter> to quit ")

# window.mainloop() # this doesn't seem to be needed
