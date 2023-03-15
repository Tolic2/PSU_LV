list = []
suma = 0
while True:
    try:
        x = input("Unesite broj ,ako zelite prekinuti petlju upisite rijec Done: ")

        if (x == 'Done'):
            break
    
        list.append(int(x))
        suma += int(x)
    except:
        print("Niste unjeli broj")  


print("Korisnik je unio:", len(list), "brojeva")
print("Minimalna vrijednost je:", min(list))
print("Srednja vrijednost je:", (suma / len(list)))
print("Maksimalna vrijednost je:", max(list))
list.sort()

print("Sortirana lista: ")
for y in list:
    print(int(y))