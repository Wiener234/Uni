#ifndef newDate_H
#define newDate_H

typedef
struct date{
    int tag;
    int monat;
    int jahr;
}date;

void newDate(date *_date, int jahr);
void printDate(date * _date);
#endif
