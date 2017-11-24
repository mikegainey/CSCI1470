# find words followed by an exclamation point

fin = open('Interjections.txt')
fout = open("interJections.txt", 'w')

words = fin.read().split()

for word in words:
    if "!" in word:
        fout.write(word + ' ')

fin.close()
fout.close()
