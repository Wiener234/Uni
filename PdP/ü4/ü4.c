#include<stdio.h>

int main(){
    char *statS = "Hallo PdP!";
    char dynS[] = "Hallo PdP!";
    //statS[1] = 'e'; //fuck segmentation faults
    dynS[1] = 'e';
    statS = "neuer String";
    //dynS = "neuer String"; //next fucking error


}
