# Braedon Lindsey, Scottie Taylor, Kyle Mrosko, and Lauren Corradino
# 10/21/2019
# ENGR 102-212 - Lab 9 Interpolate
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

print("Enter the following parameters:\n")

name = input("Name of file: ")
dataFile = open(name, 'r')

data = []
for line in dataFile:
    data.append(line[:-1])

x = ""

# saving the names of the variables then removing them from the list of values
variables = data[0]
data.pop(0)

# separating the values into lists without commas
data = [data[x].split(",") for x in range(len(data))]
data = {float(data[x][0]): float(data[x][1]) for x in range(len(data))}

# sorting the data
sortedData = {}
for key in sorted(data.keys()):
    sortedData[key] = data[key]

# defining a list with only the keys of the sorted dictionary
sortedDataKeys = [x for x in sortedData]

variables = variables.split(",")
print(f"The independent variable is {variables[0]}.")
print(f"The dependent variable is {variables[1]}.")

# main loop to request input and calculate an output
while x != "STOP":
    x = float(input(f"Enter a {variables[0]} value to interpolate at (enter STOP to stop): "))
    if x > sortedDataKeys[-1] or x < sortedDataKeys[0]:
        print("Enter a number in the valid range.")
        continue
    # determining between which two keys the input falls
    for i in range(len(sortedDataKeys)):
        if x >= sortedDataKeys[i] and x <= sortedDataKeys[i + 1]:
            x1 = sortedDataKeys[i]
            x2 = sortedDataKeys[i + 1]
            y1 = sortedData[x1]
            y2 = sortedData[x2]
            # calculating and printing the output
            answer = (y2 - y1) / (x2 - x1) * (x - x1) + y1
            print(f"{variables[1]} = {round(answer, 3)} at {variables[0]} = {x}")