txtFile = open("day13.txt", "r")

buses = txtFile.readlines()

busID = buses[1].split(',')

highest = 0

for n in busID:
    hold = 0
    if n != 'x':
        if int(n) > highest:
            highest = int(n)
busID[len(busID)-1] = busID[len(busID)-1][:-1]

i = 100000000000
while True:
    print(i)
    fail = 0
    possible = highest * i
    for id in busID:
        if id != 'x':
            relativeIndex = busID.index(str(highest)) - busID.index(id)
            if (possible-relativeIndex) % int(id) != 0:
                fail = 1
                break
    if not fail:
        print(possible-busID.index(str(highest)))
        break
    i += 1
#print()

"""for id in busID:
    if id != 'x':
        wait = int(id) - (myTime%int(id))
        if wait < best[1]:
            best = [int(id), wait]
print(best[0]*best[1])"""
