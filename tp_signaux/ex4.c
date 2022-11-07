#include <stdlib.h>
#include <stdlib.h>
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int main()
{
    int pid = fork();

    if (pid) {
        int i = 0;
        while(1) {
            i++;
            printf("%d\n", i);
        }
    } else {
        for (int i = 0; i < 3; i++) {
            printf("père : %d\n", i);
        }

        kill(pid, SIGKILL);
    }
}