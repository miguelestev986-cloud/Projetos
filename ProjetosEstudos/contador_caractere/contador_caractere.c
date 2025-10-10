/*#include <stdio.h>

int main() {

	long nc;
	nc = 0;
	while (getchar() != EOF);
		++nc; 
	printf("%ld\n", nc);
	return 0;
}
*/
#include <stdio.h>

int main() {
	
	int nc;
	for (nc = 0; getchar() != EOF; ++nc)
        ;
	// for deve ter um corpo, mesmo que seja um delaração nula
    printf("%.0f\n", nc);
	return 0;
}