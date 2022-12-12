import csv

csvPath = "./population.csv"

populationTotale = 0

populationMax = []
populationMin = []

with open(csvPath) as fichier :
    reader = csv.reader(fichier)

    cpt = 0

    for row in reader:
        if row[0].isdecimal():
            
            cpt += 1

            year, population = int(row[0]), int(row[1])

            # Init
            if populationMax == []:
                populationMax = [year, population]
            if populationMin == []:
                populationMin = [year, population]
            
            # Récupération des données
            populationTotale += population

            if population > populationMax[1] :
                populationMax = [year, population]
            if population < populationMin[1] :
                populationMin = [year, population]

moyenne = populationTotale/(cpt)

print(f"Population min : {populationMin}, Population max : {populationMax}, Moyenne : {moyenne}")