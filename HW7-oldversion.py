###############################################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #7
#
# Algorithm:
#   Define a function, translate, that takes a string parameter, alphanumeric:
#       Set numeric to the empty string. This will be the eventual output.
#       Begin a loop with character traversing alphanumeric:
#           If the current character is in "ABCabc" append "2" to numeric,
#           else, if the current character is in "DEFdef" append "3" to numeric,
#           else, if the current character is in "GHIghi" append "4" to numeric,
#           else, if the current character is in "JKLjkl" append "5" to numeric,
#           else, if the current character is in "MNOmno" append "6" to numeric,
#           else, if the current character is in "PQRSpqrs" append "7" to numeric,
#           else, if the current character is in "TUVtuv" append "8" to numeric,
#           else, if the current character is in "WXYZwxyz" append "9" to numeric.
#           otherwise, just append the current character to numeric.
#       Return numeric to the calling function/program.
#
#
#   Set again to 'y' so the loop will run the first time.
#   Loop while again is 'y':
#
#       Set phoneNumber to an alphanumeric phone number the user enters.
#       Print the corresponding numeric phone number using the translate function.
#
#       Prompt the user to translate another phone number.
#       Set again to 'n' if the user just presses <Enter>.
#       Set again to just the first character of the response and convert to lowercase.
#       (If again is 'y' the loop will run again, otherwise the program will end.)
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
