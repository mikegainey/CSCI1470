import turtle
import random

def found_treasure(turtlex, turtley):
    '''If the turtle is within the treasure square, return True
       found_treasure(turtlex : int, turtley : int) -> bool
    '''
    # print("Treasure corner is ({:.1f}, {:.1f}). Turtle is at ({:.1f}, {:.1f})" # for testing
    #       .format(treasurex, treasurey, turtlex, turtley))
    withinx = treasurex <= turtlex < (treasurex + TREASURESIZE)
    withiny = treasurey <= turtley < (treasurey + TREASURESIZE)
    return withinx and withiny


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
turtle.setup(width=SCREEN_WIDTH+20, height=SCREEN_HEIGHT+20) # set the window dimensions a bit bigger than the game area

# note: (0, 0) is the middle of the screen
# (minx, miny) is the lower-left; (maxx, maxy) is the upper-right
winminx = 0 - (SCREEN_WIDTH / 2)  # left bound
winmaxx = (SCREEN_WIDTH /2)       # right bound
winminy = 0 - (SCREEN_HEIGHT / 2) # lower bound
winmaxy = (SCREEN_HEIGHT /2)      # upper bound

TREASURESIZE = 300 # side length for the treasure square

# create the screen
window = turtle.Screen()
# window.screensize(SCREEN_WIDTH, SCREEN_HEIGHT) # this doesn't affect the windowsize (on my computer)!
# print("window width and height = {} x {}".format(window.window_width(), window.window_height()))

# create the turtle
tuttle = turtle.Turtle()
tuttle.speed(10) # Tuttle is a fast turtle

# draw a border around the game area
tuttle.penup()
tuttle.goto(winminx, winminy) # the bottom left corner of the game area
tuttle.pendown()
tuttle.setheading(90) # make the turtle point up
tuttle.color('black')
for i in range(2):
    tuttle.forward(SCREEN_HEIGHT)
    tuttle.right(90)
    tuttle.forward(SCREEN_WIDTH)
    tuttle.right(90)

# define the treasure square (see TREASURESIZE constant)
treasurex = random.randint(winminx, winmaxx - TREASURESIZE)
treasurey = random.randint(winminy, winmaxy - TREASURESIZE)

# draw the treasure square for testing
tuttle.penup()
tuttle.goto(treasurex, treasurey) # the bottom left corner of the treasure square
tuttle.pendown()
tuttle.setheading(90) # make the turtle point up
tuttle.color('blue')
for i in range(4):
    tuttle.forward(TREASURESIZE)
    tuttle.right(90)

# put the turtle in a random starting spot
randx = random.randint(winminx, winmaxx)
randy = random.randint(winminy, winmaxy)
randangle = random.randint(0,359)
tuttle.penup()
tuttle.setx(randx)
tuttle.sety(randy)
tuttle.pendown()
tuttle.color('black')
tuttle.rt(randangle + 360 * 10) # spin around 10 times plus a little more

print()
print("Enter commands for the turtle and find the treasure!")
print()


while True:

    command = input("fd=forward, rt=right, lt=left, plus a distance or angle as appropriate: ")
    command = command.split() # command[0] = the command, command[1] = the argument
    
    if len(command) != 2: # command should be a list of length 2
        print("--Enter a two-character command and its argument")
        continue          # if not, ask again

    cmd = command[0]
    if cmd not in ['fd', 'rt', 'lt']: # detect an unrecognized command
        print("--Enter a two-character command and its argument")
        continue                      # ask again
    
    arg = int(command[1]) # possible runtime error

    # execute the command
    if cmd == 'fd':
        tuttle.fd(arg)
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
tpos = tuttle.pos() # should be a tuple
theading = tuttle.heading()

# reveal the treasure square
tuttle.penup()
tuttle.goto(treasurex, treasurey) # the bottom left corner of the treasure square
tuttle.pendown()
tuttle.setheading(90) # make the turtle point up
tuttle.color('red')
for i in range(4):
    tuttle.forward(TREASURESIZE)
    tuttle.right(90)

# restore the turtle position
tuttle.penup()
tuttle.color('black')
tuttle.setpos(tpos)
tuttle.setheading(theading)

# the window persists until the user presses <Enter>
wait = input("\nPress <Enter> to quit ")
# turtle.bye() # this doesn't seem to be needed

# window.mainloop()
