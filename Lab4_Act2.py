# Name:         Kyle Mrosko, Scottie Taylor, Braedon Lindsay, Lauren Corradino
# Section:      212
# Assignment:   Lab 4_Act2
# An Aggie does not lie, cheat or steal, or tolerate those who do.

from math import *

print("This program calculates the cost of a parking ticket after some given amount of hours")

timeParked = ceil(float(input("Enter the amount of time parked (in hours, negative if lost ticket): ")))
cost = 0

if timeParked < 0:  # if ticket is lost
    cost += 36
    timeParked = abs(timeParked)

if timeParked > 24:  # if timeParked > 24, calculate how many days to pay for
    days = floor(timeParked / 24)
    cost += days * 24
    timeParked %= 24
else:
    days = 0

if timeParked <= 2:
    cost += 4
elif timeParked <= 4:
    cost += 7
elif timeParked < 21:
    cost += 7 + (timeParked - 4)
elif timeParked <= 24:
    cost += 24

print("The cost of the parking ticket for", days, "days and", timeParked, "hours is $" + str(cost) + ".")