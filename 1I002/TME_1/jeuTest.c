#include <stdio.h>

int main() { 
   int n1, n2, n3, res;

   printf("Veuillez saisir 3 valeurs entieres : ");
   scanf("%d", &n1);
   scanf("%d", &n2);
   scanf("%d", &n3);
	
   if (n1 > 8) { 
      res = 3;
   } 
   else { 
      if (n3 == 20) { 
         res = 2;
      } 
      else {
         if ((n2 >= 10) && (n3 >= 10)) { 
            res = 1;
         } 
         else { 
            res = 0; 
         }
      }
   }
   printf("%d\n", res);
   return 0;
   /* 4 triplets utilisés pour le jeu de teste : 
    * (9, 0, 2) : teste la première partie du programme (res=3).
    * (1, 0, 20) : teste la deuxième partie du programme (res=2).
    * (1, 15, 25) : teste la troisième partie du programme (res=1).
    * (1, 1, 1) : teste la dernière partie du programme (res=0).*/
}
