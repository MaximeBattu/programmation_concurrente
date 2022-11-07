#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void signal_handler(int signum);

int main() {

    int i = 0;

    signal(SIGINT, signal_handler);

    while (1)
    {   
        i++;
        printf("i : %d\n", i);
    }
    
    return 0;
}

void signal_handler(int signum)
{
    if (SIGINT == signum) {
        printf("arrêt du processus \n");
        exit(0);
    }
}