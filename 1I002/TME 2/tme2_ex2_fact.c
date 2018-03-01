#include <stdio.h>

int main(){
	int n, i, fact;
	fact=1;
	i=1;
	printf("Calcul de n!\nn = ?\n");
	scanf("%d", &n);
	/*affiche n!*/
	for (i=1; i<=n; i++){
		fact=fact*i;
		}
	printf ("%d ! = %d\n", n, fact);	
	return 0;
}
	
