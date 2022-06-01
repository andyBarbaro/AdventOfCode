txtFile = open("day7.txt", "r")

bagRules = txtFile.readlines()
bags = {}
bagListPrev = []
bagListNext = []
finalColorCount = 0
colorsToView = set(["shinygold"])
viewed = set([])

for rule in bagRules:
    fragments = rule.split('contain')
    for frag in fragments:
        elCount = 0
        possibleColors = frag.split(' ')
        for word in possibleColors:
            if "bag" in word:
                bagColor = possibleColors[elCount - 2] + possibleColors[elCount - 1]
                if "other" not in bagColor:
                    bagListNext.append(bagColor)
            elCount += 1
        if len(bagListPrev) != 0:
            for i in bagListPrev:
                if i in bags:
                    bags[i].update(bagListNext)
                else :
                    bags[i] = set(bagListNext)
        bagListPrev = bagListNext
        bagListNext = []
    bagListPrev = []

def colors(colorSet, seenColors, bagDict):
    containsBag = 0
    saveSet = set([])
    seenColors.update(colorSet)
    if len(colorSet) != 0:
        for c in colorSet:
            for bag in bagDict:
                for item in bagDict[bag]:
                    if item == c and bag not in seenColors:
                        saveSet.add(bag)
        containsBag += len(saveSet)
        return containsBag + colors(saveSet, seenColors, bagDict)
    else:
        return containsBag

finalColorCount = colors(colorsToView, viewed, bags)
print(finalColorCount)
