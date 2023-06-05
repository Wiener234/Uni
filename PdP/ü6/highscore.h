#include"date.h"

#ifndef HIGHSCORE
#define HIGHSCORE

typedef
struct highscore{
    date date;
    int score;
}highscore;

void newHighscore(highscore * _highscore, date * _date, int score);
void printHighscore(highscore * _highscore);

#endif
