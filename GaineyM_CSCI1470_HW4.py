############################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #4
#
# Pseudocode:
#   blah, blah, blah, ...
#
#   
############################################################

# Design and write a Python program that gives exact change for an item purchased with $5 or less.

while True:

    # Ask the user to enter an item cost and an amount tendered.
    print()
    cost = float(input("  Enter the cost of the item (up to $5): " ))
    tendered = float(input("  Enter the amount tendered: "))

    # Check to make sure that the amount tendered is sufficient to cover the cost of the item;
    # if not, print an error message and start over
    if tendered < cost:
        print("Error: You need to pay an amount sufficient to cover the cost.")
        continue # go back to the top of the while-loop

    # compute the amount of change due
    change = tendered - cost # change won't change
    tempchange = change      # tempchange will change (mutate)

    # initialize some variables
    ones, quarters, dimes, nickles, pennies = 0, 0, 0, 0, 0

    # compute the number of ones, quarters, dimes, nickles, and pennies
    ones = int(tempchange / 1)
    tempchange = round(tempchange % 1, 2)

    quarters = int(tempchange / .25)
    tempchange = round(tempchange % .25, 2)

    dimes = int(tempchange / .1)
    tempchange = round(tempchange % .10, 2)

    nickles = int(tempchange / .05)
    tempchange = round(tempchange % .05, 2)

    pennies = int(tempchange / .01)
    
    # Report the amount of change given: number of dollar bills, quarters, dimes, nickels and pennies.
    print("Your change is ${:.2f}. That's {} ones, {} quarters, {} dimes, {} nickles, and {} pennies."
          .format(change, ones, quarters, dimes, nickles, pennies))

    # Buy another item?
    another = input("Do you want to buy another item? (y/N) ") # 'no' is the defalt choice
    if another == '': # just pressing <Enter> = no
        another = 'n'
    another = another[0].lower() # keep just the first character and convert to lowercase
    if another == 'y':
        continue # go back to the top of the while-loop
    else:
        print()
        break # break out of the loop and end the program
