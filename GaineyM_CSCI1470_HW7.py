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
#
#       Set LETTERS equal to 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'
#       Set NUMBERS equal to '222 333 444 555 666 7777 888 9999'
#
#       Set numeric to an empty string. This will become the eventual output.
#       Begin a loop with character traversing alphanumeric:
#
#           Set in_char to character and apply the upper string method.
#           If in_char is in LETTERS ...
#               Set index to the index of in_char in LETTERS using the find method.
#               Set out_char to the character in NUMBERS with the same index.
#               Otherwise (if in_char is not in LETTERS), just set out_char to in_char.
#
#           Append out_char to numeric.
#
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

    LETTERS = 'ABC DEF GHI JKL MNO PQRS TUV WXYZ' # the map from: LETTERS
    NUMBERS = '222 333 444 555 666 7777 888 9999' #           to: NUMBERS
    
    numeric = ''                   # this will be the output string
    for character in alphanumeric: # traverse the input

        # translate one character
        in_char = character.upper()       # convert to uppercase
        if in_char in LETTERS:            # if in_char is in LETTERS ...
            index = LETTERS.find(in_char) # get it's index
            out_char = NUMBERS[index]     # get the corresponding character in NUMBERS
        else:
            out_char = in_char            # if in_char is not in LETTERS, just pass it through

        numeric += out_char               # append the translated character to the output string

    return numeric


again = 'y'         # so the loop will run the first time
while again == 'y': # loop until the user decides to stop

    phoneNumber = input("\nEnter a 10 character alphanumeric telephone number in the form of XXX-XXX-XXXX: ")
    print("The equivalent numeric phone number is {}".format(translate(phoneNumber)))

    again = input("Would you like to translate another number? (y/N) ")
    again = again or 'n'     # just pressing <Enter> means no
    again = again[0].lower() # look at only the first character and convert to lowercase

print()
