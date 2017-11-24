# find and print all the numbers in the lyrics from Little-Twelvetoes-lyrics.txt

import string

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
           'dek', 'el', 'doh', '12', '24', '36', '48', '60', '72', '84', '96', '108', '120', '132', '144']

f = open('Little-Twelvetoes-lyrics.txt')

words = f.read().split()

f.close()

for w in words:
    word = w.strip(string.punctuation)
    if word.lower() in numbers:
        print(word, end=' ')
print()
