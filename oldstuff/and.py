# If ones = 3, quarters = 2, dimes = 0, nickles = 1, and pennies = 0,
# output: "3 ones, 2 quarters, and 1 nickle."

# the order of the denominations
denominations = ( ('one', 'ones'),
                  ('quarter', 'quarters'),
                  ('dime', 'dimes'),
                  ('nickle', 'nickles'),
                  ('penny', 'pennies') )

# the (unordered) dict data structure
change = {}
change['ones'] = 3
change['quarters'] = 2
change['dimes'] = 0
change['nickles'] = 1
change['pennies'] = 0

# Where does the 'and' go? Find the penultinate nonzero denomination!
# If only 0 or 1 denom is > 0, and will remain = ''
denompresent = [denom[1] for denom in reversed(denominations) if change[denom[1]] > 0]
if len(denompresent) >= 2:
    andx = denompresent[1]
else:
    andx = ''
print(andx)
    
    
# # build the output string
# changestr = ''
# for denom in denominations:
#     if change[denom] > 0:
#         changestr += str(change[denom]) + ' '
#         changestr += denom[:-1] # this won't work because penny vs. pennies!!! ahhhhh!!!!!
#         if change[denom] > 1:
#             changestr += 's'
#         print(' ')

# print(changestr)


            

