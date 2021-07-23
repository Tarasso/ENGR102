# Braedon Lindsey, Lauren Corradino, Scottie Taylor, Kyle Mrosko
# ENGR 102 - 212
# Lab4_Act3
# An aggie does not lie, cheat or steal, nor tolerate those who do.

# Part A:

userInput = input("Enter a boolean value (True, T, t, or False, F, f): ")

if userInput in ["True", "T", "t"]:
    userBool = True
elif userInput in ["False", "F", "f"]:
    userBool = False
else:
    print("You fool! Enter a valid boolean!")

# Part B:

a = input("Enter a boolean value for a (True, T, t, or False, F, f): ")
b = input("Enter a boolean value for b (True, T, t, or False, F, f): ")
c = input("Enter a boolean value for c (True, T, t, or False, F, f): ")


if a in ["True", "T", "t"]:
    a = True
elif a in ["False", "F", "f"]:
    a = False
else:
    print("Enter a valid boolean, you buffoon!")

if b in ["True", "T", "t"]:
    b = True
elif b in ["False", "F", "f"]:
    b = False
else:
    print("Enter a valid boolean, you buffoon!")

if c in ["True", "T", "t"]:
    c = True
elif c in ["False", "F", "f"]:
    c = False
else:
    print("Enter a valid boolean, you buffoon!")

print("a and b and c =", a and b and c)
print("a or b or c =", a or b or c)

# Part C:

a = True
b = False

if (a != b):
    print("True: a is exclusive of b")
else:
  print("False: a is not exclusive of b")

a = True
b = False
c = False

trueCount = 0
if a == True:
    trueCount += 1
if b == True:
    trueCount += 1
if c == True:
    trueCount += 1

if trueCount in [1, 3]:
    print("True: An odd number of 'Trues' exist")
else:
    print("False: Either 0 or an even number of 'Trues' exist")