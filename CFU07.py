# An Aggie does not lie, cheat or steal or tolerate those who do

print("This program calculates the number of true and false outputs for various boolean expressions")

# Accepts user input and assigns true/false accordingly
A = input("Please input a Boolean value for A: ")
if A == "True":
    A = True
else:
    A = False

B = input("Please input a Boolean value for B: ")
if B == "True":
    B = True
else:
    B = False

C = input("Please input a Boolean value for C: ")
if C == "True":
    C = True
else:
    C = False

# Additional variables needed
trueCount = 0
falseCount = 0


# If statement to check each boolean expression, only adds to trueCount is expression is true, else adds to falseCount
if (A and B) and C:
    trueCount += 1
else:
    falseCount += 1

if (A and B) or C:
    trueCount += 1
else:
    falseCount += 1

if (A or B) and C:
    trueCount += 1
else:
    falseCount += 1

if (A or B) or C:
    trueCount += 1
else:
    falseCount += 1

if A and (B and C):
    trueCount += 1
else:
    falseCount += 1

if A and (B or C):
    trueCount += 1
else:
    falseCount += 1

if A or (B and C):
    trueCount += 1
else:
    falseCount += 1

if A or (B or C):
    trueCount += 1
else:
    falseCount += 1


# Print output
print("")
print(f"For A={A}, B={B}, C={C} the number of Trues is {trueCount} and the number of Falses is {falseCount}.")