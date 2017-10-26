import turtle
import random

# note: (0, 0) is the middle of the screen
# (minx, miny) is the lower-left; (maxx, maxy) is the upper-right
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

winminx = 0 - (SCREEN_WIDTH / 2)
winmaxx = (SCREEN_WIDTH /2)
winminy = 0 - (SCREEN_HEIGHT / 2)
winmaxy = (SCREEN_HEIGHT /2)


def found_treasure(turtlex, turtley):
    '''If the turtle is within the treasure square, return True
       found_treasure(turtlex : int, turtley : int) -> bool
    '''
    withinx = treasurex <= turtlex < (treasurex + 100)
    withiny = treasurey <= turtley < (treasurey + 100)
    return withinx and withiny


# create the screen
window = turtle.Screen()
window.screensize(SCREEN_WIDTH, SCREEN_HEIGHT) # this doesn't affect the windowsize (on my computer)!

# create the turtle
tuttle = turtle.Turtle()
tuttle.speed(10)

# define a 100 x 100 treasure square
treasurex = random.randint(winminx, winmaxx - 100)
treasurey = random.randint(winminy, winmaxy - 100)
# draw the treasure square for testing
tuttle.penup()
tuttle.goto(treasurex, treasurey)
tuttle.pendown()
tuttle.color('red')
for i in range(4):
    tuttle.forward(100)
    tuttle.right(90)

# put the turtle in a random starting spot
randx = random.randint(winminx, winmaxx)
randy = random.randint(winminy, winmaxy)
tuttle.penup()
tuttle.setx(randx)
tuttle.sety(randy)
tuttle.pendown()
tuttle.color('black')

while True:

    command = input("fd=forward, rt=right, lt=left, then distance or angle as appropriate: ")
    # fd 50 = forward 50, rt 90 = right 90 degrees, lt 90 = left 90 degrees
    command = command.split() # a list of the command and argument
    
    if len(command) != 2: # command should be a list of length 2
        continue          # if not, ask again

    cmd = command[0]
    if cmd not in ['fd', 'rt', 'lt']:
        print("--Enter a two-character command and its argument")
        continue
    
    arg = int(command[1]) # possible runtime error

    if cmd == 'fd':
        tuttle.fd(arg)
    elif cmd == 'rt':
        tuttle.rt(arg)
    elif cmd == 'lt':
        tuttle.lt(arg)
        
    
    
window.mainloop()
