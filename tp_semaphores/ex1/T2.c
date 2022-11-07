#include <stdio.h>
#include "fonction.h"

#define KEY 511

int main(int argc, char **argv)
{
    int mutex = sem_create(KEY, 0);

    printf("Réponse de T2 : Tient\n");
    V(mutex);
    return 0;
}