# The cost of an international call from Houston to Mexico City is calculated as follows:
#   Connection fee is $1.00
#   $1.50 for the first three minutes,
#   then $0.40 per additional minute
#
# Prompt the user for the number of minutes the call lasted and output the amount due.

print()
minutes = float(input("How many minutes was your call? "))

baseCost = 2.5 # start at $2.50 for the connection fee ($1.00) + first three minutes ($1.50)

if minutes > 3:
    minOver3 = minutes - 3
else:
    minOver3 = 0

feeOver3 = .4 # per minute charge after the 3rd minute

costOver3 = minOver3 * feeOver3

totalCost = baseCost + costOver3

print(f"Your amount due is ${totalCost:.2f}:")
print(f" That's ${baseCost:.2f} for the connection fee and first three minutes,")
print(f" and ${costOver3:.2f} for {minOver3} additional minutes at ${feeOver3:.2f} per minute.")
print()
