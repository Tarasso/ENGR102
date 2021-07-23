# Name:         Kyle Mrosko UIN: 928003182
# Section:      212
# Assignment:   Lab 1b-1

timeInitial = 13
timeFinal = 84

xInitial = 1
xFinal = 23
yInitial = 3
yFinal = -5
zInitial = 7
zFinal = 10

timeGiven = 50

xSlope = (xFinal - xInitial) / (timeFinal - timeInitial)
ySlope = (yFinal - yInitial) / (timeFinal - timeInitial)
zSlope = (zFinal - zInitial) / (timeFinal - timeInitial)

deltaTime = timeGiven - timeInitial

xAtTimeT = xSlope * deltaTime + xInitial
yAtTimeT = ySlope * deltaTime + yInitial
zAtTimeT = zSlope * deltaTime + zInitial

print("time of interest =",timeGiven,"seconds")
print("x0 =",xAtTimeT,"m")
print("y0 =",yAtTimeT,"m")
print("z0 =",zAtTimeT,"m")