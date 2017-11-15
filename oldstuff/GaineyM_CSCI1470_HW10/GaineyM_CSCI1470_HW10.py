###############################################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #10
#
# Pseudocode:
#   Import the random module from the Python Standard Library to generate random numbers
#   Seed the random number generator
#
#   Set player1 by prompting player 1 for his/her name.
#   Set player2 by prompting player 2 for his/her name.
#
#   Initialize list player to ['placeholder', player1, player2]
#   Initialize list score to a list of three zeros
#
#   Set currentPlayer to a random number between 1 and 2
#   Tell the users which player will go first: player[currentPlayer]
#
#   Begin the main game loop:
#
#       Set roll to a list of three random numbers from one to six
#       Display the currentPlayer's roll
#
#       If the roll is 6 6 6 ...
#           Add 21 to currentPlayer's score
#           Display a message: "Bunko! ..."
#
#       else if the roll contains two 6's:
#           Add 5 to currentPlayer's score
#           Display a message: "+5 points ..."
#
#       else if the roll contains one 6:
#           Add 1 to the currentPlayer's score
#           Display a message: "+1 point ..."
#
#       else ...
#           Toggle currentPlayer between 1 and 2
#           Display a message: "next player's turn ..."
#
#       Display the two scores: score[1] and score[2]
#
#       Set higher to the higher of the two scores
#       If higher is greater than or equal to 21, then exit the loop
#
#   Set winner to the index of higher in score
#   Display the winner
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
    roll = [random.randint(1,6) for r in range(3)]
    print("{} rolls a {} {} {}".format(player[currentPlayer], roll[0], roll[1], roll[2]), end='    ')

    # score the roll
    if roll.count(6) == 3:
        score[currentPlayer] += 21
        print("Bunko for {}!!!".format(player[currentPlayer]))

    elif roll.count(6) == 2:
        score[currentPlayer] += 5
        print("+5 points for {}!!".format(player[currentPlayer]))

    elif roll.count(6) == 1:
        score[currentPlayer] += 1
        print("+1 point for {}!".format(player[currentPlayer]))

    else:
        # toggle currentPlayer between 1 and 2
        currentPlayer = (currentPlayer % 2) + 1 # (1 % 2 + 1 = 2), (2 % 2 + 1 = 1)
        print("next player's turn ...")

    # display the current score
    print("Score: {} has {} points and {} has {} points\n"
          .format(player[1], score[1], player[2], score[2]))

    # did someone win?
    higher = max(score) # the higher of the two scores
    if higher >= 21:    # if >= 21, exit the loop
        break

# display the winner
winner = score.index(higher) # higher is the winning score; winner is the corresponding index (will be 1 or 2)
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
