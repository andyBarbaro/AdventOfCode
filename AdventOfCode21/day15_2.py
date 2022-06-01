import sys
import numpy as np

def main():
    input = []
    modInput = []
    visited = []
    unvisited = []
    dTable = {}

    with open('day15Input', 'r') as f:
        input = f.readlines()

    for line in input:
        modInput.append(list(line[:-1]))


    riskMap =  np.array(modInput)
    riskMap =  riskMap.astype('int')
    saved = np.copy(riskMap)

    for i in range(4):
        riskMap = np.append(saved, riskMap+1, axis=0)

    saved = np.copy(riskMap)
    for i in range(4):
        riskMap = np.append(saved, riskMap+1, axis=1)

    mapTotal = np.sum(riskMap)

    for y in range(len(riskMap[:,0])):
        for x in range(len(riskMap[0,:])):
            if riskMap[y, x] > 9:
                riskMap[y, x] = riskMap[y, x] % 9

    for y in range(len(riskMap[:,0])):
        for x in range(len(riskMap[0,:])):
            dTable[(y, x)] = [riskMap[y, x], mapTotal]

    dTable[(0,0)] = [riskMap[0,0], 0]

    shortestPathSearch((0,0), dTable, riskMap, visited, [])

    print(dTable[len(riskMap[:,0])-1, len(riskMap[0,:])-1][1])


def shortestPathSearch(currentNode, map, view, v, seen):
    end = (len(view[:,0])-1, len(view[0,:])-1)
    while (end not in v):
        v.append(currentNode)
        y = currentNode[0]
        x = currentNode[1]

        if y != 0 and ((y-1, x) not in v):
            updateTable(currentNode, map, (y-1, x), seen)

        if x != 0 and ((y, x-1) not in v):
            updateTable(currentNode, map, (y, x-1), seen)

        if y != len(view[:,0])-1 and ((y+1, x) not in v):
            updateTable(currentNode, map, (y+1, x), seen)

        if x != len(view[0,:])-1 and ((y, x+1) not in v):
            updateTable(currentNode, map, (y, x+1), seen)

        short = sys.maxsize
        shortNode = (0,0)
        for n in seen:
            heurVal = (end[0]-n[0]) + (end[1]-n[1])
            if map[n][1]+heurVal < short:
                shortNode = n
                short = map[n][1]+heurVal

        if shortNode in seen:
            seen.remove(shortNode)
        currentNode = shortNode
        print(len(v))

    return 0

def updateTable(node, map, neighbor, s):
    if neighbor not in s:
        s.append(neighbor)
    if map[node][1] + map[neighbor][0] < map[neighbor][1]:
        map[neighbor][1] = map[node][1] + map[neighbor][0]

if __name__ == "__main__":
    main()
