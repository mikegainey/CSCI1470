def reverse(number):

    reverse = 0
    while number != 0:

        reverse *= 10                   # shift all the digits of reverse to the left
        reverse = reverse + number % 10 # add the last digit of number to reverse
        number //= 10                    # strip the last digit off of number
        
    return reverse

print()
number = int(input("Enter a number to reverse: "))
print("The reverse of {} is {}.".format(number, reverse(number)))
print()
