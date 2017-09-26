import random

# the computer picks a random number from 1 to 10
number = random.randint(1,10)
#print("The random number is", number)

# guesses keeps track of the number of guesses
guesses = 0
    
while True:

    guess = int(input("Pick a number from 1 to 10: "))
    guesses += 1
    
    if guess < number:
        print("Your guess was too low. Try again.")
    elif guess > number:
        print("Your guess was too high. Try again.")
    else:
        print("You guessed the number in {} guesses!".format(guesses))
        break # exit the loop after guessing correctly
