import sys
import math

def main():
    input = []
    sumList = []

    with open('day18Input', 'r') as f:
        input = f.readlines()


    for line in input:
        hold = eval(line)
        if len(sumList) == 0:
            sumList = hold
        else:
            sumList = [sumList, hold]

        indexList = indexer(sumList)

        indexParser(indexList, sumList)
        print(sumList)



def indexer(myList):
    rtnList = []
    if type(myList[0]) is list:
        rtnList.append(0)
        rtnList += indexer(myList[0])
    else:
        rtnList.append(1)

    if type(myList[1]) is list:
        rtnList.append(0)
        rtnList += indexer(myList[1])
    else:
        rtnList.append(2)

    return rtnList


def indexParser(iList, myList):
    listDepth = 0
    prevLeft = None
    nextRight = None
    updated = False

    for i in range(len(iList)):
        print(myList)
        if iList[i] == 0:
            listDepth += 1

        else:
            if iList[i] == 1 and listDepth >= 4:
                leftExplode = accessList(iList[:i+1], myList)
                for x in iList[i-1::-1]:
                    if x != 0:
                        prevLeft = x
                        break
                if prevLeft != None:
                    updateList(iList[:prevLeft+1], myList, leftExplode, "update")

                rightExplode = accessList(iList[:i+2], myList)
                """FIX NEXT RIGHT"""
                count = 0
                print("wng")
                print(iList[i+2:])
                for x in iList[i+2:]:
                    if x != 0:
                        nextRight = count + (i+2)
                        break
                    count += 1
                if nextRight != None:
                    print(":yop")
                    print(iList[:nextRight+1])
                    updateList(iList[:nextRight+1], myList, rightExplode, "update")

                print(iList[:i+2])
                updateList(iList[:i+2], myList, 0, "zero")
                iList.pop(i-1)
                iList.pop(i)
                updated = True

            elif iList[i] == 2:
                listDepth -= 1

            """elif accessList(iList[:i+1], myList) > 9:
                print("split")
                updated = True"""


            if updated:
                indexParser(iList, myList)
                break


def accessList(iList, myList):
    if len(iList) > 1:
        numOrList = iList[0]
        if numOrList > 0:
            return accessList(iList[1:], myList)
        else:
            return accessList(iList[1:], myList[0])
    else:
        return myList[iList[0]-1]


def updateList(iList, myList, changeVal, action):
    print("pine")
    print(iList)
    print(myList)
    if len(iList) > 1:
        numOrList = iList[0]
        if numOrList > 0:
            return updateList(iList[1:], myList, changeVal, action)
        else:
            return updateList(iList[1:], myList[iList[0]], changeVal, action)

    else:
        if action == "zero":
            myList = changeVal
        elif action == "update":
            myList[iList[0]-1] += changeVal





if __name__ == "__main__":
    main()
