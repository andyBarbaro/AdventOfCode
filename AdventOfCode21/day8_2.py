import sys
import re

def main():
    input = []
    modInput = []
    total = 0

    with open('day8Input', 'r') as f:
        input = f.readlines()

    for line in input:
        modInput.append(re.split(' [|] | ', line))

    for transmission in modInput:
        tests = sorted(transmission[:10], key=len)
        spot = 3
        final = 0
        for output in transmission[10:]:
            digit = 0
            modOutput = re.sub('\n', '', output)
            if len(modOutput) == 2:
                digit = 1
            elif len(modOutput) == 4:
                digit = 4
            elif len(modOutput) == 3:
                digit = 7
            elif len(modOutput) == 7:
                digit = 8
            elif len(modOutput) == 6:
                digit = zeroSixNine(tests, modOutput)
            elif len(modOutput) == 5:
                digit = twoThreeFive(tests, modOutput)

            final += (10**spot)*digit
            spot -= 1

        total += final

    print(total)

def zeroSixNine(signals, d):
    one = set(signals[0])
    seven = set(signals[1])
    four = set(signals[2])
    compD = set(d)

    if (one & compD == one):
        if (four & compD == four):
            return 9
        else:
            return 0
    else:
        return 6

def twoThreeFive(signals, d):
    one = set(signals[0])
    four = set(signals[2])
    compD = set(d)

    if (one & compD == one):
        return 3
    elif len(four & compD) == 3:
        return 5
    else:
        return 2



if __name__ == "__main__":
    main()
