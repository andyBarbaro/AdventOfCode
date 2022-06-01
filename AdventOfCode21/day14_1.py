import sys
import numpy as np
import re
import itertools

def main():
    input = []
    modInput = []
    start = ""
    insertions = {}
    letters = {}

    with open('day14Input', 'r') as f:
        input = f.readlines()


    start = input[0][:-1]

    for line in input[2:]:
        insertions[line[:line.index('-')-1]] = line[line.index('>')+2:-1]

    temp = ""
    for x in range(10):
        for i in range(len(start)-1):
            if i == 0:
                temp += start[i:i+1] + insertions[start[i:i+2]] + start[i+1:i+2]
            else:
                temp += insertions[start[i:i+2]] + start[i+1:i+2]

        if (x % 5) == 0:
            print(len(temp))

        start = temp
        temp = ""


    for letter in start:
        if letter not in letters:
            letters[letter] = start.count(letter)


    print(max(letters.values())-min(letters.values()))


if __name__ == "__main__":
    main()
