import csv

csvPath = "./population.csv"

population_totale = 0

populationMax = []
populationMin = []

with open(csvPath) as fichier :
    reader = csv.reader(fichier)

    cpt = 0

    for row in reader:
        if row[0].isdecimal():
            
            cpt += 1

            y, p = int(row[0]), int(row[1])

            # Init
            if populationMax == []:
                populationMax = [y, p]
            if populationMin == []:
                populationMin = [y, p]
            
            # Récupération des données
            population_totale += p

            if p > populationMax[1] :
                populationMax = [y, p]
            if p < populationMin[1] :
                populationMin = [y, p]

moyenne = population_totale/(cpt)

print(f"Pmin : {populationMin}, Pmax : {populationMax}, Moyenne : {moyenne}")