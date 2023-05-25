#include<stdio.h>
#include<stdlib.h>

int main(int argc, char ** argv){
    double cub;

    if(argc >= 2){
        double temp = atof(argv[1]);
        cub = temp * temp * temp;
        printf("%lf", cub);
        return 0;

    }
    printf("No args given");
    return 1;
}
