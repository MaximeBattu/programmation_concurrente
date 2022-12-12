#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "fonction.h"

#define KEY_1 511
#define KEY_2 512

int main()
{
    int mutexT1 = sem_create(KEY_1, 0);
    int mutexT2 = sem_create(KEY_2, 0);
    printf("J'attend\n");
    
    V(mutexT1);    
    P(mutexT2);
    afficherRendezVous();

    return 0;
}

void afficherRendezVous(){
    printf("Rendez-Vous !\n");
}