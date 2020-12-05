import os
import re


def getInput(file: str) -> dict:
    dt = []
    passports = {}
    passports[0] = {}
    j = 0
    with open(file, "r") as file:
        for line in file:
            dt.extend(line.split(" "))
        for i in range(len(dt)):
            temp = dt[i].split(":")
            if temp != ["\n"]:
                passports[j][temp[0]] = temp[1].replace("\n", "")
            else:
                j += 1
                passports[j] = {}
    return passports


def simpleValidation(passport: dict, fields: tuple) -> bool:
    return all(f in passport for f in fields)


def strictValidation(passport: dict, conditions: dict) -> bool:
    for field in conditions:
        if re.fullmatch(conditions[field], passport[field]) is None:
            return False
    return True


path = "D:\\Adventofcode\\2020\\4"
os.chdir(path)

# day 4 part1 - solution
result = 0
fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
pass_input = getInput("input.txt")
for i in range(len(pass_input)):
    if (simpleValidation(pass_input[i], fields)):
        result += 1
print("The answer for the first puzzle is: ", result)

# day 4 part2 - solution
result = 0
rules = {
        "byr": "19[2-9][0-9]|200[0-2]",
        "iyr": "20(1[0-9]|20)",
        "eyr": "20(2[0-9]|30)",
        "hgt": "(1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in)",
        "hcl": "#([0-9]|[a-f]){6}",
        "ecl": "amb|blu|brn|gry|grn|hzl|oth",
        "pid": "[0-9]{9}",
        }
for i in range(len(pass_input)):
    if (simpleValidation(pass_input[i], fields)):
        if (strictValidation(pass_input[i], rules)):
            result += 1
print("The answer for the second puzzle is: ", result)
