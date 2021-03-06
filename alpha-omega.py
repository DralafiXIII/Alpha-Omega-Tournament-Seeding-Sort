# Alpha-Omega Sorting for Tournament Seeding
# Did it in python first for proof of concept, but will convert to JS/C# later for experience

# Creates a list of teams

numSeeds = 1000 # number of initial seeds

seeds = []
for i in range(numSeeds):
    seeds.append([i + 1,""])

# Sorts list of teams. Necessary when the list is generated manually.
def keyGet(seeds):
    return seeds[0]

seedsSorted = sorted(seeds, key=keyGet)

# Generates byes
twoN = 0
twoN2 = 0
for i in range(1, len(seedsSorted)):
    temp = 2**i
    if temp >= len(seedsSorted):
        twoN = temp
        twoN2 = i
        break

twoN3 = twoN - len(seedsSorted)
for i in range(twoN3):
    seedsSorted.append([seedsSorted[len(seedsSorted) - 1][0] + 1, "BYE"])

# Prints list before alpha-omega sorting. Demonstrates that the list has been properly sorted and that byes have been properly generated.
print(seedsSorted)

# Alpha-omega sorting algorithm
for i in range(twoN2):
    temp = []
    for j in range(0,int(len(seedsSorted) / 2),2**i):
        for k in range(2**i):
            temp.append(seedsSorted[j + k])
        for k in range(2**i,0,-1):
            temp.append(seedsSorted[len(seedsSorted) - (j + k)])
    seedsSorted = temp

"""
# D13 sorting algorithm
# This portion moves all the byes ensuring that the higher ranked seeds face off against those byes (ideal no matter how you seed).
if twoN3 > 0:
    temp = seedsSorted[0:int(len(seedsSorted) / 2)]
    temp.extend(seedsSorted[len(seedsSorted) - twoN3:len(seedsSorted)])
    temp.extend(seedsSorted[int(len(seedsSorted) / 2):len(seedsSorted) - twoN3])
    seedsSorted = temp

# Actual sorting algorithm
for i in range(twoN2):
    temp = []
    for j in range(0,int(len(seedsSorted) / 2),2**i):
        for k in range(2**i):
            temp.append(seedsSorted[j + k])
        for k in range(2**i):
            temp.append(seedsSorted[int(len(seedsSorted) / 2) + j + k])
    seedsSorted = temp
"""

# Prints list after alpha-omega sorting. Data is now ready to be brought to the front-end for use.
print("\n",seedsSorted)
input()

# The following simulates the tournament assuming that the higher seeds always move forward. If the algorithm worked properly, the finals should always end up with the two highest seeds listed.
while len(seedsSorted) >= 4:
    temp = []
    for i in range(int(len(seedsSorted)/2)):
        temp.append(seedsSorted[i*2])
    seedsSorted = temp
    print("\n",seedsSorted)
    input()