/*
Le tarif d'un billet de train depend de l'age des participants au voyage selon les regles suivantes :

le tarif de base est applique pour les voyageurs ages de 11 a 59 ans.
les enfants de 0 a 10 ans paient 75% du tarif de base.
les seniors de 60 ans et plus paient 75% du tarif de base.

Complétez le programme suivant pour qu'il affiche le tarif a regler pour 2 personnes. L'affichage doit etre 
TARIF : XXX 
(ou XXX est le tarif a regler)

 Les ages des deux voyageurs et le tarif de base sont definis en utilisant des primitives #define
*/


#include <stdio.h>

/* Dans les 3 lignes suivantes, vous ne pouvez que modifier les valeurs pour pouvoir tester votre
programme sur d'autres jeux de test */
#define TARIFBASE 200
#define AGE1 4
#define AGE2 50

/* Vous devez completer la fonction main suivante sans modifier les declarations et instructions */
/* qui vous sont donnees */
int main() {
	
	float tarif;
	tarif=0;
	
	if (AGE1<=10 || AGE1>=60){
		tarif=tarif+(75*TARIFBASE/100);}
	else{
		tarif=tarif+TARIFBASE;}
	if (AGE2<=10 || AGE2>=60){
		tarif=tarif+(75*TARIFBASE/100);}
	else{
		tarif=tarif+TARIFBASE;}
	
	
		

   /*A COMPLETER, vous devez, en particulier, remplacer les points de suspension */
  printf("TARIF : %f\n", tarif);
  return 0;
}

