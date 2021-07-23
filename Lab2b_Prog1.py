# Name:         Kyle Mrosko UIN: 928003182
# Section:      212
# Assignment:   Lab 1b-1

print("Interesting fact: I am left-handed\n")

import math

# Ohm's Law: resistance (ohms), current (amperes) --> voltage (volts)
resistance = 20  # ohms
current = 5  # amperes
print("The voltage across the conductor is", resistance * current, "volts.")

mass = 100  # kilograms
velocity = 21  # meters/second
# Kinetic Energy Formula: mass (kg), velocity (m/s) --> kinetic energy (joules)
print("The kinetic energy of the object is", (1 / 2) * mass * velocity ** 2, "joules.")

fluidVelocity = 100  # meters/second
kinematicViscosity = 1.2  # meters^2/second
linearDimension = 2.5  # 2.5 meters
# Reynolds Number: velocity (m/s), characteristic linear dimension (m),
# kinematic viscosity (m^2/s) --> Reynold's number (unitless)
print("Reynolds Number for the fluid is", (fluidVelocity * linearDimension) / kinematicViscosity)

initialProductionRate = 100  # barrels per day
initialDeclineRate = 2  # barrels per day
hyperbolicConstant = .8  # unitless
days = 20  # days since production
# Arps Equation: inital production rate (barrels per day), inital decline rate (barrels per day),
# hyperbolic constant (unitless), time (days since production) --> production rate in future "time" (barrels per day)
print("The production of the well after 20 days is", initialProductionRate / ((1 + hyperbolicConstant * initialDeclineRate * days) ** (1 / hyperbolicConstant)), "barrels per day")

normalStress = 20  # lbf/in^2
angleInternalFriction = 35  # degrees
cohesion = 2  # lbf/in^2
# Mohr-Coulomb Failure Criterion: normal stress (lbf/in^2), angle of internal friction (degrees),
# cohesion (lbf/in^2) --> shear stress (lbf/in^2)
print("The shear stress of the material is", normalStress * math.tan(math.radians(angleInternalFriction)) + cohesion, "lbf/in^2")
