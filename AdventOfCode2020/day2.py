txtFile = open("day2.txt", "r")

passwords = txtFile.readlines()
goodPass = 0

for lines in passwords:
    count = 0
    limit1 = lines.split('-')
    lowerLimit = int(limit1[0])
    limit2 = limit1[1].split(' ')
    upperLimit = int(limit2[0])
    charQ = limit2[1][0]
    for x in limit2[2]:
        if charQ == x:
            count += 1
    if count <= upperLimit and count >= lowerLimit:
        goodPass += 1
print(goodPass)
