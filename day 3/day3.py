import math


def getInput(file: str, slope_cord: list) -> str:
    dt = []
    slope = math.ceil(slope_cord[1]/slope_cord[0])
    with open(file, "r") as file:
        for line in file:
            dt.extend(line.split())
    for i in range(len(dt)):
        dt[i] *= len(dt) * math.ceil(slope/len(dt[0]))
    return dt


def goSlope(data: list, slope_cord: list) -> int:
    sum_trees = 0
    down, right = slope_cord[0], slope_cord[1]
    j = right
    for i in range(down, len(data), down):
        if data[i][j] == "#":
            sum_trees += 1
        j += right
    return sum_trees


# day 3 part1 - solution
slope_cord = [1, 3]
path_input = getInput("input.txt", slope_cord)
print("The answer for the first puzzle is: ", goSlope(path_input, slope_cord))

# day 3 part2 - solution
result = 1
slope_cord = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
for i in range(len(slope_cord)):
    path_input = getInput("input.txt", slope_cord[i])
    result *= goSlope(path_input, slope_cord[i])
print("The answer for the second puzzle is: ", result)
