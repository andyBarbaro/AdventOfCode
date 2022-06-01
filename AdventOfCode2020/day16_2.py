txtFile = open("day16.txt", "r")

ticketData = txtFile.readlines()
validInputs = set([])
validTickets = []
myTicket = []
fieldDict = {}
index = 0
tser = 0

while ticketData[index] != '\n':
    fieldLine = ticketData[index].split(' ')
    fieldDict[ticketData[index].split(':')[0]] = []
    rest1 = fieldLine[len(fieldLine)-3]
    rest2 = fieldLine[len(fieldLine)-1]
    i = int(rest1[:rest1.index('-')])
    end = int(rest1[rest1.index('-')+1:])
    while i <= end:
        validInputs.add(i)
        fieldDict[ticketData[index].split(':')[0]].append(i)
        i += 1
    i = int(rest2[:rest2.index('-')])
    end = int(rest2[rest2.index('-')+1:])
    while i <= end:
        validInputs.add(i)
        fieldDict[ticketData[index].split(':')[0]].append(i)
        i += 1
    index += 1
index += 2
while ticketData[index] != '\n':
    myTicket = ticketData[index].split(',')
    index += 1
index += 2
for line in ticketData[index:]:
    values = line.split(',')
    valSize = len(values)
    invalidCount = 0
    tempCount = 0
    for x in values:
        if int(x) not in validInputs:
            invalidCount = 1
            break
    if not invalidCount:
        validTickets.append(values)

i = 0
finalMult = 1
depFields = {}
while i < len(myTicket):
    depFields[i] = []
    for field in fieldDict:
        inField = 0
        for tick in validTickets:
            if int(tick[i]) in fieldDict[field]:
                inField += 1
        if inField == len(validTickets):
            if field not in depFields:
                depFields[i].append(field)
    i += 1

finalFields = {}
done = 0
while not done:
    done = 1
    i = 0
    for field in depFields:
        if len(depFields[field]) == 1:
            finalFields[depFields[field][0]] = field
            for f in depFields:
                if depFields[field][0] in depFields[f] and len(depFields[f]) != 1:
                    depFields[f].remove(depFields[field][0])
        else:
            done = 0
        i += 1

for f2 in finalFields:
    if "departure" in f2:
        finalMult *= int(myTicket[finalFields[f2]])
print(finalMult)
