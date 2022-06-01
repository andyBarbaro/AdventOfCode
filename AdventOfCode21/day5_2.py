import sys
import re

def main():
    input = []
    modInput = []
    covered = {}

    with open('day5Input', 'r') as f:
        input = f.readlines()

    for line in input:
        modLine = re.split(' -> |,', line)
        modList = [(int(modLine[0]), int(modLine[1])), (int(modLine[2]), int(modLine[3]))]
        modInput.append(modList)

    for pair in modInput:
        deltaY = (pair[0][1]-pair[1][1])
        deltaX = (pair[0][0]-pair[1][0])
        slope = 0
        if deltaX != 0:
            slope = float(deltaY/deltaX)
        else:
            slope = sys.maxsize

        linePts = findLineSeg(slope, pair)

        for pt in linePts:
            if pt in covered:
                covered[pt] += 1
            else:
                covered[pt] = 1


    count = 0
    for val in covered.values():
        if val > 1:
            count += 1

    print(count)

def findLineSeg(m, pts):
    x = [pts[0][0], pts[1][0]]
    y = [pts[0][1], pts[1][1]]
    x.sort()
    y.sort()
    xList = list(range(x[0], x[1]+1))
    yList = list(range(y[0], y[1]+1))
    solutions = []
    if (m != sys.maxsize):
        b = pts[0][1] - m * pts[0][0]
        for xVal in xList:
            if (m * xVal + b) in yList:
                solutions.append((xVal, int(m * xVal + b)))
    else:
        for yVal in yList:
            solutions.append((x[0], yVal))

    return solutions


if __name__ == "__main__":
    main()
