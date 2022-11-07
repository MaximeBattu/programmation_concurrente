#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    // Successif
    system("ls");
    system("who");
    system("ps");

    // Simultané
    if (!fork()) 
    {
        if (!fork()) 
        {
            execlp("ls", "ls", "-l", NULL);
        }
        execlp("ps", "ps", NULL);
    }
    execlp("who", "who", NULL);

    return 0;
}
