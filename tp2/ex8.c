#include <stdio.h>

int main()
{
    int i, delai;
    for (i = 0; i < 4; i++)
        if (fork())
            break;
    srand(getpid());
    delai = rand() % 4;
    sleep(delai);
    printf("Mon nom est %c, j’ai dormi pendant %d secondes\n", ’A’ + i, delai);
    exit(0);
}