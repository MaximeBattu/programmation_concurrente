import argparse

parser = argparse.ArgumentParser(description='nom du fichier')
parser.add_argument('filename', metavar='N', type=str, nargs=1, help='filename')
parser.add_argument('--operation', choices='nomFichier')

args = parser.parse_args()

with open(args.filename[0], 'r') as file:
    
    contenu = file.read()
    
    nbCaracteres = len(contenu)
    nbLignes = len(contenu.splitlines())
    premiersCaracteres = contenu.split(' ')[:20]
    nbMots = len(contenu.split(' '))
    nbSpecific = set(contenu.split(' '))

    print("Nombre de caractères : ", nbCaracteres)
    print("Nombre de lignes : ", nbLignes)
    print("20 premiers caractères : ", premiersCaracteres)
    print("Mot spécifique: ", nbSpecific)
    print("Nombre de mots : ", nbMots)
        
    
