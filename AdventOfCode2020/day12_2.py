import math
txtFile = open("day12.txt", "r")

directions = txtFile.readlines()

#[0] is east west and [1] is north south
currentLocation = [0, 0]
waypoint = [10, 1]

def cardinals(direct, distance):
    if direct == 'N':
        waypoint[1] += distance
    elif direct == 'S':
        waypoint[1] -= distance
    elif direct == 'E':
        waypoint[0] += distance
    elif direct == 'W':
        waypoint[0] -= distance

def rotate(dir, deg):
    holder = 0
    if (deg == 90 and dir == 'R') or (deg == 270 and dir == 'L'):
        holder = waypoint[0]
        waypoint[0] = waypoint[1]
        waypoint[1] = -holder
    elif deg == 180:
        waypoint[0] = -waypoint[0]
        waypoint[1] = -waypoint[1]
    elif (deg == 270 and dir == 'R') or (deg == 90 and dir == 'L'):
        holder = waypoint[0]
        waypoint[0] = -waypoint[1]
        waypoint[1] = holder

for step in directions:
    move = step[0]
    amount = int(step[1:])

    if move == 'F':
        currentLocation[0] += amount*waypoint[0]
        currentLocation[1] += amount*waypoint[1]
    elif move == 'L':
        rotate(move, amount)
    elif move == 'R':
        rotate(move, amount)
    else:
        cardinals(move, amount)

print(abs(currentLocation[0])+abs(currentLocation[1]))
