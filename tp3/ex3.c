#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define QUANTITE 10

// Fonction d'aléatoire
void srand(unsigned int seed);

// Fonction d'aléatoire
int generateRandom(int a, int b);

int main()
{
    // Random
    srand((unsigned int)time(0));

    // Création des pipes
    int tubePair[2], tubeImpair[2], sommePair[2], sommeImpair[2];

    int *nombres;

    // Vérification des pipes
    if (pipe(tubePair) != 0 || pipe(tubeImpair) != 0 || pipe(sommePair) != 0 || pipe(sommeImpair) != 0)
    {
        perror("problème création du tube\n");
        exit(1);
    }

    // Générateur
    if (fork() == 0)
    {
        close(tubePair[0]);
        close(tubeImpair[0]);

        // On génère dix nombres alétoires
        for (int i = 0; i < QUANTITE; i++)
        {
            int rdmNbr = generateRandom(0, 10);

            nombres[i] = rdmNbr;

            // Si il est impair
            if (rdmNbr % 2)
            {
                write(tubeImpair[1], &rdmNbr, sizeof(int));
            }
            // Si il est pair
            else
            {
                write(tubePair[1], &rdmNbr, sizeof(int));
            }
        }

        // On dépose la valeur -1 dans les 2 tubes pour indiquer la fin de la série des nombres
        int end = -1;
        write(tubePair[1], &end, sizeof(int));
        write(tubeImpair[1], &end, sizeof(int));
        close(tubePair[1]);
        close(tubeImpair[1]);

        // On récupère les deux nombres déposés respectivement dans le tube SommePairs et SommeImpairs
        int sommeP, sommeI;
        read(sommePair[0], &sommeP, sizeof(int));
        read(sommeImpair[0], &sommeI, sizeof(int));

        // On réalise leur somme et on affiche le résultat
        printf("Somme des deux tubes : %d + %d = %d \n", sommeP, sommeI, sommeP + sommeI);

        close(sommePair[0]);
        close(sommeImpair[0]);
    }
    else
    {
        // Si on est dans le filtrePair
        if (fork() == 0)
        {
            int sommeP = 0;
            int nbrRecupere;

            // On récupère les nombres déposés dans le tube NombresPairs
            while (read(tubePair[0], &nbrRecupere, sizeof(int)) > 0)
            {
                // Si le nombre est -1
                if (nbrRecupere != -1)
                {
                    // On réalise la somme de ces nombres
                    sommeP += nbrRecupere;
                }
                else
                {
                    // On dépose le résultat dans le tube SommePairs
                    write(sommePair[1], &sommeP, sizeof(int));
                    close(sommePair[1]);
                    break;
                }
            }
        }
        else
        {
            // Si on est dans le filtreImpair
            if (fork() == 0)
            {
                int sommeI = 0;
                int nbr;

                // On récupère les nombres déposés dans le tube NombresImpairs
                while (read(tubeImpair[0], &nbr, sizeof(int)) > 0)
                {
                    // Si le nombre est -1
                    if (nbr == -1)
                    {
                        // On dépose le résultat dans le tube SommeImpairs
                        write(sommeImpair[1], &sommeI, sizeof(int));
                        close(sommeImpair[1]);
                        break;
                    }
                    else
                    {
                        // On réalise la somme de ces nombres
                        sommeI += nbr;
                    }
                }
            }
        }
    }

    return 0;
}

int generateRandom(int a, int b)
{
    return a + rand() % (b - a + 1);
}