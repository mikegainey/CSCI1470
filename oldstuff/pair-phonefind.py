def isPhoneNumber(maybeNumber):
    
    if len(maybeNumber) != 12:
        return False
    
    first3 = maybeNumber[:3].isdecimal()
    second3 = maybeNumber[4:7].isdecimal()
    last4 = maybeNumber[-4:].isdecimal()
    hyphens = maybeNumber[3] + maybeNumber[7] == '--'

    found = first3 and second3 and last4 and hyphens
    return found


def phoneFind(sentence):
    
    if len(sentence) < 12:
        return [] # too short to have a phone number
    
    else:
        phonelist = []
        for i in range(len(sentence) - 11):
            
            slice2check = sentence[i:(i+12)]
            
            if isPhoneNumber(slice2check):
                phonelist.append(slice2check)

        return phonelist


print(phoneFind(sentence1))
