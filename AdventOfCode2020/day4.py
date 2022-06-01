txtFile = open("day4.txt", "r")

passports = txtFile.readlines()
validPassports = 0
requiredFields = {"byr" : 0, "iyr" : 0, "eyr" : 0, "hgt" : 0, "hcl" : 0, "ecl" : 0, "pid" : 0, "cid" : 0}
individualPassport = []

for data in passports:
    if data != '\n':
        fields = data.split(' ')
        for i in fields:
            individualPassport.append(i)
    else :
        for item in individualPassport:
            for cat in requiredFields:
                if cat in item:
                    requiredFields[cat] = 1
        sumCat = 0
        for catAgain in requiredFields:
            sumCat += requiredFields[catAgain]

        if (sumCat == 8 or (sumCat == 7 and requiredFields["cid"] == 0)) :
            validPassports += 1
        individualPassport = []
        requiredFields = {"byr" : 0, "iyr" : 0, "eyr" : 0, "hgt" : 0, "hcl" : 0, "ecl" : 0, "pid" : 0, "cid" : 0}
print(validPassports)
