txtFile = open("day18.txt", "r")

expressions = txtFile.readlines()
finalSum = 0
openParen = []
closedParen = []
parens = []

def solve(eqStr):
    numbers = []
    ops = []
    i = 0
    partial = 0
    while i < len(eqStr):
        if i % 2 == 0:
            numbers.append(int(eqStr[i]))
        else:
            ops.append(eqStr[i])
        i += 1
    j = 0
    while j < len(numbers):
        if ops[j] == '+':
            partial = 

for terms in expressions:
    terms = terms.replace(" ", "")
    i = 0
    print(terms)
    while i < len(terms):
        if terms[i] == '(':
            openParen.append(i)
        elif terms[i] == ')':
            closedParen.append(i)
        i += 1
    oppo = openParen[::-1]

    j = 0
    while j < len(openParen):
        parenO = oppo[j]
        lowest = 10000
        for pos in closedParen:
            if pos > parenO and abs(pos - parenO) < abs(lowest - parenO):
                lowest = pos
        closedParen.remove(lowest)
        j += 1
        parens.append([parenO, lowest])

    for pair in parens:
        eqList = list(terms)
        print(eqList[pair[0]+1:pair[1]])
        value = solve(eqList[pair[0]+1:pair[1]])
        del eqList[pair[0]:pair[1]+1]
        eqList.insert(pair[0], value)

    openParen = []
    closedParen = []
    parens = []
