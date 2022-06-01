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
    mapTotal = np.sum(riskMap)

    for y in range(len(riskMap[:,0])):
        for x in range(len(riskMap[0,:])):
            dTable[(y, x)] = [riskMap[y, x], mapTotal, (-1,-1)]
            unvisited.append((y, x))

    dTable[(0,0)] = [riskMap[0,0], 0, None]

    shortestPathSearch((0,0), dTable, riskMap, visited, unvisited)

    print(dTable[len(riskMap[:,0])-1, len(riskMap[0,:])-1][1])



def shortestPathSearch(currentNode, map, view, v, u):
    #print(currentNode)
    while (len(u) != 0):
        v.append(currentNode)
        u.remove(currentNode)
        y = currentNode[0]
        x = currentNode[1]

        if y != 0 and ((y-1, x) not in v):
            updateTable(currentNode, map, (y-1, x))

        if x != 0 and ((y, x-1) not in v):
            updateTable(currentNode, map, (y, x-1))

        if y != len(view[:,0])-1 and ((y+1, x) not in v):
            updateTable(currentNode, map, (y+1, x))

        if x != len(view[0,:])-1 and ((y, x+1) not in v):
            updateTable(currentNode, map, (y, x+1))

        shortPath = [sys.maxsize, (0,0)]
        for val in u:
            if map[val][1] < shortPath[0]:
                shortPath = [map[val][1], val]

        currentNode = shortPath[1]

    return 0

def updateTable(node, map, neighbor):
    if map[node][1] + map[neighbor][0] < map[neighbor][1]:
        map[neighbor][1] = map[node][1] + map[neighbor][0]
        map[neighbor][2] = node

if __name__ == "__main__":
    main()
