#include "date.h"
#include "highscore.h"
#include<stdio.h>

//#define TEST

void newHighscore(highscore * _highscore, date * _date, int score){
    _highscore->date = *_date;
    _highscore->score = score;
}

void printHighscore(highscore * _highscore){
    printf("Score ab %d\n", firstYear);
    printf("%d.%d.%d \t %d\n", _highscore->date.tag, _highscore->date.monat, _highscore->date.jahr, _highscore->score);
}

#if defined TEST
int main(){
    date _date = {2,2,1999};
    highscore _highscore = {_date, 5};
    printHighscore(&_highscore);
    newHighscore(&_highscore, &_date, 5);
    newDate(&_date, 2000);
    printDate(&_date);
}
#endif

