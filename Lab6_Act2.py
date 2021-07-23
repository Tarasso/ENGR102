# Braedon Lindsey, Kyle Mrosko, Lauren Corradino, and Scottie Taylor
# Lab6_Act2.py
# An Aggie does not lie, cheat or steal or tolerate those who do

dictionary = {}
allScores = []
sortedScores = []

print("Given a list of names and scores, this program will calculate the players who did and did not make the cut for the next round.")

print("Input your information as follows. When you are finished, enter a negative number for the first round score")

# runs until a negative number is entered
while True:
    score1 = int(input("First round score: "))
    if score1 <= 0:
        break
    # Storing user entered data
    score2 = int(input("Second round score: "))
    name = input("Name: ")
    dictionary[name] = score1 + score2
    allScores += [score1 + score2] # combines scores
    print("")

# Finds the minimum score to append it to an ordered list
for i in range(len(allScores)):
    minimum = 99999999
    for j in allScores:
        if j < minimum:
            minimum = j
    sortedScores.append(minimum)
    allScores.remove(minimum)

# Determines if the list is even or odd, and finds the median accordingly
if len(sortedScores) % 2 == 0:
    median = (sortedScores[int(len(sortedScores) / 2 - 1)] + sortedScores[int(len(sortedScores) / 2)]) / 2
else:
    median = sortedScores[(len(sortedScores)-1) // 2]

# prints whether or not a person made the cut based on the median score
a = []
b = []
for x in dictionary:
    if dictionary[x] <= median:
        a.append(x)
    else:
        b.append(x)

print("\n"+"Those who made it:")
for x in a:
    print(f"{x} (score: {dictionary[x]})")

print("\n"+"Those who didn't make it:")
for x in b:
    print(f"{x} (score: {dictionary[x]})")