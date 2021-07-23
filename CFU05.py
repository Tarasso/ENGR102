# An aggie does not lie, cheat or steal, nor tolerate those who do.

#what this program does
print("Lets play FizzBuzz!")

#sets the upper limit
upper = int(input("Please enter an upper limit: "))

#loops through each number checking divisibility
for i in range(1,upper+1):
    if(i%3==0 and i%5==0):
        print("FizzBuzz",end=" ")
    elif(i%3==0):
        print("Fizz",end=" ")
    elif(i%5==0):
        print("Buzz",end=" ")
    else:
        print(i,end=" ")