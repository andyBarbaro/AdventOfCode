import sys
import numpy as np
import re
import itertools

def main():
    input = []
    modInput = []
    folds = []

    with open('day13Input', 'r') as f:
        input = f.readlines()

    for line in input:
        if ',' in line:
            modInput.append((int(line[:line.index(',')]), int(line[line.index(',')+1:])))
        elif "fold" in line:
            folds.append((line[line.index('=')-1], int(line[line.index('=')+1:])))

    newSheet = []

    for f in folds:
        if f[0] == 'x':
            for val in modInput:
                if val[0] > f[1]:
                    newMark = (f[1]-(val[0]-f[1]), val[1])
                    if newMark not in newSheet:
                        newSheet.append(newMark)
                elif val not in newSheet:
                    newSheet.append(val)
        else:
            for val in modInput:
                if val[1] > f[1]:
                    newMark = (val[0], f[1]-(val[1]-f[1]))
                    if newMark not in newSheet:
                        newSheet.append(newMark)
                elif val not in newSheet:
                    newSheet.append(val)

        modInput = newSheet
        newSheet = []

    print(len(modInput))

    for x in range(7):
        for y in range(50):
            if (y,x) in modInput:
                print("#", end="")
            else:
                print(" ", end="")
        print()

if __name__ == "__main__":
    main()
