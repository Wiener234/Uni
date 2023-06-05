#include "date.h"
#include<stdio.h>

void newDate(date * _date, int jahr){
    _date->tag = 1;
    _date->monat = 1;
    _date->jahr = jahr;
}

void printDate(date * _date){
    printf("%d.%d.%d", _date->tag, _date->monat, _date->jahr);
}
