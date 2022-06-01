txtFile = open("day9.txt", "r")

ciphertext = txtFile.readlines()

i = 0
preLen = 25
preamble = ciphertext[:preLen]
linesToRead = ciphertext[preLen:]

for code in linesToRead:
    underQuestion = int(code)
    valid = 0
    for p1 in preamble:
        for p2 in preamble[1:]:
            if int(p1) + int(p2) == underQuestion:
                valid = 1
    if valid == 0:
        print(underQuestion)
        break
    else:
        i += 1
        preamble = ciphertext[i:preLen+i]
