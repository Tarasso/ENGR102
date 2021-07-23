# Kyle Mrosko
# Lab5b_b
# An aggie does not lie, cheat or steal, nor tolerate those who do.

from math import *

print("This program finds the prime numbers between 2 and 100")

count = 0

#goes through each number
for num in range(2, 101):
    check = ceil(sqrt(num))
    isPrime = True
    while(check>=2):
        if(num%check==0): #if it is divisible by a given number, it is not prime
            isPrime = False
            break
        check -= 1
    if(num<=2):
        isPrime = True
    if isPrime:
        print(f"{num} is prime")
        count += 1
    else:
        print(f"{num} is not prime")

print(f"There are {count} number of primes between 2 and 100")

