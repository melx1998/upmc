#include <stdio.h>
#include <string.h>


int main(){
	
	char chaine1[]="bonjour";
	char chaine2[]="jours";
	int i, j, indice;
	i=0;
	j=0;
	
	while(chaine2[i]!=chaine1[j] && chaine1[j]!='\0'){
		j++;
		}
	if (chaine1[j]!='\0'){
		indice=j;
		while (chaine2[i]==chaine1[j] && chaine2[i]!='\0' && chaine1[j]!='\0'){
			i++;
			j++;}
		}
	if (chaine2[i]=='\0'){
		printf("chaine2 est incluse dans chaine1\nindice de chaine1 à partir duquel chaine2 commence: %d\n", indice);}
	else{
		printf("chaine2 n'est pas incluse dans chaine1\n");}
		
	return 0;
}
