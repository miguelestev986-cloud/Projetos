#include <stdio.h>

int main(){

    int c;

    printf("%d\n", EOF);
    printf("Digite algo:\n");
    while ((c = getchar()) != EOF)
      putchar(c);
    return 0;
}
