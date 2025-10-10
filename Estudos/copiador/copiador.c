#include <stdio.h>

int main(){

    int c;

    printf("%d\n", EOF);
    printf("Digite algo:\n");
    while ((c = getchar()) != EOF){
        if (c == ' ' | c == '\t')
            printf("\n");
        else 
            putchar(c);
    }
    return 0;
}
