txtFile = open("day8.txt", "r")

codeLines = txtFile.readlines()

currentPos = 0
accumulator = 0
visited = []

while True:
    visited.append(currentPos)
    op = codeLines[currentPos].split(' ')[0]
    arg = codeLines[currentPos].split(' ')[1]
    if op == "acc":
        accumulator += int(arg)
        currentPos += 1
    elif op == "jmp":
        currentPos += int(arg)
    else:
        currentPos += 1
    if (currentPos in visited):
        break

print(accumulator)
