#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {

    if (argv[1] == 0) {
        return 0;
    }

    for (int i = 1; i <= argc -1; i++) {
        int nbCaracteres = strlen(argv[i]);

        for (int j = 0; j <= nbCaracteres; j++) {
            printf("%c", argv[i][nbCaracteres - j]);
        }
        printf("\n");
    }

    return 0;
}