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

A = P * (1 + (r / n))**(n * t)  # compute compound interest
print("The amount due when years =", t, "is", A)




Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: /home/michael/prog/git/CSCI1470/homework_01.py ==========
How many years? 10
The amount due when years = 10 is 22196.40234544711
>>> 
========== RESTART: /home/michael/prog/git/CSCI1470/homework_01.py ==========
How many years? 25
The amount due when years = 25 is 73401.75963739285
>>> 
========== RESTART: /home/michael/prog/git/CSCI1470/homework_01.py ==========
How many years? 50
The amount due when years = 50 is 538781.8317865595
>>> 
