# find words with an apostrophe

fin = open('ConjunctionJunction.txt')
fout = open("conJunction.txt", 'w')

words = fin.read().split()

for word in words:
    if "'" in word:
        fout.write(word + ' ')

fin.close()
fout.close()
