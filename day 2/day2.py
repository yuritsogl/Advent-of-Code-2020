import os


# day 2 part1 - solution
def checkPassword_old(min_let: int, max_let: int, let: str,
                      password: str) -> int:
    sum = 0
    for i in password:
        if (i == let):
            sum += 1
    if (sum < min_let or sum > max_let):
        return 0
    else:
        return 1


# day 2 part2 - solution
def checkPassword_new(first_pos: int, second_pos: int, let: str,
                      password: str) -> int:
    if ((password[first_pos-1] == let and password[second_pos-1] == let) or
            password[first_pos-1] != let and password[second_pos-1] != let):
        return 0
    else:
        return 1


path = "D:\\Adventofcode\\2020\\2"
os.chdir(path)

i = 0
dt = []
result_1 = 0
result_2 = 0
with open("input.txt", "r") as file:
    for line in file:
        dt.extend(line.split(": "))

for i in range(0, len(dt)-1, 2):
    min_letter = int((dt[i].split("-")[0]))
    max_letter = int((dt[i].split("-")[1].split(" ")[0]))
    letter = (dt[i][len(dt[i])-1])
    password = dt[i+1]
    result_1 += checkPassword_old(min_letter, max_letter, letter, password)
    result_2 += checkPassword_new(min_letter, max_letter, letter, password)

print("The answer for the first puzzle is:", result_1)
print("The answer for the second puzzle is:", result_2)
