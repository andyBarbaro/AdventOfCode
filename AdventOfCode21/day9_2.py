import sys
import numpy as np

def main():
    input = []
    modInput = []
    lowPts = []
    basins = []

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
                lowPts.append((y, x))

    for pt in lowPts:
        visited = []
        basins.append(explore(depthChart, pt, visited)+1)

    basins.sort()
    print(basins[-3]*basins[-2]*basins[-1])


def explore(depthChart, pt, v):
    y = pt[0]
    x = pt[1]
    basinArea = 0
    v.append((y, x))

    if y != 0 and ((y-1, x) not in v) and (depthChart[y-1, x] != 9):
        basinArea += 1 + explore(depthChart, (y-1, x), v)

    if x != 0 and ((y, x-1) not in v) and (depthChart[y, x-1] != 9):
        basinArea += 1 + explore(depthChart, (y, x-1), v)

    if y != len(depthChart[:,0])-1 and ((y+1, x) not in v) and (depthChart[y+1, x] != 9):
        basinArea += 1 + explore(depthChart, (y+1, x), v)

    if x != len(depthChart[0,:])-1 and ((y, x+1) not in v) and (depthChart[y, x+1] != 9):
        basinArea += 1 + explore(depthChart, (y, x+1), v)

    return basinArea


if __name__ == "__main__":
    main()
