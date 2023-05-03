//-------------------Aufgabe-1&2---------------------
 /*#include<stdio.h>
 | #include<stdlib.h>
 | 
 | int y;
 | 
 | int f(int a, int b){
 |     if(b == 0){
 |         printf("Can't divide by 0!");
 |         exit(1);
 |     }
 |     return (2*a)/b;
 | }
 | 
 | int main(){
 |     int x = 4;
 |     printf("Geben Sie eine ganze Zahl ein: ");
 |     scanf("%d", &y);
 |     printf("f: %d", f(x, y));
 |     return 0;
 | }
*/

#include<stdio.h>

int main(){
    int i;
    int* ptr;
    ptr = &i;
    i = 1;
    printf("ptr: %p\n", ptr);
    printf("ptrObject: %d\n", *ptr);
    printf("i: %d\n", i);
    *ptr = 2;
    printf("i2: %d\n", i);
    return 0;
}
