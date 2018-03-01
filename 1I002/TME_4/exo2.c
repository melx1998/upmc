#include <stdio.h>
	
#define TAILLE 10

int main(){
	
	int i;
	int tab[TAILLE]={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, tab_copy[TAILLE];
	
	for (i=0; i<TAILLE; i++){
		tab_copy[i]=tab[i];
		printf("tab[%d]=%d\n", i, tab[i]);
		printf("tab_copy[%d]=%d\n", i, tab_copy[i]);
		}
		
	return 0;
}
	
	
