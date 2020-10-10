# Alpha-Omega Sorting for Tournament Seeding
# Did it in python first for proof of concept, but will convert to JS/C# later for experience

import math

# Creates a list of teams

numSeeds = 30 # number of initial seeds

seeds = []
for i in range(numSeeds):
    seeds.append([i + 1,""])

# Sorts list of teams. Necessary when the list is generated manually.
def keyGet(seeds):
    return seeds[0]

seedsSorted = sorted(seeds, key=keyGet)

# Generates byes
twoN = 0
for i in range(1, len(seedsSorted)):
    temp = 2**i
    if temp >= len(seedsSorted):
        twoN = temp
        break

for i in range(twoN - len(seedsSorted)):
    seedsSorted.append([seedsSorted[len(seedsSorted) - 1][0] + 1, "BYE"])

# Prints list before alpha-omega sorting. Demonstrates that the list has been properly sorted and that byes have been properly generated.
print(seedsSorted)

# Alpha-omega sorting algorithm
for i in range(math.ceil(math.log(len(seedsSorted)))):
    temp = []
    for j in range(0,int(len(seedsSorted) / 2),2**i):
        for k in range(2**i):
            temp.append(seedsSorted[j + k])
        for k in range(2**i,0,-1):
            temp.append(seedsSorted[len(seedsSorted) - (j + k)])
    seedsSorted = temp

# Prints list after alpha-omega sorting. Data is now ready to be brought to the front-end for use.
print(seedsSorted)

"""

"""