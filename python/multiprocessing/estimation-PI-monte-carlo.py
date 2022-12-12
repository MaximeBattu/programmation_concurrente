"""
    
    4IRC
    Exercice course hippique
    Groupe :
        - Maxime BATTU
        - Eileen BALAGUER
        - Batiste LALOI

"""

import random
import time
import multiprocessing as mp
from multiprocessing import Pool

NB_PROCESS = 4

def calculMonteCarlo(nbIteration, queue = []):
    """
        calculer le nbr de hits dans un cercle unitaire (utilisé par les différentes méthodes)
    """
    count = 0
    for i in range(int(nbIteration)):
        x = random.random()
        y = random.random()
        # si le point est dans l’unit circle
        if x * x + y * y <= 1:
            count += 1
    if queue :
        queue.put(count)
    else :
        return count


def estimePI(count, nbIterations):
    """
        Permet d'estimer PI
    """
    return (4 * count) / nbIterations


def multiprocess(nbIterations, queue):
    """
        Méthode Monte Carlo en multi-processus
    """
    # Tableau de processus
    processes = []
    # On divise le nombre d'itération par le nombre de processus
    iterationsParProcess = [nbIterations/NB_PROCESS for i in range(NB_PROCESS)]

    # Création du multiprocessing
    for i in range(NB_PROCESS):
        process = mp.Process(target=calculMonteCarlo, args=(iterationsParProcess[i], queue,))
        processes.append(process)
        process.start()

    pi = 0
    for process in processes:
        process.join()
        pi += estimePI(queue.get(), nbIterations)

    print(
        f"Valeur estimée Pi par la méthode Hit-Miss avec {NB_PROCESS} processus : {pi}")


def monoprocess(nbIterations):
    """
        Méthode Monte Carlo en mono-processus
    """
    nbHits = calculMonteCarlo(nbIterations)
    pi = estimePI(nbHits, nbIterations)

    print(f"Valeur estimée Pi par la méthode Hit-Miss en mono-processus : {pi}")


if __name__ == "__main__":
    queue = mp.Queue()

    # Nombre d’essai pour l’estimation
    nbIterations = 100_000_000
    
    print("Début du multiprocessing")
    start = time.time()

    multiprocess(nbIterations, queue)

    end = time.time()
    temps = end - start

    print(
        f"Temps de traitement {temps:.2f} secondes pour {nbIterations} iterations en monoprocessus")
    print("Fin du multiprocessing\n")

    print("Début du monoprocessus")
    start = time.time()

    monoprocess(nbIterations)

    end = time.time()
    temps = end - start

    print(
        f"Temps de traitement {temps:.2f} secondes pour {nbIterations} iterations en multiprocess")
    print("Fin du monoprocessus")

