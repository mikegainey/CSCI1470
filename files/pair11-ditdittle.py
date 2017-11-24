# count dit and dittle in Telegraph Line
# also, find the largest and shortest word

import string

with open("telegraph-line-lyrics.txt") as f:
    words = f.read().split()

dits = 0
dittles = 0
longest = ''
shortest = ''

words = map(lambda w: w.strip(string.punctuation).lower(), words)
words = list(words)

dits = words.count('dit')
dittles = words.count('dittle')

words.sort(key=len)

shortest = words[0]
longest = words[-1]

print("The number of dits = {}".format(dits))
print("The number of dittles = {}".format(dittles))
print("The shortest word is '{}'".format(shortest))
print("The longest word is '{}'".format(longest))

