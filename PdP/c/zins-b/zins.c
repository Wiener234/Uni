#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define ZINS 5.0

double berechne(double grundkapital, int jahr){
    if(grundkapital >= 0 && jahr >=1){
        double erg = grundkapital * pow(1+(ZINS/100.0),jahr); 
        return erg;
    }else{
        printf("Falsche Werte um in Funktion \"berechne\" ein Ergebnis zu erhalten. Überprüfen Sie ihre Eingabe.");
        exit(1);
    }
}

void erzeuge_kapital_list(double grundkapital, int laufzeit, double kapital[laufzeit+1]){
    if(grundkapital >= 0 && laufzeit >=1){
        kapital[0] = grundkapital;
        for(int i = 1; i <=laufzeit; i++){
            kapital[i] = berechne(grundkapital, i);
        }
    }else{
        printf("Falsche Werte um in Funktion \"erzeuge_kapital_list\" ein Ergebnis zu erhalten. Überprüfen Sie ihre Eingabe.");
        exit(1);
    }
}

void pretty_print(double grundkapital, int laufzeit, double kapital[laufzeit+1]){
    printf("Jahr\tKapital\n");
    for(int i = 0; i<=laufzeit; i++){
        printf("%4d\t%.2lf\n", i, kapital[i]);
    }

}

int main(){

    double grundkapital;
    int jahr;

    printf("Geben Sie ihr Grundkapital ein: ");
    scanf("%lf", &grundkapital);

    printf("Geben Sie die Laufzeit ein: ");
    scanf("%d", &jahr);


    double kapital[jahr+1];


    printf("Erg: %f\n", berechne(grundkapital, jahr));
    erzeuge_kapital_list(grundkapital, jahr, kapital); 
    pretty_print(grundkapital, jahr, kapital);


    return 0;
}
