# Kyle Mrosko
# ENGR 102 - 212
# Burt Dow Problem
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

import matplotlib.pyplot as plt
from math import *
import random

def dist(x1,y1,x2,y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)


infile = open("lobsterPotPoints.txt", 'r')
xList = [0]
yList = [0]
for line in infile:
    pair = line.split(",")
    xList.append(int(pair[0]))
    if "\n" in pair[1]:
        pair[1] = pair[1][:-1]
    yList.append(int(pair[1]))

xList.append(0)
yList.append(0)

sum = 0
for i in range(len(xList)-1):
    sum += dist(xList[i],yList[i],xList[i+1],yList[i+1])

x = f"Total distance of the original path is: {sum} ft."

plt.plot(xList,yList)
plt.title(x)
plt.xlabel("East")
plt.ylabel("North")
plt.show()

#Part 2 ---------------------------------------------------

origX = xList[1:-1]
origY = yList[1:-1]

pairList = []
for i in range(len(origX)):
    pairList.append([origX[i], origY[i]])

tempPairList = pairList
bestDist = 9999999
bestOrder = []
for i in range(1000):
    random.shuffle(tempPairList)
    tempPairList.append([0, 0])
    tempPairList.insert(0, [0, 0])
    tempDist = 0
    for j in range(len(tempPairList)-1):
        tempDist += dist(tempPairList[j][0], tempPairList[j][1], tempPairList[j+1][0], tempPairList[j+1][1])
    if tempDist < bestDist:
        bestOrder = tempPairList
        bestDist = tempDist
        print(f"The distance of path {i+1} is {bestDist} ft.")
    tempPairList.pop(0)
    tempPairList.pop(len(tempPairList)-1)

bestX = [0]
bestY = [0]

for i in bestOrder:
    bestX.append(i[0])
    bestY.append(i[1])

bestX.append(0)
bestY.append(0)

plt.plot(bestX, bestY)
x = f"Total distance of the best of 1000 paths is: {bestDist} ft."
plt.title(x)
plt.xlabel("East")
plt.ylabel("North")
plt.show()

#Part 3 ------------------------------------------

pointsRemaining = pairList
currentPoint = [0, 0]
prevPoint = []
finalList = [[0, 0]]
totalDist = 0
while len(pointsRemaining) > 0:
    minDist = [9999999, -1]
    for i in range(len(pointsRemaining)):
        tempDist = dist(currentPoint[0], currentPoint[1], pointsRemaining[i][0], pointsRemaining[i][1])
        if tempDist < minDist[0]:
            minDist = [tempDist, i]
    prevPoint = currentPoint
    currentPoint = pointsRemaining[minDist[1]]
    totalDist += minDist[0]
    finalList.append(currentPoint)
    pointsRemaining.remove(currentPoint)

finalList.append([0, 0])
totalDist += dist(0,0,finalList[-2][0],finalList[-2][1])
finalX = []
finalY = []
for i in finalList:
    finalX.append(i[0])
    finalY.append((i[1]))

plt.plot(finalX, finalY)
x = f"Total distance of nearest path is: {totalDist} ft."
plt.title(x)
plt.xlabel("East")
plt.ylabel("North")
plt.show()


