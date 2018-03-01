#include <stdio.h>
#include <string.h>

#define MAX 5

int main(){
	
	float tab[MAX];
	int taille, i=0, e, compteur, n=0, x; /* nombre d'occurrences*/;
	int vu=0; /* booléeen inintilaisé à faux*/
	
	printf("Entrez maximum %d valeurs, tappez -1 quand vous avez terminé\n", MAX);
	do{ /* creation du tableau*/
		scanf("%f", &tab[i]);
		i++;
	} while(i<MAX && tab[i-1]!=-1);
	
	taille=i-1;
	
	for(e=0; e<=taille; e++){ /*on parcourt le tableau*/
		
		if (tab[e]!=-1){ /* on compte pas le -1*/
			while (vu==0 && x<e){ /* on verifife que la valeur n'a pas deja ete comptée*/
				if (tab[e]==tab[x]){
					vu=1;}
				x++;	
				}
				
				
			if (vu==0){ /*comptabilistaion*/
				
				for(compteur=0; compteur<=taille; compteur++){
					if (tab[compteur]==tab[e]){
						n+=1;}
				}
				printf("La valeur %f apparait %d fois dans le tableau.\n", tab[e], n);
				n=0;
			}
			else{
				vu=0;}
		}
	
	}
		

	return 0;
}
