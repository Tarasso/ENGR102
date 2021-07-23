# Name:         Bryson Mrosko
# Section:      212
# Assignment:   Lab 1b-1

print("Interesting fact: I am left-handed\n")

import math

#Ohm's Law: resistance (ohms), current (amperes) --> voltage (volts)
print("The voltage across the conductor is", 20 * 5, "volts.")

#Kinetic Energy Formula: mass (kg), velocity (m/s) --> kinetic energy (joules)
print("The kinetic energy of the object is", (1 / 2) * 100 * 21 ** 2, "joules.")

#Reynolds Number: velocity (m/s), characteristic linear dimension (m),
#kinematic viscosity (m^2/s) --> Reynold's number (unitless)
print("Reynolds Number for the fluid is", (100 * 2.5) / 1.2)

#Arps Equation: inital production rate (barrels per day), inital decline rate (barrels per day),
#hyperbolic constant (unitless), time (days since production) --> production rate in future "time" (barrels per day)
print("The production of the well after 20 days is", 100/((1+.8*2*20)**(1/.8)), "barrels per day")

#Mohr-Coulomb Failure Criterion: normal stress (lbf/in^2), angle of internal friction (radians),
# cohesion (lbf/in^2) --> shear stress (lbf/in^2)
print("The shear stress of the material is", 20*math.tan(math.radians(35))+2, "lbf/in^2")
