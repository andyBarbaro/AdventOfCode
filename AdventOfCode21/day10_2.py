import sys
import statistics

def main():
    input = []
    modInput = []
    opens = ['{', '[', '(', '<']
    incompletes = []

    with open('day10Input', 'r') as f:
        input = f.readlines()

    for line in input:
        modInput.append(list(line[:-1]))

    for line in modInput:
        currentChunk = []
        corrupt = False
        for val in line:
            if val in opens:
                currentChunk.append(val)
            else:
                test = checkChunk(currentChunk, val)
                if test != None:
                    corrupt = True
                    break
        if not corrupt:
            incompletes.append(currentChunk)

    incompleteVals = []
    for str in incompletes:
        score = 0
        for brace in str[::-1]:
            score *= 5
            if brace == '{':
                score += 3
            elif brace == '(':
                score += 1
            elif brace == '[':
                score += 2
            elif brace == '<':
                score += 4

        incompleteVals.append(score)

    print(statistics.median(incompleteVals))


def checkChunk(chunk, symbol):
    if symbol == '}':
        if chunk[-1] == '{':
            chunk.pop()
        else:
            return symbol
    elif symbol == ')':
        if chunk[-1] == '(':
            chunk.pop()
        else:
            return symbol
    elif symbol == ']':
        if chunk[-1] == '[':
            chunk.pop()
        else:
            return symbol
    elif symbol == '>':
        if chunk[-1] == '<':
            chunk.pop()
        else:
            return symbol


if __name__ == "__main__":
    main()


#grammer
# <term> = \epsilon | <<term>> | (<term>) | [<term>] | {<term>}
