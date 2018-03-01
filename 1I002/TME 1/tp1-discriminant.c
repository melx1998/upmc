#include <stdio.h>
#include <math.h>


int main()
{
int a, b, c, discriminant;
printf("Entrez les valeurs des 3 coefficients du polynome de second degré (dans l'ordre croissant de leurs indices)\n");
scanf("%d %d %d", &a, &b, &c);
discriminant=(b*b)-4*a*c;
printf("valeur du discriminant : %dn", discriminant);
if (discriminant==0){ 
	printf("racine réellle : %d\n", (-b/2*a));}
else if (discriminant>0){
	printf("2 racines réellles : %f et %f\n", (-2+sqrt(discriminant))/2*a, ((-2-sqrt(discriminant))/2*a));}	 
return 0;
}

/* Jeu de tests : (0, 0, 0) == 0 
 * (-5, 0, -9)==180
 * (-1, 1, 1)==5*/
