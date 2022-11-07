#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void signal_handler(int signum);

int fin = 0;

int main() {

    int i = 0;

    signal(SIGINT, signal_handler);

    while (1)
    {
        i++;
        printf("%d\n", i);

        if (fin == 1) exit(0);
    }
    

}

void signal_handler(int signum)
{
    if (SIGINT == signum) {
        fin = 1;
    }
}