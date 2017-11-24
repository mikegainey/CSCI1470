# filter out words with no 'e' in GettysburgAddress.txt and write output to GettysNoE.txt

import string

def hasNoE(word):
    """Return True if the given word doesn't contain an 'e"""
    return 'e' not in word

def nopunc(word):
    """Given a word, return the word stripped of leading & trailing punctuation."""
    return word.strip(string.punctuation)


f = open('GettysburgAddress.txt', errors='ignore')
words = f.read().split()
f.close()

newWords = []
for word in words:
    if hasNoE(word):
        newWords.append(word)

f = open('GettysNoE.txt', 'w')
for word in newWords:
    f.write(nopunc(word) + '\n')
f.close()
