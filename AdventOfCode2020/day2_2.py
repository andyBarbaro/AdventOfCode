txtFile = open("day2.txt", "r")

passwords = txtFile.readlines()
goodPass = 0

for lines in passwords:
    charCount = 1
    exactOne = 0
    limit1 = lines.split('-')
    index1 = int(limit1[0])
    limit2 = limit1[1].split(' ')
    index2 = int(limit2[0])
    charQ = limit2[1][0]
    for x in limit2[2]:
        if charQ == x and (charCount == index1 or charCount == index2) and not exactOne:
            exactOne = 1
        elif charQ == x and (charCount == index1 or charCount == index2) and exactOne:
            exactOne = 0
        charCount += 1
    if exactOne:
        goodPass += 1
print(goodPass)
