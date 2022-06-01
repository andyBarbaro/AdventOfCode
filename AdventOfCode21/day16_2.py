import sys
from operator import mul

def main():
    input = []
    modInput = ""

    with open('day16Input', 'r') as f:
        input = f.readline()

    input = input[:-1]

    for val in input:
        x = int(val, 16)
        x = format(x, '04b')
        modInput += x

    print(len(modInput))
    x, result = handleTrans(modInput, 0, False)

    print(result)

def handleTrans(binaryStr, pos, op):
    litInt = 0
    bitCount = 0
    if pos == len(binaryStr):
        return pos, 0
    version = int(binaryStr[pos:pos+3], 2)
    pos += 3
    bitCount += 3
    typeID = int(binaryStr[pos:pos+3], 2)
    pos += 3
    bitCount += 3

    if typeID == 4:
        literal = ""
        while int(binaryStr[pos]) != 0:
            literal += binaryStr[pos+1:pos+5]
            pos += 5
            bitCount += 5
        literal += binaryStr[pos+1:pos+5]
        litInt = int(literal, 2)
        pos += 5
        bitCount += 5
        if not op:
            if (bitCount % 4 != 0):
                pos += 4 - (bitCount%4)
                bitCount += 4 - (bitCount%4)

    elif typeID == 0:
        pos, valList = operations(binaryStr, pos)
        litInt = sum(valList)

    elif typeID == 1:
        pos, valList = operations(binaryStr, pos)
        litInt = 1
        for i in valList:
            litInt *= i

    elif typeID == 2:
        pos, valList = operations(binaryStr, pos)
        litInt = min(valList)

    elif typeID == 3:
        pos, valList = operations(binaryStr, pos)
        litInt = max(valList)

    elif typeID == 5:
        pos, valList = operations(binaryStr, pos)
        if valList[0] > valList[1]:
            litInt = 1
        else:
            litInt = 0

    elif typeID == 6:
        pos, valList = operations(binaryStr, pos)
        if valList[0] < valList[1]:
            litInt = 1
        else:
            litInt = 0

    elif typeID == 7:
        pos, valList = operations(binaryStr, pos)
        if valList[0] == valList[1]:
            litInt = 1
        else:
            litInt = 0

    return pos, litInt



def operations(binaryStr, pos):
    valList = []
    if int(binaryStr[pos]) == 0:
        pos += 1
        length = int(binaryStr[pos:pos+15], 2)
        pos += 15
        savePos = pos
        while pos - savePos < length:
            temp1, temp2 = handleTrans(binaryStr, pos, True)
            pos = temp1
            valList.append(temp2)

    else:
        pos += 1
        numOfSubs = int(binaryStr[pos:pos+11], 2)
        pos += 11
        for i in range(numOfSubs):
            temp1, temp2 = handleTrans(binaryStr, pos, True)
            pos = temp1
            valList.append(temp2)

    return pos, valList



if __name__ == "__main__":
    main()
