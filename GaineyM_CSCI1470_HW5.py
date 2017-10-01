#################################################################################
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
#   Set LOWERBOUND to 1 and UPPERBOUND to 20, the bounds of the numbers used in the questions.
#   Set again to 'y' so the loop will run the first time
#   Loop while again is 'y':
#       Initialize (to zero) variables to track the number of questions asked & number of correct responses.
#       Display the main welcome message.
#
#       Display an "Addition" heading.
#       Begin a loop to cover the 2 addition questions:
#           Generate 2 random numbers (LOWERBOUND to UPPERBOUND), num1 & num2.
#           Display an addition question, (num1 + num2 = ), and get a response.
#           Increment the question counter.
#           Set answer to the correct answer (num1 + num2).
#           If the response is correct, tell the student and increment the correct response counter.
#
#       Display a "Subtraction" heading.
#       Begin a loop to cover the 2 subtraction questions:
#           Generate 2 random numbers (LOWERBOUND to UPPERBOUND), num1 & num2.
#           Display a subtraction question, (num1 - num2 = ), and get a response.
#           Increment the question counter.
#           Set answer to the correct answer (num1 - num2).
#           If the response is correct, tell the student and increment the correct response counter.
#
#       Display a "Multiplication" heading.
#       Begin a loop to cover the 2 multiplication questions:
#           Generate 2 random numbers (LOWERBOUND to UPPERBOUND), num1 & num2.
#           Display a multiplication question, (num1 * num2 = ), and get a response.
#           Increment the question counter.
#           Set answer to the correct answer (num1 * num2).
#           If the response is correct, tell the student and increment the correct response counter.
#
#       Display a "Division" heading (with a note to only give the whole number answer).
#       Begin a loop to cover the 2 division questions:
#           Generate 2 random numbers (LOWERBOUND to UPPERBOUND), num1 & num2.
#           Display a division question, (num1 ÷ num2 = ), and get a response.
#           Increment the question counter.
#           Set answer to the correct answer (num1 // num2).
#           If the response is correct, tell the student and increment the correct response counter.
#
#       Display a "Modulus" heading.
#       Begin a loop to cover the 2 modulus questions:
#           Generate 2 random numbers (LOWERBOUND to UPPERBOUND), num1 & num2.
#           Display a modulus question, (num1 % num2 = ), and get a response.
#           Increment the question counter.
#           Set answer to the correct answer (num1 % num2).
#           If the response is correct, tell the student and increment the correct response counter.
#
#   Set score to the percentage of questions answered correctly.
#   Round score to a whole number to make the output look lice.
#
#   Display the score.
#
#   Prompt the user to take the quiz again.
#   Set again to 'no' if the user just presses <Enter>.
#   Set again to just the first character of the response and convert to lowercase.
#   (If again is 'y' the loop will run again, otherwise the program will end.)
#
#################################################################################

import random
random.seed()

LOWERBOUND = 1     # lower bound of the numbers in the questions
UPPERBOUND = 20    # upper bound of the numbers in the questions

again = 'y'         # set the loop to run the first time
while again == 'y': # at the end, the user will be asked to try again

    # to keep track of the number of questions given and number answered correctly
    questions, correct = 0, 0

    print()
    print("It's time for a math quiz!  Answer these 10 questions.  Good luck!")
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

    score = (correct / questions) * 100
    score = round(score)
    
    endingpunctuation = '!' if score >= 80 else '.'
    print("You answered {}% of the questions correctly{}\n"
          .format(score, endingpunctuation))

    again = input("Do you want to try again? (y/n) ")
    if again == '': # just pressing <Enter> means no
        again = 'n'
    again = again[0].lower() # look at just the first character of the response (forced lowercase)
    # if again == 'y' the outer loop will continue again, otherwise the program will end

print() # print a blank line before the next shell prompt
