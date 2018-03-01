#include <stdio.h>
#include <cini.h>
	
#define TAILLE 10

int main(){

	int temp, tab[TAILLE]={1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	CINI_open_window(1000, 400, "tableau");
	
	CINI_draw_int_table(50, 50, tab, TAILLE, "white", "black");
	CINI_loop_until_keydown();
	
	temp=tab[TAILLE-1];
	tab[TAILLE-1]=tab[0];
	CINI_draw_int_table(50, 50, tab, TAILLE, "white", "red");
	CINI_loop_until_keyup();
	
	tab[0]=temp;
	CINI_draw_int_table(50, 50, tab, TAILLE, "white", "green");
	CINI_loop();

	return 0;
}	
