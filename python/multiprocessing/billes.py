"""
    
    4IRC
    Exercice billes
    Groupe :
        - Maxime BATTU
        - Eileen BALAGUER
        - Batiste LALOI

"""
import multiprocessing as mp
import time

V = mp.Lock()
N = int(input("Nombre de processus : "))
M = int(input("Nombre d'itérations : "))
B = int(input("Nombre max de billes : "))
D = B
tabRessource = []
tabProcess = []

def Controleur():
    global D
    global B
    ## Mon contrôleur vérifie toutes les secondes si mon
    ## nombre de billes disponible est supérieur à 0 et inférieur
    ## au nombre de billes max autorisées
    while True:
        with V:
            if (D < 0 or D > B):
                print("ERROR !")
                exit()
        time.spleep(1)
     

def Demander(k_bills, j):
    global D
    print("Process n°",j," demande. Ressources dispo : ", D)
    ## Tant que je n'ai pas assez de ressources en stock, j'attends 1 seconde
    ## avant de les redemander
    while (D < k_bills):
        with V:
            print("Process n°",j," en attente de ressources")
            time.sleep(1)
    ## Quand je les obtiens, je déduis de mon stock le nombre de ressources nécessaires
    with V:
        D -= k_bills
    print("Process n°",j," a reçu. Ressources dispo : ", D)

def Rendre(k_bills, j):
    global D
    ## Dès que personne ne touche au stock, je rajoute au stock le nombre
    ## de ressources prises
    print("Process n°",j," rends. Ressources dispo : ", D)
    with V:
        D += k_bills
    print("Process n°",j," a rendu. Ressources dispo : ", D)

def Travailleur(j):
    global tabRessource
    global M
    ## Pour un nombre d'itération, je demande mes ressources, je les utilise
    ## pendant 2 secondes puis je les rends
    for i in range (0, M):
        Demander(tabRessource[j], j)
        print("Process n°",j, " utilise ses ressources")
        time.sleep(2)
        Rendre(tabRessource[j], j)

if __name__ == '__main__':
    ## Je demande à mon utiliseur de saisir le nombre de ressources requis
    ## Pour chaque joueur comprise entre 0 et le max de billes
    for i in range (0, N):
        tmp = int(input("Ressources requises : "))
        while (tmp < 0 or tmp > B):
            tmp = int(input("Merci de choisir un nombre de ressource requis supérieur à 0 et inférieur au nombre de billes max : "))
        tabRessource.append(tmp)
    ## Pour chaque joueur je créé un nouveau processus dans lequel il agira
    ## qui renvoit vers ma fonction Travailleur avec pour argument le n°
    ## de processus
    for i in range (0, N):
        tabProcess.append(mp.Process(target=Travailleur, args=(i,)))
        tabProcess[i].start()
    ## Je join tous mes processus pour les terminer
    for i in range (0, N):
        tabProcess[i].join()
