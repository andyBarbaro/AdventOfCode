import copy
txtFile = open("day11.txt", "r")

seatRow = txtFile.readlines()
neighbors = [[-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0]]
noChange = 0

sRow = []
sRowHold = []
for x in seatRow:
    sRow.append(list(x[:len(x)-1]))

sRowHold = copy.deepcopy(sRow)

while not noChange:
    noChange = 1
    for i in range(len(sRow)):
        for j in range(len(sRow[0])):
            adjFullCount = 0
            seat = sRow[i][j]
            if seat != '.':
                for n in neighbors:
                    if i+n[0] in range(len(sRow)) and j+n[1] in range(len(sRow[0])):
                        adjSeat = sRow[i+n[0]][j+n[1]]
                        if (adjSeat == '#'):
                            adjFullCount += 1
                if seat == 'L' and adjFullCount == 0:
                    noChange = 0
                    sRowHold[i][j] = '#'
                elif seat == '#' and adjFullCount >= 4:
                    noChange = 0
                    sRowHold[i][j] = 'L'
    sRow = copy.deepcopy(sRowHold)


takenCount = 0
for row in sRow:
    for seat in row:
        if seat == "#":
            takenCount += 1
print(takenCount)
