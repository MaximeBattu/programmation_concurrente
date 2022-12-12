from genericpath import isfile
import os
import argparse

parser = argparse.ArgumentParser(description="nom du dossier à parcourir")
parser.add_argument('path', metavar='N', type=str, nargs=1, help='path')
parser.add_argument('--operation', choices='cheminVersLeDossier')

args = parser.parse_args()

liste_fichiers = []

for root, dirs, fichiers in os.walk(args.path[0]):

    for fichier in fichiers:
        liste_fichiers.append(os.path.join(root, fichier))

for nom in liste_fichiers :
    print(nom)
