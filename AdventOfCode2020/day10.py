import numpy as np
txtFile = open("day10.txt", "r")

adapters = txtFile.readlines()
adaptersInt = []
joltDif1 = 0
joltDif3 = 1

for a in adapters:
    adaptersInt.append(int(a))

adaptersInt.append(0)
adapters = np.sort(adaptersInt)

for i in range(len(adapters)-1):
    if adapters[i+1] - adapters[i] == 1:
        joltDif1 += 1
    elif adapters[i+1] - adapters[i] == 3:
        joltDif3 += 1

print(joltDif1*joltDif3)
