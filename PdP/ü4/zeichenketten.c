#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define stringMaxSize 50
#define lenArray(x) (sizeof(x)/sizeof(x[0]))

int main(){
    char s1[stringMaxSize]; 
    char s2[stringMaxSize];
    scanf("%s", s1);
    scanf("%s", s2);
    
    if(strcmp(s1,s2) == 0){
        printf("Same\n");
    }
    else
        printf("not same\n");

    int i = 0;

    while(1){
        if(s2[i] == '\0'){
            printf("%s\n", s2);
            break;
        }
        if(s2[i]<126 && s2[i] > 97){
            s2[i] = s2[i] - 32;
        }
        i++;
    }

    int len = lenArray(s1)+lenArray(s2)+1;
    char name[lenArray(s1)+lenArray(s2)+1];
    //char name[len]; // adds random char befor s1 in print name after second run
    //printf("%s\n", name);

    strcat(name, s1);
    strcat(name, " ");
    strcat(name, s2);
    printf("\n");
    printf("%s\n", name);
    printf("%d\n", len);

    return 0;
}
