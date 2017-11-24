# Ask the user to input a string and a word.
# Count the number of occurances of the word in the string.

print()
string = input("Enter a string: ")
targetWord = input("Enter a word: ")

count = 0
for word in string.split():
    if word == targetWord:
        count += 1

print("'{}' occurs {} times in '{}'.".format(targetWord, count, string))
print()
