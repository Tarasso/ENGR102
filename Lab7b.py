# Kyle Mrosko
# Lab7b
# An Aggie does not lie, cheat or steal or tolerate those who do

# strain and stress (x,y) of points: origin, a, b, c, d, and e on the stress strain graph
strainO = 0
stressO = 0

strainA = .012
stressA = 43.8

strainB = .012
stressB = 43.8

strainC = .057
stressC = 44

strainD = .18
stressD = 60

strainE = .263
stressE = 51

# Read user input
givenStrain = float(input("Please enter a strain value to evaluate the stress at: "))

# Calculates the stress depending on what line segment the given strain falls in
# For each region, the slope is calculated for the segment then multiplied by the difference in strain
# from the initial strain in the segment
# Finally, the initial stress at the beginning of the line segment is added to calculate the answer
if(givenStrain < 0):
    outputStress = "Invalid input, please try again."
elif(givenStrain <= strainA): # Calculates for both of the segments OA and AB since points A & B are the same
    slope = (stressA-stressO)/(strainA-strainO)
    outputStress = stressO + slope * givenStrain
elif(givenStrain <= strainC):
    slope = (stressC - stressB) / (strainC - strainB)
    outputStress = stressB + slope * (givenStrain-strainB)
elif(givenStrain <= strainD):
    slope = (stressD - stressC) / (strainD - strainC)
    outputStress = stressC + slope * (givenStrain-strainC)
elif(givenStrain <= strainE):
    slope = (stressE - stressD) / (strainE - strainD)
    outputStress = stressD + slope * (givenStrain-strainD)
elif(givenStrain > strainE):
    outputStress = "Fractured"
else:
    outputStress = "Invalid input, please try again."

# Print Young's Modulus
slope = (stressA-stressO)/(strainA-strainO)
print(f"Young's Modulus is {slope.__round__()}")

# Prints the answer
print(f"The stress at the strain {givenStrain} is: {outputStress} ksi")
