txtFile = open("day3.txt", "r")

slopes = txtFile.readlines()
runs = [1, 3, 5, 7, 1]

lineLen = len(slopes[0])
multTotal = 1
runElement = 0

for i in runs:
    currentPos = 0
    treesHit = 0
    evenRow = 0
    for row in slopes:
        if (runElement != 4 or evenRow%2 == 0):
            if (row[currentPos] == '#'):
                treesHit += 1
            currentPos = (currentPos+i)%(lineLen-1)
        evenRow += 1
    print(treesHit)
    multTotal *= treesHit
    runElement += 1
print(multTotal)
