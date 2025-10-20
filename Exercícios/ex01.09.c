#include <stdio.h>

/*Escreva um programa que substitui
uma sequência de espaços por apenas um espaço.*/

int main(){

    int ca;
    while ((ca = getchar()) != EOF){
        if (ca == '  ')
            printf(" ");
        else
            putchar(ca);
    }
    return 0;
}