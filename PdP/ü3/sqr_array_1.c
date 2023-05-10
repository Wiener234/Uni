#include<stdio.h>
#include<math.h>

#define zv printf("\n")

int main(){
    int array[10];
    for(int i=1; i <11;i++){
        array[i]=pow(i, 2);
        printf("%d\t", array[i]);
    }
    zv;

}
