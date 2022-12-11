"""
    
    4IRC
    Exercice course hippique
    Groupe :
        - Maxime BATTU
        - Eileen BALAGUER
        - Batiste LALOI

"""

import time
import multiprocessing as mp

NB_PROCESS = 4

def arc_tangente(nbIteration, queue):
    """
        calculer le nbr de hits dans un cercle unitaire (utilisé par les différentes méthodes)
    """
    pi = 0
    for i in range(int(nbIteration)):
        pi += 4/(1+ ((i+0.5)/nbIteration)**2)

    queue.put(pi)


def estimePI(piArcTan, nbIterations):
    """
        Permet d'estimer PI
    """
    return (1/nbIterations) * float(piArcTan)


def multiprocess(nbIterations, queue):
    """
        Méthode Monte Carlo en multi-processus
    """
    processes = []

    # On divise le nombre d'itération par le nombre de processus
    iterationsParProcess = [nbIterations/NB_PROCESS for i in range(NB_PROCESS)]


    # Création du multiprocessing
    for i in range(NB_PROCESS):
        process = mp.Process(target=arc_tangente, args=(iterationsParProcess[i], queue,))
        processes.append(process)
        process.start()

    pi = 0
    for process in processes:
        process.join()
        pi += estimePI(queue.get(), nbIterations)

    print(
        f"Valeur estimée Pi par la méthode arc-tangente avec {NB_PROCESS} processus : {pi}")

if __name__ == "__main__":
    queue = mp.Queue()

    # Nombre d’essai pour l’estimation
    nbIterations = 100_000_000
    
    start = time.time()

    multiprocess(nbIterations, queue)    
    
    end = time.time()

    temps = end - start

    print(
        f"Temps de traitement {temps:.2f} secondes pour {nbIterations} iterations en multiprocess")