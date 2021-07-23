# Kyle Mrosko
# ENGR 102-212
# Lab 11b
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

from math import *

# A--------------------------------------------

def materialRemaining(length, width, height, radius):
    CubeVolume = length * width * height
    CylinderVolume = pi*radius*radius*height
    return CubeVolume - CylinderVolume

print("Volume:",materialRemaining(10,10,10,2))
print("")

# B--------------------------------------------

def leastProfit(names, values, costs):
    minNum = 999999999
    minName = ""
    for i in range(len(names)):
        diff = values[i] - costs[i]
        if (diff<minNum):
            minNum = diff
            minName = names[i]
    return [minName,minNum]

names = ["place1","place2","place3"]
values = [20,15,10]
costs = [5,5,5]
print("Least profit:",leastProfit(names,values,costs))

# C--------------------------------------------

def mailLabel(name,city,state,zip,address,address2=""):
    print(name)
    print(address)
    if address2!="":
        print(address2)
    print(f"{city}, {state} {zip}")

print("")
mailLabel("Kyle Mrosko","Conroe","Texas","77304","2 Hartwick Court")
print("")
mailLabel("Scottie Taylor","Kilgore","Texas","75662","123 Wateroak Street","P.O. Box 32")
print("")

# D--------------------------------------------

def csvTotsv(fileName):
    file = open(fileName, "r")
    tsv = open("output.tsv", "w")
    for line in file:
        elements = line.split(",")
        for i in range(len(elements)):
            if (i == len(elements) - 1):
                tsv.write(elements[i])
            else:
                tsv.write(elements[i] + "\t")

    file.close()
    tsv.close()

csv = input("Enter a .csv filename:")+".csv"
csvTotsv(csv)
print("")

# E--------------------------------------------

def stats(list):
    minNum = min(list)
    maxNum = max(list)
    total = sum(list)
    avg = total/len(list)
    return [minNum,avg,maxNum]

list = [1,2,3,4,5,6,7,8,9,10]
print("[min,mean,max]:",end="")
print(stats(list))
print("")

# F--------------------------------------------

def calcVelocities(times,distances):
    vels = []
    for i in range(len(times)-1):
        x1 = times[i]
        y1 = distances[i]
        x2 = times[i + 1]
        y2 = distances[i + 1]
        vels.append((y2-y1)/(x2-x1))
    return vels

times = [1,2,3,4,5]
distances = [0, 1, 2, 4, 8]
print("Velocities:",calcVelocities(times,distances))

# --------------------------------------------
