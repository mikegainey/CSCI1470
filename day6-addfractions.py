# add two fractions

from reducefrac import reducefrac # a little extra at the end

print()
print("Let's add two fractions!")

n1 = int(input("Enter the numerator of the first number: "))
d1 = int(input("Enter the denominator of the first number: "))

n2 = int(input("Enter the numerator of the second number: "))
d2 = int(input("Enter the denominator of the second number: "))

# Find a common denominator by multiplying the denominators.
#   It may not be the lowest common denominator, so the result,
#   while correct, may not be in simplest form.
cd = d1 * d2 # for 3/4 + 4/5, the cd = 4 * 5 = 20

# adjust the numerators of the two numbers to reflect the new, common denominator
n1cd = (cd / d1) * n1 # (20 / 4) * 3 = 15, so 3/4 becomes 15/20
n2cd = (cd / d2) * n2 # (20 / 5) * 4 = 16, so 4/5 becomes 16/20

# rn and rd are the result numerator and result denominator
rn = n1cd + n2cd # add the adjusted numerators
rd = cd          # the denominator of the result is the common denominator

rn = int(rn) # get rid of the .0 to make the output look nice

print("{}/{} + {}/{} = {}/{}".format(n1, d1, n2, d2, rn, rd))
print()

reducefrac(rn, rd) # reduce the fraction



