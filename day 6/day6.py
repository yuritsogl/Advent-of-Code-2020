def getInput(file: str) -> list:
    data = []
    data.append([])
    i = 0
    with open(file, "r") as file:
        for line in file:
            if line == "\n":
                i += 1
                data.append([])
            else:
                data[i].append(line.strip())
    return data


def sumYesUnique(answer: list) -> int:
    return len(set("".join(answer)))


def sumYesAll(answer: list) -> int:
    if (len(answer) == 1):
        return len(answer[0])
    else:
        yes = set(answer[0])
        for i in range(1, len(answer)):
            checkyes = list(filter(lambda a: a in yes, answer[i]))
            yes = checkyes
    return (len(checkyes))


answers = getInput("input.txt")

# day 6 part1 - solution
result = 0
for i in range(len(answers)):
    result += sumYesUnique(answers[i])
print("The answer for the first puzzle is: ", result)

# day 6 part2 - solution
result = 0
for i in range(len(answers)):
    result += sumYesAll(answers[i])
print("The answer for the second puzzle is: ", result)
