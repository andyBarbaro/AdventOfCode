import sys

def main():
    input = []
    diagonstics = []
    gamma = ""
    epsilon = ""

    with open('day3Input', 'r') as f:
        input = f.readlines()

    for i in range(len(input[0])-1):
        diagonstics.append(0)

    for report in input:
        count = 0
        for val in report[:-1]:
            if int(val) == 1:
                diagonstics[count] += 1
            count += 1

    for i in range(len(input[0])-1):
        if diagonstics[i] > (len(input)/2):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(int(gamma,2)*int(epsilon,2))


if __name__ == "__main__":
    main()
