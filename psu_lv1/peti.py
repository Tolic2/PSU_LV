import os
import sys

fo = open(os.path.join(sys.path[0], "song.txt"), "r")

rijeci = {}

for line in fo:
    r = line.split()

    for newline in r: 
    
        bez = newline.replace(",", "")
        
        if bez.lower() in rijeci:
            rijeci[bez.lower()] += 1
        else:
            rijeci[bez.lower()] = 1
print(rijeci)

print("Rijeci koje se samo jednom pojavljuju: ")
for x in rijeci:
    if(rijeci.get(x) == 1):
        print(x, end=", ")