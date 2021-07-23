# Name:         Kyle Mrosko
# Section:      212
# Assignment:   Lab 4b_Prog3
# An Aggie does not lie, cheat or steal, or tolerate those who do.

print("This program calculates the number of widgets produced by a machine given the days it has been working.")

days = int(input("Enter the amount of days the machine has been running (1-100): "))

if(days<1 or days>100):
    print("Please rerun the program and enter a valid number.")
    exit()

widgets = 0

for i in range(1, days+1):
    if(i<11):
        widgets += 10
    elif(i<61):
        widgets += 40
    elif(i<100):
        widgets += 40-(i-60)
    else:
        widgets += 0

print("A machine running for",days,"days produces",widgets,"widgets")



