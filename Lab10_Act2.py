# Braedon Lindsey, Lauren Corradino, Scottie Taylor, Kyle Mrosko
# ENGR 102-212
# Lab 10 Assignment 1
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

import matplotlib.pyplot as plt
import numpy as np
import math

# BRAEDON'S PLOTS
data = {"a": [math.sin(theta*math.pi/25) for theta in range(50)],
        "b": [math.cos(theta*math.pi/25) for theta in range(50)],
        "c": [1 * x ** 0.5 for x in range(50)],
        "d": np.random.randint(0, 100, 50)}

plt.scatter("a", "b", c="c", s="d", data=data)
plt.show()

plt.scatter([theta*math.sin(theta/10*math.pi) for theta in range(0, 50)],
            [theta * math.cos(theta/10*math.pi) for theta in range(0, 50)])
plt.show()


# SCOTTIE'S PLOTS
plt.plot([4.1,2,2,4,4,2,2,4.1,4.1,2.1,2.1,4.1,4.1],[4,4,3,3,2,2,1.9,1.9,3.1,3.1,3.9,3.9,4])
plt.show()

t=np.arange(0.,17.,.1)
plt.plot(t,(t-3)**2+2,'r--',t,-2*t+7,'b--')
plt.axis([0,5,0,17])
plt.show()


# LAUREN'S PLOTS
from math import e
t = np.arange(0., 5., 0.2)
plt.plot(t, t, "r--", t, t**2, "bs", t, t**e, "g^")
plt.show()

names = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
values = [50, 23, 100, 5, 10, 60]
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()


# KYLE'S PLOTS

a = np.random.randint(0, 100, 100)
b = np.arange(100)

a.sort()
plt.hist(b,a)
plt.xlabel("Number Value")
plt.ylabel("Number of Occurrences")
plt.title("Distribution of Random Numbers (0-100)")
plt.show()



labels = ["Dr.Cahill","Nadia","Kristin","Grace"]
percents = [20,60,10,10]
explode = (0,.1,0,0)

plt.pie(percents, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
plt.title("Breakdown of Student's Favorite Instructor")
plt.show()