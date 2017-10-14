###############################################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #7
#
# Algorithm:
#   blah, blah, blah, ...
#
###############################################################################

def translate(alphanumeric):
    '''Given an alphanumeric phone number, return the equivalent all-numeric phone number.
       translate(alphanumeric: str) -> str
    '''

    numeric = ''
    for character in alphanumeric: # traverse the input
        if character in 'ABCabc':  # build the output string
            numeric += '2'
        elif character in 'DEFdef':
            numeric += '3'
        elif character in 'GHIghi':
            numeric += '4'
        elif character in 'JKLjkl':
            numeric += '5'
        elif character in 'MNOmno':
            numeric += '6'
        elif character in 'PQRSpqrs':
            numeric += '7'
        elif character in 'TUVtuv':
            numeric += '8'
        elif character in 'WXYZwxyz':
            numeric += '9'
        else:
            numeric += character # just pass through any other character

    return numeric


again = 'y'         # so the loop will run the first time
while again == 'y': # loop until the user decides to stop

    phoneNumber = input("\nEnter a 10 character alphanumeric telephone number in the form of XXX-XXX-XXXX: ")
    print("The equivalent numeric phone number is {}".format(translate(phoneNumber)))

    again = input("Would you like to translate another number? (y/N) ")
    again = again or 'n'     # just pressing <Enter> means no
    again = again[0].lower() # look at only the first character and convert to lowercase

print()
