#include <stdio.h>
#define M 4
#define N 7

int main(){ /*M lignes et N colonnes*/
	int i, e;
	for (i=0; i<M; i++){
		for (e=0; e<N-1; e++){
			if(i==0 || i==M-1 || e==0){
				printf("*");}
			else{
				printf(" ");}
			}
		printf("*\n");}
	return 0;
}
	

