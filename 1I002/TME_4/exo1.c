#include <stdio.h>
#define M 10

int main() {

int n, k, factn;

for (n = 0; n <= M; n++) {
/* on fait varier n de 0 � M */
	factn = 1;
	for (k = 2; k <= n ; k++) {
		factn = k * factn;
		}
	printf("%d! = %d\n", n, factn);
	}

	return 0;
}
 /*Ce programme affiche les r�sultats des factorielles de 0 � M. Il est mal ident�, le nom des variables n'est pas tr�s �quivoque math�matiquement*/
