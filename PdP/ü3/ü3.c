#include<stdio.h>

#define zv printf("\t")

int main(){
    int array[3][4] = {{0, 1, 2, 3}, {10, 11, 12}};

    for(int i = 0; i<3; i++){
        for(int j = 0; j<4;j++){
            printf("%d",array[i][j]);
            zv;
        }
        printf("\n");
    }

    return 0;
}
