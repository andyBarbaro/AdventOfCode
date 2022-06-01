txtFile = open("day15.txt", "r")

turns = txtFile.readlines()

turn = turns[0].split(',')
turnDict = {}
lastTurn = 0

i = 1
for t in turn:
    turnDict[int(t)] = i
    lastTurn = int(t)
    i += 1

saveTurn = [lastTurn, turnDict.pop(lastTurn)]
while i <= 30000000:
    if saveTurn[0] not in turnDict:
        turnDict[saveTurn[0]] = saveTurn[1]
        saveTurn = [0, i]
    else:
        prev = saveTurn[1] - turnDict[saveTurn[0]]
        turnDict[saveTurn[0]] = saveTurn[1]
        saveTurn = [prev, i]
    i += 1
print(saveTurn[0])
