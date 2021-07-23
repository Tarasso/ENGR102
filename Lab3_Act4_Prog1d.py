# Name:         Kyle Mrosko
# Section:      212
# Assignment:   Lab 3_Act4_Prog1d
#An Aggie does not lie, cheat or steal, or tolerate those who do.

print("Given the initial production rate, initial decline rate, hyperbolic constant, and days to check the well, this program calculates the production rate on the later given day.")
initialProductionRate = float(input("What is the initial production rate? (barrels per day): "))
initialDeclineRate = float(input("What is the initial decline rate? (barrels per day): "))
hyperbolicConstant = float(input("What is the hyperbolic constant?: "))
days = float(input("How many days do you want to estimate the production at?: "))
# Arps Equation: inital production rate (barrels per day), inital decline rate (barrels per day),
# hyperbolic constant (unitless), time (days since production) --> production rate in future "time" (barrels per day)
print("The production of the well after 20 days is", initialProductionRate / ((1 + hyperbolicConstant * initialDeclineRate * days) ** (1 / hyperbolicConstant)), "barrels per day")