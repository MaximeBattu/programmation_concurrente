#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char **argv) {
    int tmp = 0;
    int k = 0;
    int status;
    int pid;

    tmp = fork();   
    for (k = 0; k < 3; k++) {
        pid = wait(&status);
        if (status != 0)
            printf("(k = %d) : je suis le processus : %i, mon pere est : %i, retour : %d\n", 
                k, getpid(), getppid(), status);
    }
}