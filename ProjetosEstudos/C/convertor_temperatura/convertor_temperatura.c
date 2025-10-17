#include <stdio.h>

int main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;   /* lower limit of temperature table */
    upper = 300; /* upper limit */
    step = 20;   /* step size */

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
/*  outra forma

include <stdio.h>

#define LOWER 0 
#define UPPER 300 
#define STEP 20 

int main(){
    int fahr;
    for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
        printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
*/
