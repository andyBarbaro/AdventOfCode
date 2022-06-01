import numpy as np
txtFile = open("day10.txt", "r")

adapters = txtFile.readlines()
adaptersInt = []
nextAdapt = {}
seen = {}
highestValue = 0
combos = 0

for a in adapters:
    if int(a) > highestValue:
        highestValue = int(a)
    adaptersInt.append(int(a))

highestValue += 3
adaptersInt.append(0)
adaptersInt.append(highestValue)
adapters = np.sort(adaptersInt)

for i in range(len(adapters)-1):
    next = 1
    possibleNext = []
    nextAdapt[adapters[i]] = set([])
    while i+next < len(adapters) and adapters[i+next] - adapters[i] <= 3:
        nextAdapt[adapters[i]].add(adapters[i+next])
        next += 1

def numberOfLeaves(root, leafAdapt, adaptTree):
    leafTotal = 0
    if root != leafAdapt:
        #look at all possible next adapters
        for child in adaptTree[root]:
            if child not in seen:
                #adds up the total number of leaves at the end of this root
                leafForRoot = numberOfLeaves(child, leafAdapt, adaptTree)
                seen[child] = leafForRoot
            else:
                leafForRoot = seen[child]
            leafTotal += leafForRoot

        return leafTotal
    else :
        return 1

combos = numberOfLeaves(0, highestValue, nextAdapt)
print(seen)
print(combos)
