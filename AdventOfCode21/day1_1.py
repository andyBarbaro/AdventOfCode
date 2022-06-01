import sys

def main():
    input = []
    prevNum = sys.maxsize
    count = 0

    with open('day1Input', 'r') as f:
        input = f.readlines()

    for num in input:
        if int(num) > prevNum:
            count += 1
        prevNum = int(num)

    print(count)

if __name__ == "__main__":
    main()
