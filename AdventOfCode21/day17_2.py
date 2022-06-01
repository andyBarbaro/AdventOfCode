import sys
import numpy as np

def main():
    input = []
    possibleAngles = set()
    hits = set()
    target = set()

    with open('day17Input', 'r') as f:
        input = f.readline()

    input = input[:-1]
    input = input.split('=')
    xRange = input[1][:-3].split('..')
    yRange = input[-1].split('..')

    for x in range(int(xRange[0]), int(xRange[1])+1):
        for y in range(int(yRange[0]), int(yRange[1])+1):
            target.add((x,y))

    bottom = int(yRange[0])
    outerEdge = int(xRange[1])

    lowX = 0
    i = 2
    while sum(list(range(1, i))) < int(xRange[0]):
        i += 1

    lowX = max(list(range(1, i)))
    highX = outerEdge

    lowY = bottom
    highY = sum(list(range(1, abs(int(yRange[0])))))

    for x in range(lowX, highX+1):
        for y in range(lowY, highY+1):
            possibleAngles.add((x,y))

    for angle in possibleAngles:
        probePos = [0,0]
        deltaX = angle[0]
        deltaY = angle[1]
        while probePos[0] < outerEdge and probePos[1] > bottom:
            probePos[0] += deltaX
            probePos[1] += deltaY
            if tuple(probePos) in target:
                hits.add(angle)
                break
            deltaY -= 1
            if deltaX > 0:
                deltaX -= 1


    print(len(hits))

if __name__ == "__main__":
    main()
