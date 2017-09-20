# Plan the logic for giving change.
#   Input the cost of an item and the dollars tendered.
#   Assume for this exercise that no item costs more than $5 and that no bill > $5 will be tendered.
#   Output the number of bills, quarters, dimes, nickels and pennies to be returned to the shopper.

while True:
    print()
    tendered = float(input("Enter the amount tendered: "))
    if tendered < 0:
        print("  This program only works with positive number inputs.")
    else:
        break # the amount tendered is in range; continue the program

fives = 0
ones = 0
quarters = 0
dimes = 0
nickles = 0
pennies = 0

fives = int(tendered // 5)
tendered %= 5

ones = int(tendered // 1)
tendered %= 1

quarters = int(tendered // .25)
tendered %= .25

dimes = int(tendered // .1)
tendered %= .1

nickles = int(tendered // .05)
tendered %= .05

pennies = int(tendered // .01)
tendered %= .01

print("That is {} fives, {} ones, {} quarters, {} dimes, {} nickles, and {} pennies."\
      .format(fives, ones, quarters, dimes, nickles, pennies))
print()
