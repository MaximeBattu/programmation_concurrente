#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define NB_FORK 3

#define INCREMENT_LIMIT 3

int data = 0;


void job(int i) {
    int tid = getpid();
    if (i == 0)
        execlp("who", "who", NULL);
    else if (i == 1)
        execlp("ps", "ps", NULL);
    else
        execlp("ls", "ls -l", NULL);
    sleep(1);
    printf("Fin du fork %i\n", tid);
    exit(EXIT_SUCCESS);
}

void waitForAll() {
    int status;
    pid_t pid;
    int n = 0;

    while (n < NB_FORK) {
        pid = wait(&status);
        printf("Fork [%i] termine avec le code %i\n", pid, status);
        n++;
    }
}

int main() {
    // Simultanément

    execlp("who", "who", NULL);
    execlp("ps", "ps", NULL);
    execlp("ls", "ls -l", NULL);

    printf("\n\n");
    // Sucessivement

    for (int i = 0; i < NB_FORK; i++) {
        pid_t pid = fork();
        if (pid == -1)
            perror("fork");
        else if (pid == 0)
            job(i);
    }
    waitForAll();
    return 0;
}
