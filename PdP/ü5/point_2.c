/* point_2.c
 * 
 * Datentyp eines zweidimensionalen Punktes
 * verschiedene Methoden der Komponentenselektion
 */

#include <stdio.h>

  struct point {
    float x;
    float y;
  };

void change(struct point * p, int x, int y){
    p->x = 6;
    p->y = 5;
}

int main() {
  struct point p1, p2;
  struct point * ptr;

  ptr = &p1;

  // Pfeil- VS. Punktschreibweise
  p1.x = 3;  // Hier .x da p1 ein struct point ist
  ptr->y = 4; // Hier ->y da ptr ein POINTER auf struct point ist

  printf("\nx-Koordinate von p1: %f", ptr->x);
  printf("\ny-Koordinate von p1: %f", (*ptr).y);

  change(ptr, 6, 5);

  printf("\nx-Koordinate von p1: %f", ptr->x);
  printf("\ny-Koordinate von p1: %f", (*ptr).y);

  p2 = p1;

  printf("\nx-Koordinate von p2: %f", p2.x);
  printf("\ny-Koordinate von p2: %f", (&p2)->y);

  printf("\n\n");
  return 0;
}

