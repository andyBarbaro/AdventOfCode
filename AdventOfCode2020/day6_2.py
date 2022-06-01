txtFile = open("day6.txt", "r")

responses = txtFile.readlines()
yesCount = 0
yesQuestions = []
yesQuestions2 = []
lineCount = 0

for line in responses:
    if line != '\n':
        if lineCount == 0:
            for c in line:
                if c not in yesQuestions and c != '\n':
                    yesQuestions.append(c)
        else :
            for c in line:
                if c not in yesQuestions2 and c != '\n':
                    yesQuestions2.append(c)

        if len(yesQuestions2) != 0:
            yesQuestions = list(set(yesQuestions) & set(yesQuestions2))
        yesQuestions2 = []
        lineCount = 1
    else :
        lineCount = 0
        yesCount += len(yesQuestions)
        yesQuestions = []

print(yesCount)
