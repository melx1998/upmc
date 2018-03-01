#include <stdio.h>

int main()
{
int a, b, c, discriminant;
printf("Entrez les valeurs des 3 coefficients du polynome de second degré (dans l'ordre croissant de leurs indices)\n");
scanf("%d %d %d", &a, &b, &c);
discriminant=(b*b)-4*a*c;
printf("valeur du discriminant : %d", discriminant);
return 0;
}

