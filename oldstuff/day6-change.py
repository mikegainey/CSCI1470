# Plan the logic for giving change.
#   Input the cost of an item and the dollars tendered.
#   Assume for this exercise that no item costs more than $5 and that no bill > $5 will be tendered.
#   Output the number of bills, quarters, dimes, nickels and pennies to be returned to the shopper.

while True:
    print()
    cost = float(input("Enter the cost of the item (up to $5):" ))
    tendered = float(input("Enter the amount tendered: "))
    if cost < 0 or tendered < 0:
        print("  This program only works with positive number inputs.")
    else:
        break # the amount tendered is in range; continue the program

change = tendered - cost
change = round(change, 2) # 30 - 23.46 = 6.539999999999999 (in Python); round to 6.54
tempchange = change

fives = 0
ones = 0
quarters = 0
dimes = 0
nickles = 0
pennies = 0

fives = int(tempchange // 5) # floor division returns a float! Why?
tempchange %= 5

ones = int(tempchange // 1)
tempchange %= 1

quarters = int(tempchange // .25)
tempchange %= .25

dimes = int(tempchange // .1)
tempchange %= .1

nickles = int(tempchange // .05)
tempchange %= .05

pennies = int(tempchange // .01)
tempchange %= .01

print("Your change is {} ({} fives, {} ones, {} quarters, {} dimes, {} nickles, and {} pennies)."
      .format(change, fives, ones, quarters, dimes, nickles, pennies))
print()
