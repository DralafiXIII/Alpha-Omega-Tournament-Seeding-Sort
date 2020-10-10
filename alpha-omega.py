# Alpha-Omega Sorting for Tournament Seeding
# Did it in python first for proof of concept, but will convert to JS/C# later for experience

import math

seeds = []
for i in range(64):
    seeds.append([i + 1,""])

def keyGet(seeds):
    return seeds[0]

seedsSorted = sorted(seeds, key=keyGet)

twoN = 0
for i in range(1, len(seedsSorted)):
    temp = 2**i
    if temp >= len(seedsSorted):
        twoN = temp
        break

for i in range(twoN - len(seedsSorted)):
    seedsSorted.append([seedsSorted[len(seedsSorted) - 1][0] + 1, "BYE"])

print(seedsSorted)

for i in range(math.ceil(math.log(len(seedsSorted)))): # <-- this is where the problem is
    temp = []
    for j in range(0,int(len(seedsSorted) / 2),2**i):
        for k in range(2**i):
            temp.append(seedsSorted[j + k])
            print(temp)
        for k in range(2**i,0,-1):
            temp.append(seedsSorted[len(seedsSorted) - (j + k)])
            print(temp)
    seedsSorted = temp

"""

"""