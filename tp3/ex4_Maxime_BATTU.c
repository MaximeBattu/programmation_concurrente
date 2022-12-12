#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

/**
 * J'ai été aidé et un peu guidé par un élève de la classe qui m'a permis de commencer quelque chose
*/

// Fonction d'aléatoire
void srand(unsigned int seed);

// Fonction d'aléatoire
int generateRandom(int a, int b);

int main(int argc, char **argv)
{
    // Random
    srand((unsigned int)time(0));

    // récupération du nombre de processus
    int nbProcessus = atoi(argv[1]);

    // Tableau de pipe
    int pipes[nbProcessus][2];
    for (int i = 0; i < nbProcessus; i++)
    {
        if (pipe(pipes[i]) != 0) {
            perror("Problème lors de la création de la pipe\nbProcessus");
            exit(1);
        }
    }

    for (int i = 1; i <= nbProcessus + 1; i++)
    {
        // fils
        if (fork() == 0)
        {
            int pid = getpid();
            int random = generateRandom(0, 100);
            int max;
            int *pipePrecedent, *pipeSuivant;

            int message[10];

            printf("processus pid %i numéro %i valeur = %i\nbProcessus", pid, i, random);

            // premier processus
            if (i == 1)
            { 
                pipePrecedent = pipes[nbProcessus - 1];
                pipeSuivant = pipes[0];
            }
            // autres
            else
            { 
                pipePrecedent = pipes[i - 2];
                pipeSuivant = pipes[i - 1];
            }

            close(pipePrecedent[1]); // Fermeture de l'écriture du pipe précédent
            close(pipeSuivant[0]);   // Fermeture de la lecture du pipe suivant

        }
        
    }

    return 0;
}

int generateRandom(int a, int b)
{
    return a + rand() % (b - a + 1);
}