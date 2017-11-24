# Ask the user for a word and a letter.
# Count the number of times the letter occurs in the word

print()
word = input("Enter a word: ")
letter = input("Enter a letter: ")

count = 0
for char in word:
    if char == letter:
        count += 1

print("'{}' occurs {} times in {}.".format(letter, count, word))
print()
