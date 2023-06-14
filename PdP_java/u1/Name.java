
/**
 * Vorlage.java
 * 
 * Programmfragment, das Tastatureingaben ermoeglicht 
 *
 */

import java.util.Scanner;

// Klassenname MUSS = Dateiname sein
class Name {

  public static void main(String[] args) {

    // Boilerplate Code - bitte erstmal einfach verwenden, Details folgen später
    Scanner scanner = new Scanner(System.in);

    System.out.print("Vorname: ");
    String vorname = scanner.next();
    System.out.print("Nachname: ");
    String famname = scanner.next();
    System.out.print("Alter: ");
    int alter = scanner.nextInt();

    System.out.println(vorname + " " + famname);
    System.out.println(vorname.length());
    System.out.println(vorname.substring(0, 1) + "." + famname.substring(0, 1) + ".");
    System.out.println(alter);

    // Methoden für weitere Datentypen existieren
    // siehe API

  }

}

// Vorlage

