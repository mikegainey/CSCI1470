###############################################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #10
#
# Pseudocode:
#   Blah, blah, blah, ...
#
###############################################################################

import random
random.seed()

print("\nGet ready for some Bunko!!!\n")

player1 = input("Enter player 1's name: ")
player2 = input("Enter player 2's name: ")

# initialize variables; [0] is not used
player = ["placeholder", player1, player2] # player[n] = player n's name
score = [0, 0, 0]                          # score[n] = player n's score

# the toss-up
currentPlayer = random.randint(1,2)
print("\n{} will go first.\n".format(player[currentPlayer]))

while True:

    # roll is a list representing the rolling of three dice
    roll = [random.randint(5,6) for r in range(3)]
    print("{} rolls a {} {} {}".format(player[currentPlayer], roll[0], roll[1], roll[2]), end='    ')
    
    if roll.count(6) == 3:
        score[currentPlayer] = 21
        print("Bunko for {}!!!".format(player[currentPlayer]))

    elif roll.count(6) == 2:
        score[currentPlayer] += 5
        print("+5 points for {}!".format(player[currentPlayer]))

    elif roll.count(6) == 1:
        score[currentPlayer] += 1
        print("+1 point for {}!".format(player[currentPlayer]))

    else:
        # toggle currentPlayer between 1 and 2
        currentPlayer = 2 if currentPlayer == 1 else 1
        print("next player's turn ...")

    print("Score: {} has {} points and {} has {} points\n"
          .format(player[1], score[1], player[2], score[2]))

    # did someone win?
    higher = max(score) # the higher of the two scores
    if higher >= 21:    # if >= 21, exit the loop
        break

# display the winner
winner = score.index(higher) # winner will be 1 or 2
print("{} wins!".format(player[winner]))
        
print()
    
        
# Homework #10

# Due: Tuesday, November 14th 11:59pm

# Write a Python program that plays a two-player game of Bunko.

# In this game each player rolls 3 dice.
# - If all 3 dice are sixes, the player gets 21 points, wins the game and the game is over. That is called a Bunko.
# - If the player rolls 1 six the player gets one point and continues rolling.
# - If the player rolls 2 sixes the player gets 5 points and continues rolling.
# - If the player doesn't roll any sixes, it is the other player's turn.

# - Use random numbers from 1 to 6 for the dice rolls.
# - Keep score for both players and determine the winner.
# - Display all dice rolls each turn, and each player's score at the end of each player's turn. (10 points)
