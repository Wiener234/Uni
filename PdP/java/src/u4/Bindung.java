/** Bindung.java
 * 
 * Eine Klasse, die am Beispiel des figure-Pakets
 * statische und dynamische Typen ausprobiert
 */
package u4;

import u3.*;

public class Bindung {

  public static void main(String[] args) {

    Figure f = new Square();
    f.moveFigRel(2,3);  
    f.calcArea();
    // f.show(); //absoluter bullshit mach keine fehler

    if (f instanceof Square) {
      ((Square)f).show();  // analog: (double)17
    }

    System.out.println("Flaecheninhalt: " + f.calcArea());
    f = new Circle(10);
    System.out.println("Flaecheninhalt: " + f.calcArea());

  }
}

// Bindung
