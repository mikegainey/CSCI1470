############################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #3
#
# Algorithm:
#   Begin loop to execute this program 3 times:
#     Assign variables with user input
#     Using age, determine the hourly fee
#     Compute the bill (hours * hourly fee)
#     Print the final bill with all relevant information
#   
############################################################

# Note: This program requires Python 3.6 to use f-strings (formatted string literals)

# Loop to execute this program 3 times:
for child in range(3):

    print()
    print("=" * 80)
    print("{:^80}".format("Welcome to UH Clear Lake Child Care!"))
    print("=" * 80)
    
    # Assign variables with user input
    # Non-numeric characters in age and hours will cause a runtime error
    while True:
        fname = input("  What is your child's first name? ")
        lname = input("  What is the family name? ")

        age = input("  What is your child's age? ")
        age = float(age) # convert any numeric string (like "3.5") to a float
        age = int(age)   # round any float down (so an age of 10.5 is considered a 10-year-old)
        if (age < 0) or (age > 10):
            print("    (We only accept children through age 10.)")
            print() # loop back and ask for another child (of acceptable age)
        else:
            break   # age is within range, so continue the program

    hours = input("  How many hours will your child stay today? ")
    hours = float(hours) # hours doesn't have to be a whole number

    # Using age (an integer from 0 to 10), determine the hourly fee
    if  age in [0, 1]:     # for ages 0 and 1, the fee is $15/hr
        fee = 15
    elif age in [2, 3, 4]: # age has been cast to an int (so age = 4.5 doesn't have to be considered)
        fee = 10
    elif age in [5, 6, 7]:
        fee = 8
    elif age in [8, 9, 10]:
        fee = 6
    else:
        print("\nError - All ages should have been handled by now. (age = {}) \n".format(age))
        quit() # this should never happen

    # Compute the bill (hours * hourly fee)
    bill = fee * hours

    # Display the final bill with all relevant information
    # For string formatting info: https://docs.python.org/3/whatsnew/3.6.html#pep-498-formatted-string-literals
    print()
    print(f"{fname} {lname}, age {age}, stayed {hours} hours today at ${fee} per hour. You owe ${bill:.2f}.")
    print("=" * 80)
    print()
