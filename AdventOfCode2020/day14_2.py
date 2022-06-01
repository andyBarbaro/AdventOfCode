from itertools import product
import copy
txtFile = open("day14.txt", "r")

binaryLines = txtFile.readlines()
memDict = {}

for line in binaryLines:
    value = ''
    if "mask" in line:
        mask = line[7:]
    else:
        memSpot = int(line[4:line.index(']')])
        value = int(line.split(' ')[2])
        memSpot = str(bin(memSpot).replace("0b",""))
        memSpot = list(memSpot.rjust((36-len(memSpot))+len(memSpot), '0'))
        i = 0
        xCount = 0
        for bit in mask[:-1]:
            if bit == 'X':
                memSpot[i] = 'X'
                xCount += 1
            elif bit == '1':
                memSpot[i] = bit
            i += 1
        #print(memSpot)
        hold = copy.deepcopy(memSpot)
        floatingVals = product(['0','1'], repeat=xCount)
        for combo in floatingVals:
            i = 0
            comboSpot = 0
            for position in memSpot:
                if position == 'X':
                    memSpot[i] = combo[comboSpot]
                    comboSpot += 1
                i += 1
            string1 = ""
            string1 = string1.join(memSpot)
            memDict[string1] = value
            memSpot = copy.deepcopy(hold)

finalSum = 0
for key in memDict:
    finalSum += memDict[key]
print(finalSum)
