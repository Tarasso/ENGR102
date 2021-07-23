# Name:         Kyle Mrosko
# Section:      212
# Assignment:   Lab 3_Act4_Prog2
#An Aggie does not lie, cheat or steal, or tolerate those who do.

import math

obstemp = input("Observer location x,y,z: ").replace(" ","").split(",")
obs = list([float(obstemp[x]) for x in range(len(obstemp))])
point1temp = input("Point 1 x,y,z: ").replace(" ","").split(",")
point1 = list([float(point1temp[x]) for x in range(len(point1temp))])
point2temp = input("Point 2 x,y,z: ").replace(" ","").split(",")
point2 = list([float(point2temp[x]) for x in range(len(point2temp))])

v1 = (point1[0]-obs[0],point1[1]-obs[1],point1[2]-obs[2])
v2 = (point2[0]-obs[0],point2[1]-obs[1],point2[2]-obs[2])

v1Dotv2 = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

v1Mag = math.sqrt(v1[0]**2+v1[1]**2+v1[2]**2)
v2Mag = math.sqrt(v2[0]**2+v2[1]**2+v2[2]**2)

angle = math.acos(v1Dotv2/(v1Mag*v2Mag))

print("The angle between the points is", math.degrees(angle), "degrees.")