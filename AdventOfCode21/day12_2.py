import sys

def main():
    input = []
    modInput = []
    caveMap = {}
    paths = 0


    with open('day12Input', 'r') as f:
        input = f.readlines()

    for line in input:
        connection = line.split('-')
        if connection[1][:-1] != "start":
            if connection[0] in caveMap:
                caveMap[connection[0]].append(connection[1][:-1])
            else:
                caveMap[connection[0]] = [connection[1][:-1]]

        if connection[0] != "start":
            if connection[1][:-1] in caveMap:
                caveMap[connection[1][:-1]].append(connection[0])
            else:
                caveMap[connection[1][:-1]] = [connection[0]]


    visitedCaves = {}
    paths = findPath("start", caveMap, visitedCaves, False)

    print(paths)

def findPath(currentCave, caveMap, vC, doubleSmall):
    newPaths = 0

    for connected in caveMap[currentCave]:
        if connected == "end":
            newPaths += 1
        elif (connected not in vC) or (2 not in vC.values()):
            if not connected.isupper():
                if connected in vC:
                    vC[connected] += 1
                else:
                    vC[connected] = 1

            newPaths += findPath(connected, caveMap, vC, doubleSmall)

            if not connected.isupper():
                if vC[connected] == 2:
                    vC[connected] -= 1
                else:
                    vC.pop(connected)


    return newPaths


if __name__ == "__main__":
    main()
