class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return ("{}, {} years old".format(self.name, self.age))

    def birthday(self):
        self.age += 1
        

def armyCareer(person): # is person a copy of the argument, or is it an alias of the argument?
    print("Join the Army?  You will age 20 years!")
    for y in range(20):
        person.birthday()

        
m = Person("Mike", 27)
print(m) # print the value of the object

armyCareer(m)

print(m) # the object mutated in the function!

