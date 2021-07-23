# Lauren Corradino, Braedon Lindsey, Scottie Taylor, and Kyle Mrosko
# ENGR 102 - 212
# Lab 7
# An Aggie does not lie, cheat, or steal; nor tolerate those who do.

print("This program calculates the risk percent of a user based on several input conditions.")

# input and assignment for all required variables

sex = input("Enter your sex (M/F): ")

age = int(input("Enter your age: "))

smoker = input("Do you smoke (Y/N): ")
if smoker == "Y":  # determining a boolean value based on (Y/N) input
    smoker = True
else:
    smoker = False

bloodPressure = float(input("Enter your systolic blood pressure(the number on top): "))
bpTreated = input("Has your BP been treated? (Y/N): ")
if bpTreated == "Y":  # determining a boolean value based on (Y/N) input
    bpTreated = True
else:
    bpTreated = False

HDLCholesterol = float(input("Enter your HDL cholesterol: "))

totalCholesterol = float(input("Enter your total cholesterol: "))

riskPoints, riskPercent = 0, 0

# lists containing the percent values corresponding to certain point values

percentsMale =   ["<1", 1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 25, ">30"]
percentsFemale = ["<1", 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 11, 14, 17, 22, 27, ">30"]

agePointsMale =   [-9, -4, 0, 3, 6, 8, 10, 11, 12, 13]
agePointsFemale = [-7, -3, 0, 3, 6, 8, 10, 12, 14, 16]

smokerPointsMale =   [8, 5, 3, 1, 1]
smokerPointsFemale = [9, 7, 4, 2, 1]

HDLPointsMale =   [-1, 0, 1, 2]
HDLPointsFemale = [-1, 0, 1, 2]

# determining the category of a person's HDL cholesterol

if HDLCholesterol >= 60:
    HDLIndex = 0
elif HDLCholesterol >= 50:
    HDLIndex = 1
elif HDLCholesterol >= 40:
    HDLIndex = 2
else:
    HDLIndex = 3

# matrices representing the different amount of possible points for Systolic BP

systolicPointsMale = [
    [0, 0],
    [0, 1],
    [1, 2],
    [1, 2],
    [2, 3],
]
systolicPointsFemale = [
    [0, 0],
    [1, 3],
    [2, 4],
    [3, 5],
    [4, 6],
]

# determining the category of the person's BP

if bloodPressure <120:
    systolicIndex = 0
elif bloodPressure < 130:
    systolicIndex = 1
elif bloodPressure < 140:
    systolicIndex = 2
elif bloodPressure < 160:
    systolicIndex = 3
else:
    systolicIndex = 4

# matrices representing all the amounts of points that can be received for a person's cholesterol points

cholesterolPointsMale = [
    [0, 0, 0, 0, 0],
    [4, 3, 2, 1, 0],
    [7, 5, 3, 1, 0],
    [9, 6, 4, 2, 1],
    [11, 8, 5, 3, 1],
]
cholesterolPointsFemale = [
    [0, 0, 0, 0, 0],
    [4, 3, 2, 1, 1],
    [8, 6, 4, 2, 1],
    [11, 8, 5, 3, 2],
    [13, 10, 7, 4, 2],
]

# determining the category of a person's cholesterol

if totalCholesterol < 160:
    totalCholesterolIndex = 0
elif totalCholesterol < 200:
    totalCholesterolIndex = 1
elif totalCholesterol < 240:
    totalCholesterolIndex = 2
elif totalCholesterol < 280:
    totalCholesterolIndex = 3
else:
    totalCholesterolIndex = 4


# main loop, separated into 'M' and 'F' if statements
# subdivided into age categories to add the corresponding points

if sex == "M":
    if age < 35:
        riskPoints += agePointsMale[0]  # adding points based on a person's age category
        riskPoints += cholesterolPointsMale[totalCholesterolIndex][0]  # adding points based on a person's cholesterol category and age category
        if smoker:
            riskPoints += smokerPointsMale[0] # adding points based on a person's smoker status and age category
    elif age < 40:
        riskPoints += agePointsMale[1]
        riskPoints += cholesterolPointsMale[totalCholesterolIndex][0]
        if smoker:
            riskPoints += smokerPointsMale[0]
    elif age < 45:
        riskPoints += agePointsMale[2]
        riskPoints += cholesterolPointsMale[totalCholesterolIndex][1]
        if smoker:
            riskPoints += smokerPointsMale[1]
    elif age < 50:
        riskPoints += agePointsMale[3]
        riskPoints += cholesterolPointsMale[totalCholesterolIndex][1]
        if smoker:
            riskPoints += smokerPointsMale[1]
    elif age < 55:
        riskPoints += agePointsMale[4]
        riskPoints += cholesterolPointsMale[totalCholesterolIndex][2]
        if smoker:
            riskPoints += smokerPointsMale[2]
    elif age < 60:
        riskPoints += agePointsMale[5]
        riskPoints += cholesterolPointsMale[totalCholesterolIndex][2]
        if smoker:
            riskPoints += smokerPointsMale[2]
    elif age < 65:
        riskPoints += agePointsMale[6]
        riskPoints += cholesterolPointsMale[totalCholesterolIndex][3]
        if smoker:
            riskPoints += smokerPointsMale[3]
    elif age < 70:
        riskPoints += agePointsMale[7]
        riskPoints += cholesterolPointsMale[totalCholesterolIndex][3]
        if smoker:
            riskPoints += smokerPointsMale[3]
    elif age < 75:
        riskPoints += agePointsMale[8]
        riskPoints += cholesterolPointsMale[totalCholesterolIndex][4]
        if smoker:
            riskPoints += smokerPointsMale[4]
    else:
        riskPoints += agePointsMale[9]
        riskPoints += cholesterolPointsMale[totalCholesterolIndex][4]
        if smoker:
            riskPoints += smokerPointsMale[4]

    riskPoints += HDLPointsMale[HDLIndex]  # adding points based on HDL category

    if bpTreated:  # adding points based on treatment status and BP category
        riskPoints += systolicPointsMale[systolicIndex][1]
    else:
        riskPoints += systolicPointsMale[systolicIndex][0]

    for i in range(-1,18):  # determining the percent based on the points
        if riskPoints == i:
            riskPercent = percentsMale[i+1]
    if riskPoints < 0:  # handling exception cases
        riskPercent = percentsMale[0]
    if riskPoints >= 17:  # handling exception cases
        riskPercent = percentsMale[-1]

elif sex == "F":
    if age < 35:
        riskPoints += agePointsFemale[0]  # adding points based on a person's age category
        riskPoints += cholesterolPointsFemale[totalCholesterolIndex][0]  # adding points based on a person's cholesterol category and age category
        if smoker:
            riskPoints += smokerPointsFemale[0]  # adding points based on a person's smoker status and age category
    elif age < 40:
        riskPoints += agePointsFemale[1]
        riskPoints += cholesterolPointsFemale[totalCholesterolIndex][0]
        if smoker:
            riskPoints += smokerPointsFemale[0]
    elif age < 45:
        riskPoints += agePointsFemale[2]
        riskPoints += cholesterolPointsFemale[totalCholesterolIndex][1]
        if smoker:
            riskPoints += smokerPointsFemale[1]
    elif age < 50:
        riskPoints += agePointsFemale[3]
        riskPoints += cholesterolPointsFemale[totalCholesterolIndex][1]
        if smoker:
            riskPoints += smokerPointsFemale[1]
    elif age < 55:
        riskPoints += agePointsFemale[4]
        riskPoints += cholesterolPointsFemale[totalCholesterolIndex][2]
        if smoker:
            riskPoints += smokerPointsFemale[2]
    elif age < 60:
        riskPoints += agePointsFemale[5]
        riskPoints += cholesterolPointsFemale[totalCholesterolIndex][2]
        if smoker:
            riskPoints += smokerPointsFemale[2]
    elif age < 65:
        riskPoints += agePointsFemale[6]
        riskPoints += cholesterolPointsFemale[totalCholesterolIndex][3]
        if smoker:
            riskPoints += smokerPointsFemale[3]
    elif age < 70:
        riskPoints += agePointsFemale[7]
        riskPoints += cholesterolPointsFemale[totalCholesterolIndex][3]
        if smoker:
            riskPoints += smokerPointsFemale[3]
    elif age < 75:
        riskPoints += agePointsFemale[8]
        riskPoints += cholesterolPointsFemale[totalCholesterolIndex][4]
        if smoker:
            riskPoints += smokerPointsFemale[4]
    else:
        riskPoints += agePointsFemale[9]
        riskPoints += cholesterolPointsFemale[totalCholesterolIndex][4]
        if smoker:
            riskPoints += smokerPointsFemale[4]

    riskPoints += HDLPointsFemale[HDLIndex]  # adding points based on HDL category

    if bpTreated:  # adding points based on treatment status and BP category
        riskPoints += systolicPointsFemale[systolicIndex][1]
    else:
        riskPoints += systolicPointsFemale[systolicIndex][0]

    for i in range(8, 25):  # determining the percent based on the points
        if riskPoints >= i:
            riskPercent = percentsFemale[i-8]
    if riskPoints < 9:  # handling exception cases
        riskPercent = percentsFemale[0]
    if riskPoints >= 25:  # handling exception cases
        riskPercent = percentsFemale[-1]

print(f"Your risk percentage is {riskPercent}% and your risk point total is {riskPoints}.")