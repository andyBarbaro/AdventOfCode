txtFile = open("day7.txt", "r")

bagRules = txtFile.readlines()
bags = {}
bagPrev = []
bagListNext = []
finalBagCount = 0
colorToView = "shinygold"

for rule in bagRules:
    fragments = rule.split('contain')
    fragNum = 0
    for frag in fragments:
        elCount = 0
        possibleColors = frag.split(' ')
        for word in possibleColors:
            if "bag" in word and fragNum == 0:
                bagColor = possibleColors[elCount - 2] + possibleColors[elCount - 1]
                bagPrev = bagColor
                bags.update({bagPrev : set([])})
            elif "bag" in word and fragNum == 1:
                bagColor = possibleColors[elCount - 2] + possibleColors[elCount - 1]
                if "other" not in bagColor:
                    numberBags = int(possibleColors[elCount - 3])
                    bagListNext.append([bagColor, numberBags])
                else:
                    bagListNext.append([bagColor, 0])
            elCount += 1
        if fragNum == 1:
            bags[bagPrev] = bagListNext
        fragNum = 1
    bagListNext = []
    bagPrev = []

def numberOfBags(color, numBags, bagDict):
    bagTotal = 0
    if color != "noother":
        for bag in bagDict:
            #find our bag and its contents
            if bag == color:
                #look at the bags inside our bag
                for b in bagDict[bag]:
                    #adds up the total number of bags in our bag
                    bagTotal += b[1] + b[1] * numberOfBags(b[0], b[1], bagDict)

        return bagTotal
    else :
        return 1


finalBagCount = numberOfBags(colorToView, 0, bags)
print(finalBagCount)
