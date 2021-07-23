# Name:         Kyle Mrosko
# Section:      212
# Assignment:   Lab 4b_Prog2
# An Aggie does not lie, cheat or steal, or tolerate those who do.

print("This program calculates and evaluates Reynold's Number")

V = float(input("Enter the characteristic velocity of the flow (m/s): "))
d = float(input("Enter the pipe diameter (m): "))
v = float(input("Enter the fluid kinematic viscosity (m^2/s): "))

Re = (V*d)/v
print("Reynold's Number: 1",Re,end=" ")

if(Re<2300):
    print("Laminar")
elif(Re<2900):
    print("Transition")
else:
    print("Fully Turbulent")



