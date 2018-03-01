#include <stdio.h>
#include <string.h>

#define MAX 5

int main(){
	
	float tab[MAX];
	int i=0, e, S=0;
	
	printf("Entrez maximum %d valeurs, tappez -1 quand vous avez terminé\n", MAX);
	do{
		scanf("%f", &tab[i]);
		if (tab[i]!=-1){
			S+=tab[i];}
		i++;
	} while(i<MAX && tab[i-1]!=-1);
	
	for(e=0; e<=i-1; e++){
		printf("%f\t", tab[e]);
		}	
	if (i-1!=0){
		printf("\nmoyenne=%f\n", S*1.0/(i-1));}
		
	return 0;
}
