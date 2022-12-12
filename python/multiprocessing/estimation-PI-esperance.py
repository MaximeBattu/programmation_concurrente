import time
import multiprocessing as mp
import math
import random

NB_PROCESS = 4

def loiEsperance(array, queue):
    """
        Méthode prenant un tableau de valeur et une Queue
        Elle permet de calculer la moyenne d'une aire d'un cercle par la méthode d'espérance
    """
    somme = 0

    formule = "math.sqrt(1 - math.pow(x, 2))"

    for nombre in array:
        f = formule.replace("x", str(nombre))
        somme += eval(f)
    
    queue.put(somme)


def estimePI(pi, nbIterations):
    """
        Permet d'estimer PI
    """
    return pi / nbIterations


if __name__ == "__main__":
    queue = mp.Queue()

    # Nombre d’essai pour l’estimation
    nbIterations = 1_000_000
        
    start = time.time()

    # Tableau de processus
    processes = []

    tableau = [random.random() for _ in range(nbIterations)]
    
    # Création du multiprocessing
    for i in range(NB_PROCESS):
        process = mp.Process(target=loiEsperance, args=(tableau, queue,))
        processes.append(process)
        process.start()

    pi = 0
    for process in processes:
        process.join()
        pi += estimePI(queue.get(), nbIterations)

    print(
        f"Valeur estimée Pi par la méthode d'espérance avec {NB_PROCESS} processus : {pi}")
    
    end = time.time()

    temps = end - start

    print(
        f"Temps de traitement {temps:.2f} secondes pour {nbIterations} iterations en multiprocess")
