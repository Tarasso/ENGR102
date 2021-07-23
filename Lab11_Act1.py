# Braedon Lindsey, Scottie Taylor, Lauren Corradino, and Kyle Mrosko
# ENGR 102 - 212
# Lab 11 Act 1
# An aggie does not lie, cheat or steal, or tolerate those who do.

import math

# Returns y value of a function at an x value
def F(x):
    ans = math.exp(x**3) * (x-2)
    return ans


# Calculates the derivative of a function
def deriv(x):
    num = F(x+0.001) - F(x)
    denom = 0.001
    return (num / denom)


# Calculation for a single iteration of Newton's method
def newton_step(x_i):
    ans = x_i - F(x_i) / deriv(x_i)
    return(ans)

# Tolerance
TOL = 10e-6

# Main logic for Newton's method
def newton(x_0):
    x_i = newton_step(x_0)
    count = 0
    while True:
        count += 1
        x_i = newton_step(x_0)
        if abs(x_i - x_0) < TOL:
            return f"x = {x_i} in {count} iterations"
        else:
            x_0 = x_i


print(newton(float(input("Enter an initial x value: "))))