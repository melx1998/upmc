#include <stdio.h>
#include <cini.h>
	
#define N 5

int main(){

	int Snotes, Scoeffs, i, tabN[N]={15, 14, 17, 18, 16}, tabC[N]={9, 7, 3, 7, 3};
	Snotes=0;
	Scoeffs=0;
	
	for (i=0; i<N; i++){
		Snotes=Snotes+tabN[i]*tabC[i];
		Scoeffs=Scoeffs+tabC[i];
	}
	printf("%f\n", (Snotes*1.0/Scoeffs));
	
	return 0;
}
	
