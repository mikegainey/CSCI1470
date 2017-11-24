# find words that start with a capital letter

import string # to use string.punctuation

def nopunc(word):
    return word.strip(string.punctuation)


fin = open('DeclarationOfIndependence.txt')
fout = open("capital.txt", 'w')

words = fin.read().split()

for word in words:
    if word[0] == word[0].upper():
        fout.write(nopunc(word) + '\n')

fin.close()
fout.close()
