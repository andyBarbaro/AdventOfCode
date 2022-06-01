import sys
import re

def main():
    input = []
    crabPos = []
    minFuel = sys.maxsize

    with open('day7Input', 'r') as f:
        input = f.readlines()

    crabPos = input[0].split(',')
    crabPos = list(map(int, crabPos))

    leftCrab = min(crabPos)
    rightCrab = max(crabPos)
    possiblePos = list(range(leftCrab, rightCrab+1))

    for val in possiblePos:
        fuelUsed = 0
        for crab in crabPos:
            fuelUsed += abs(crab - val)
        if fuelUsed < minFuel:
            minFuel = fuelUsed

    print(minFuel)



if __name__ == "__main__":
    main()
