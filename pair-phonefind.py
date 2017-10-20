# sentence = "This sentence has a phone number. It is 482-2547.  It is an old number."
sentence = "55a lalala"
print(sentence)
print()

i = 0 # the index of the string
lasti = len(sentence) - 8 # the last index that could have a 7-digit phone number

while i <= lasti:
    print("looking at i = {}\n".format(i))
    
    if sentence[i].isdigit():
        maybe = 1 # one digit found
        print("{} maybe = {}".format(sentence[i], maybe))
        
        if sentence[i+1].isdigit():
            maybe = 2
            print("{} maybe = {}".format(sentence[i+1], maybe))
                        
            if sentence[i+2].isdigit():
                maybe = 3
                print("{} maybe = {}".format(sentence[i+2], maybe))
                
    i += maybe
    maybe = 0
