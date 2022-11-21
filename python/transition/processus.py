import os
import random

liste = [random.randint(0, 100) for i in range(10)]
print(liste, sum(liste))

def sommeImpairs():
    somme = 0
    for i in range(1, len(liste), 2):
        somme += liste[i]
    return somme

def sommePairs():
    somme = 0
    for i in range(0, len(liste), 2):
        somme += liste[i]
    return somme

def main():
    tube = os.pipe()
    pid = os.fork()

    if pid == 0:
        # Processus fils
        os.close(tube[0])
        # On écrit dans le tube la somme des éléments pairs
        os.write(tube[1], str(sommeImpairs()).encode())
        os.close(tube[1])
    else:
        # Processus "sous père"
        pid = os.fork()
        if pid == 0:
            # Processus fils
            os.close(tube[0])
            # On écrit la somme des pairs dans le tube
            os.write(tube[1], str(sommePairs()).encode())
            os.close(tube[1])
        else:
            # Processus père
            os.close(tube[1])
            somme = 0
            # Récupération des résultats
            for _ in range(2):
                somme += int(os.read(tube[0], 100).decode())
            print(somme)
            os.close(tube[0])
    
if __name__ == "__main__":
    main()