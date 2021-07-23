# Braedon Lindsey, Kyle Mrosko, Scottie Taylor, and Lauren Corradino
# Lab5_Act1.py
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# if A=1, B=2, C=3, D=4: a = -2, b = -1, root at x = -1.65063
# if A=-1, B=-2, C=3, D=4: a = -1.5, b = -0.5, root at x = -1.00000
# if A=1, B=0, C=0, D=1: a = -2, b = -1, root at x = -1.25992
# if A=3.1415, B=-3.1415, C=10, D=25: a = -2, b = -1, root at x = -1.29379

from math import *

# tolerance value
TOL = 1e-6

print("This program finds roots of a cubic polynomial to within a given tolerance")
print("Enter the following coefficients for the polynomial Ax^3 + Bx^2 + Cx + D = 0")

# save user input values
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
D = float(input("D: "))
a = float(input("Left Bound: "))
b = float(input("Right Bound: "))
p = 0
count = 0

# initial difference
dif = b-a


# function to calculate polynomial value
def Polynomial(x):
    answer = exp(x**3)*(x-2)
    return answer


# decreasing from left to right:
if Polynomial(a) > 0:
    # running the code until the difference between a and b is less than the tolerance
    while dif > TOL:
        count += 1
        dif = b-a
        p = (a + b)/2
        # this if tree determines where to set the new bound
        if Polynomial(p) > 0:
            a = p
        elif Polynomial(p) < 0:
            b = p
        elif Polynomial(p) == 0:
            break
# increasing from left to right
elif Polynomial(a) < 0:
    # running the code until the difference between a and b is less than the tolerance
    while dif > TOL:
        count += 1
        dif = b-a
        p = (a + b)/2
        # this if tree determines where to set the new bound
        if Polynomial(p) > 0:
            b = p
        elif Polynomial(p) < 0:
            a = p
        elif Polynomial(p) == 0:
            break

# prints answer
print(f"The polynomial has a solution at x = {p}. It took {count} iterations!")