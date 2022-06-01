import sys
import numpy as np

def main():
    input = []

    with open('day17Input', 'r') as f:
        input = f.readline()

    input = input[:-1]
    input = input.split('=')
    xRange = input[1][:-3].split('..')
    yRange = input[-1].split('..')

    targetBottom = abs(int(yRange[0]))

    highY = sum(list(range(1,targetBottom)))


    print(highY)

if __name__ == "__main__":
    main()
