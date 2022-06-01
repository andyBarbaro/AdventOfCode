txtFile = open("day8.txt", "r")

codeLines = txtFile.readlines()

done = 0
edited = []

i = 0
for l in codeLines:
    x = l.split(' ')[0]
    if x != "acc":
        edited.append(i)
    i += 1

for lineNum in edited:
    currentPos = 0
    accumulator = 0
    visited = []
    while True:
        visited.append(currentPos)
        op = codeLines[currentPos].split(' ')[0]
        arg = codeLines[currentPos].split(' ')[1]
        if currentPos == lineNum:
            if op == "acc":
                accumulator += int(arg)
                currentPos += 1
            elif op == "jmp":
                currentPos += 1
            else:
                currentPos += int(arg)
            if (currentPos in visited):
                break
        else:
            if op == "acc":
                accumulator += int(arg)
                currentPos += 1
            elif op == "jmp":
                currentPos += int(arg)
            else:
                currentPos += 1
            if (currentPos in visited):
                break
            if  (currentPos == len(codeLines)):
                done = 1
                break
    if (done == 1):
        break

print(accumulator)
