def getInput(file: str) -> list:
    dt = []
    with open(file, "r") as file:
        for line in file:
            dt.extend(line.split())
    return list(map(int, dt))


# day 1 part 1 - solution
def findTwoSum(data: list, target: int) -> int:
    for i in data:
        if (target - i) in data:
            return i, (target - i)
    return 0, 0


# day 1 part 2 - solution
def findThreeSum(data: list, target: int) -> int:
    for i in data:
        for j in data:
            if (target - i - j) in data:
                return i, j, (target - i - j)
    return 0, 0


if __name__ == "__main__":
    data = getInput("data.txt")
    num1, num2 = findTwoSum(data, 2020)
    print("The two numbers that their sum is 2020 are: ", num1, "and", num2)
    print("The result is: ", num1*num2)

    num1_2, num2_2, num2_3 = findThreeSum(data, 2020)
    print("The three numbers that their sum is 2020 are: ", num1_2, num2_2,
          "and", num2_3)
    print("The result is: ", num1_2 * num2_2 * num2_3)
