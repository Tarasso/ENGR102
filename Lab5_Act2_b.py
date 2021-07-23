# Braedon Lindsey, Kyle Mrosko, Scottie Taylor, Lauren Corradino
# Lab5_Act2_b.py
# An aggie does not lie, cheat or steal, nor tolerate those who do.

from math import *

# Part b:

print("This program evaluates the derivative of a polynomial at a given point numerically")

# stores user input
print("Enter the coefficients of the polynomial A*x^3 + B*x^2 + C*x + D = 0")
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
D = float(input("D: "))

A_prime = A * 3
B_prime = B * 2
C_prime = C * 1

a = 1
h1 = 0.1
h2 = 0.1 * 0.5
TOL = 1e-6
count = 1

exactDerivative = A_prime*a**2 + B_prime*a + C_prime

# defining a function to evaluate the polynomial
def cubic(x):
    answer = A*x**3 + B*x**2 + C*x + D
    return answer


# defining a function to evaluate the derivative of a function at a given value with a given h
def Derivative(x, difference):
    answer = (cubic(x+difference) - cubic(x))/difference
    return answer


def Derivative2(x, difference):
    answer = (cubic(x) - cubic(x-difference))/difference
    return answer


def Derivative3(x, difference):
    answer = (cubic(x + difference) - cubic(x - difference))/(difference*2)
    return answer


# loops until derivatives are within the tolerance
while abs(Derivative(a, h1) - Derivative(a, h2)) > TOL:
    count += 1
    h1 *= 0.5
    h2 *= 0.5

polynomialstr = f"{A}x**3 + {B}x**2 + {C}x + {D} = 0"

print(f"The derivative of {polynomialstr} at x = {a} is {Derivative(a,h2)}. It took {count} iterations! This number varies from the exact derivative of {exactDerivative} by {abs(Derivative(a,h2) - exactDerivative)}")

# We used the other 2 formulas for the derivatives above and got the answers 9.999999040737748 with a count of 19 tries, and 10.000000152585926 with a count of 8 tries respectively. It takes the last derivative formula many fewer iterations to reach the final value.
