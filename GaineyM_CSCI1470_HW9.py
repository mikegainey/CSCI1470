import turtle
import random

def found_treasure(turtlex, turtley):
    '''If the turtle is within the treasure square, return True.
       found_treasure(turtlex : int, turtley : int) -> bool
    '''
    withinx = treasurex <= turtlex < (treasurex + TREASURESIZE)
    withiny = treasurey <= turtley < (treasurey + TREASURESIZE)
    found = withinx and withiny
    return found


# draw a rectangle starting from the bottom left corner, going clockwise
def draw_rectangle(startx, starty, width, height, size, color):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(startx, starty) # the bottom left corner
    turtle.pendown()
    turtle.pensize(size)
    turtle.setheading(90) # make the turtle point up
    turtle.color(color)
    for i in range(2):
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
    turtle.showturtle()
    turtle.pensize(1)


def reveal_treasure_square(color='red'): # default color is 'red'
    draw_rectangle(treasurex, treasurey, TREASURESIZE, TREASURESIZE, 5, color)


# set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# set the window dimensions a bit bigger than the game area
turtle.setup(width=SCREEN_WIDTH+20, height=SCREEN_HEIGHT+20)

# create the screen
window = turtle.Screen()
# window.screensize(SCREEN_WIDTH, SCREEN_HEIGHT) # this doesn't affect the windowsize (on my computer)!
# print("window width and height = {} x {}".format(window.window_width(), window.window_height()))

# set variables to define the limits of the game area
# note: (0, 0) is the middle of the screen
# (winminx, winminy) is the lower-left corner; (winmaxx, winmaxy) is the upper-right
winminx = 0 - (SCREEN_WIDTH / 2)  # left boundary
winmaxx = (SCREEN_WIDTH / 2)      # right boundary
winminy = 0 - (SCREEN_HEIGHT / 2) # bottom boundary
winmaxy = (SCREEN_HEIGHT /2)      # top boundary

# draw a border around the game area
draw_rectangle(winminx, winminy, SCREEN_WIDTH, SCREEN_HEIGHT, 1, 'black')


TREASURESIZE = 300 # side length for the treasure square

# define the treasure square (TREASURESIZE = side length)
treasurex = random.randint(winminx, winmaxx - TREASURESIZE)
treasurey = random.randint(winminy, winmaxy - TREASURESIZE)

# show the treasure square for testing
# reveal_treasure_square('blue')


# create the turtle
tuttle = turtle.Turtle()
tuttle.speed(10) # Tuttle is a fast turtle

# put the turtle in a random starting spot
randx = random.randint(winminx, winmaxx)
randy = random.randint(winminy, winmaxy)
randangle = random.randint(0,359)
tuttle.penup()
tuttle.setx(randx)
tuttle.sety(randy)
tuttle.pendown()
tuttle.color('black')
tuttle.rt(360 * 10 + randangle) # spin around 10 times plus a little more

print()
print("Enter commands for the turtle and find the treasure!")
print()


# the game loop
while True:

    command = input("fd=forward, bk=back, rt=right, lt=left, plus a distance or angle as appropriate: ")
    command = command.split() # list: [two-letter command, distance or angle]

    # command should be a list of length 2
    if len(command) != 2:
        print("--Enter a two-character command and its argument\n")
        continue # if not, ask again

    # catch unrecognized commands
    cmd = command[0]
    if cmd not in ['fd', 'bk', 'rt', 'lt']:
        print("--Enter a two-character command and its argument\n")
        continue # on unrecognized command, ask again

    # catch invalid arguments
    arg = command[1]
    validArg = True
    for n in arg: # verify arg can be cast to an int
        validArg  = validArg and n.isdecimal()
    if validArg != True:
        print("--Enter a two-character command and its argument\n")
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

    # check to see if the treasure was found
    turtlex = tuttle.xcor()
    turtley = tuttle.ycor()
    if found_treasure(turtlex, turtley):
        print("\nYou found the treasure!")
        break # exit the loop and celebrate


# save the turtle position
saved_position = tuttle.pos() # returns a tuple
saved_heading = tuttle.heading()

# reveal the treasure square
reveal_treasure_square('red')

# restore the turtle position
tuttle.penup()
tuttle.color('black')
tuttle.setpos(saved_position)
tuttle.setheading(saved_heading)

# show the celebration picture
window.bgpic("treasure.png")

# the window persists until the user presses <Enter>
wait = input("\nPress <Enter> to quit ")
# turtle.bye() # this doesn't seem to be needed

# window.mainloop() # this doesn't seem to be needed
