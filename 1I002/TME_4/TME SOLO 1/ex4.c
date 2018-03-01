/* Soit une fenetre graphique de dimensions LF x HF.
 * Ecrivez un programme qui dessine au centre de cette fenetre une 
 * croix rouge obtenue par superposition d'un rectangle de dimensions L x H
 * et d'un rectangle de dimensions H x L. 
 * Les cotes des rectangles sont paralleles aux bords de la fenetre.
 * Les points a l'interieur de la croix doivent aussi etre rouges.
 * Vous utiliserez exclusivement la fonction CINI_draw_pixel pour le trace.
 */

#include <stdio.h>
#include <cini.h>

#define HF  300
#define LF  400
#define L   150
#define H    50

int main() {
	int x, y;


	CINI_open_window(LF, HF, "fenetre");

	for (x=(LF/2)-(H/2); x<=(LF/2)+(H/2); x++){
		for (y=(HF/2)-(L/2); y<=(HF/2)+(L/2); y++){
			CINI_draw_pixel(x, y, "red");}
		}
	for (x=(LF/2)-(L/2); x<=(LF/2)+(L/2); x++){
		for (y=(HF/2)-(H/2); y<=(HF/2)+(H/2); y++){
			CINI_draw_pixel(x, y, "red");}
		}
	

	CINI_loop();
	return 0;
   
   
}
   
