#include <sys/types.h>
#include <unistd.h>

int main()
{
    int i, n = 0;
    pid_t pid;
    for (i = 1; i < 5; i++)
    {
        pid = fork(); /*1*/
        if (pid > 0)
        {               /*2 */
            wait(NULL); /*3*/
            n = i * 2;
            break; /*sortie de la boucle*/
        }
    }
    printf("%d\n", n); /* 4 */
}