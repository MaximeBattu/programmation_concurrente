#include <stdio.h>

int main(int argc, char const *argv[])
{

    int status;
    pid_t pid;

    for (int i = 0; i < argc - 1; i++)
    {
        /* code */
        pid = fork();

        if (pid == 0) 
        {
            // enfant

        } 
        else if (pid == -1) 
        {
            perror("fork");
        }
        
        if (wait(&status)) {
            exit(status);
        }
    }
    


    return 0;
}
