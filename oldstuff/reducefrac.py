import random # used to generate interesting numbers for testing

def reducefrac(n, d):
    '''Reduces a fraction given its numerator and denominator.'''
    print("\nLet's reduce the fraction {}/{} ...\n".format(n, d))
    wn = n # working numerator
    wd = d # working denominator

    while True:
        for divisor in range(2, int(min(wn, wd))):
            print("checking {}/{} and {}/{}".format(wn, divisor, wd, divisor), end=" ")
            if wn % divisor == 0 and wd % divisor == 0:
                print("Both numbers divide by {}!".format(divisor))
                wn //= divisor
                wd //= divisor
                break # after an intermediate reduction, redo the algorithm with the new wn & wd
                      # after this break, program execution resumes from the top of the while-loop
            else:
                print() # this else clause is only needed to print a line feed
        else: # the for-loop completed without break (meaning no further reduction is possible)
            print("\n{}/{} reduces to {}/{}!\n".format(n, d, wn, wd))
            return (wn, wd) # the while-loop terminates with the return statement

        
# reducefrac(random.randint(1, 1000), random.randint(1, 1000)) # test the function with random input

# Note: The algorithm should be obvious from the intermediate output showing the computer thinking.  Its inefficiency
# should also be obvious, but it's good enough for "normal" numbers (under xx,xxx/xx,xxx or so) as long as the function
# itself isn't placed inside another loop with too many iterations.

 
# ===== Sample output =====

# Let's reduce the fraction 266/588 ...

# checking 266/2 and 588/2 Both numbers divide by 2!
# checking 133/2 and 294/2 
# checking 133/3 and 294/3 
# checking 133/4 and 294/4 
# checking 133/5 and 294/5 
# checking 133/6 and 294/6 
# checking 133/7 and 294/7 Both numbers divide by 7!
# checking 19/2 and 42/2 
# checking 19/3 and 42/3 
# checking 19/4 and 42/4 
# checking 19/5 and 42/5 
# checking 19/6 and 42/6 
# checking 19/7 and 42/7 
# checking 19/8 and 42/8 
# checking 19/9 and 42/9 
# checking 19/10 and 42/10 
# checking 19/11 and 42/11 
# checking 19/12 and 42/12 
# checking 19/13 and 42/13 
# checking 19/14 and 42/14 
# checking 19/15 and 42/15 
# checking 19/16 and 42/16 
# checking 19/17 and 42/17 
# checking 19/18 and 42/18 

# 266/588 reduces to 19/42!
