#include<stdio.h>
#include<stdlib.h>

//------------- wrong idea using malloc ----------------
/*
int* swap(int x, int y){
    int* tmp = malloc(2* sizeof(int));
    tmp[0] = y;
    tmp[1] = x;
    return tmp;
}
*/

void swap(int * x, int * y){
    int tmp = *x;

    *x = *y;
    *y = tmp;

}

int main(){
    int x = 5;
    int y = 10;
    printf("x: %d\ny: %d\n", x, y);

    swap(&x, &y);
    printf("x: %d\ny: %d\n", x, y);




    //int* swap_res = swap(x,y); //for use with malloc
    //printf("x: %d\ny: %d\n", swap_res[0], swap_res[1]);
    return 0;
}
