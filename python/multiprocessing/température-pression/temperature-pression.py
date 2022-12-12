"""
    
    4IRC
    Exercice temperature-pression
    Groupe :
        - Maxime BATTU
        - Eileen BALAGUER
        - Batiste LALOI

"""
import multiprocessing as mp
import random
import time
import utils as utils


# Variables globales de gestion
MAX_TEMP = 65
MAX_PRESS = 5
VAR_TEMP = 0.1
VAR_PRESS = 0.005
SECU_TEMP = 5
SECU_PRESS = 1
TPS_RELOAD = 0.15

def lireValeur(mesureTemperature, mesurePression, capteur):
    if capteur == "temperature":
        return mesureTemperature.value
    elif capteur == "pression":
        return mesurePression.value
    return 0.0


def ecrireValeur(value, param):
    with param:
        param.value = value


def convertisseurAD(value, seuil):
    """
        Convertit des valeurs analogiques en digitales
    """
    return max(0.0, min(value, seuil))


def pression(stop, verrou, seuilPression, mesurePression, pressionMesuree, secondes):
    """
        Récupération de la valeur de la pression et conversion de cette dernière dans le 
        convertisseur AD et enregistrement de cette dernière dans la variable partagée mesurePression
    """
    while not stop.value:
        time.sleep(secondes)
        value = lireValeur(None, pressionMesuree, "pression")
        convertisseurAD(value, seuilPression.value)
        verrou.acquire()
        ecrireValeur(value, mesurePression)
        verrou.release()


def temperature(stop, verrou, seuilTemperature, mesureTemperature, pressionMesuree, secondes):
    """
        Récupération de la valeur de la température et conversion de cette dernière dans le 
        convertisseur AD et enregistrement de cette dernière dans la variable partagée mesureTemperature
    """
    while not stop.value:
        time.sleep(secondes)
        value = lireValeur(pressionMesuree, None, "temperature")
        convertisseurAD(value, seuilTemperature.value)
        verrou.acquire()
        ecrireValeur(value, mesureTemperature)
        verrou.release()


def pompe(stop, verrou, pompeEnRoute, pressionMesuree, secondes):
    """
        Affichage de la ligne "Pression : x.xx bar"
    """
    while not stop.value:
        time.sleep(secondes)
        if pompeEnRoute.value:
            utils.ecrireLigne(5, "Pompe : " + utils.green("ON"))
            verrou.acquire()
            pressionMesuree.value += VAR_PRESS + (random.random() / 10)
            verrou.release()
        else:
            utils.ecrireLigne(5, "Pompe : " + utils.red("OFF"))
            verrou.acquire()
            pressionMesuree.value -= VAR_PRESS + (random.random() / 10)
            verrou.release()

def chauffage(chauffageEnRoute, temperatureMesuree, stop, secondes):
    """
        Affichage de la ligne "Chauffage: xx.xx °c"
    """
    while not stop.value:
        time.sleep(secondes)
        if chauffageEnRoute.value:
            utils.ecrireLigne(4, "Chauffage : " + utils.green("ON"))
            temperatureMesuree.value += VAR_TEMP + random.random()
        else:
            utils.ecrireLigne(4, "Chauffage : " + utils.red("OFF"))
            temperatureMesuree.value -= VAR_TEMP + random.random()


def ecran(stop, verrou, mesureTemperature, mesurePression, secondes):
    """
        Affichage ds informations à l'écran
    """
    while not stop.value:
        time.sleep(secondes)
        verrou.acquire()
        temperature = lireValeur(mesureTemperature, mesurePression, "temperature")
        pression = lireValeur(mesureTemperature, mesurePression, "pression")
        verrou.release()
        
        if round(max(0, temperature), 2) > MAX_TEMP :
            utils.ecrireLigne(1, "Température : " + utils.red(str(round(max(0, temperature), 2))) + " °C")
        else : 
            utils.ecrireLigne(1, "Température : " + utils.green(str(round(max(0, temperature), 2))) + " °C")

        if round(max(0, pression), 2) > MAX_PRESS :
            utils.ecrireLigne(2, "Pression : " + utils.red(str(round(max(0, pression), 2))) + " bar")
        else :
            utils.ecrireLigne(2, "Pression : " + utils.green(str(round(max(0, pression), 2))) + " bar")


def controller(stop, verrou, seuilTemperature, chauffageEnRoute, pompeEnRoute, seuilPression, mesureTemperature,
               mesurePression, secondes):
    """
        Permet de centraliser le comportement du dispositif met en place
        Le controller à pour but de lire les valeurs récupérées "température" et "pression"
        et de décider l'état d'activation des deux dispositifs
    """
    while not stop.value:
        time.sleep(secondes)
        
        verrou.acquire()
        
        # Récupération des valeurs de température et de pression
        temperature = lireValeur(mesureTemperature, mesurePression, "temperature")
        pression = lireValeur(mesureTemperature, mesurePression, "pression")
        
        verrou.release()
        
        # Controle l'activation du chauffage 
        if temperature < seuilTemperature.value - SECU_TEMP:
            chauffageEnRoute.value = True
        elif temperature > seuilTemperature.value:
            chauffageEnRoute.value = False
            
         # Controle l'activation de la pompe 
        if pression < seuilPression.value - SECU_PRESS:
            pompeEnRoute.value = True
        elif pression > seuilPression.value:
            pompeEnRoute.value = False

if __name__ == "__main__":
    # Initialiser un verrou pour synchroniser les processus
    verrou = mp.Lock()
    
    # Initialiser des valeurs partagées pour les seuils de température et de pression
    seuilTemperature = mp.Value("i", MAX_TEMP)
    seuilPression = mp.Value("i", MAX_PRESS)

    # Initialiser des valeurs partagées pour les valeurs réelles de température et de pression
    mesureTemperature = mp.Value("f", 0)
    mesurePression = mp.Value("f", 0)
    
    # Initialiser des valeurs partagées pour les valeurs lues de température et de pression
    temperatureMesuree = mp.Value("f", 0)
    pressionMesuree = mp.Value("f", 0)
    
    # Initialiser des valeurs partagées pour les contrôleurs de la pompe et du chauffage
    pompeEnRoute = mp.Value("b", False)
    chauffageEnRoute = mp.Value("b", False)
    
    # Initialiser une valeur partagée pour arrêter les processus
    stop = mp.Value("b", False)

    # clear screen
    print("\033[2J")
    # hide cursor
    print("\033[?25l")

    # Tableau des proccessus 
    processus = [
        mp.Process(
            target=temperature,
            args=(stop, verrou, seuilTemperature, mesureTemperature, temperatureMesuree, TPS_RELOAD)
        ),
        mp.Process(
            target=pression,
            args=(stop, verrou, seuilPression, mesurePression, pressionMesuree, TPS_RELOAD)
        ),
        mp.Process(
            target=ecran,
            args=(stop, verrou, mesureTemperature, mesurePression, TPS_RELOAD / 2)
        ),
        mp.Process(
            target=controller,
            args=(
                stop, verrou, seuilTemperature, chauffageEnRoute, pompeEnRoute, seuilPression, mesureTemperature,
                mesurePression, TPS_RELOAD / 2
            )
        ),
        mp.Process(
            target=pompe,
            args=(stop, verrou, pompeEnRoute, pressionMesuree, TPS_RELOAD)
        ),
        mp.Process(
            target=chauffage,
            args=(chauffageEnRoute, temperatureMesuree, stop, TPS_RELOAD)
        )
    ]

    for process in processus:
        process.start()

    for process in processus:
        process.join()

    utils.ecrireLigne(8, "Fin du programme")
