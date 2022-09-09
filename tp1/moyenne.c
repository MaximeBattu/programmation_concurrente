#include <stdio.h>
#include <stdlib.h>

#define BORNE_SUP 20
#define BORNE_INF 0
#define MSG_ERROR "Aucune moyenne à calculer\n"

double calculMoyenne(char *notes[], int nbNotes);

int main(int argc, char *argv[]) {

    if (1 == argc) {
        printf("Aucune moyenne à calculer\n");
        return 0;
    }

    for (int i = 1; i <= argc - 1; i++) {
        // Vérification du passage d'une valeur numérique
        if (atof(argv[i]) == 0) {
            printf(MSG_ERROR);
            return 0;
        }

        // Vérificiation de la valeur numérique passée entre 0 et 20 inclus
        if (atof(argv[i]) < BORNE_INF || atof(argv[i]) > BORNE_SUP) {
            printf(MSG_ERROR);
            return 0;
        }
    }

    printf("Moyenne est : %0.2f\n", calculMoyenne(argv, argc));

    return 0;
}

/// @brief fonction permettant de calculer une moyenne
/// @return la moyenne
double calculMoyenne(char *notes[], int nbNotes) {

    float somme = 0;

    for (int i = 0; i < nbNotes; i++) {
        somme += atof(notes[i]);
    }

    return somme / (nbNotes - 1);
}