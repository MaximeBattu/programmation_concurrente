"""
    
    4IRC
    Fichier utilitaire
    Groupe :
        - Maxime BATTU
        - Eileen BALAGUER
        - Batiste LALOI

"""

# Variables gloables de couleur
RED="\033[31m"
GREEN="\033[32m"
WHITE="\033[0m"

def red(message):
    """
        Affiche le message passé en rouge
    """
    return RED + message + WHITE


def green(message):
    """
        Affiche le message passé en vert
    """
    return GREEN + message + WHITE


def effacerLigne(ligne):
    """
        Efface une ligne dans le terminal
    """
    print("\033[{};1H".format(ligne) + " " * 80)


def ecrireLigne(ligne, texte):
    """
        Ecrit une ligne dans le terminal
    """
    effacerLigne(ligne + 1)
    print("\033[{};1H{}".format(ligne + 1, str(texte)))
