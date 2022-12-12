
nb = int(input("Nombre d'étages : "))

for i in range(nb):
    for j in range(1, i+1):
        print(j, end="")
    print("")