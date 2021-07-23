# An aggie does not lie, cheat, or steal, nor tolerate those who do.

openFile = open("Temperature.dat",'r')
outFile = open("WeeklyAverages.dat",'w')

count = 1
sum = 0
avg = 0


for line in openFile:
    num = float(line)
    sum += num
    avg = sum / count
    count += 1
    if(count==8):
        outFile.write(str(avg)+"\n")
        sum = 0
        count = 1
