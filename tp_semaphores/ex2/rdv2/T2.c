#include <stdio.h>
#include "fonction.h"

#define KEY_1 511
#define KEY_2 512

int main()
{
    int mutexT1 = sem_create(KEY_2, 0);
    int mutexT2 = sem_create(KEY_1, 0);

    sleep(2);
    V(T1);
    V(T2);
    P(T3);
    P(T3);
    afficherRendezVous();   

    return 0;
}

void afficherRendezVous(){
    printf("Rendez-Vous !\n");
}