# An Aggie does not lie, chat or steal or tolerate those who do.

ranking = []
newRanking = []

for i in range(5):
    print(f"Enter you number {i+1} pop music star of the 2000s-2010s: ",end="")
    answer = input()
    ranking.append(answer)

if not("Jonas Brothers" in ranking):
    newRanking.append("Jonas Brothers")
    newRanking += ranking[:len(ranking)-1]
else:
    newRanking = ranking

print("Ok, so you like", newRanking)
