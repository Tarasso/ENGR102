# Name:         Bryson Mrosko
# Section:      212
# Assignment:   Lab 1b-2

import math

print("This shows the evaluation of sin(x)/x evaluated close to x=0")
print("My guess is 1")
print(math.sin(1)/1)
print(math.sin(.1)/.1)
print(math.sin(.01)/.01)
print(math.sin(.001)/.001)
print(math.sin(.0001)/.0001)
print(math.sin(.00001)/.00001)
print(math.sin(.000001)/.000001)
print(math.sin(.0000001)/.0000001)

print('\n')

print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")
print("My guess is 0.5")
print((1-math.cos(1))/(1)**2)
print((1-math.cos(.1))/(.1)**2)
print((1-math.cos(.01))/(.01)**2)
print((1-math.cos(.001))/(.001)**2)
print((1-math.cos(.0001))/(.0001)**2)
print((1-math.cos(.00001))/(.00001)**2)
print((1-math.cos(.000001))/(.000001)**2)
print((1-math.cos(.0000001))/(.0000001)**2)

print("\n")

print("This shows the evaluation of (1+(1/x))^x evaluated close to infinity")
print("My guess is 1")
print((1+(1/1))**1)
print((1+(1/10))**10)
print((1+(1/100))**100)
print((1+(1/1000))**1000)
print((1+(1/10000))**10000)
print((1+(1/100000))**100000)
print((1+(1/1000000))**1000000)
print((1+(1/10000000))**10000000)