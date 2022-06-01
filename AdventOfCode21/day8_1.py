import sys
import re

def main():
    input = []
    modInput = []
    outputCount = {}

    with open('day8Input', 'r') as f:
        input = f.readlines()

    for line in input:
        modInput.append(re.split(' [|] | ', line))

    for i in range(10):
        outputCount[i] = 0

    for transmission in modInput:
        for output in transmission[10:]:
            modOutput = re.sub('\n', '', output)
            if len(modOutput) == 2:
                outputCount[1] += 1
            elif len(modOutput) == 4:
                outputCount[4] += 1
            elif len(modOutput) == 3:
                outputCount[7] += 1
            elif len(modOutput) == 7:
                outputCount[8] += 1

    print(sum(outputCount.values()))

if __name__ == "__main__":
    main()
