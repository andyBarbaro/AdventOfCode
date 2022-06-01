txtFile = open("day13.txt", "r")

buses = txtFile.readlines()

myTime = int(buses[0])
busID = buses[1].split(',')

best = [0, myTime]

for id in busID:
    if id != 'x':
        wait = int(id) - (myTime%int(id))
        if wait < best[1]:
            best = [int(id), wait]
print(best[0]*best[1])
