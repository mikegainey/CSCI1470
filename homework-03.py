############################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #3
#
# Algorithm:
#   Assign variables with user input
#   Using age, determine the hourly fee
#   Compute the bill (hours * hourly fee)
#   Print the final bill with all relavent information
#   
############################################################

print()
print("=" * 80) # horizontal line
print("Welcome to UH Clear Lake Child Care!")

# Assign variables with user input
fname = input("  What is your child's first name? ")
lname = input("  What is the family name? ")

while True:
    age = input("  What is your child's age? ")
    age = int(age)
    if (age > 10) or (age < 0):
        print("We only accept children through age 10.")
    else:
        break # age <= 10, so continue the program

hours = input("  How many hours will your child stay today? ")
hours = int(hours)

# Using age, determine the hourly fee
if  age < 2:
    fee = 15
elif 2 <= age <= 4:
    fee = 10
elif 5 <= age <= 8:
    fee = 8
elif 8 < age <= 10:
    fee = 6
else:
    print("Error - All inputs should have been handled by now.")

# Compute the bill (hours * hourly fee)
bill = fee * hours

# Print the final bill with all relavent information
print()
print("{} {}, age {}, stayed {} hours at ${} per hour. You owe ${} today.".format(fname, lname, age, hours, fee, bill))
print("=" * 80) # horizontal line
