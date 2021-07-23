# Kyle Mrosko
# Lab6b_Prog2
# An Aggie does not lie, cheat or steal or tolerate those who do

from math import *

print("This program will calculate some vector mathematics")

times = int(input("Please enter the amount of elements in the vector: "))

v1 = []
v2 = []

# stores vectors 1 and 2 as lists
for i in range(times):
    v1.append(float(input("Enter the next value for the first vector: ")))
for i in range(times):
    v2.append(float(input("Enter the next value for the second vector: ")))

sumv1 = 0
sumv2 = 0
dotSum = 0
v1Plusv2 = []
v1Minusv2 = []

# traverse through vectors to prefrom operations
for i in range(times):
    sumv1 += v1[i]**2 # adds to squared sum of v1
    sumv2 += v2[i] ** 2 # adds to squared sum of v2
    dotSum += v1[i] * v2[i] # adds product of v1 and v2
    v1Plusv2.append(v1[i] + v2[i]) # adds each element in v1 and v2
    v1Minusv2.append(v1[i] - v2[i]) # subtracts each element in v1 and v2

# taking sqrt to calc the magnitudes
magv1 = sqrt(sumv1)
magv2 = sqrt(sumv2)


# printing outputs
print(f"The magnitude of vector 1 is {magv1}.")
print(f"The magnitude of vector 2 is {magv2}.")
print(f"Vector 1 plus vector 2 is {v1Plusv2}.")
print(f"Vector 1 minus vector 2 is {v1Minusv2}.")
print(f"The dot product of vector 1 and vector 2 is {dotSum}.")




