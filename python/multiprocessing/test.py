from multiprocessing import Process, Value, Lock

def arc_tangente(n, pi, lock):
  for i in range(n):
     with lock:
       pi.value += 4/(1+ ((i+0.5)/n)**2)

if __name__ == '__main__':
  # Créer une variable partagée
  pi = Value('d', 0.0)
  # Créer un verrou pour synchroniser l'accès à la variable partagée
  lock = Lock()

  # Démarrer plusieurs processus qui calculent la valeur de pi en parallèle
  processes = []
  for i in range(4):
    p = Process(target=arc_tangente, args=(10000, pi, lock))
    p.start()
    processes.append(p)

  # Attendre que tous les processus se terminent
  for p in processes:
    p.join()

  # Afficher la valeur finale de pi
  print((pi.value / 4) / 10000)
