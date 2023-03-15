while True:
    try:
        x = float(input("Unesite broj iz intevala [0.0, 1.0]: "))

        if (x >= 0.0 and x <= 1.0):
            break
        else: 
            print("Unjeli ste broj koji nije u zadanom intervalu [0.0, 1.0]")
    except:
        print("Niste unjeli broj")

if x >= 0.9:
    print("A", x)

elif x >= 0.8:
    print("B", x)

elif x >= 0.7:
    print("C", x)

elif x >= 0.6:
    print("D", x)

else:
    print("F", x)