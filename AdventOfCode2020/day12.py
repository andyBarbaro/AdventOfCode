txtFile = open("day12.txt", "r")

directions = txtFile.readlines()

turnR = ['E', 'S', 'W', 'N']
turnL = ['E', 'N', 'W', 'S']
currentDirection = 'E'
#[0] is east west and [1] is north south
currentLocation = [0, 0]

def cardinals(direct, distance):
    if direct == 'N':
        currentLocation[1] += distance
    elif direct == 'S':
        currentLocation[1] -= distance
    elif direct == 'E':
        currentLocation[0] += distance
    elif direct == 'W':
        currentLocation[0] -= distance

for step in directions:
    move = step[0]
    amount = int(step[1:])

    if move == 'F':
        cardinals(currentDirection, amount)
    elif move == 'L':
        deg = int(amount / 90)
        listLoc = turnL.index(currentDirection)
        currentDirection = turnL[(listLoc+deg)%4]
    elif move == 'R':
        deg = int(amount / 90)
        listLoc = turnR.index(currentDirection)
        currentDirection = turnR[(listLoc+deg)%4]
    else:
        cardinals(move, amount)

print(abs(currentLocation[0])+abs(currentLocation[1]))
