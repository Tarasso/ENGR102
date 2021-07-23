# Name:         Kyle Mrosko
# Section:      212
# Assignment:   Lab 3_Act4_Prog1c
#An Aggie does not lie, cheat or steal, or tolerate those who do.

import math

print("Given the normal stress, angle of internal friction, and cohesion factor, this program calculates the shear stress of a material.")
normalStress = float(input("What is the normal shear stress? (lbf/in^2): "))
angleInternalFriction = float(input("What is the angle of internal friction? (degrees): "))
cohesion = float(input("What is the cohesion factor? (lbf/in^2): "))
# Mohr-Coulomb Failure Criterion: normal stress (lbf/in^2), angle of internal friction (degrees),
# cohesion (lbf/in^2) --> shear stress (lbf/in^2)
print("The shear stress of the material is", normalStress * math.tan(math.radians(angleInternalFriction)) + cohesion, "lbf/in^2")