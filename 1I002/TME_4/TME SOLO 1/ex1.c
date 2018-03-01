/* Ce programme doit comparer deux valeurs et afficher celle qui est la plus grande.
*/

#include <stdio.h>

#define A  9
#define B 15

int main() {
   int a = A, b = B;
   
   if ( a > b ) {
      printf ("%d est plus grand que %d\n", a, b);
   }
   else if (b > a){
         printf ("%d est plus grand que %d\n", b, a);
      }
      else {
         printf("%d et %d sont egaux\n", a, b);
      }
  
  return 0; 
  }

