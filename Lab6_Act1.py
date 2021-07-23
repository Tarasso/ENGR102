# Braedon Lindsey, Kyle Mrosko, Lauren Corradino, and Scottie Taylor
# Lab6_Act1.py
# An Aggie does not lie, cheat or steal or tolerate those who do

print("This program will calculate the rate at which production is changing given daily production values.")
print("Enter the amount of widgets per day one per line (once done, enter a negative number to stop the input loop)")

values = []

# stores data into list until negative number is entered
while True:
    x = int(input())
    if x >= 0:
        values.append(x)
    else:
        break

# loops over every possible interval length
for interval_length in range(1, len(values)):
    increasing = 0  # count of increasing intervals
    decreasing = 0  # count of decreasing intervals
    # loops through each possible interval in the list
    for offset in range(len(values) - interval_length):
        # tests if the interval is increasing or decreasing
        if values[interval_length+offset] - values[offset] > 0:
            increasing += 1
        elif values[interval_length+offset] - values[offset] < 0:
            decreasing += 1
    # calculates percentage of increasing and decreasing intervals
    increasing_percent = increasing / (len(values)-interval_length) * 100
    decreasing_percent = decreasing / (len(values)-interval_length) * 100
    # prints everything
    print("For", interval_length, "day intervals,", round(increasing_percent, 1), "% increasing and", round(decreasing_percent, 1), "% decreasing")