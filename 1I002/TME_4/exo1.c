#include <stdio.h>
#define M 10

int main() {

int n, k, factn;

for (n = 0; n <= M; n++) {
/* on fait varier n de 0 à M */
	factn = 1;
	for (k = 2; k <= n ; k++) {
		factn = k * factn;
		}
	printf("%d! = %d\n", n, factn);
	}

	return 0;
}
 /*Ce programme affiche les résultats des factorielles de 0 à M. Il est mal identé, le nom des variables n'est pas très équivoque mathématiquement*/
