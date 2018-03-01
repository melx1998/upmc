#include <stdio.h>
#include <cini.h>

#define A 2
#define B 36


/* DROITE D'ÉQUATION y = A x + B */

int main(){
	
	int x, max_x, max_y;
	
	CINI_open_window(max_x=400, max_y=400, "fenetre");
	
	for(x=0; x <= max_x-1; x++){
		if (A*x+B <= max_y-1){
			CINI_draw_pixel(x, A*x+B, "red");}
			else{
				break;}
	}
	
	CINI_loop();
	
	return 0;
}
	
