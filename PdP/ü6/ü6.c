#include<stdio.h>

unsigned long long explode(unsigned int m, unsigned int n){
    unsigned long long erg;

    erg = m << n;

    return erg;
}

int main(){
    printf("%llu", explode(5, 5));

}
