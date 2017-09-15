############################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #3
#
# Algorithm:
#   Loop to execute this program 3 times:
#     Assign variables with user input
#     Using age, determine the hourly fee
#     Compute the bill (hours * hourly fee)
#     Print the final bill with all relevant information
#   
############################################################

# Loop to execute this program 3 times:
for child in range(3):

    print()
    print("=" * 80)
    print("{:^80}".format("Welcome to UH Clear Lake Child Care!"))
    print("=" * 80)
    
    # Assign variables with user input
    while True:
        fname = input("  What is your child's first name? ")
        lname = input("  What is the family name? ")

        age = input("  What is your child's age? ")
        age = float(age) # this converts any numeric string (like "3.5") to a float
        age = int(age)   # this rounds any float down (so an age of 3.5 is considered a 3-year-old)
        if (age > 10) or (age < 0):
            print("    (We only accept children through age 10.)")
            print()
        else:
            break # age is within range, so continue the program (otherwise, ask again)

    hours = input("  How many hours will your child stay today? ")
    hours = float(hours) # hours doesn't have to be a whole number

    # Using age, determine the hourly fee
    #   Note: "... expressions like a < b < c have the interpretation that is conventional in mathematics"
    #   see https://docs.python.org/3/reference/expressions.html#comparisons
    if  age < 2:
        fee = 15
    elif 2 <= age <= 4: # age is an int (so age = 4.5 doesn't have to be considered)
        fee = 10
    elif 5 <= age <= 7:
        fee = 8
    elif 8 <= age <= 10:
        fee = 6
    else:
        print("Error - All ages should have been handled by now.")

    # Compute the bill (hours * hourly fee)
    bill = fee * hours

    # Display the final bill with all relevant information
    # for string formatting info see: https://docs.python.org/3/library/string.html#format-string-syntax
    print()
    print("{} {}, age {}, stayed {} hours today at ${} per hour. You owe ${:.2f}."\
          .format(fname, lname, age, hours, fee, bill))
    print("=" * 80)
    print()
