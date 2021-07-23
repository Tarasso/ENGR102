# Name:         Kyle Mrosko, Scottie Taylor, Braedon Lindsay, Lauren Corradino
# Section:      212
# Assignment:   Lab 4_Act1
# An Aggie does not lie, cheat or steal, or tolerate those who do.

from math import *

# testing for round-off error

TOL = 1e-10

a = 1/7
print(a)
b = a*7
print(b, "\n")
c = 2*a
d = 5*a
e = c+d
print(e)
# check if b and e are equal within specified tolerance
if abs(b-e) < TOL:
    print('b and e are equal within tolerance of', TOL)
else:
    print('b and e are NOT equal within tolerance of',TOL)

# testing for round-off error with even more complicated operations

x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z, "\n")

if abs(y-z) < TOL:
    print('y and z are equal within tolerance of', TOL)
else:
        print('y and z are NOT equal within tolerance of', TOL)