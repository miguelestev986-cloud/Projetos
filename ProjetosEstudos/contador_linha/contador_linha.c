#include <stdio.h>
/* count lines in input */
int main(){

    int c, nl;
    nl = 0;

    printf("Escreva oque quiser:\n");
    while ((c = getchar()) != EOF)
        if (c == '\n')
            ++nl;
    printf("Linhas:", nl);
    return 0;
}