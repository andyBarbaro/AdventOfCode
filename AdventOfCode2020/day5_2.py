import math
txtFile = open("day5.txt", "r")

boardingPasses = txtFile.readlines()
idList = []

for p in boardingPasses:
    letter = 0
    passRow = 0
    passCol = 0
    id = 0
    lowRow = 0
    highRow = 127
    lowCol = 0
    highCol = 7
    row = p[:7]
    column = p[7:10]
    for r in row:
        if letter != 6:
            if r == 'F':
                highRow = math.trunc((lowRow+highRow)/2)
            else :
                lowRow = math.trunc((lowRow+highRow)/2) + 1
        else:
            if r == 'F':
                passRow = lowRow
            else :
                passRow = highRow
        letter += 1
    for c in column:
        if letter != 9:
            if c == 'L':
                highCol = math.trunc((lowCol+highCol)/2)
            else :
                lowCol = math.trunc((lowCol+highCol)/2) + 1
        else :
            if c == 'L':
                passCol = lowCol
            else :
                passCol = highCol
        letter += 1
    id = passRow * 8 + passCol
    idList.append(id)

x = 1
while x < 888:
    myID = 1
    for i in idList:
        if x == i:
            myID = 0
    if myID :
        print(x)
    x += 1
