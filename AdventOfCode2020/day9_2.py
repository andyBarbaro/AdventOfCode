from itertools import combinations
txtFile = open("day9.txt", "r")

ciphertext = txtFile.readlines()

i = 0
preLen = 25
preamble = ciphertext[:preLen]
linesToRead = ciphertext[preLen:]
currentLong = []

for code in linesToRead:
    underQuestion = int(code)
    valid = 0
    for p1 in preamble:
        for p2 in preamble[1:]:
            if int(p1) + int(p2) == underQuestion:
                valid = 1
    if valid == 0:
        combos = []
        k = 0
        while k < preLen + i:
            j = 1
            while j < preLen + i - k:
                combos.append(ciphertext[j:j+k])
                j += 1
            k += 1
        #print(combos)
        for list in combos:
            sum = 0
            #print(list)
            for c in list:
                sum += int(c)
                if sum > underQuestion:
                    break
            if sum == underQuestion:
                #print(list)
                leastEl = int(list[0])
                mostEl = int(list[0])
                for element in list:
                    if int(element) < leastEl:
                        leastEl = int(element)
                    elif int(element) > mostEl:
                        mostEl = int(element)
                print(list)
                print(leastEl + mostEl)
                exit();
        break
    else:
        i += 1
        preamble = ciphertext[i:preLen+i]
