#include<stdio.h>
#include<math.h>

#define ZINS 5.0

double berechne(double grundkapital, int jahr){
    double erg = grundkapital * pow(1+(ZINS/100.0),jahr); 
    return erg;
}

int main(){

    double* grundkapital;
    int* jahr;

    printf("Geben Sie ihr Grundkapital ein: ");
    scanf("%lf\n", grundkapital);

    printf("Geben Sie die Laufzeit ein: ");
    scanf("%d", jahr);

    if(*grundkapital >= 0 && *jahr >=1){
        printf("%f", berechne(*grundkapital, *jahr));
    }else{
        printf("Fasche werte um in Funktion berechne ein Ergebnis zu erhalten. Überprüfen Sie ihre Eingabe.");
        return 1;
    }
    return 0;
}
