import os
import sys

f1 = input("Unesite ime prve datoteke: ")
f2 = input("Unesite ime druge datoteke: ")

def average(f): 

    fo = open(os.path.join(sys.path[0], f), "r")
    brojac = 0
    total = 0

    for line in fo:
        if line.startswith("X-DSPAM-Confidence:"):
            brojac += 1

            novi_string = line.partition("X-DSPAM-Confidence: ")[2]

            total += float(novi_string.rstrip())
            
    print("Ime datoteke:", f)
    print("Average X-DSPAM-Confidence:", (total/brojac))

average(f1)
average(f2)