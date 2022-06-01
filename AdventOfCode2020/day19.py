txtFile = open("day19.txt", "r")

rulesAndMsgs = txtFile.readlines()
rules = {}
msgs = []
beginMsg = 0

for line in rulesAndMsgs:
    if line == "\n":
        beginMsg = 1
    if not beginMsg:
        rules[line[:line.index(':')]] = line.split(' ')[1:]
    else:
        msgs.append(line)
msgs.remove("\n")

for r in rules:
    for value in rules[r]
