############################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #5
#
# Algorithm:
#
#   Import the random module in order to generate random numbers later.
#   Seed the random number generator.
#   Set LOWERBOUND to 1 and UPPERBOUND to 20, the bounds of the numbers used in the quesions.
#   Begin the outer loop (covering the whole quiz).
#       Initialize (to zero) variables to track the number of questions asked & number of correct responses.
#       Display the main welcome mesage.
#
#       Display an "Addition" heading.
#       Begin a loop to cover the 2 addition questions.
#           Generate 2 random numbers (LOWERBOUND to UPPERBOUND), num1 & num2.
#           Display an addition question and get a response.
#           Increment the question counter.
#           Set answer to the correct answer (num1 + num2).
#           If the response is correct, tell the student and increment the correct response counter.
#
#       Display a "Subtraction" heading.
#       Begin a loop to cover the 2 subtraction questions.
#           Generate 2 random numbers (LOWERBOUND to UPPERBOUND), num1 & num2.
#           Display a subtraction question and get a response.
#           Increment the question counter.
#           Set answer to the correct answer (num1 - num2).
#           If the response is correct, tell the student and increment the correct response counter.
#
#       Display a "Multipliction" heading.
#       Begin a loop to cover the 2 multiplication questions.
#           Generate 2 random numbers (LOWERBOUND to UPPERBOUND), num1 & num2.
#           Display a multiplication question and get a response.
#           Increment the question counter.
#           Set answer to the correct answer (num1 * num2).
#           If the response is correct, tell the student and increment the correct response counter.
#
#       Display a "Division" heading (with a note to only give the whole number answer).
#       Begin a loop to cover the 2 division questions.
#           Generate 2 random numbers (LOWERBOUND to UPPERBOUND), num1 & num2.
#           Display a division question and get a response.
#           Increment the question counter.
#           Set answer to the correct answer (num1 // num2).
#           If the response is correct, tell the student and increment the correct response counter.
#
#       Display a "Modulus" heading.
#       Begin a loop to cover the 2 modulus questions.
#           Generate 2 random numbers (LOWERBOUND to UPPERBOUND), num1 & num2.
#           Display a modulus question and get a response.
#           Increment the question counter.
#           Set answer to the correct answer (num1 % num2).
#           If the response is correct, tell the student and increment the correct response counter.
#
#   Display the number of questions answered correctly and the total number of questions.
#
#   Prompt the user to take the quiz again.
#   If the response is 'y' continue the while-loop.
#   Otherwise, break out of the loop and end the program.
#
############################################################

import random
random.seed()

LOWERBOUND = 1   # lower bound of the numbers in the questions
UPPERBOUND = 20  # upper bound of the numbers in the questions

again = 'y' # set the loop to run the first time
while again == 'y': # at the end, the user will be asked to try again

    # used to keep track of the number of questions given and number answered correctly
    questions, correct = 0, 0

    print()
    print("Test your math skills!  Answer these 10 questions.  Good luck!")
    print()

    print("===== Addition =====\n")

    for rep in range(2):

        num1 = random.randint(LOWERBOUND, UPPERBOUND)
        num2 = random.randint(LOWERBOUND, UPPERBOUND)

        response = int(input("{} + {} = ".format(num1, num2)))
        questions += 1
        answer = num1 + num2

        if response == answer:
            print("Correct!")
            correct += 1

        print()


    print("===== Subtraction =====\n")

    for rep in range(2):

        num1 = random.randint(LOWERBOUND, UPPERBOUND)
        num2 = random.randint(LOWERBOUND, UPPERBOUND)

        if num2 > num1:
            num1, num2 = num2, num1

        response = int(input("{} - {} = ".format(num1, num2)))
        questions += 1
        answer = num1 - num2

        if response == answer:
            print("Correct!")
            correct += 1

        print()


    print("===== Multiplication =====\n")

    for rep in range(2):

        num1 = random.randint(LOWERBOUND, UPPERBOUND)
        num2 = random.randint(LOWERBOUND, UPPERBOUND)

        response = int(input("{} x {} = ".format(num1, num2)))
        questions += 1
        answer = num1 * num2

        if response == answer:
            print("Correct!")
            correct += 1

        print()


    print("===== Division  ===== (just the whole number answer)\n")

    for rep in range(2):

        num1 = random.randint(LOWERBOUND, UPPERBOUND)
        num2 = random.randint(LOWERBOUND, UPPERBOUND)

        if num2 > num1:
            num1, num2 = num2, num1

        response = int(input("{} \N{DIVISION SIGN} {} = ".format(num1, num2)))
        questions += 1
        answer = num1 // num2

        if response == answer:
            print("Correct!")
            correct += 1

        print()


    print("===== Modulus  =====\n")

    for rep in range(2):

        num1 = random.randint(LOWERBOUND, UPPERBOUND)
        num2 = random.randint(LOWERBOUND, UPPERBOUND)

        if num2 > num1:
            num1, num2 = num2, num1

        response = int(input("{} % {} = ".format(num1, num2)))
        questions += 1
        answer = num1 % num2

        if response == answer:
            print("Correct!")
            correct += 1

        print()

    endingpunctuation = '!' if correct / questions >= 0.8 else '.'
    print("You answered {} out of {} questions correctly{}\n"
          .format(correct, questions, endingpunctuation))

    again = input("Do you want to try again? (y/n) ")
    if again == '': # just pressing <Enter> means no
        again = 'n'
    again = again[0].lower() # look at just the first character of the response (forced lowercase)
    # if again == 'y' the outer loop will continue again, otherwise the program ends

print() # print a blank line before the next shell prompt
