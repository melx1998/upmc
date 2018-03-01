#include <cini.h>

#define N 4
#define COEFX 50 /* coefficients d’echelle */
#define COEFY 38
#define DX 250 /* position dans la fenetre */
#define DY 420

int main() {
	float tab_A[N] = {0.5, 0.2, -0.15, 0.85}; /* les coefficients a_i pour chaque probabilité*/
	float tab_B[N] = {0, -0.26, 0.28, 0.04}; /* les coefficients b_i pour chaque probabilité*/
	float tab_C[N] = {0, 0.23, 0.26, -0.04}; /* les coefficients c_i pour chaque probabilité*/
	float tab_D[N] = {0.16, 0.22, 0.24, 0.85}; /* les coefficients d_i pour chaque probabilité*/
	float tab_E[N] = {0, 0, 0, 0}; /* les coefficients e_i pour chaque probabilité*/
	float tab_F[N] = {0, 1.6, 0.44, 1.6}; /* les coefficients f_i pour chaque probabilité*/
	int S, tab_P[N] = {1, 7, 7, 85}; /* pourcentages de chaque transformation */
	int rand_; /*pour l'affectation à une probabilité*/
	int noT; /*numero de la transorfmation a appliquer*/
	int i;
	int x=0, y=0; /* point à tracer*/
	string couleurs[N] = {"lime green", "fuchsia", "yellow", "turquoise"};
	S=0; /* pour le tableau cumulatif*/
	
	srand(time(NULL));
	
	for (i=0; i<N; i++){ /* creation du tableau cumulatif*/
		S=S+tab_P[i];
		tab_P[i]=S;
	}

	CINI_open_window(500, 500, "feuille");
	
	
	do {
		/* Choix du numero noT de la transformation a appliquer */
		rand_=srand()%100;
		noT=0;
		while rand_>tab_P[noT]{ /* affectation de noT (numero de la transormation) */
			noT+=1;}
			
		CINI_draw_pixel(x*tab_A[noT]+y*tab_B[noT]+tab_E[noT], x*tab_C[noT]+y*tab_D[noT]+tab_F[noT], couleurs[noT]);
		
		
		/* Calcul du point a tracer (coordonnees x et y) */
		/* A COMPLETER */
		CINI_draw_pixel(DX + x*COEFX, DY - y*COEFY, couleurs[noT]);
		} while (! CINI_key_down());
		
	return 0;

}
