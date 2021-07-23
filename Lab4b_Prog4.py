# Name:         Kyle Mrosko
# Section:      212
# Assignment:   Lab 4b_Prog4
# An Aggie does not lie, cheat or steal, or tolerate those who do.

import math

print("Input A,B,C for the equation Ax^2+Bx+C=0 and this program will calculate the roots.")

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

discrim = b**2-4*a*c

if(a==0 and b==0 and c!=0):
    print("User input error")
    exit()

if(a==0 and b==0 and c==0):
    print("True")
    exit()

if(discrim==0):
    root1 = -b/(2*a)
    if(b==0): root1=0
    print("Root: x =", root1)
elif(discrim>0):
    root1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    root2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    print("Roots: x =",root1,"and x =",root2)
else:
    print(f"Roots: x = ({-b} + sqrt({math.fabs(discrim)})i)/{2*a}")
    print(f"       x = ({-b} - sqrt({math.fabs(discrim)})i)/{2 * a}")

