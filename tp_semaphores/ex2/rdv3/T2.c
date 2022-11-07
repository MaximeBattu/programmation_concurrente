#include <stdio.h>
#include "fonction.h"

#define KEY_1 511
#define KEY_2 512
#define KEY_3 513

int main()
{
    int T1 = sem_create(KEY_1, 0);
    int T2 = sem_create(KEY_2, 0);
    int T3 = sem_create(KEY_3, 0);

    sleep(2);
    V(T1);
    V(T3);
    printf("J'attends ...\n");
    P(T2);
    printf("On attend ...\n");
    P(T2);
    afficherRendezVous();   

    return 0;
}

void afficherRendezVous(){
    printf("Rendez-Vous !\n");
}