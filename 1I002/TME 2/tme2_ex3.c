#include <stdio.h>
#include <cini.h>

int main(){
	
	int x, y;
	x=0;
	y=0;
	CINI_open_window(400, 400, "fenetre");
	while (x<=399 && y<=399){
		CINI_draw_pixel(x, y, "red");
		x+=1;
		y+=1;
	}
	CINI_loop();
	
	return 0;
}
