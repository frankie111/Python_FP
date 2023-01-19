# Benotung:
# 1.a 3 Punkte
# 1.b 1 Punkt

# 2.a 2 Punkte
# 2.b 2 Punkte

# 3. 1 Punkt
# Insgesamt: 9 Punkte

# 1.
# a. Geben sei eine Textdatei mit dem Namen "zahlen.txt" an, auf eine mehreren Zeilen, Zahlen die durch
# ein Tab-Zeichen "\t" getrennt sind.
# schreiben Sie eine Funktion namens "ub1", die:
#   - einen Parameter namens "greatest" erhält
# 	- aus der angegebenen CSV-Datei "zahlen.txt" liest
# 	- wenn "greatest" der Wert "True" (bool) hat, für jede Zeile, behaltet man nur die größte Zahl (0.25p)
# 	- wenn "greatest" der Wert "False" (bool) hat, für jede Zeile, behaltet man nur die niedrigste Zahl (0.25p)
# 	- Das Ergebnis der Funktion ist die Multiplikation aller behaltenen Zahlen (0.5p)
# Es sind keine for- oder while-Schleifen erlaubt. Es wird erwartet, dass die Lösung map, filter oder reduce und
# andere mathematische Operationen, falls erforderlich, benützt sind. (2p)
#
# b. Schreiben Sie für die Funktion "ub1" zwei Testfälle. (1p)
# Einer, der das erwartete Ergebnis der Funktion bestätigt und ein anderer, der absichtlich fehlschlägt.
#
# 2. a. Schreiben Sie die Definition für eine Klasse namens "DecryptedText". Die Klasse sollte in der Lage sein,
# das Folgende zu tun: - bei der Initialisierung wird die Instanzvariable "characters" auf einen gegebenen Parameter
# gesetzt. Der Typ des Parameters ist eine Liste von Zeichen. (0.5p) - eine Methode namens "encrypt" haben,
# die: - für alle Zeichen aus der Liste "characters" prüft, dass sich alle im Interval "a-z" sich befindet (0.5pp) -
# gibt eine Liste mit den konvertierten Zeichen in Zahlen zurück, die die ASCII-Tabelle verwenden (0.5p) - eine
# benutzerdefinierte Ausnahme namens "UnacceptedValue" wirft, wenn ein Zeichen nicht im Interval befindet (0.5p)
#
# b. Schreiben Sie die Definition für eine Klasse namens "ActualDecryptedText", die von "DecryptedText" erbt. Die
# Klasse sollte folgendes können: - bei der Initialisierung setzt sie neben den Variablen von "CaesarDecryptedText"
# auch eine Instanzvariable namens "numbers" auf None Wert (0.25p) - Überschreiben der Methode "decrypt",
# um Folgendes zu tun: - Wiederverwendung der Methode "decrypt" aus der Basisklasse (0.25) - Im Falle eines
# erfolgreichen Aufrufs wird das Ergebnis zurückgegeben und im Instanzvariable "numbers" gespeichert (0.25p) - im
# Falle einen fehlgeschlagenen Aufruf wird die Instanzvariable "numbers" auf leere Liste gesetzt (0.25p) - Das
# Ergebnis der Addition zwischen einer Instanz des Typs "ActualDecryptedText" und einer Zahl (instanz + 3) ist eine
# neue Instanz des Typs "ActualDecryptedText", die die Elemente aus "numbers" um die Zahl (aus der Addition) erhöht.
# (1p)
#
# 3. Schreibe die folgende Funktion so um, dass sie rekursiv ist: (1p)
def my_func(lst):
    n = len(lst)
    total = 0
    for num in lst:
        total += num
    return total / n
