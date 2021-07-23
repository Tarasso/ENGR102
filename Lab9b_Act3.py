# Kyle Mrosko
# 10/23/2019
# ENGR 102-212 - Lab 9b Act 3
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

from math import *

openFile = open("WeatherDataWindows.csv",'r')

# Lists to store values
maxTemps = []
minTemps = []
dailyPrecip = []
humidity = []
dates = []

# Reads in data
openFile.readline()
for line in openFile:
    words = line.split(',')
    dates.append(words[0])
    maxTemps.append(int(words[1]))
    minTemps.append(int(words[3]))
    dailyPrecip.append(float(words[-1]))
    humidity.append(float(words[-6]))

# Find max temp
max = -99999
for i in maxTemps:
    if i > max:
        max = i
print(f"The max temperature is {max}")

# Find max temp
min = 99999
for i in minTemps:
    if i < min:
        min = i
print(f"The min temperature is {min}")

# Find average daily precip
rainSum = 0
for i in dailyPrecip:
    rainSum += i
avgDailyRain = rainSum / len(dailyPrecip)
print(f"The average daily rainfall is {round(avgDailyRain,3)} in.")

# Percentage of Days that humidity was over threshhold
threshHold = 90
humidCount = 0
for i in humidity:
    if i > threshHold:
        humidCount += 1
print(f"There are {humidCount} days that have a humidity over {threshHold}%.")

# Calculate the mean and std dev of the precipitation levels
count = 0;
sum = 0;
squaredSum = 0;

for i in dailyPrecip:
    count += 1
    sum += i
    squaredSum += i**2

mean = sum/count
stdev = sqrt((squaredSum/count)-mean**2)
print(f"The average precipitation level is {round(mean,3)} in.")
print(f"The standard deviation of the precipitation levels is {round(stdev,3)} in.")

# Find max and min temp for a date of the year
targetDate = input("Enter the month and day of desired date to check (ex: 10/16): ")
max = -99999
min = 99999
for i in range(len(maxTemps)):
    if targetDate in dates[i]:
        if maxTemps[i] > max:
            max = maxTemps[i]
for i in range(len(minTemps)):
    if targetDate in dates[i]:
        if minTemps[i] < min:
            min = minTemps[i]

print(f"The min temp for the date {targetDate} from 2015-2017 is {min}.")
print(f"The max temp for the date {targetDate} from 2015-2017 is {max}.")
