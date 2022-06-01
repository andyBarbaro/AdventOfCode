txtFile = open("day6.txt", "r")

responses = txtFile.readlines()
yesCount = 0
yesQuestions = []


for line in responses:
    if line != '\n':
        for c in line:
            if c not in yesQuestions and c != '\n':
                yesQuestions.append(c)
    else :
        yesCount += len(yesQuestions)
        yesQuestions = []

print(yesCount)
