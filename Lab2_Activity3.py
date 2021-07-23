from math import *

#Name: Kyle Mrosko, Scottie Taylor, Braedon Lindsey, Lauren Corradino
#Section: 212
#Assigenment: Lab2_Activity3

# time measurements are in seconds
# distance measurements are in meters past the starting line

xInitial = 50
xFinal = 615

timeInitial = 30
timeFinal = 45

# input time for desired position
timeGiven = 37

# determining position on the track at time t
slope = (xFinal - xInitial) / (timeFinal - timeInitial)

deltaTime = timeGiven - timeInitial

xAtTimeT = slope * deltaTime + xInitial

radius = 500

circumference = 2 * pi * radius

xAtTimeT = xAtTimeT % circumference

print(f"The distance from the start of the track at time t = {timeGiven}, is {xAtTimeT} m.")