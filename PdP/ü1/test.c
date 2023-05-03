#include<stdio.h>

int main(){
    int a = 3;
    int *p = &a;

    printf("a:%i\t&a:%i\n", a, &a);
    printf("*p:%i\tp:%i", *p, p);
}
