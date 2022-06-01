import sys
import numpy as np

def main():
    input = []
    modInput = []
    opens = ['{', '[', '(', '<']
    errors = {'}': 0, ']': 0, ')': 0, '>': 0}

    with open('day10Input', 'r') as f:
        input = f.readlines()

    for line in input:
        modInput.append(list(line[:-1]))

    for line in modInput:
        currentChunk = []
        for val in line:
            if val in opens:
                currentChunk.append(val)
            else:
                test = checkChunk(currentChunk, val)
                if test != None:
                    errors[test] += 1
                    break

    print((errors[')']*3) + (errors[']']*57) + (errors['}']*1197) + (errors['>']*25137))


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
