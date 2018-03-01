/* Completez le programme suivant pour qu'il affiche la somme des puissances de X 
   inferieures a N1 et multiples de N2 

  La valeur de X, N1 et N2 est definie par une primitive #define
*/

#include <stdio.h>

/* Dans les 3 lignes suivantes, vous ne pouvez que modifier les valeurs pour pouvoir tester votre
programme sur d'autres jeux de test */
#define N1 100
#define N2 9
#define X 3

/* Vous devez completer la fonction main suivante sans modifier les declarations et instructions */
/* qui vous sont donnees */
int main() {
	
	int xn, S;
	xn=1;
	S=0;
	
	while (xn<N1){
		xn=xn*X;
		if (xn%N2==0){
			S=S+xn;}
		}	
	printf("Somme=%d\n", S);

	return 0;
}
