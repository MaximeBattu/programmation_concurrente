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
        Calcule l'air d'un quart de cercle trigonométrique par la méthode arc-tangente.
    """
    pi = 0
    for i in range(int(nbIteration)):
        pi += 4/(1+ ((i+0.5)/nbIteration)**2)

    queue.put(pi)

if __name__ == "__main__":
    queue = mp.Queue()

    # Nombre d’essai pour l’estimation
    nbIterations = 100_000_000
    
    # Tableau de processes
    processes = []
    
    start = time.time()

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
        pi += (1/nbIterations) * float(queue.get())

    print(
        f"Valeur estimée Pi par la méthode arc-tangente avec {NB_PROCESS} processus : {pi}")   
    
    end = time.time()

    temps = end - start

    print(
        f"Temps de traitement {temps:.2f} secondes pour {nbIterations} iterations en multiprocess")
