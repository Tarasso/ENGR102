# Kyle Mrosko
# 10/23/2019
# ENGR 102-212 - Lab 9b Act 2
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Get user input
loanAmount = float(input("Amount of the loan: "))
annualInterestRate = float(input("Annual Interest Rate Decimal:"))
monthlyPayment = float(input("Amount paid monthly: "))
outLocation = input("Output file name: ")
outLocation += ".csv"
outFile = open(outLocation,'w')

# Extra variables needed
monthlyInterest = annualInterestRate/12
interestAccrued = 0
month = 1
outFile.write("month,total interest,loan balance\n")
outFile.write("0,0,"+str(loanAmount)+"\n")

interestAccrued = 0
while loanAmount > 0:
    if month == 31:
        break
    outFile.write(str(month) + ",")
    interestAccrued += monthlyInterest*(loanAmount-monthlyPayment)
    loanAmount += monthlyInterest*(loanAmount-monthlyPayment)
    outFile.write(str(interestAccrued)+",")
    if(monthlyPayment > loanAmount):
        monthlyPayment = loanAmount
    loanAmount -= monthlyPayment
    outFile.write(str(loanAmount)+"\n")
    month += 1
