#include<stdio.h>
#include<math.h>

#define zv printf("\n")

#define zehn 10

void rev_print(int * array){
    for(int i=zehn-1; i >= 0; i--){
        printf("%d\t",array[i]);
    }
}

int main(){
    int array[zehn];
    for(int i=0; i < 10;i++){
        array[i]=pow(i+1, 2);
        printf("%d\t", array[i]);
    }
    zv;

    rev_print(array);

}
