# input = [1 (2 (5)*3 3)*2 7], output = 1 2 5 5 5 3 2 5 5 5 3 7

# Note: I didn't know the rules of how to form the possible inputs.  So, this function may sometimes fail because
# my method of finding the matching left parenthesis is very naive.  But it works with the example you gave me in class.

# After finding a parenthasis matching algorithm online, I noticed that my algorithm seems to work in a similiar manner:
#   Search from the left.  After finding a closing parenthesis, check that the previous parenthesis is an opening parenthesis
#   of the same type.  My program assumes all parenthesis are the () type and doesn't know about [] or {}.

# Assumptions:
# - A right paren is immediately to the left of each * operator
# - A multiplier argument is immediately to the rigth of each * operator.
# - Multiplier arguments are only single-digit integers.
# - Other than the square brackets surrounding the entire expression, only () parentheses are used.

# strmult = string multiply; my name for what this program does
# inpstr = input string
# opx = operator (*) index
# argx = argument index; this is the number to multiply by; in '[1 (2 (5)*3 3)*2 7]' the arguments are 3 and 2
# arg = the integer argument (argx is the index of the argument)
# rparenx = right parenthesis index (just to the left of the operator)
# lparenx = left parenthesis index; searches left from the right parenthasis; this is not an intelligent way of finding
#   the correct matching parenthesis; it might fail on other inputs -- I don't know all the rules of what inputs can be
# insert1 = the string to be multiplied; in [(5)*3], insert = 5; in [1 (2 5 5 5 3)*2 7], insert = 2 5 5 5 3
# insert2 = if insert1 = 5 and arg = 3, then insert2 = ['5', '5', '5']
# insert3 = if insert2 = ['5', '5', '5'], then insert3 = '5 5 5'
# leftstr = the left part of the string that's not being multiplied
# rightstr = the right part of the string that's not being multiplied


def strmult(inpstr):

    while '*' in inpstr: # run the body of this function for each '*' (left to right)

        opx = inpstr.find('*')  # the index of the *
        argx = opx + 1          # the index of the number to multiply by
        arg = int(inpstr[argx]) # the number to multiply by
        rparenx = opx - 1       # the index of the right paren (just left of the *)
        lparenx = inpstr.rfind('(', 0, rparenx) # the index of the left paren (might find the wrong one)

        insert = inpstr[(lparenx + 1):rparenx]  # the string to be multiplied (within parens but not including them)
        insert = [insert for a in range(arg)]   # do the multiplication with a list comprehension
        insert = ' '.join(insert)               # convert to a string with spaces in between

        leftstr = inpstr[:lparenx]              # the left part of the rest of the string
        rightstr = inpstr[(argx + 1):]          # the right part of the rest of the string
        inpstr = leftstr + insert + rightstr    # put it all together
        # keep looping while '*' in inpstr
        
    return inpstr[1:-1] # and strip the square brackets off


s = '[(2)*3]'
print("\ninput = {}, output = {}".format(s, strmult(s)))

s = '[1 (2 5 5 5 3)*2 7]' # output should be: 1 2 5 5 5 3 2 5 5 5 3 7
print("\ninput = {}, output = {}".format(s, strmult(s)))

s = '[1 (2 (5)*3 3)*2 7]' # output should be: 1 2 5 5 5 3 2 5 5 5 3 7
print("\ninput = {}, output = {}".format(s, strmult(s)))

s = '[9 (8 (7 6)*3 5)*2 4]' # output should be 9 8 7 6 7 6 7 6 5 8 7 6 7 6 7 6 5 4
print("\ninput = {}, output = {}".format(s, strmult(s)))

print()
