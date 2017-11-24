# Count the number of occurences of each word in a file and print the word and number of times it occurs.

import string

while True:
    filename = input("\nEnter the name of a text file (in the current directory): ")
    try:
        with open(filename, errors='ignore') as f:
            words = f.read().split()
            break
    except:
        print("Error -- couldn't read the file. Please try again.")

# remove punctuation and convert to lowercase
words = map(lambda w: w.strip(string.punctuation).lower(), words)

# count words
wordMap = dict()
for word in words:
    if word in wordMap:
        wordMap[word] += 1
    else:
        wordMap[word] = 1

# print word frequencies in order (highest to lowest)
wordFreqs = wordMap.items() # wordFreqs is a list of tuples (word, freq)
wordFreqs = sorted(wordFreqs, key=lambda item: item[1], reverse=True)

# print the 30 words with highest frequency
for i in range(30):
    print("{}, {} times".format(wordFreqs[i][0], wordFreqs[i][1]))
