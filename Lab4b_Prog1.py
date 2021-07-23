# Name:         Kyle Mrosko
# Section:      212
# Assignment:   Lab 4b_Prog1
# An Aggie does not lie, cheat or steal, or tolerate those who do.

print("Input 3 numbers and this program will return the largest number.")

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))

if(num1>num2 and num1>num3):
    print(num1,"is the largest number.")
elif(num2>num1 and num2>num3):
    print(num2, "is the largest number.")
else:
    print(num3, "is the largest number.")
