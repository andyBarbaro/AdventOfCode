import sys

def main():
    input = []
    horizontal = 0
    depth = 0

    with open('day2Input', 'r') as f:
        input = f.readlines()

    for line in input:
        dirAmount = line.split()
        if (dirAmount[0] == "forward"):
            horizontal += int(dirAmount[1])
        else:
            if (dirAmount[0] == "up"):
                depth -= int(dirAmount[1])
            else:
                depth += int(dirAmount[1])

    print(depth*horizontal)
if __name__ == "__main__":
    main()
