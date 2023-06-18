#include<stdio.h>



int main(){

/* //print "Ich kenne die Formatelemente yu 100%."
 
    printf("Ich kenne die Formatelemente zu 100%%.");
*/




/*//print even numbers from 12 to 0
  //print odd numbers from -1 to -13
  //print i*i from 0 to 9
    for(int i=12; i>=0; i--){
        if(i % 2 == 0){
            printf("%d", i);
        
            if(i>0)
                printf(", ");
        }

    }

    printf("\n");

    for(int i=-1; i>=-13;i--){
        if(i % 2 != 0){
            printf("%d", i);

            if(i > -13)
                printf(", ");
        }
    }

    printf("\n");

    for(int i=0; i<=9; i++){
        printf("%d", i*i);
        if(i<9)
            printf(", ");
    }
*/

/* //same as above with while loop
    int i = 12;

    while(i>=0){
        printf("%d", i);
        if(i>0)
            printf(", ");
        i--;
    }

    i = -1;

    while(i>=-13){
        printf("%d", i);
        if(i>-13)
            printf(", ");
        i--;
    }

    i = 0;

    while(i<=9){
        printf("%d", i);
        if(i<9)
            printf(", ");
        i++;
    }
*/

/* print Farenheit converted to Celsius in table format
    int i = 0;

    printf("Farenheit\t Celsius\n");
    while(i<=300){

        int x = 5.0/9 * (i - 32);
        printf("%5d  %15d\n",i,  x);

        i+=20;
    }
*/



    return 0;
}

