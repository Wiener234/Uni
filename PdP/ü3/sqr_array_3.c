#include<stdio.h>
#include<math.h>

#define zv printf("\n")

#define zehn 1000

int main(){
    int array[zehn];
    for(int i=0; i < zehn;i++){
        array[i]=pow(i+1, 2);
        //printf("%d\t", array[i]);
    }
    while(1){
        int var;
        printf("Input a number between 1 and %d: ", zehn);
        scanf("%d",&var);

        if(var < 0 || var > zehn){
            printf("no negative number or bigger then 1000");
            zv;
            continue;
        }
        if(var == 0)
            break;

        printf("%d", array[var-1]);
        zv;




    }
    
}
