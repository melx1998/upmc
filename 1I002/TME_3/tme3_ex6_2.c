#include <stdio.h>
#include <cini.h>

int main(){
	
	int i, x, u;
	printf("Saisissez le premier terme de la suite\n");
	scanf("%d", &u);
	CINI_open_window(70*10, 3000, "fenetre");
	for (i=0; i<70; i++){
		if (u%2==0){
			u=u/2;}
		else{
			u=3*u+1;}
		for (x=0; x<10; x++){
			if (u*10<=3000){
				CINI_draw_line(i+x, 0, i+x, u*10, "white");}}
		}
	CINI_loop();
		
	return 0;
}
