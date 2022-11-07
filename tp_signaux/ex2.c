#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

int main()
{

    int i = 0;

    signal(SIGINT, SIG_IGN); // il faut kill -KILL du processus ps -a | grep a.out

    while (1)
    {
        i++;
        printf("i : %d\n", i);
    }

    return 0;
}