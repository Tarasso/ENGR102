# Kyle Mrosko
# 10/23/2019
# ENGR 102-212 - Lab 9b Act 1
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

openFile = open("Celsius.txt",'r')
outFile = open("Fahrenheit.txt",'w')

for line in openFile:
    num = float(line)
    num = num*9/5+32
    num = str(num)+"\n"
    outFile.write(num)