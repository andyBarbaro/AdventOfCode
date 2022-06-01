import sys

def main():
    input = []
    prevSum = sys.maxsize
    count = 0

    with open('day1Input', 'r') as f:
        input = f.readlines()

    i = 0

    while (i+2 < len(input)):
        windowSum = int(input[i]) + int(input[i+1]) + int(input[i+2])
        if (windowSum > prevSum):
            count += 1
        prevSum = windowSum
        i += 1

    print(count)

if __name__ == "__main__":
    main()
