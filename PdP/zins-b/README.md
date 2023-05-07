# Erste Projektaufgabe zur Programmierung in C (Abgabe bis 28.05.2023)

Geben Sie die Lösung zu dieser ersten Projektaufgabe bis zum Sonntag, dem 28. Mai 2023, 23.59 Uhr ab. Folgen Sie den Instruktionen...

Und hier kommt die Aufgabe:

Schreiben Sie ein C-Porgramm `zins.c`, das die jährliche Entwicklung eines Grundkapitals bei einer festverzinslichen Anlage über eine wählbare Laufzeit (in ganzen Jahren) ermittelt. Die jährlich fälligen Zinsen sollen nicht ausgeschüttet, sondern mit dem Kapital wieder angelegt werden. Folgende Vorgaben sind bei der Entwicklung des Programms einzuhalten:

1. Der Zinssatz wird als Wert einer symbolischen Konstanten mit dem Namen `ZINS` festgelegt. Setzen Sie den Wert von `ZINS` auf 5.0 (also 5 Prozent Zinssatz).
2. Es gibt eine Funktion `double berechne(double grundkapital, int jahr)`, die den Kontostand nach `jahr` Jahren, einem Zinssatz von `ZINS` (symbolische Konstante) und einem Anfangsguthaben von `grundkapital` berechnet und zurückgibt.
*Fehlerbehandlung:* Ist `jahr < 1` oder `grundkapital` negativ, dann gibt es eine Fehlermeldung, in der genannt wird, dass der Fehler in der Funktion `berechne` aufgetreten ist, und dann wird das gesamte Programm abgebrochen.
3. Es gibt eine Funktion `void erzeuge_kapital_liste(double grundkapital, int laufzeit, double kapital[laufzeit + 1])`, die durch Aufrufe der Funktion `berechne` alle jährlichen erreicheten Kontostände innerhalb der Laufzeit berechnet und in das übergebene Array `kapital` einfügt. Der erste Eintrag des Arrays soll das Anfangsguthaben `grundkapital` entalten.
*Fehlerbehandlung:* Ist `jahr < 1` oder `grundkapital` negativ, dann gibt es eine Fehlermeldung, in der genannt wird, dass der Fehler in der Funktion `erzeuge_kapital_liste` aufgetreten ist, und dann wird das gesamte Programm abgebrochen.
4. Es gibt eine Funktion `void pretty_print(double grundkapital, int laufzeit, double kapital[laufzeit + 1])`, die die Entwicklung des Kapitals tabellarisch auf die Konsole ausgibt. Es wird eine Tabelle mit folgenden Angaben erzeugt:
laufendes Jahr und angesammeltes Kapital (in Euro und Cent).
Jedes Jahr aus dem Anlagezeitraum eintspricht einer Zeile in der Tabelle. 
Die Tabellenspalten sind durch einen Tabulatorstop voneinander getrennt.
Alle Ausgaben von Kapitalwerten (Datentyp `double`) sollen mit genau zwei Nachkommastellen erfolgen.
5. Das Programm realisiert dann folgenden Ablauf:
     - Der Benutzer wird aufgefordert, die gewünschte Anlagesumme und den Anlagezeitraum einzugeben. Mit den eingegebenen Werten werden entsprechendne lokale Variablen initialisiert.
     - Die Kapitalentwicklung wird (durch Aufruf der Funktion `erzeuge_kapital_liste`) berechnet und in einem Array vom Datentyp `double` gespeichert.
     - Die zu erwartende Kontoentwicklung wird tabellarisch (durch Aufruf der Funktion `pretty_print`) auf die Konsole ausgegeben.

Testen Sie Ihr Programm ausgiebig, bevor Sie es abgeben.
