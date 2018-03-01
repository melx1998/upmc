#include <stdio.h>

int main(){
	int n;
	float x, S, min, max;
	x=0;
	S=0;
	n=0;
	min=20;
	max=0;
	do{
		scanf("%f", &x);
		if (x<=20 && x>=0){
			S=S+x;
			
			if (x>max){
				max=x;}
			if (x<min){
				min=x;}	
			
			n+=1;}
		
		else if (x>20){
			printf("Veuillez saisir une valuer comprise entre 0 et 20 !\n");}
	
	}while (x>=0 && n<10);
	
	if (n==0){ /* cas n=0*/
		printf("moyenne = 0\n");}
	else{
		printf("moyenne = %f\nmin=%f\nmax=%f", S/n, min, max);} /*on enlève la dernière note négative*/
	
	return 0;
	}
