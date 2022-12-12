"""
    
    4IRC
    Exercice course hippique
    Groupe :
        - Maxime BATTU
        - Eileen BALAGUER
        - Batiste LALOI

"""
CLEARSCR="\x1B[2J\x1B[;H"          #  Clear SCReen
CLEAREOS = "\x1B[J"                #  Clear End Of Screen
CLEARELN = "\x1B[2K"               #  Clear Entire LiNe
CLEARCUP = "\x1B[1J"               #  Clear Curseur UP
GOTOYX   = "\x1B[%.2d;%.2dH"       #  ('H' ou 'f') : Goto at (y,x), voir le code

DELAFCURSOR = "\x1B[K"             #  effacer après la position du curseur
CRLF  = "\r\n"                     #  Retour à la ligne

CURSON   = "\x1B[?25h"             #  Curseur visible
CURSOFF  = "\x1B[?25l"             #  Curseur invisible

NORMAL = "\x1B[0m"                  #  Normal
BOLD = "\x1B[1m"                    #  Gras
UNDERLINE = "\x1B[4m"               #  Souligné

CL_BLACK="\033[22;30m"                  #  Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"                    #  Rouge
CL_GREEN="\033[22;32m"                  #  Vert
CL_BROWN = "\033[22;33m"                #  Brun
CL_BLUE="\033[22;34m"                   #  Bleu
CL_MAGENTA="\033[22;35m"                #  Magenta
CL_CYAN="\033[22;36m"                   #  Cyan
CL_GRAY="\033[22;37m"                   #  Gris

CL_DARKGRAY="\033[01;30m"               #  Gris foncé
CL_LIGHTRED="\033[01;31m"               #  Rouge clair
CL_LIGHTGREEN="\033[01;32m"             #  Vert clair
CL_YELLOW="\033[01;33m"                 #  Jaune
CL_LIGHTBLU= "\033[01;34m"              #  Bleu clair
CL_LIGHTMAGENTA="\033[01;35m"           #  Magenta clair
CL_LIGHTCYAN="\033[01;36m"              #  Cyan clair
CL_WHITE="\033[01;37m"                  #  Blanc

import multiprocessing as mp

import threading
import time
import random
import string
import os,sys
import platform
import ctypes

lyst_colors=[CL_WHITE, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY,
             CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN,  CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]

def effacer_ecran() : print(CLEARSCR,end='')
def erase_line_from_beg_to_curs() : print("\033[1K",end='')
def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')
def move_to(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end='')
def en_couleur(Coul) : print(Coul,end='')

S = int(input("Nombre de serveurs : "))
T = int(input("Max de commande possible : "))

## Variables partagées
tampon = []
tabServeurs = []
tabCommandes = []
lastServie = ""
endService = 0
locker = threading.Lock()

def clients():
    global tampon
    global T
    ## Je viens créer au fur et à mesure mes commandes jusqu'à atteindre le nombre 
    ## maximum de commande possible
    for i in range (0, T):
        if (i > 0):
            ## Entre chaque commande j'attends de manière aléatoire entre 1 et 4 secondes
            sleeping = random.randint(1, 4)
            time.sleep(sleeping)
        ## Je viens verrouiller ma liste de commandes et je le remplis d'une combinaison
        ## Nombre de 1 à 50 et une letter au hasard entre A et Z
        with locker:
            tampon.append(str(random.randint(1, 50)) + str(random.choice(string.ascii_uppercase)))

def major_dHomme():
    global S
    global tampon
    global endService
    global lastServie
    global tabCommandes
    ## Tant que je ne suis pas en fin de services et que j'ai des commandes encore en traitement
    ## alors
    while (endService == 0 and len(tabCommandes) > 0):
        ## Je verrouille ma variable
        with locker:
            effacer_ecran()
            curseur_invisible()
            ## Pour chaque serveur j'affiche sur une ligne différente
            for i in range (1, S+1):
                move_to(i, 0)
                erase_line_from_beg_to_curs()
                en_couleur(lyst_colors[i%len(lyst_colors)])
                if (len(tabCommandes[i-1]) > 1):
                    ## S'il traite une commande et son numéro
                    print('Le serveur',i,"traite la commande", tabCommandes[i-1])
                else :
                    ## S'il ne traite pas de commande
                    print('Le serveur',i,"ne traite pas de commande pour le moment")
            move_to(i+2, 0)
            erase_line_from_beg_to_curs()
            en_couleur(lyst_colors[i+1%len(lyst_colors)])
            ## J'affiche les commandes en attente
            print("Les commandes clients en attente : ", tampon)
            move_to(i+3, 0)
            erase_line_from_beg_to_curs()
            ## j'affiche le nombre de commande en attente
            print('Nombres de commandes attente : ', len(tampon))
            move_to(i+4, 0)
            erase_line_from_beg_to_curs()
            ## Je viens afficher la dernière commande servie par les serveurs
            if (lastServie == ""):
                print("Aucune commande n'a été servie pour le moment")
            else:
                print('Commande', lastServie,'est servie au client')
        time.sleep(1)

def serveurs(i):
    global tabCommandes
    global tampon
    global lastServie
    global endService
    time.sleep(5)
    ## Si je ne suis pas en fin de service, que j'ai des commandes en attentes
    ## Et des commandes en traitement
    while (endService == 0 and len(tampon) > 0 and len(tabCommandes) > 0):
        ## Je verrouille ma variable
        with locker:
            ## Si j'ai des commandes en attente, j'assigne la tampon[0]
            ## à mon serveur
            if (len(tampon) > 0):
                tabCommandes[i] = tampon[0]
                del tampon[0]
            else:
                tabCommandes[i] = "0"
        time.sleep(2)
        ## J'attends 2 secondes avant de traiter la commande
        with locker:
            ## J'attends entre 1 et 3 secondes de manière aléatoire et je passe la commande 
            ## en dernière servie
            sleeping = random.randint(1, 3)
            time.sleep(sleeping)
            lastServie = tabCommandes[i]
            tabCommandes[i] = "0"
        time.sleep(2)

if __name__ == '__main__':

    ## Je viens remplir mon tableau de commandes de 0
    for i in range(0, S):
        tabCommandes.append("0")

    if platform.system() == "Darwin" :
        mp.set_start_method('fork')

    ## Je viens créer mon processus client qui va créer mes commandes
    processClient = threading.Thread(target=clients, args=[])
    processClient.start()

    ## je viens créer mon processus majorHomme qui va afficher les informations
    ## au fur et à mesure
    majorHomme = threading.Thread(target=major_dHomme, args=[])
    majorHomme.start()

    ## Je crée un processus pour chaque serveur que je stocke dans mon tableau
    ## tabServeurs
    for i in range(0, S):
        tabServeurs.append(threading.Thread(target=serveurs, args=[i]))
        tabServeurs[i].start()

    ## Je join tous mes processus pour les faire terminer
    for i in range(0, S):
        tabServeurs[i].join()
    processClient.join()
    majorHomme.join()
