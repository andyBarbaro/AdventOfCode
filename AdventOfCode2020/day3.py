txtFile = open("day3.txt", "r")

slopes = txtFile.readlines()

lineLen = len(slopes[0])
currentPos = 0;
treesHit = 0

for row in slopes:
    if (row[currentPos] == '#'):
        treesHit += 1
    currentPos = (currentPos+3)%(lineLen-1)
print(treesHit)
