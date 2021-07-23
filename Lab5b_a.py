# Kyle Mrosko
# Lab5b_a
# An aggie does not lie, cheat or steal, nor tolerate those who do.

print("This program will calculate the Collatz conjecture for a given number.")

#gets input
n = int(input("Please input a positive, whole number: "))


count = 0

#loops to create sequence
while n >= 1:
    count += 1
    print(n,end=" ")
    if n == 1:
        break
    if n % 2 == 1:
        n = n*3+1
    else:
        n = n // 2

print("")
print(f"It took {count} iterations!")