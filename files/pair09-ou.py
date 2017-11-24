# In the Busy Prepositions file, find the words containing 'ou' and output them to busyPrep.txt

import string

fin = open('BusyPrepositions.txt')
fout = open('busyPrep.txt', 'w')

words = fin.read().split()

ouWords = filter(lambda w: 'ou' in w, words)

for word in ouWords:
    outword = word.strip(string.punctuation)
    fout.write(outword + '\n')

fin.close()
fout.close()
