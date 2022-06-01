import sys
import numpy as np

def main():
    input = []
    calls = []
    worstBingo = 0
    boardNum = 0
    bestBoard = np.empty([5,5])

    with open('day4Input', 'r') as f:
        input = f.readlines()

    calls = input[0].split(',')

    input = input[2:]
    for line in input:
        if line == "\n":
            input.remove(line)


    while ((boardNum+1)*5 <= len(input)):
        board = []
        for line in input[boardNum*5:(boardNum+1)*5]:
            board.append(line.split())

        board = np.array(board)
        board = board.astype('int')

        for num in calls:
            if int(num) in board:
                board[np.where(board == int(num))] = -1
                if bingo(board):
                    if (calls.index(num) > worstBingo):
                        worstBingo = calls.index(num)
                        bestBoard = board
                    break

        boardNum += 1



    winnerSum = 0
    for x in np.nditer(bestBoard):
        if x != -1:
            winnerSum += x

    print(winnerSum*int(calls[worstBingo]))




def bingo(board):

    if -5 in board.sum(axis=0):
        return True
    elif -5 in board.sum(axis=1):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
