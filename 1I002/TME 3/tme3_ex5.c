#include <stdio.h>

int main(){
	
	int premier, nb, diviseur, m;
	printf("Entrez un entier\n");
	scanf("%d", &m);
	for (nb=2; nb<=m; nb++){
		premier=1;
		diviseur=nb-1;
		while (premier && diviseur>=2){
			if(nb%diviseur==0){
					premier=0;}
			diviseur=diviseur-1;}
		if (premier==1){
			printf("\t%d\n", nb);}
		else{
			printf("\t%d", nb);}
		}
			
	return 0;
	}
	
	
