#include <stdio.h>
#include <cini.h>

#define CENTRE_X 200
#define CENTRE_Y 200
#define LONGUEUR 100

int main(){

	int x, y;
	CINI_open_window(400, 400, "fenetre");

	for(x=CENTRE_X; x<=CENTRE_X+LONGUEUR; x++){ /*horizontale droite*/
		CINI_draw_pixel(x, CENTRE_Y, "blue");
		}
	for(x=CENTRE_X; x>=CENTRE_X-LONGUEUR; x--){ /*horizontale gauche*/
		CINI_draw_pixel(x, CENTRE_Y, "blue");
		}
	for(y=CENTRE_Y; y>=CENTRE_Y-LONGUEUR; y--){ /*verticale haut*/
		CINI_draw_pixel(CENTRE_X, y, "blue");
		}
	for(y=CENTRE_Y; y<=CENTRE_Y+LONGUEUR; y++){ /*verticale bas*/
		CINI_draw_pixel(CENTRE_X, y, "blue");
		}
	
	CINI_loop();

	return 0;

}
