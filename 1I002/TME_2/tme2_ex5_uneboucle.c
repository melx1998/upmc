#include <stdio.h>
#include <cini.h>
#include <math.h>


int main(){
	
	int i, x0, y0, c;
	printf("Entrer la valeur de c, le coté du carré\n");
	scanf("%d", &c);
	printf("Entrer la valeur de x et y, le coin superieur gauche du carré\n");
	scanf("%d %d", &x0, &y0);
	
	CINI_open_window(400, 400, "fenetre");
	
	
	for (i=0; i<=c; i++){
		CINI_draw_pixel(x0+i, y0, "red"); /*côté horizontal haut*/
		CINI_draw_pixel(x0+i, y0+c, "red"); /*côté horizontal bas*/
		CINI_draw_pixel(x0, y0+i, "red"); /*côté vertical gauche*/
		CINI_draw_pixel(x0+c, y0+i, "red"); /*côté vertical droit*/
		}
	
	CINI_loop();
	
	return 0;
}


