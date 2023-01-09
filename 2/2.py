input = open("strat.txt", "r")
inputStr = input.read()

matchList = inputStr.split("\n")
matchListByPlayer = []

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
    print(sumOfScores)

print(count)
print(sumOfScores)