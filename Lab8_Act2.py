# Braedon Lindsey, Scottie Taylor, Kyle Mrosko, and Lauren Corradino
# Lab 8 Activity 2
# ENGR 102-212 - 10/14/19
# An aggie does not lie, cheat or steal, nor tolerate those who do.AttributeError

print("Given two points (x,y), this program will output an estimated y value for any x given.")


# BRAEDON'S SECTION
# input for first and second points
x1 = float(input("Enter the x value of the first point: "))
y1 = float(input("Enter the y value of the first point: "))
x2 = float(input("Enter the x value of the second point: "))
y2 = float(input("Enter the y value of the second point: "))


# KYLE'S SECTION
# calculate the components of the equation
# m = y2-y1 / x2-x1
slope = (y2 - y1) / (x2 - x1)


# SCOTTIE'S SECTION
# b = -mx1 + y1
b = -slope * x1 + y1


# LAUREN'S SECTION
# continually accepts user input for x values to estimate the corresponding y values
while True:
    xInput = input("Enter an x value to evaluate, enter 'STOP' to stop: ")
    if xInput == "STOP":
        break
    else:
        xInput = float(xInput)
    yOutput = slope * xInput + b  # estimation equation
    print(f"The estimated y value at x = {xInput} is y = {yOutput}")

print("Thanks for using our program :) have a nice day bby TTYLXOX <3")
