import sys
import re

def main():
    input = []
    temp = []
    day = 0
    numberOfDays = 80

    with open('day6Input', 'r') as f:
        input = f.readlines()

    initialFish = input[0].split(',')
    initialFish = list(map(int, initialFish))
    fishCopy = initialFish.copy()

    while day < numberOfDays:
        for fishNum in range(len(initialFish)):
            if initialFish[fishNum] == 0:
                fishCopy[fishNum] = 6
                fishCopy.append(8)
            else:
                fishCopy[fishNum] -= 1

        initialFish = fishCopy
        day += 1


    print(len(initialFish))

if __name__ == "__main__":
    main()
