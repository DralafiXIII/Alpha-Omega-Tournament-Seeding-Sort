# Alpha-Omega Sorting for Tournament Seeding
# Did it in python first for proof of concept, but will convert to JS/C# later for experience

seeds = [
    [4, "Team2"],
    [3, "Team Liquid"],
    [2, "Astralis"],
    [34, "Dingle"],
    [1, "Patriots"],
    [17, "Reds"]
]

def keyGet(seeds):
    return seeds[0]

seedsSorted = sorted(seeds, key=keyGet)

twoN = 0
for i in range(1, len(seedsSorted)):
    temp = 2**i
    if temp >= len(seedsSorted):
        twoN = temp
        break

print(seedsSorted[len(seedsSorted) - 1])

for i in range(0,twoN - len(seedsSorted)):
    seedsSorted.append([seedsSorted[len(seedsSorted) - 1][0] + i, "BYE"])

print(seedsSorted)