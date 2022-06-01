txtFile = open("day4.txt", "r")

passports = txtFile.readlines()
validPassports = 0
hclRest = "abcdef0123456789"
eclRest = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
pidRest = "0123456789"
individualPassport = []

for data in passports:
    if data != '\n':
        fields = data.split(' ')
        for i in fields:
            individualPassport.append(i.replace("\n", ""))
    else :
        requiredFields = {"byr" : 0, "iyr" : 0, "eyr" : 0, "hgt" : 0, "hcl" : 0, "ecl" : 0, "pid" : 0, "cid" : 0}
        for item in individualPassport:
            catValue = item.split(':')[0]
            itemValue = item.split(':')[1]
            if (catValue == "byr"):
                if (int(itemValue) >= 1920 and int(itemValue) <= 2002): requiredFields[catValue] = 1
            elif (catValue == "iyr"):
                if (int(itemValue) >= 2010 and int(itemValue) <= 2020): requiredFields[catValue] = 1
            elif (catValue == "eyr"):
                if (int(itemValue) >= 2020 and int(itemValue) <= 2030): requiredFields[catValue] = 1
            elif (catValue == "hgt"):
                if ("cm" in itemValue):
                    if (int(itemValue[0:len(itemValue)-2]) >= 150 and int(itemValue[0:len(itemValue)-2]) <= 193): requiredFields[catValue] = 1
                elif ("in" in itemValue):
                    if (int(itemValue[0:len(itemValue)-2]) >= 59 and int(itemValue[0:len(itemValue)-2]) <= 76): requiredFields[catValue] = 1
            elif (catValue == "hcl"):
                improper = 0
                if (itemValue[0] == '#' and len(itemValue) == 7):
                    for c in itemValue[1:]:
                        if c not in hclRest:
                            improper = 1
                    if improper == 0:
                        requiredFields[catValue] = 1
            elif (catValue == "ecl"):
                if itemValue in eclRest:
                    requiredFields[catValue] = 1
            elif (catValue == "pid"):
                improper = 0
                if (len(itemValue) == 9):
                    for num in itemValue:
                        if num not in pidRest:
                            improper += 1
                    if improper == 0:
                        requiredFields[catValue] = 1
            else:
                requiredFields[catValue] = 1
        sumCat = 0
        for catAgain in requiredFields:
            sumCat += requiredFields[catAgain]
        if (sumCat == 8 or (sumCat == 7 and requiredFields["cid"] == 0)) :
            validPassports += 1
        individualPassport = []
print(validPassports)
