#include <stdio.h>

int main()
{
int x;
int y;
x=65;
y=65.9;
printf("int x = %d", &x);
printf("float x = %f", &x);
printf("char x = %c", &x);
printf("int y = %d", &y); 
/*printf("float y = %lf", &y);*/ /*impossible*/
/*printf("char y = %c", &y);*/ /*impossible*/
return 0;
}
