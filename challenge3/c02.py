#!/usr/bin/env python
from utils import *

readline()
dictFile = readline()
readline()
n = readint()
readline()

words = []
results = {}

def sort(word):
    wrd = list(word)
    wrd.sort()
    return "".join(wrd)

for x in xrange(n):
    word = readline()
    words.append(word)
    results[sort(word)] = []

# Find the suggestions
for line_nl in open(dictFile, "r"):
    line = line_nl.strip()
    sl = sort(line)
    if sl in results:
        results[sl].append(line)

for word in words:
    res = results[sort(word)]
    res.sort()
    print word + " -> " + (" ".join(filter(lambda x: x != word, res)))

