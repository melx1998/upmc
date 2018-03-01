#include <stdio.h>
#include <cini.h>
#include <math.h>


int main(){
	
	int x, y, x0, y0, c;
	printf("Entrer la valeur de c, le coté du carré\n");
	scanf("%d", &c);
	printf("Entrer la valeur de x et y, le coin superieur gauche du carré\n");
	scanf("%d %d", &x0, &y0);
	
	CINI_open_window(400, 400, "fenetre");
	
	for(x=x0; x<=x0+c; x++){ /*côté horizontal haut*/
		CINI_draw_pixel(x, y=y0, "red");
		}
	for(y=y0; y<=y0+c; y++){ /*côté vertical droit*/
		CINI_draw_pixel(x=x0+c, y, "red");
		}
	for(x=x0+c; x>=x0; x--){ /*côté horizontal bas*/
		CINI_draw_pixel(x, y=y0+c, "red");
		}
	for(y=y0+c; y>=y0; y--){ /*côté vertical gauche*/
		CINI_draw_pixel(x=x0, y, "red");
		}
		 
	
	CINI_loop();
	
	return 0;
}

