#include <stdio.h>
#include <cini.h>


int main(){
	
	int x, y, c;
	printf("Entrer la valeur de c, le coté du carré\n");
	scanf("%d", &c);
	
	CINI_open_window(400, 400, "fenetre");
	
	for(x=0; x<=c; x++){ /*côté horizontal haut*/
		CINI_draw_pixel(x, y=0, "red");
		}
	for(y=0; y<=c; y++){ /*côté vertical droit*/
		CINI_draw_pixel(x=c, y, "red");
		}
	for(x=c; x>=0; x--){ /*côté horizontal bas*/
		CINI_draw_pixel(x, y=c, "red");
		}
	for(y=c; y>=0; y--){ /*côté vertical bas*/
		CINI_draw_pixel(x=0, y, "red");
		}
		 
	
	CINI_loop();
	
	return 0;
}
