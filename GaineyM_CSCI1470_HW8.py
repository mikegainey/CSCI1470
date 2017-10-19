###############################################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #
#
# Algorithm:
#   Variable assignments
#   Prompt user for dayOfWeek
#   Get dayOfWeek
#   if dayOfWeek is Tuesday
#    ...
###############################################################################

def decode(sentence):

    words = sentence.split()                   # split the sentence into words

    firstletters = [word[0] for word in words] # make a list of the first letter of each word

    secretword = ''.join(firstletters)         # join the lists to make a string again

    return secretword


def dateconv(shortdate):

    months = ['zero', 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    inmonth, inday, inyear = shortdate.split('/')
    inmonth = int(inmonth) # runtime error occurs if inmonth isn't two digits!
    
    outmonth = months[inmonth]
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
    
    again = input("\nAgain? (y/N) ")
    again = again or 'n'
    again = again[0].lower()

