def translate(alphanumeric):
    '''Given an alphanumeric phone number, return the equivalent all-numeric phone number.
       translate(alphanumeric: str) -> str
    '''

    letters = 'ABC DEF GHI JKL MNO PQRS TUV WXYZ' # the map from: letters
    numbers = '222 333 444 555 666 7777 888 9999' #           to: numbers
    
    numeric = ''                   # this will be the output string
    for character in alphanumeric: # traverse the input

        # translate one character
        in_char = character.upper()
        if in_char in letters:
            index = letters.find(in_char)
            out_char = numbers[index]
        else:
            out_char = in_char

        numeric += out_char # build the output string

    return numeric


again = 'y'         # so the loop will run the first time
while again == 'y': # loop until the user decides to stop

    phoneNumber = input("\nEnter a 10 character alphanumeric telephone number in the form of XXX-XXX-XXXX: ")
    print("The equivalent numeric phone number is {}".format(translate(phoneNumber)))

    again = input("Would you like to translate another number? (y/N) ")
    again = again or 'n'     # just pressing <Enter> means no
    again = again[0].lower() # look at only the first character and convert to lowercase

print()
