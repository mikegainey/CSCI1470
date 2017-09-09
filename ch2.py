# HTTLACS Ch. 2, Exercises 1-5

# 1. Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable,
#    then print out the sentence on one line using print.

s1 = 'All'
s2 = 'work'
s3 = 'and'
s4 = 'no'
s5 = 'play'
s6 = 'makes'
s7 = 'Jack'
s8 = 'a'
s9 = 'dull'
s10 = 'boy.'

# print(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10)

# 2. Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.

# print(6 * (1 - 2))

# 3. Place a comment before a line of code that previously worked, and record what happens when you rerun the program.

# print("This worked")

# 4. Assign a value to bruce so that bruce + 4 evaluates to 10.

bruce = 6

# print(bruce + 4)

# 5.
'''The formula for computing the final amount if one is earning compound interest is given on Wikipedia as

A = P * (1 + (r/n))**(nt)

P = principal amount (initial investment)
r = annual nominal interest rate (as a decimal)
n = number of times the interest is compounded per year
t = number of years

Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, 
and assign to r the interest rate of 8%. Then have the program prompt the user for the number of years 
that the money will be compounded for. Calculate and print the final amount after t years.'''

P = 10000
n = 12
r = 0.08
t_input = input("How many years? ")
t = float(t_input)

A = P * (1 + (r/n))**(n * t)
print("The amount due when years =", t, "is", A)
