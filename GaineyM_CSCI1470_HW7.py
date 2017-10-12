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

def translate(phnum):
    '''Translate an alphanumeric phone number to an all-numeric phone number'''
    output = ''      # initialize the output string
    for ch in phnum: # build the output string
        if ch in 'ABCabc':
            output += '2'
        elif ch in 'DEFdef':
            output += '3'
        elif ch in 'GHIghi':
            output += '4'
        elif ch in 'JKLjkl':
            output += '5'
        elif ch in 'MNOmno':
            output += '6'
        elif ch in 'PQRSpqrs':
            output += '7'
        elif ch in 'TUVtuv':
            output += '8'
        elif ch in 'WXYZwxyz':
            output += '9'
        elif ch in '0123456789': # if the current character is a number, juss pass it through
            output += ch
    first3 = output[:3]
    second3 = output[3:6]
    last4 = output[-4:]
    output = '-'.join([first3, second3, last4])
    return output # return the output string


while True:
    phonein = input("\nEnter a 10 character alphanumeric telephone number in the form of XXX-XXX-XXXX: ")
    print("The equivalent numeric phone number is {}".format(translate(phonein)))
    again = input("Would you like to translate another number? (y/N) ")
    again = again or 'n'
    again = again[0].lower()
    if again != 'y':
        break
    else:
        continue
