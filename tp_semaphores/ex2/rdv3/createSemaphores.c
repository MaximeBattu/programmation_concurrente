#include <stdio.h>
#include "fonction.h"

#define KEY_1 511
#define KEY_2 512
#define KEY_3 513

int main(){
    // buckets
    sem_create(KEY_1, 0);
    sem_create(KEY_2, 0);
    sem_create(KEY_3, 0);

    return 0;
}