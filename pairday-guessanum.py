# The computer picks a random number (from 1 to upperbound).
# You try to guess it (in the fewest number of guesses).
#
# pseudocode:
#
#   Set number to a random number (from 1 to 10)
#   Initialize guesses to zero
#
#   Start a while-loop:
#
#     Set guess to a number that the user picks
#     Increment guesses by 1
#
#     If the user's guess was too low, print a message "... too low."
#     If the user's guess was too high, print a message "... too high."
#     Otherwise, print a message telling the user that he/she guessed correctly
#       and how many guesses it took (guesses); then exit the program
#     (continue the while-loop)

import random

upperbound = 100

number = random.randint(1,upperbound)

#print("The random number is", number)

guesses = 0

while True:

    print()
    guess = int(input("  Pick a number from 1 to {}: ".format(upperbound)))
    guesses += 1
    
    if guess < number:
        print("Your guess was too low. Try again.")
    elif guess > number:
        print("Your guess was too high. Try again.")
    else:
        print("You guessed the number in {} guesses!".format(guesses))
        print()
        break # exit the loop after guessing correctly
