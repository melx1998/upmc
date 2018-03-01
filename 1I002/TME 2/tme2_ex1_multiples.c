#include <stdio.h>

int main(){
	int n, m, i;
	i=1;
	printf("entrez les valeurs de n et m\n");
	scanf("%d %d", &n, &m);
	/* affiche les multiples de m tant qu'ils sont plus petits que n*/
	while (i*m<n){
		printf("%d ", i*m);
		i+=1;}
	return 0;
}
	
	
	
