import random
random.seed()

LOWERBOUND = 1     # lower bound of the numbers in the questions
UPPERBOUND = 20    # upper bound of the numbers in the questions

# ops is the key data structure in this program. It removes the need for separate
#     blocks of code to handle each arithmetic operation.
# It is a dictionary where the key is an operation code: add, sub, mul, div, or mod.
# The value is a tuple with 3 elements:
#     the operation title ('Addition')
#     the operation symbol ('+')
#     and the function itself
# Python will allow functions to be elements of lists, tuples, etc. For example:
#     ops['add'][0] = 'Addition'
#     ops['add'][1] = '+'
#     ops['add'](5, 7) = 13

ops = { 'add' : ('Addition', '+', lambda x, y: x + y),
        'sub' : ('Subtraction', '-', lambda x, y: x - y),
        'mul' : ('Multiplication', 'x', lambda x, y: x * y),
        'div' : ('Division', '\N{DIVISION SIGN}', lambda x, y: x // y),
        'mod' : ('Modulus', '%', lambda x, y: x % y)
}

again = 'y'         # set the loop to run the first time
while again == 'y': # at the end, the user will be asked to try again

    # to keep track of the number of questions given and number answered correctly
    questions, correct = 0, 0

    print()
    print("It's time for a math quiz!  Answer these 10 questions.  Good luck!")
    print()

    # loops through the five operations
    for op in ['add', 'sub', 'mul', 'div', 'mod']:

        # print an operation heading
        print("===== {} =====\n".format(ops[op][0]))

        # ask two questions of each operation
        for rep in range(2):

            # get the random numbers
            num1 = random.randint(LOWERBOUND, UPPERBOUND)
            num2 = random.randint(LOWERBOUND, UPPERBOUND)

            # get the user input; ops[op][1] is the operation symbol: '+', '-', etc.
            response = int(input("{} {} {} = ".format(num1, ops[op][1], num2)))
            questions += 1
            answer = ops[op][2](num1, num2) #ops[op][2](arg1, arg2) is the arithmetic function

            if response == answer:
                print("Correct!")
                correct += 1
            else:
                print("No.")

            print()

    score = (correct / questions) * 100
    score = round(score)
    
    print("You answered {}% of the questions correctly".format(score), end = "")
    print("!") if score >= 80 else print(".") # A score of 80% or better earns a "!"
    
    print()
    again = input("Do you want to try again? (y/N) ")
    again = again or 'n'     # just pressing <Enter> means no
    again = again[0].lower() # look at just the first character of the response (forced lowercase)
    # if again == 'y' the outer loop will continue again, otherwise the program will end

print() # print a blank line before the next shell prompt
