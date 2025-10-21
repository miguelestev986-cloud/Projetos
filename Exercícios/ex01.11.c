#include <stdio.h>

int main(){

    int palavras, frase;
    palavras = 0;

    printf("Digite algo:\n");
    while ((frase = getchar()) != EOF)
        if (frase == ' '| frase == '\n'| frase == '\t')
           ++palavras;
    printf("Palavras: %d", palavras);
    return 0;
}
/*Observação: o código contabiliza novas linhas como palavras,
mesmo que não tenham nada escrito*/