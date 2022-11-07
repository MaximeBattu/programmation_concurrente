#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "fonction.h"

#define KEY 511

int main(int argc, char **argv)
{
    int mutex = sem_create(KEY, 0);
    printf("J'attend\n");
    P(mutex);
    printf("Merci\n");
    V(mutex);
    sem_delete(mutex);
    return 0;
}

