#include <stdio.h>

int main(){
	float u;
	int i, k;
	u=41;
	printf("Entrez le k-ième terme que vous souhaitez afficher\n");
	scanf("%d", &k);
	for (i=1; i<k; i++){
		if (i%2==0){
			u=u/2;}
		else{
			u=3*u+1;}
		}
	printf("u%d=%f\n", k, u);
	
	return 0;
}
