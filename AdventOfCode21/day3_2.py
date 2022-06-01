import sys

def main():
    input = []
    o2 = []
    co2 = []

    with open('day3Input', 'r') as f:
        input = f.readlines()

    input2 = input.copy()
    temp = []

    i = 0
    while (len(input) > 1):
        oneCount = 0
        for report in input:
            if int(report[i]) == 1:
                oneCount += 1

        if (oneCount >= (len(input)/2)):
            for report in input:
                if int(report[i]) == 1:
                    temp.append(report)
        else:
            for report in input:
                if int(report[i]) == 0:
                    temp.append(report)

        i += 1
        input = temp.copy()
        temp = []


    i = 0
    while (len(input2) > 1):
        oneCount = 0
        for report in input2:
            if int(report[i]) == 1:
                oneCount += 1

        if (oneCount >= (len(input2)/2)):
            for report in input2:
                if int(report[i]) == 0:
                    temp.append(report)
        else:
            for report in input2:
                if int(report[i]) == 1:
                    temp.append(report)

        i += 1
        input2 = temp.copy()
        temp = []


    print(int(input[0],2)*int(input2[0],2))




if __name__ == "__main__":
    main()
