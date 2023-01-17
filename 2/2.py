def readMatchList():
    input = open("strat.txt", "r")
    inputStr = input.read()

    return inputStr.split("\n")

def part1():
    matchList = readMatchList()
    sumOfScores = 0
    count = 0

    for index, x in enumerate(matchList):
        matchList[index] = x.split(" ")

    for xIndex, x in enumerate(matchList):
        p1 = matchList[xIndex][0]
        p2 = matchList[xIndex][1]

        if(p1 == "A"):
            if(p2 == "X"):
                sumOfScores += (1 + 3)
            if(p2 == "Y"):
                sumOfScores += (2 + 6)
            if(p2 == "Z"):
                sumOfScores += (3 + 0)
        if(p1 == "B"):
            if(p2 == "X"):
                sumOfScores += (1 + 0)
            if(p2 == "Y"):
                sumOfScores += (2 + 3)
            if(p2 == "Z"):
                sumOfScores += (3 + 6)
        if(p1 == "C"):
            if(p2 == "X"):
                sumOfScores += (1 + 6)
            if(p2 == "Y"):
                sumOfScores += (2 + 0)
            if(p2 == "Z"):
                sumOfScores += (3 + 3)
        count += 1

    return sumOfScores

def part2():
    matchList = readMatchList()
    col1 = {"A": 1, "B": 2, "C": 3}
    col2 = {"X": 0, "Y": 3, "Z": 6}

    total_score = 0

    for line in matchList:
        shape1, shape2 = line.split()
        x = col1[shape1]
        round_score = col2[shape2]

        match round_score:
            case 6:  # win
                y = x % 3 + 1
            case 3:  # draw
                y = x
            case 0:  # loss
                y = (x + 1) % 3 + 1

        total_score += y + round_score

    return total_score

print(part1())
print(part2())