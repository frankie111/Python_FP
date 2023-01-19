# Benotung:
# 1.a 3 Punkte
# 1.b 1 Punkt

# 2.a 2 Punkte
# 2.b 2 Punkte

# 3. 1 Punkt
# Insgesamt: 9 Punkte

# 1.
# a. Geben sei eine Textdatei mit dem Namen "zahlen.txt" an, auf eine mehreren Zeilen, Zahlen die durch
# die Zeichenkette "UBB" getrennt sind.
# schreiben Sie eine Funktion namens "ub1", die:
#   - einen Parameter namens "even_row" erhält
# 	- aus der angegebenen CSV-Datei "zahlen.txt" liest
# 	- wenn "even_row" der Wert "True" (bool) hat, behalten nur die Zeilen, wo alle Zahlen gerade Zahlen sind (0.25p)
# 	- wenn "even_row" der Wert "False" (bool) hat, behalten nur die Zeilen, wo alle Zahlen ungerade Zahlen sind (0.25p)
# 	- Das Ergebnis der Funktion ist die Summe der Zahlen der behaltenen Zeilen (0.5p)
# Es sind keine for- oder while-Schleifen erlaubt. Es wird erwartet, dass die Lösung map, filter oder reduce und
# andere mathematische Operationen, falls erforderlich, benützt sind. (2p)
#
# b. Schreiben Sie für die Funktion "ub1" zwei Testfälle. (1p)
# Einer, der das erwartete Ergebnis der Funktion bestätigt und ein anderer, der absichtlich fehlschlägt.
#
# 2.
# a. Schreiben Sie die Definition für eine Klasse namens "Shop".
# Die Klasse sollte in der Lage sein, das Folgende zu tun:
# 	 - bei der Initialisierung wird die Instanzvariable "products" auf einen gegebenen Parameter gesetzt.
# 	   Der Typ des Parameters ist eine Liste von strings. (0.5p)
# 	 - eine Methode namens "buy" haben, die:
# 	 	- einen einzelnen ganzzahligen Parameter namens "price" bekommt
# 	 	- für alle Element aus der Liste "products" prüft, dass die doppelte Länge des Elements nicht größer als "price" ist (0.5pp)
# 	 	- gibt eine neue Liste mit strings zurück, die dem folgenden Format behalten: "<element> - <price>" (0.5p)
# 	 	- eine benutzerdefinierte Ausnahme namens "BadName" wirft, wenn die Prüfung der Lange nicht fördert(0.5p)
#
# b. Schreiben Sie die Definition für eine Klasse namens "BetterShop", die von "Shop" erbt.
#  Die Klasse sollte folgendes können:
# 	- bei der Initialisierung setzt sie neben den Variablen von "Shop" auch eine Instanzvariable namens
#  	  "total" auf 0 (0.25p)
# 	- Überschreiben der Methode "buy", um Folgendes zu tun:
# 		- Wiederverwendung der Methode "buy" aus der Basisklasse (0.25)
# 		- Im Falle eines erfolgreichen Aufrufs wird das Ergebnis zurückgegeben und die Instanzvariable "total" mit dem
# 	      Wert von "price" erhöht (0.25p)
# 		- im Falle einen fehlgeschlagenen Aufruf wird die Instanzvariable "total" auf -1 gesetzt (0.25p)
# 	- Das Ergebnis der Subtraktion zwischen zwei Instanzen des Typs "BetterShop" (shop1 - shop2) ist eine Liste
#     von strings die sich in der "products" der beiden Instanzen befinden.
#     (1p)
#
# 3. Schreibe die folgende Funktion so um, dass sie rekursiv ist: (1p)
def my_func(some_list, other_function):
    my_list = []
    for num in some_list:
        if other_function(num):
            my_list.append(num)
    return my_list
