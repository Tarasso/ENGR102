# Kyle Mrosko
# Lab5b_b
# An aggie does not lie, cheat or steal, nor tolerate those who do.

print("This program will calculate the sum of numbers 0 to an entered number")

num = int(input("Please enter a whole, postive number: "))
sum = 0
product = 1

for i in range(num):
    sum += i+1
    product *= i+1

print(f"Using a for loop, the sum of of numbers 0-{num} is {sum} and the product is {product}")

sum = 0
product = 1
i = num

while i>0:
    sum += i
    product *= i
    i-=1

print(f"Using a while loop, the sum of of numbers 0-{num} is {sum} and the product is {product}")
