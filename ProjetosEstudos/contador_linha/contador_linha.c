#include <stdio.h>
/* count lines in input */
int main(){

    int c, nl, tab, blank;

    nl = 0;
    tab = 0;
    blank = 0;
    printf("Escreva oque quiser:\n");
    while ((c = getchar()) != EOF){
        if (c == '\t')
            ++tab;
        if (c == '\n')
            ++nl;
        if (c == ' ')
            ++blank;
        }
    printf("Linhas: %d\nTab: %d\nEspaços: %d", nl, tab, blank);
    return 0;

}