# Name:         Kyle Mrosko
# Section:      212
# Assignment:   Lab 3_Act4_Prog1b
#An Aggie does not lie, cheat or steal, or tolerate those who do.

# Kinetic Energy Formula: mass (kg), velocity (m/s) --> kinetic energy (joules)
print("Given a mass and a velocity, this program calculates the kinetic energy of an object.")
mass = float(input("What is the mass? (kg): "))
velocity = float(input("What is the velocity? (m/s): "))
print("The kinetic energy of the object is", (1 / 2) * mass * velocity ** 2, "joules.")