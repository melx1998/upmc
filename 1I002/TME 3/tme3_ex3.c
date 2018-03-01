#include <stdio.h>
#include <cini.h>
#include <math.h>
#define DIM_X 400
#define DIM_Y 400
#define EPAISSEUR 3

int main(){
	int x, y;
	CINI_open_window(DIM_X, DIM_Y, "fenetre");
	
	for (x=0; x<DIM_X; x++){
		for(y=0; y<DIM_Y; y++){
			if (abs(x-y)<=EPAISSEUR){
				CINI_draw_pixel(x, y, "yellow");
				}
			else if (y-x<EPAISSEUR){
				CINI_draw_pixel(x, y, "blue");}
			else if (y-x>EPAISSEUR){
				CINI_draw_pixel(x, y, "red");}
			}
		}
				
	CINI_loop();
	return 0;
	}
		
	
	
