#include<stdio.h>
#include<math.h>

#define zv printf("\n")

int main(){
    int array[10];
    for(int i=0; i < 10;i++){
        array[i]=pow(i, 2);
        printf("%d\t", array[i]);
    }
    zv;

}
