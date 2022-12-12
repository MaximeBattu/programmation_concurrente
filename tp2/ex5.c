#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

void waitForAll(int argc) {
    int status;
    pid_t pid;
    int n = 0;

    while (n < argc - 1) {
        pid = wait(&status);
        printf("Edition de liens");
        execlp("gcc", "gcc -o *.o", NULL);
        n++;
    }
}

void job(char argv) {
    char stence[] = "gcc -c ";
    strcat(stence, argv);

    execlp("gcc", stence, NULL);
}

int main(int argc, char **argv) {
    for (int i = 1; i < argc - 1; i++) {
        pid_t pid = fork();
        if (pid == -1)
            perror("fork");
        else if (pid == 0)
            job(argv[i]);
    }
    waitForAll(argc);
    return 0;
}
