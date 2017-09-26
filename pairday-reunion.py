print()
print("Register for the family reunion!  (Press <Enter> after the last entry.)")
print()

#initialize variables
total = Morales = Poloski = Jones = Ahmed =  over50 = under5 = 0

while True:
    fname = input("What is your first name? ")
    if fname == '':
        break
    lname = input("What is your last name? ")
    age = int(input("What is your age? "))
    print()
    
    total += 1
    if lname == "Morales":
        Morales += 1
    if lname == "Poloski":
        Poloski += 1
    if lname == "Jones":
        Jones += 1
    if lname == "Ahmed":
        Ahmed += 1
    if age > 50:
        over50 += 1
    if age < 5:
        under5 += 1

print()
print("The total number of people attending the reunion will be {}.".format(total))
print("  {} from the Morales family".format(Morales))
print("  {} from the Poloski family".format(Poloski))
print("  {} from the Jones family".format(Jones))
print("  {} from the Ahmed family".format(Ahmed))
print("  {} over age 50".format(over50))
print("  {} four years old or younger".format(under5))
print()
