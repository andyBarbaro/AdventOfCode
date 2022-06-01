txtFile = open("day1.txt", "r")

numbers = txtFile.readlines()

for i in numbers:
    for j in numbers:
        for k in numbers:
            if (int(i)+int(j)+int(k) == 2020):
                print(int(i)*int(j)*int(k))
