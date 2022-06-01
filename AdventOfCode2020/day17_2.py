from itertools import product
import copy
txtFile = open("day17.txt", "r")

dimMap = txtFile.readlines()
neighbors = list(product([0,1,-1], repeat=4))
neighbors.remove((0,0,0,0))
actives = set([])
inactives = set([])

rowNum = 0
while rowNum < len(dimMap):
    columnNum = 0
    while columnNum < len(dimMap[0])-1:
        if dimMap[rowNum][columnNum] == '#':
            actives.add((rowNum, columnNum, 0, 0))
        columnNum += 1
    rowNum += 1

i = 0
while i < 6:
    toRemA = []
    toRemIn = []
    toAddA = []
    toAddIn = []
    for cube in actives:
        activeNeighbors = 0
        for n in neighbors:
            if (n[0]+cube[0], n[1]+cube[1], n[2]+cube[2], n[3]+cube[3]) in actives:
                activeNeighbors += 1
            else:
                inactives.add((n[0]+cube[0], n[1]+cube[1], n[2]+cube[2],  n[3]+cube[3]))
        if activeNeighbors != 2 and activeNeighbors != 3:
            toAddIn.append(cube)
            toRemA.append(cube)

    for iCube in inactives:
        activeNeighbors = 0
        for n in neighbors:
            if (n[0]+iCube[0], n[1]+iCube[1], n[2]+iCube[2],  n[3]+iCube[3]) in actives:
                activeNeighbors += 1
        if activeNeighbors == 3:
            toAddA.append(iCube)
            toRemIn.append(iCube)
    for term in toRemA:
        actives.remove(term)
    for term in toRemIn:
        inactives.remove(term)
    for term in toAddA:
        actives.add(term)
    for term in toAddIn:
        inactives.add(term)
    i += 1

print(len(actives))
