# endswith ax, axe, acks; rstrip '.!,;?'

def rhymes(word):

    if not word[-1].isalpha(): # if it ends with a non-alpha
        word = word[:-1]       # strip the last character

    endings = ['ax', 'axe', 'acks']

    for ending in endings:
        if word.endswith(ending):
            return True

    return False


fin = open("TaxManMax.txt")
fout = open("rhymesWithMax.txt", "w")

words = fin.read().split()
for word in words:
    if rhymes(word):

        if not word[-1].isalpha(): # if it ends with a non-alpha
            word = word[:-1]       # strip the last character

        fout.write(word + ' ')

fin.close()
fout.close()
