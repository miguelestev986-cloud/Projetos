
# ***Anotaciones Generales

Toda declaración en C termina con un punto y coma;

Para hacer comentarios utilizamos //. Si ellos tienen más de una línea, utilizamos / * comentário * /;

Secuencias de escape son utilizadas para representar caracteres invisibles o demasiado dificiles de escribir. Algunos de ellos son \n (nueva línea), \t (tabulación), \\ (para el caracter \), \" (para el caracter ");

return 0 indica que el programa ha terminado con exito, es dispensable pero, por buenas practicas, lo escribimos;

El operador relacional != significa "no igual a". La orden de precedencia de != es mayor que =;

# ***A Tutorial Introduction Chapter 1***


## *1.1 Getting Started

```c
#include <stdio.h>  // archivo de encabezado
  
int main() {  //función
  printf("Hello World!\n");  
  return 0;  
}
```

### Archivos de Encabezado (header files)

Archivos de encabezado agregan funcionalidades para programas en C. Por ejemplo, # include<stdio.h> es un archivo de encabezado que nos permite trabajar con funciones de input y output, como printf().

### Funciones (functions)

Una función tiene declaraciones que dicen que computaciones tienen que ser hechas. La función main() indica el comienzo de tu pograma para que pueda ejecutarse, se observa que esta función no tiene argumentos( lista de valores). Los {} incluye la(s) declaración(es) de la función main(), que es printf(), que imprimirá su lista de argumentos: la cadena de caracteres (que deben estar entre comillas dobles) "Hello World!" y, con la secuencia de escape \n ,una nueva línea al final.


## *1.2 Variables and Arithmetic Expressions

```c
#include <stdio.h>

int main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;   /* lower limit of temperature table */
    upper = 300; /* upper limit */
    step = 20;   /* step size */

    printf("\nConversor de Temperatura\n\nFahrenheit\tCelsius\n");

    fahr = lower;
    while (fahr <= upper)
    {
        celsius = (5.0 / 9.0) * (fahr - 32);
        printf("%8.0f %14.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
    return 0;
}
```
### Variables

En C, variables deben ser declaras antes que sean usadas. Su declaración dice sus propriedades. El tipo de dato int declara que las variables listadas son números inteiros, y float declara que son números decimales. Variables armacenan valores que pueden ser alterado mientras la execución del programa.

### Bucle While

Bucles son utilizados para repetir un código hasta que una condicións sea falsa o verdadeira. While verifica si la variables fahr es menor o igual que upper, si sí, el executa el corpo del bucle. Si esto se torna falso, el bucle se termina y el programa sigue. El bucle executa solo la primera línea después de while, si las instrucciones soman más que una línea, usamos while(condición){instrucciones}

### Especificadores de formato

% indica que viene un especificador de formato y donde los argumentos deben colocarse. (%)d reserba un espacio en la cadena de caracteres(string) para un argumento de número inteiro. Tenemos otros especificadores de formato, como (%)f para números decimales y (%)s para strings. Podemos (com d y s) definir cuantas casas decimales lo numero deve ter, ex: %.1f define una casa decimal. 

## *1.3 The For Statement

```c
#include <stdio.h>

#define LOWER 0 
#define UPPER 300
#define STEP 20

main() { 
	int fahr; } 
	for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP) 
		printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
}
```

### Bucle For

Es un bucle igual que while, pero sus estruturas son destintas. El bucle for es separado en tres partes: la inicialización(En este caso, fahr = 0), la condición(En este caso, fahr <= 300) y el incremiento. Lo programa comienza, verifica la condición, si la condición for TRUE, el ejecutará el corpo del bucle y entonces haz el incremiento y retoma el bucle hasta que él resulte FALSE.
Podemos elegir while o for
## *1.4 Symbolic Constants

#### Numeros mágicos

Son numeros sin significado aparente y que son dificiles de alterar de maneira sistematica. Usalos resulta en más practicas. Los substituimos por constantes simbólicas.

#### Constantes Simbólicas

Constantes son como variables, pero no mudan de valor (mientras la ejecución del programa).Por convención, son escritas en letras mayuscúlas y no terminan con punto y coma. Definimos su valor con # define, como en el capítulo 1.3.

## *1.5 Character Input and Output

### 1.5.1 File Copying

```c
#include <stdio.h>

int main() {
	int c;
	while ((c = getchar()) != EOF) 
		putchar(c)
```
Obs: c = getchar() está en paréntesis porque la orden de precedencia de != es mayor que =
#### getchar()

Es una función de la biblioteca estándar (stdio.h) que lee el siguiente carácter no consumido(que aún no ha sido procesado) de la entrada estándar(text stream, fluxo de texto) y lo devuelve como int. En caso de EOF(End-of-File, geralmente -1) o error, devuelve EOF.

##### putchar()

Tiene la función opuesta que getchar(), putchar() recibe un único carácter (como int), y lo escribe en la salida estándar (stdout).

### 1.5.2 Character Counting

```c
#include

int main() {
	long nc;
	nc = 0;
	while (getchar() != EOF) 
		++nc; 
	printf("%ld\n", nc);
	return 0;
}

ou

#include

main() {
	
	long nc;
	for (nc = 0; getchar() != EOF; ++nc)
		;  
	// for deve ter um corpo, mesmo que seja um delaração nula
	printf("%ld\n", nc);
	return 0;
}

```

#### El Tipo long

Variables de tipo short conseguem armacenar valores hasta 16 bits, int conseguem armacenar valores hasta 16 bits(32 en sistemas más actuales). Ya variables de tipo long armacenan de 32 hasta 64 bites a depender del sistema. El especificador %ld indica que es un inteiro largo. Para numeros ainda mayores, usamos double.

#### Los operadores

El operador ++  incrementa más 1 en la variable, -- decrementa 1 de la variable. Y el operador relacional != significa "no es igual a".

### 1.5.3 Line Counting

```c
#include <stdio.h>

/* count lines in input */

int main(){

    int c, nl;
 
    nl = 0;
    printf("Escreva oque quiser:\n");

    while ((c = getchar()) != EOF)
        if (c == '\n')
           ++nl;
    printf("%d\n", nl);
    return 0;
}
```

#### Los sinales = y ==

Como en Python, = significa recibe y == significa "igual que".
#### El operador | 

Significa "o". Usamos en bucles o condicionales.

## *1.6 Arrays
