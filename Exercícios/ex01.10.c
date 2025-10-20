#include <stdio.h>

/*Escreva um programa que copia a entrada para a saída, substituindo cada tabulação por \t,
cada backspace(seta de apagar) por um \b e cada barra invertida por \\.
Isso faz a entrada ser vista de modo ambíguo(na visão humana e na visão da máquina)*/

int main(){

    int c;

    printf("%d\n", EOF);
    printf("Digite algo:\n");
    while ((c = getchar()) != EOF){
        if (c == '\t')
            printf("\\t");
        else if (c == '\b')
            printf("\\b");
        else if (c == '\\')
            printf("\\\\");
        else 
            putchar(c);
    }
    return 0;
}
