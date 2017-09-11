#**********************  homework_01.py  *********************
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #1
#
# Algorithm:
#   Variable assignments
#   Prompt user for number of years to comute compound interest
#   Compute compount interest
#   Print result
#**********************************************************

P = 10000  # principal amount (initial investment)
n = 12     # number of times the interest is compounded per year
r = 0.08   # annual nominal interest rate (as a decimal)

t_input = input("How many years? ")
t = int(t_input)  # number of years

A = P * (1 + (r / n))**(n * t)
print("The amount due when years =", t, "is", A)
