# Kyle Mrosko
# ENGR 102-212
# Lab 10b Assignment 1
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

import matplotlib.pyplot as plt
import numpy as np

Xnums = []
Ynums = []
mat = np.array([1.00583,-.087156,.087156,1.00583]).reshape(2,2)
point = np.array([1,0]).reshape(2,1)
for i in range(250):
    point = mat @ point
    Xnums.append(point[0])
    Ynums.append(point[1])

print(Xnums)
plt.plot(Xnums,Ynums)
plt.title("Spiral Trend Graph")
plt.xlabel("X Value")
plt.ylabel("Y Value")
plt.show()