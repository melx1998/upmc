#include <stdio.h>

int main(){
	int enfant_petit, enfant_grand, senior, adulte;
	float prix;
	prix=0;
	printf("Nombre d'enfants de moins de 5 ans ?\n");
	scanf("%d", &enfant_petit);
	printf("Nombre d'enfants entre 5 et 15 ans ?\n");
	scanf("%d", &enfant_grand);
	printf("Nombre de seniors (plus de 60 ans) ?\n");
	scanf("%d", &senior);
	printf("Nombre d'adultes restants ?\n");
	scanf("%d", &adulte);
	
	if (adulte+senior>=2 && enfant_grand>=2){
		prix=prix+59;
		if (adulte>=2){
			adulte=adulte-2;}
		else if (adulte<2){
			if (senior-(2-adulte)<=0){
				senior=0;}
			else if (senior-(2-adulte)>0){
				senior=senior-(2-adulte);}
			adulte=0;
			}
		if (enfant_grand-3<=0){
			enfant_grand=0;}
		else if (enfant_grand-3>0){
			enfant_grand-=3;}
		}
	prix=prix+enfant_grand*11+senior*18.70+adulte*22;
	printf("prix à payer : %f\n", prix);
		
	return 0;	
}
	
	
	
	
	
	
	
	
	
	
	
	
