txtFile = open("day16.txt", "r")

ticketData = txtFile.readlines()
validInputs = set([])
index = 0
tser = 0

while ticketData[index] != '\n':
    fieldLine = ticketData[index].split(' ')
    rest1 = fieldLine[len(fieldLine)-3]
    rest2 = fieldLine[len(fieldLine)-1]
    i = int(rest1[:rest1.index('-')])
    end = int(rest1[rest1.index('-')+1:])
    print(i, end)
    while i <= end:
        validInputs.add(i)
        i += 1
    i = int(rest2[:rest2.index('-')])
    end = int(rest2[rest2.index('-')+1:])
    print(i, end)
    while i <= end:
        validInputs.add(i)
        i += 1
    index += 1
index += 1
while ticketData[index] != '\n':
    index += 1
index += 2
print(validInputs)
for line in ticketData[index:]:
    values = line.split(',')
    valSize = len(values)
    invalidCount = 0
    tempCount = 0
    for x in values:
        if int(x) not in validInputs:
            tempCount += int(x)
            invalidCount += 1
    tser += tempCount

print(tser)
