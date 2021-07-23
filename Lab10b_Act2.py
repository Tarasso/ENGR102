# Kyle Mrosko
# ENGR 102-212
# Lab 10b Assignment 2
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

import matplotlib.pyplot as plt
import numpy as np

openFile = open("WeatherDataWindows.csv",'r')

# Lists to store values
dates = []
avgTemp = []
avgPressure = []
precip = []
avgDew = []
data = [i[:-1].split(",") for i in openFile]
data.pop(0)

openFile.close()
openFile = open("WeatherDataWindows.csv",'r')

# Reads in data
openFile.readline()
for line in openFile:
    words = line.split(',')
    dates.append(words[0])
    avgTemp.append(float(words[2]))
    avgPressure.append(float(words[-3]))
    precip.append(float(words[-1]))
    avgDew.append(float(words[5]))


datesSince = np.arange(len(dates))


# Line Plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(datesSince,avgTemp, '-r')
ax.set_ylabel("Average Temp (F)")
ax.set_xlabel("Days since 01/01/2015")
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', colors='red')
plt.title("Pressure and Temperature vs. Time")
ax2 = ax.twinx()
ax2.plot(datesSince,avgPressure)
ax2.set_ylabel("Average Pressure (atm)")
ax2.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', colors='blue')
plt.show()


# Histogram
bins = 20
plt.hist(precip,bins=bins,range=[.01,9])
# Intentionally did not include the 0 in. of precipitation because that accounts for nearly 800 days
# Such a large frequency makes the rest of the graph extremely hard to read
plt.title("Histogram of Average Precipitation")
plt.xlabel("Average Precipitation (in.)")
plt.ylabel("Frequency (days)")
plt.show()


# Scatter Plot
plt.scatter(avgTemp,avgDew)
plt.title("Average Dew Point vs. Average Temperature")
plt.xlabel("Average Temperature (F)")
plt.ylabel("Average Dew Point (F)")
plt.show()

# Bar Chart
temps2015 = [[] for i in range(12)]
temps2016 = [[] for i in range(12)]
temps2017 = [[] for i in range(12)]

high_temps2015 = [[] for i in range(12)]
high_temps2016 = [[] for i in range(12)]
high_temps2017 = [[] for i in range(12)]

low_temps2015 = [[] for i in range(12)]
low_temps2016 = [[] for i in range(12)]
low_temps2017 = [[] for i in range(12)]

# Loops through the year 2015 and stores data
for i in range(1, 13):
    for j in data[:364]:
        if f"{i}/" in j[0][:len(f"{i}/")]:
            temps2015[i - 1].append(float(j[2]))
            high_temps2015[i - 1].append(float(j[1]))
            low_temps2015[i - 1].append(float(j[3]))

# Loops through the year 2016 and stores data
for i in range(1, 13):
    for j in data[364:730]:
        if f"{i}/" in j[0][:len(f"{i}/")]:
            temps2016[i - 1].append(float(j[2]))
            high_temps2016[i - 1].append(float(j[1]))
            low_temps2016[i - 1].append(float(j[3]))

# Loops through the year 2017 and stores data
for i in range(1, 13):
    for j in data[730:]:
        if f"{i}/" in j[0][:len(f"{i}/")]:
            temps2017[i - 1].append(float(j[2]))
            high_temps2017[i - 1].append(float(j[1]))
            low_temps2017[i - 1].append(float(j[3]))

# Find sum for each
sum2015 = [sum([i for i in temps2015[j]]) for j in range(12)]
sum2016 = [sum([i for i in temps2016[j]]) for j in range(12)]
sum2017 = [sum([i for i in temps2017[j]]) for j in range(12)]

# Find max temps for each
maxes2015 = [max(high_temps2015[i]) for i in range(12)]
maxes2016 = [max(high_temps2016[i]) for i in range(12)]
maxes2017 = [max(high_temps2017[i]) for i in range(12)]

# Find min temps for each
mins2015 = [min(low_temps2015[i]) for i in range(12)]
mins2016 = [min(low_temps2016[i]) for i in range(12)]
mins2017 = [min(low_temps2017[i]) for i in range(12)]

# Find averages for each
averages = []
averages2015 = [sum2015[i]/len(temps2015[i]) for i in range(12)]
averages2016 = [sum2016[i]/len(temps2016[i]) for i in range(12)]
averages2017 = [sum2017[i]/len(temps2017[i]) for i in range(12)]
averages.extend(averages2015)
averages.extend(averages2016)
averages.extend(averages2017)

# Calculates the magnitude of upper error bar
maxes = []
maxes.extend([maxes2015[i]-averages2015[i] for i in range(12)])
maxes.extend([maxes2016[i]-averages2016[i] for i in range(12)])
maxes.extend([maxes2017[i]-averages2017[i] for i in range(12)])

# Calculates the magnitude of lower error bar
mins = []
mins.extend([averages2015[i]-mins2015[i] for i in range(12)])
mins.extend([averages2016[i]-mins2016[i] for i in range(12)])
mins.extend([averages2017[i]-mins2017[i] for i in range(12)])

plt.bar(range(36), averages, yerr=[mins, maxes])
plt.title("Average Temperature Per Month (with max and min temp error bars)")
plt.xlabel("Months since January 2015")
plt.ylabel("Temperature (F)")
plt.show()

