############################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #5
#
# Algorithm:
#   blah, blah, blah
#   
############################################################

import random

while True:

    # used to keep track of number of questions given and number answered correctly
    questions, correct = 0, 0

    print()
    print("Test your math skills! Here are 10 math questions.  Good luck!")
    print()

    print("===== Addition! =====")

    for rep in range(2):

        num1 = random.randint(1,20)
        num2 = random.randint(1,20)

        response = int(input("{} + {} = ".format(num1, num2)))
        questions += 1
        answer = num1 + num2

        if response == answer:
            print("Correct!")
            correct += 1

        print()


    print("===== Subtraction! =====")

    for rep in range(2):

        num1 = random.randint(1,20)
        num2 = random.randint(1,20)

        if num2 > num1:
            num1, num2 = num2, num1

        response = int(input("{} - {} = ".format(num1, num2)))
        questions += 1
        answer = num1 - num2

        if response == answer:
            print("Correct!")
            correct += 1

        print()


    print("===== Multiplication! =====")

    for rep in range(2):

        num1 = random.randint(1,20)
        num2 = random.randint(1,20)

        response = int(input("{} x {} = ".format(num1, num2)))
        questions += 1
        answer = num1 * num2

        if response == answer:
            print("Correct!")
            correct += 1

        print()


    print("===== Division!  ===== (just the whole number answer)")

    for rep in range(2):

        num1 = random.randint(1,20)
        num2 = random.randint(1,20)

        if num2 > num1:
            num1, num2 = num2, num1

        response = int(input("{} \N{DIVISION SIGN} {} = ".format(num1, num2)))
        questions += 1
        answer = num1 // num2

        if response == answer:
            print("Correct!")
            correct += 1

        print()


    print("===== Modulus!  ===== (the remainder after division)")

    for rep in range(2):

        num1 = random.randint(1,20)
        num2 = random.randint(1,20)

        if num2 > num1:
            num1, num2 = num2, num1

        response = int(input("{} % {} = ".format(num1, num2)))
        questions += 1
        answer = num1 % num2

        if response == answer:
            print("Correct!")
            correct += 1

        print()

    print("You answered {} out of {} questions correctly!".format(correct, questions))
    print()

    again = input("Do you want to try again? (y/n) ")
    if again != 'y':
        break
    else:
        print()
