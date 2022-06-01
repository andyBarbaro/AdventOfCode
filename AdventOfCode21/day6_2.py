import sys
import re

def main():
    input = []
    numberOfDays = 256
    totalFish = 0
    fishMap = {}
    final = 0

    with open('day6Input', 'r') as f:
        input = f.readlines()

    initialFish = input[0].split(',')
    initialFish = list(map(int, initialFish))
    fishSet = set(map(int, initialFish))

    for f in fishSet:
        fishMap[f] = 0

    for fish in fishMap:
        totalFish += reproduce(fish, numberOfDays) + 1
        fishMap[fish] = totalFish
        totalFish = 0
        print(fishMap)

    for i in initialFish:
        final += fishMap[i]

    print(final)

def reproduce(f, days):
    fishCount = 0

    if days - (f+1) >= 0:
        fishCount += 1
        fishCount += reproduce(6, days - (f+1)) + reproduce(8, days - (f+1))

    return fishCount




if __name__ == "__main__":
    main()
