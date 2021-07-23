# Kyle Mrosko
# Lab6b_Prog1
# An Aggie does not lie, cheat or steal or tolerate those who do

print("Given a word or sentence, this program returns the translated word(s) into pig latin")

vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"]

while True:
    # runs until stop is entered
    line = input("Enter a word or sentence: ")
    if(line=="stop"):
        break
    words = line.split(" ") # breaks line into each word
    for word in words:
        if ('.' in word):
            word = word[:len(word)-1] # removes '.' from the sentence
        # changes word accordingly
        if(word[0] in vowels):
            print(word+"yay")
        else:
            print(word[1:]+word[0]+"ay")