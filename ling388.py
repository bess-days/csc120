paragraph1 = """Alice was beginning to get very tired of sitting by her
sister on the bank, and of having nothing to do. Once or twice she had
peeped into the book her sister was reading, but it had no pictures or
conversations in it, "and what is the use of a book," thought Alice,
"without pictures or conversations?"""
list = [4,3,2,1]
lowest = list.pop()
slowest = list.pop()
mid = list.pop()
highest = list.pop()
list.append(lowest)
list.append(slowest)
list.append(mid)
list.append(highest)
vowels = {"a", "e", "i", "o", "u", "u"}
sentence = "You're smart if you can read this"
def remove_vowels(sentence):
    return "".join([letter for letter in sentence if letter not in vowels])
l = sentence.split()
print(" ".join([x[0]+remove_vowels(x[1:]) for x in l]))
owners = ["Sydney", "Lisa", "Jozlin"]
dogs = ["Luna", "Peyton", "Izzy"]

for own, dog in zip(owners,dogs):
    print("Who is {}'s dog? {}".format(own,dog))


paragraph2 = paragraph1
#for i in range(len(paragraph2.split())): print(paragraph2.split()[i])
import re
word = 'conversations?"'
print(re.sub('[?\"/.]',"", word))
#for i in range(len(paragraph2.split())): print(re.sub('[?\"/.,]', "", paragraph2.split()[i]))
#print([x.lower() for x in paragraph2])
#print([re.sub("[?\',\"'.]", "", x.lower()) for x in paragraph2])

paragraph2 = paragraph1.split()
for word in paragraph2:
    print(re.sub(r"[?\"',.]", "", word))

from collections import Counter
c = Counter(['this', 'is', 'a', 'test', 'of', 'this', 'code'])
#print(c.most_common())
text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way-in short, the period was so far like the present period that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."
c = Counter([re.sub("[?\',\"\-.]", "", x.lower()) for x in text.split()])
#print(c.most_common())

import matplotlib
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt
courses = ["ling 388", "ling 438", "ling 538"]
enrollment = [10,14,16]
"""plt.bar(courses, enrollment)
plt.xticks(np.arange(3), courses)
#plt.show()"""
t = Counter([re.sub("[?\',\"\-.]", "", w.lower()) for w in text.split()])
lists_of = t.most_common()
words = [list[0] for list in lists_of]
counts = [list[1] for list in lists_of]
plt.barh(words, counts)
plt.xticks(np.arange(len(words)), words)
plt.show()

