# Braedon Lindsey, Scottie Taylor, Kyle Mrosko, and Lauren Corradino
# 10/21/2019
# ENGR 102-212 - Lab 9 Collect Data
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

print("Enter the following parameters:\n")
name = input("Name of file: ")

# creates a new file to write to
dataFile = open(name, 'w')

# accepting input from the user
independent_variable = input("Name of the independent variable: ")
dependent_variable = input("Name of the dependent variable: ")
numDataPoints = int(input("Number of data points to enter: "))

# writing the names of the independent and dependent variables to the file
dataFile.write(independent_variable + "," + dependent_variable + "\n")

# writing data to the file in the form (x,y)
for i in range(numDataPoints):
    data = input("Enter a data point in the form x,y: ")
    dataFile.write(data + "\n")

dataFile.close()
