def trans_char(in_char):
    '''Translate one character'''
    
    letters = 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'
    numbers = '222 333 444 555 666 7777 888 9999'

    in_char = in_char.upper()
    if in_char in letters:
        index = letters.find(in_char)
        out_char = numbers[index]
    else:
        out_char = in_char

    return out_char


def translate(alphanumeric):
    '''translate a string'''
    
    numeric = ''
    for character in alphanumeric:
        numeric += trans_char(character)
    return numeric


again = 'y'         # so the loop will run the first time
while again == 'y': # loop until the user decides to stop

    phoneNumber = input("\nEnter a 10 character alphanumeric telephone number in the form of XXX-XXX-XXXX: ")
    print("The equivalent numeric phone number is {}".format(translate(phoneNumber)))

    again = input("Would you like to translate another number? (y/N) ")
    again = again or 'n'     # just pressing <Enter> means no
    again = again[0].lower() # look at only the first character and convert to lowercase

print()
