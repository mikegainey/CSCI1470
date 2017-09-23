############################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #4
# Design and write a Python program that gives exact change for an item purchased with $5 or less.
#
# Pseudocode:
#
# Start a while loop
#
#   Prompt the user to enter the cost of an item
#   Prompt the user to enter the amount tendered
#   If the amount tendered is not sufficient, go to the top of the loop
#  
#   Compute the change (tendered - cost)
#   Set tempchange to also equal change
#  
#   Initialize variables for monetary denominations (ones, quarters, dimes, nickles, and pennies) to zero
#  
#   Set ones to the number of times 1 will divide evenly into change
#   Set tempchange to whatever amount is left
#  
#   Set quarters to the number of times .25 will divide evenly into change
#   Set tempchange to whatever amount is left
#
#   Set dimes to the number of times .10 will divide evenly into change
#   Set tempchange to whatever amount is left
#
#   Set nickles to the number of times .05 will divide evenly into change
#   Set tempchange to whatever amount is left
#
#   Set pennies to the number of times .01 will divide evenly into change
#  
#   Print the amount of change including the number of one dollar bills, quarters, dimes, nickles, and pennies
#  
#   Prompt user to buy another item (default is no)
#   Set another to 'n' if the user just presses <Enter>
#   Set another to equal only its first character and convert to lowercase
#  
#   If another is 'y' go to the top of the loop, otherwise the program ends
#
############################################################


while True: # this is how a do-while loop is done in Python; the break is at the bottom of the program
            # see https://www.python.org/dev/peps/pep-0315/

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
