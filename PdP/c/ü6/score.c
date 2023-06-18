#include "date.h"
#include "highscore.h"
#include<stdio.h>

int firstYear = 2017;

int main(){
    
    date _date = {2,2,1999};
    highscore _highscore = {_date, 5};
    printHighscore(&_highscore);
    newHighscore(&_highscore, &_date, 5);
    newDate(&_date, 2000);
    printDate(&_date);


    return 0;
}
