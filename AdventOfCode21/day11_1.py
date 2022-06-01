import sys
import numpy as np

def main():
    input = []
    modInput = []


    with open('day11Input', 'r') as f:
        input = f.readlines()

    for line in input:
        modInput.append(list(line[:-1]))

    octopi = np.array(modInput)
    octopi = octopi.astype('int')

    flashCount = 0
    for i in range(100):
        octopi += 1
        visited = []
        for y in range(len(octopi[:,0])):
            for x in range(len(octopi[0,:])):
                if octopi[y, x] > 9:
                    flashCount += exploreSurroudings(octopi, y, x, visited) + 1

    print(flashCount)

def exploreSurroudings(o, y, x, v):
    o[y, x] = 0
    v.append((y, x))
    flash = 0

    if y != 0 and ((y-1, x) not in v): #up
        if (o[y-1, x]+1 > 9):
            flash += exploreSurroudings(o, y-1, x, v) + 1
        else:
            o[y-1, x] += 1

    if x != 0 and ((y, x-1) not in v): #left
        if (o[y, x-1]+1 > 9):
            flash += exploreSurroudings(o, y, x-1, v) + 1
        else:
            o[y, x-1] += 1

    if y != len(o[:,0])-1 and ((y+1, x) not in v): #down
        if (o[y+1, x]+1 > 9):
            flash += exploreSurroudings(o, y+1, x, v) + 1
        else:
            o[y+1, x] += 1

    if x != len(o[0,:])-1 and ((y, x+1) not in v): #right
        if (o[y, x+1]+1 > 9):
            flash += exploreSurroudings(o, y, x+1, v) + 1
        else:
            o[y, x+1] += 1

    if y != 0 and x != 0 and ((y-1, x-1) not in v): #up-left
        if (o[y-1, x-1]+1 > 9):
            flash += exploreSurroudings(o, y-1, x-1, v) + 1
        else:
            o[y-1, x-1] += 1

    if x != 0 and y != len(o[:,0])-1 and ((y+1, x-1) not in v): #down-left
        if (o[y+1, x-1]+1 > 9):
            flash += exploreSurroudings(o, y+1, x-1, v) + 1
        else:
            o[y+1, x-1] += 1

    if x != len(o[0,:])-1 and y != 0 and ((y-1, x+1) not in v): #up-right
        if (o[y-1, x+1]+1 > 9):
            flash += exploreSurroudings(o, y-1, x+1, v) + 1
        else:
            o[y-1, x+1] += 1

    if x != len(o[0,:])-1 and y != len(o[:,0])-1 and ((y+1, x+1) not in v): #down-right
        if (o[y+1, x+1]+1 > 9):
            flash += exploreSurroudings(o, y+1, x+1, v) + 1
        else:
            o[y+1, x+1] += 1


    return flash



if __name__ == "__main__":
    main()
