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
        value = str(bin(value).replace("0b",""))
        value = list(value.rjust((36-len(value))+len(value), '0'))
        #print(value)
        i = 0
        for bit in mask[:-1]:
            if bit != 'X':
                value[i] = bit
            i += 1
        #print(value)
        string1 = ""
        string1 = string1.join(value)
        #print(string1)
        memDict[memSpot] = int(string1, 2)

finalSum = 0
for key in memDict:
    finalSum += memDict[key]
print(finalSum)
