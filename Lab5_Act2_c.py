# Braedon Lindsey, Kyle Mrosko, Scottie Taylor, Lauren Corradino
# Lab5_Act2_c.py
# An aggie does not lie, cheat or steal, nor tolerate those who do.

from math import *

# Part c:

print("This program calculates the derivatives of various functions at a given point")

# This function calculates the derivative of a given function at a given point to within a certain tolerance
def derivative(x, difference, function):
    answer = (function(x+difference) - function(x))/difference
    return answer

# This is the first complex function to evaluate the derivative of
def function1(x):
    answer = 1/sin(radians(x))
    return answer


function_1 = "1/sin(radians(x))"
TOL = 1e-6
a = float(input(f"Input the point at which to evaluate the derivative of {function_1}: "))
h1 = 0.1
h2 = 0.1 * 0.5
count = 1

# This iterates the difference value until it produces results within the tolerance
while abs(derivative(a,h1,function1) - derivative(a,h2,function1)) > TOL/100:
    count += 1
    h1 *= 0.5
    h2 *= 0.5
print(f"The derivative of {function_1} at {a} is {derivative(a,h2, function1)}. It took {count} iterations!")


# This is the second complex function to evaluate the derivative of
def function2(x):
    e = 2.7182818
    answer = x * e ** x
    return answer


count = 1
h1 = 0.1
h2 = 0.1 * 0.5
function_2 = "x*e^x"
a = float(input(f"Input the point at which to evaluate the derivative of {function_2}: "))

# This iterates the difference value until it produces results within the tolerance
while abs(derivative(a,h1,function2) - derivative(a,h2,function2)) > TOL/100:
    count += 1
    h1 *= 0.5
    h2 *= 0.5
print(f"The derivative of {function_2} at {a} is {derivative(a,h2, function2)}. It took {count} iterations!")


# This is the third complex function to evaluate the derivative of
def function3(x):
    answer = atan(x)
    return answer


count = 1
h1 = 0.1
h2 = 0.1 * 0.5
function_3 = "atan(x)"
a = float(input(f"Input the point at which to evaluate the derivative of {function_3}: "))

# This iterates the difference value until it produces results within the tolerance
while abs(derivative(a,h1,function3) - derivative(a,h2,function3)) > TOL/100:
    count += 1
    h1 *= 0.5
    h2 *= 0.5
print(f"The derivative of {function_3} at {a} is {derivative(a,h2, function3)}. It took {count} iterations!")


# This is the fourth complex function to evaluate the derivative of
def function4(x):
    answer = log(x)
    return answer


count = 1
h1 = 0.1
h2 = 0.1 * 0.5
function_4 = "log(x)"
a = float(input(f"Input the point at which to evaluate the derivative of {function_4}: "))

# This iterates the difference value until it produces results within the tolerance
while abs(derivative(a,h1,function4) - derivative(a,h2,function4)) > TOL/100:
    count += 1
    h1 *= 0.5
    h2 *= 0.5
print(f"The derivative of {function_4} at {a} is {derivative(a,h2, function4)}. It took {count} iterations!")