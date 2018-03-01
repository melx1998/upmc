#include <stdio.h>

int main() {

int i, n, resu, max;
printf("Saisie de max : ");
scanf("%d",&max);

for (n = 0; n <= max; n++) {
/*calcul de n!*/
	resu = 1;
	for (i = 2; i <= n ; i++) {
		resu = i*resu;}
		printf("%d! = %d\n", n, resu);}
return 0;
}

/* Les valeurs deviennent bizarres (négatives, puis égales à 0) à partir de n=17.*/
/* Cela vient du fait que nous dépassons la valeur maximale prise par un int en mémoire (2 147 483 647).*/
