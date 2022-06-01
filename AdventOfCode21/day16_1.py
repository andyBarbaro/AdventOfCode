import sys
import numpy as np

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

    x, versionSum = handleTrans(modInput, 0, False)

    print(versionSum)

def handleTrans(binaryStr, pos, op):
    versionSum = 0
    sum = 0
    if pos > len(binaryStr):
        return pos, versionSum
    version = int(binaryStr[pos:pos+3], 2)
    pos += 3
    sum += 3
    typeID = int(binaryStr[pos:pos+3], 2)
    pos += 3
    sum += 3

    versionSum += version

    if typeID == 4:
        literal = ""
        while int(binaryStr[pos]) != 0:
            literal += binaryStr[pos+1:pos+5]
            pos += 5
            sum += 5
        literal += binaryStr[pos+1:pos+5]
        pos += 5
        sum += 5
        if not op:
            while (sum % 4 != 0):
                pos += 4 - (sum%4)
                sum += 4 - (sum%4)

    else:
        if int(binaryStr[pos]) == 0:
            pos += 1
            length = int(binaryStr[pos:pos+15], 2)
            pos += 15
            savePos = pos
            while pos - savePos < length:
                temp1, temp2 = handleTrans(binaryStr, pos, True)
                pos = temp1
                versionSum += temp2
        else:
            pos += 1
            numOfSubs = int(binaryStr[pos:pos+11], 2)
            pos += 11
            for i in range(numOfSubs):
                temp1, temp2 = handleTrans(binaryStr, pos, True)
                pos = temp1
                versionSum += temp2

    return pos, versionSum


if __name__ == "__main__":
    main()
