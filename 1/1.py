input = open("calories.txt", "r")
inputStr = input.read()

elfListLb = inputStr.split("\n\n")

sums = []

for x in elfListLb:
    calories = x.split("\n")
    sum = 0
    for y in calories:
        sum += int(y)
    sums.append(sum)

sums.sort(reverse=True)

highestSums = []
highestSums.append(sums[0])
highestSums.append(sums[1])
highestSums.append(sums[2])

highestSum = 0
for x in highestSums:
    highestSum += x

print(highestSum)