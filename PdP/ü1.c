#include<stdio.h>


int grad(int x){
    int c = (x -32) * 5/9;
    printf("%d", x);
    return 5/9 * (x - 32);
}

int main(){

//    int i = 100; 
//
//    printf("Ich kenne die Formatelemente zu 100%%.", i);





//    for(int i=12; i>=0; i--){
//        printf("%d", i);
//        if(i>0)
//            printf(", ");
//
//    }
//
//    printf("\n");
//
//    for(int i=-1; i>=-13;i--){
//        printf("%d", i);
//        if(i>-13)
//            printf(", ");
//    }
//
//    printf("\n");
//
//    for(int i=0; i<=9; i++){
//        printf("%d", i*i);
//        if(i<9)
//            printf(", ");
//    }


//    int i = 12;
//
//    while(i>=0){
//        printf("%d", i);
//        if(i>0)
//            printf(", ");
//        i--;
//    }
//
//    i = -1;
//
//    while(i>=-13){
//        printf("%d", i);
//        if(i>-13)
//            printf(", ");
//        i--;
//    }
//
//    i = 0;
//
//    while(i<=9){
//        printf("%d", i);
//        if(i<9)
//            printf(", ");
//        i++;
//    }


    printf("%d", grad(0));


    return 0;
}

