import math


def getInput(file: str) -> list:
    data = []
    with open(file, "r") as file:
        for line in file:
            data.extend(line.split())
    return data


def findSeatID(ticket: str, row_sum: int, col_sum: int) -> int:
    return (findRowCol(ticket[:7], row_sum, "F", "B") * 8
            + findRowCol(ticket[-3:], col_sum, "L", "R"))


def findRowCol(ticket: str, rowcol_sum: int, l_half: str,
               u_hlaf: str) -> int:
    lower = 0
    upper = rowcol_sum - 1
    for i in range(len(ticket)):
        if (ticket[i] == l_half):
            upper -= math.ceil((upper - lower) / 2)
        elif (ticket[i] == u_hlaf):
            lower += math.ceil((upper - lower) / 2)
        else:
            raise ValueError("Unknown indicator")
    assert lower == upper, "upper and lower aren't equal!"
    return lower


def findMissingSeatID(seats: list) -> int:
    for i in range(len(seats) - 1):
        if (seats[i+1] - seats[i]) == 2:
            return seats[i] + 1


# day 5 part1 - solution
SeatsID = []
rows, columns = 128, 8
tickets = getInput("input.txt")
for i in range(len(tickets)):
    SeatsID.append(findSeatID(tickets[i], rows, columns))
print("The answer for the first puzzle is: ", max(SeatsID))

# day 5 part2 - solution
SeatsID.sort()
print("The answer for the second puzzle is: ", findMissingSeatID(SeatsID))
