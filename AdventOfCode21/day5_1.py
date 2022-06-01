import sys
import re

def main():
    input = []
    hors = []
    verts = []
    covered = {}

    with open('day5Input', 'r') as f:
        input = f.readlines()

    for line in input:
        modLine = re.split(' -> |,', line)
        if int(modLine[0]) == int(modLine[2]):
            verts.append(modLine)
        elif int(modLine[1]) == int(modLine[3]):
            hors.append(modLine)

    for vent in verts:
        y = [int(vent[1]),int(vent[3])]
        y.sort()
        for yVal in list(range(y[0], y[1]+1)):
            orderedPair = (int(vent[0]), yVal)
            if orderedPair in covered:
                covered[orderedPair] += 1
            else:
                covered[orderedPair] = 1

    for vent in hors:
        x = [int(vent[0]),int(vent[2])]
        x.sort()
        for xVal in list(range(x[0], x[1]+1)):
            orderedPair = (xVal, int(vent[1]))
            if orderedPair in covered:
                covered[orderedPair] += 1
            else:
                covered[orderedPair] = 1

    count = 0
    for val in covered.values():
        if val > 1:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
