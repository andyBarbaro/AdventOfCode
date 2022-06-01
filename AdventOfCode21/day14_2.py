import sys
import numpy as np
import re
import itertools

def main():
    input = []
    modInput = []
    start = ""
    insertions = {}
    letterPairs = {}
    letters = {}

    with open('day14Input', 'r') as f:
        input = f.readlines()

    start = input[0][:-1]

    for line in input[2:]:
        insertions[line[:line.index('-')-1]] = line[line.index('>')+2:-1]
        letterPairs[line[:line.index('-')-1]] = 0

    for val in set(insertions.values()):
        letters[val] = 0

    for l in start:
        letters[l] += 1

    for i in range(len(start)-1):
        letterPairs[start[i:i+2]] += 1

    for x in range(40):
        temp = letterPairs.copy()
        for p in letterPairs:
            letters[insertions[p]] += letterPairs[p]
            newPair1 = p[0] + insertions[p]
            newPair2 = insertions[p] + p[1]
            temp[newPair1] += letterPairs[p]
            temp[newPair2] += letterPairs[p]
            temp[p] -= letterPairs[p]

        letterPairs = temp.copy()

    print(max(letters.values())-min(letters.values()))


if __name__ == "__main__":
    main()
