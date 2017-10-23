###############################################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #
#
# Algorithm:
#   Define a function decode that takes a string parameter public_sentence.
#       Set words to a list of words created by splitting public_sentence at spaces.
#       Set firstletters to a list of letters formed from the first letter of each word in words.
#       Set secret_word to a string formed by joining the letters of firstletters.
#
#       Return secret_word to the calling function/program.
#
#
#   Define a function dateconv that takes a string parameter shortdate.
#       Set months to the list of months with a dummy placeholder value in index 0.
#
#       Set inmonth, inday, and inyear to the two character month, day, and year the user input.
#       Convert inmonth from a string to the corresponding integer.
#
#       Set outmonth to the element of months with index inmonth.
#       Set outday to inday.
#       Set outyear to "20" concatenated with inyear
#
#       Set longdate to a string of the form: outmonth outday, outyear
#       Return longdate to the calling function/program.
#
#
#   Set again to 'y' so the program loop will run the first time.
#   Begin a loop that executes while again is 'y':
#
#       Set shortdate to a date the users enters of the form mm/dd/yy.
#       Print the corresponding long date using the dateconv function.
#
#       Set string to a sentence the user enters.
#       Print the corresponding secret word using the decode function.
#
#       Prompt the user to enter another date and sentence.
#       Set again to 'n' if the user just presses <Enter>.
#       Set again to just the first character of the response and convert to lowercase.
#       (If again is 'y' the loop will run again, otherwise the program will end.)
#
###############################################################################

def decode(public_sentence):
    '''Given a string of words, return a word made from first letters of each word in the input string.
       decode(public_sentence : str) -> str
    '''

    words = public_sentence.split()            # split the public_sentence into words

    firstletters = [word[0] for word in words] # make a list of the first letter of each word

    secret_word = ''.join(firstletters)        # join the lists to make a string again

    return secret_word


def dateconv(shortdate):
    '''Given a date string in mm/dd/yy format, return a date string in Month dd, yyyy format
       dateconv(shortdate : str) -> str
    '''

    # month numbers correspond to list indices; note the placeholder at months[0]
    months = ['placeholder', 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    inmonth, inday, inyear = shortdate.split('/')
    inmonth = int(inmonth) # runtime error occurs if inmonth isn't two digits!
    
    outmonth = months[inmonth] # lookup the month string from the months list
    outday = inday
    outyear = '20' + inyear

    longdate = '{} {}, {}'.format(outmonth, outday, outyear)
    return longdate


again = 'y'
while again == 'y':

    shortdate = input("\nEnter a date in the format mm/dd/yy: ")
    print("That is {}.".format(dateconv(shortdate)))

    string = input("\nEnter your sentence to see the secret message: ")
    print("The secret message is {}.".format(decode(string)))
    
    again = input("\nDo you have another date and sentence? (y/N) ")
    again = again or 'n'
    again = again[0].lower()
    # if again == 'y' the loop will run again

