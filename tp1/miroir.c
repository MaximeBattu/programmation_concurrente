#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {

    if (argv[1] == 0) {
        return 0;
    }

    int nbCaracteres = strlen(argv[1]);

    for (int i = 0; i <= nbCaracteres; i++) {
        printf("%c", argv[1][nbCaracteres - i]);
    }
    printf("\n");

    return 0;
}