#include <stdio.h>
#define M 7
#define N 7

int main(){ /*M lignes et N colonnes*/
	int i, e;
	for (i=0; i<M; i++){
		for (e=0; e<N-1; e++){
			printf("*");}
		printf("*\n");}
	return 0;
}
	
