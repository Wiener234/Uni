#include<stdio.h>
#include<math.h>

#define zv printf("\n")

#define zehn 10

int main(){
    int array[zehn];
    for(int i=0; i <10;i++){
        array[i]=pow(i+1, 2);
        printf("%d\t", array[i]);
    }
    zv;

}
