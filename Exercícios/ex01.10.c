#include <stdio.h>

int main(){

    int c;

    printf("%d\n", EOF);
    printf("Digite algo:\n");
    while ((c = getchar()) != EOF){
        if (c == '\n')
            printf("\\n");
        if (c == '\t')
            printf("\\t");
        if (c == '\b')
            printf("\\b");
        else 
            putchar(c);
    }
    return 0;
}
