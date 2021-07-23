# Braedon Lindsey, Kyle Mrosko, Scottie Taylor, Lauren Corradino
# Lab5_Act2_a.py
# An aggie does not lie, cheat or steal, nor tolerate those who do.

# Part a:

# This program evaluates a cubic polynomial limit analytically.

print("This program calculates the derivative of a polynomial and evaluates it at a given point")

# stores user inputs
print("Enter the coefficients for the polynomial A*x^3 + B*x^2 + C*x + D = 0")
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
D = float(input("D: "))


# calculates f prime coefficents
A_prime = A * 3
B_prime = B * 2
C_prime = C * 1
print(f"The derivative of the polynomial is {A_prime}*x^2 + {B_prime}*x + {C_prime}")

#evaluates derivative at the point x
x = float(input("Enter a value at which to evaluate the derivative: "))
answer = A_prime*x**2 + B_prime*x + C_prime
print(f"The value of the derivative of the polynomial at x={x} is {answer}.")