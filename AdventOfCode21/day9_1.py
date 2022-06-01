import sys
import numpy as np

def main():
    input = []
    modInput = []
    lowPts = []

    with open('day9Input', 'r') as f:
        input = f.readlines()

    for line in input:
        modInput.append(list(line[:-1]))

    depthChart = np.array(modInput)
    depthChart = depthChart.astype('int')

    for y in range(len(depthChart[:,0])):
        for x in range(len(depthChart[0,:])):
            up = True
            down = True
            left = True
            right = True

            if y != 0 and (depthChart[y-1, x] <= depthChart[y, x]):
                up = False

            if x != 0 and (depthChart[y, x-1] <= depthChart[y, x]):
                left = False

            if y != len(depthChart[:,0])-1 and (depthChart[y+1, x] <= depthChart[y, x]):
                down = False

            if x != len(depthChart[0,:])-1 and (depthChart[y, x+1] <= depthChart[y, x]):
                right = False

            if (up and down and left and right):
                lowPts.append(depthChart[y, x])




    print(sum(lowPts) + len(lowPts))

if __name__ == "__main__":
    main()
