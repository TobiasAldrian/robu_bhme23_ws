# ... einzeiliger Kommentar

"""
Mehrzeilige Kommentare oder ein DocString
Doc-Strings sind Beschreibungen für Funktion/Methoden/Klasse und Module
Doc-Strings müssen immer direkt nach der Deklaration eingefügt werden
"""

#1. Interpreter
#Aufruf des Interpreter über das Terminal-Fenster
#Terminal: python3
#Der Interpreter kann mit exit() oder STRG+Z beendet
#Beim Interpreter werden Befehle direkt ausgeführt und das Ergebnis angezeigt
#--> Praktisch zum Testen

print("\n1. Rechenoperation")
print (2+3)
print (11/3)
print (11//3)   #Ganzzahlige Division (ohne Rest)
print (11%3)    #Nur den Rest der Division anzeigen
print (2**4)    #2 Hoch 4, Potenzieren mit **
print ("Hallo Python!");

# %%2. Variablen, Datentypen und Ausgabe
# Python unterstützt eine dynamische Typisierung, d.h. der Datentyp einer Variablen wird automatisch erkannt

# Regeln: 
# Klassen werden in PascalCase geschrieben
# Variablen und Methoden werden in snake_case geschrieben (einzelne Wörter werden mit Unterstrich getrennt)
# keine Sonderzeichen in Variablenbezeichnungen, keine Leerzeichen, keine Zahlen am Anfang, keine reservierten Wörter (z.B. print, if, for, while, def, class)
# Unterschied zwischen Groß- und Kleinschreibung beachten (case-sensitive)

print("\n2. Variablen, Datentypen und Ausgabe");
titel = "Datentypen"                # wird als String erkannt Klasse Str
vorname = "Tobias"          
nachname = "Aldrian"
name = vorname + " " + nachname
volljaehrig = True                  # wird als Boolean erkannt bool
groesse = 1.75                      # wird als Gleitkommazahl erkannt float
schuhgroesse = 43                   # wird als Ganzzahl erkannt int
impedanz = 10 + 20j                 # wird als komplexe Zahl erkannt complex

print("Ausgabe von unterschiedlichen", titel)
print(f"Mein Name ist {name}")    # von Lehrer bevorzugte String-Formatierung (f-Strings)
print("Mein Name ist %s" % name)  # String-Formatierung mit Platzhalter (wie in C)
print(volljaehrig, type(volljaehrig))
print(groesse, type(groesse))
print(schuhgroesse, type(schuhgroesse))
print(impedanz, type(impedanz))

# %%3. Typannotation und Umwandlung
print("\n3. Typannotation und Umwandlung")
# Angabe des Datentyps erleichter das Programmieren
# Weil: VSC kann dadurch bessere Vorschläge machen und Fehler erkennen
# VSC listet dann automatisch alle Methoden auf, die für den Datentyp verfügbar sind
resistor: float = 1_000 # Underlines optional zum einfachen Abzählen (gut bei großen Zahlen)
print(type(resistor)) # <class 'int'>
resistor = float(resistor) # Umwandlung in float, weil zuerst als int erkannt wurde
print(type(resistor)) # <class 'float'>
print(f"Widerstand: {resistor: <10.2f} Ohm")

# %%4. Bibliotheken importieren
print("\n4. Bibliotheken importieren")
import math # importiert die gesamte Bibliothek
from math import pi as M_PI # importiert nur die Konstante pi (und benennt sie wegen dem Schlüsselwort um in den Aliasnamen M_PI (eignet sich sehr gut um Import-Namen abzukürzen!))
import matplotlib.pyplot as plt # importiert die Bibliothek matplotlib.pyplot und benennt sie in den Aliasnamen plt um (eignet sich sehr gut um Import-Namen abzukürzen!)

print(math.pi)
print(M_PI)

# %%5. RC-Reihenschaltung und Grenzfrequenz
print("\n5. RC-Reihenschaltung und Grenzfrequenz")

resistor: float = 1_000
capacitor: float = 1e-6
frequency: float = 50.0 

impedance: complex = complex(resistor, -1/(2*math.pi*frequency*capacitor))
tau = resistor * capacitor
cutoff_frequency = 1/(2*math.pi*tau)

print(f"Impedanz:       {impedance / 1000: <10.2f} kOhm")
print(f"Zeitkonstante:  {1000*tau: <10.2f} ms")
print(f"Grenzfrequenz:  {cutoff_frequency: <10.2f} Hz")

# %%6. Listen, Indizes und Sclicing
print("\n6. Listen, Indizes und Sclicing")
# Listen sind muetable (veränderbare) Datenstrukturen, die mehrere Werte speichern können
# private in Java wäre inmutable (unveränderbar) und public wäre muetable (veränderbar)
my_list = [1, 2, -5, 3.14, "Hallo", [3, 2], (1+2j)]
print(my_list [0]) # Zugriff auf das erste Element der Liste
print(my_list [1]) # Zugriff auf das zweite Element der Liste
#print(my_list [-1]) # Zugriff auf das letzte Element der Liste
print(my_list [5][1]) # Zugriff auf das zweite Element der Liste, die an der Stelle 5 gespeichert ist
#print(my_list [6].real) # Zugriff auf den Realteil der komplexen Zahl, die an der Stelle 6 gespeichert ist
#print(my_list [2:5]) # Zugriff auf die Elemente der Liste von Index 2 bis Index 4 (Index 5 ist nicht enthalten)
#print(my_list [2:]) # Zugriff auf die Elemente der Liste von Index 2 bis zum Ende der Liste
#print(my_list [:5]) # Zugriff auf die Elemente der Liste von Index 0 bis Index 4 (Index 5 ist nicht enthalten)
print(my_list [::2]) # Zugriff auf die Elemente der Liste von Index 0 bis zum Ende der Liste, wobei jedes zweite Element ausgewählt wird
#print(my_list [::-1]) # Zugriff auf die Elemente der Liste von Index -1 bis zum Anfang der Liste, wobei die Reihenfolge umgekehrt wird
print(my_list [-2:]) # Zugriff auf die Elemente der Liste von Index -2 bis zum Ende der Liste
print(my_list [1:3]) # Zugriff auf die Elemente der Liste von Index 1 bis Index 2 (Index 3 ist nicht enthalten)
print(my_list [:5:2]) # Zugriff auf die Elemente der Liste von Index 0 bis Index 4 (Index 5 ist nicht enthalten), wobei jedes zweite Element ausgewählt wird

print(my_list[::-1]) # Dreht die Ausgabe um
#print(my_list.reverse()) # Die die komplette Liste permanent um!
print(my_list) # Ausgabe der Liste nach dem permanenten Umdrehen

my_list.append([]) # Fügt eine leere Liste am Ende der Liste hinzu
# Wichtig: Sacehn wie __add__ nicht nehmen wegen Doppelunterstrich
print(my_list[-1]) # Zugriff auf das letzte Element der Liste, das eine leere Liste ist

my_list = my_list + [5, 4, 3] # Fügt die Elemente 5, 4 und 3 am Ende der Liste hinzu
print(my_list)

#entpacken von Listen
a, b, c = my_list[:3] # Entpacken der ersten drei Elemente der Liste in die Variablen a, b und c
print(a, b, c) # Ausgabe der Variablen a, b, c

# %%7. Tupel und Entpacken
print("\n7. Tupel und Entpacken")
# Tupel sind inmutable (unveränderbare) Datenstrukturen, die mehrere Werte speichern können

tup_numbers = (1, 2, 3)
print(tup_numbers + (4, 5, 6)) # Ausgabe der Elemente des Tupels und der Elemente des neuen Tupels (1, 2, 3, 4, 5, 6)
print(2 * tup_numbers) # Ausgabe der Elemente des Tupels zweimal (1, 2, 3, 1, 2, 3)
a, b, c = tup_numbers # Entpacken der Elemente des Tupels in die Variablen a, b und c
print(a, b, c) # Ausgabe der Variablen a, b und c

# %%8. Sets und eindeutige Werte
print("\n8. Sets und eindeutige Werte")
# Sets sind muetable (veränderbare) Datenstrukturen, die mehrere Werte speichern können
# Sets speichern nur eindeutige Werte, d.h. doppelte Werte werden automatisch entfernt
# Sets werden mit geschweiften Klammern {} definiert, wobei die Elemente durch Kommas getrennt werden
basket = {"Apfel", "Banane", "Kirsche", "Apfel", "Banane"} # doppelte Werte werden automatisch entfernt
print(basket) # Ausgabe der Elemente des Sets (Apfel, Banane, Kirsche)
basket.add("Orange") # Fügt ein Element zum Set hinzu
print(basket) # Ausgabe der Elemente des Sets (Apfel, Banane, Kirsche, Orange)
basket.remove("Banane") # Entfernt ein Element aus dem Set
print(basket) # Ausgabe der Elemente des Sets (Apfel, Kirsche, Orange)

# len() gibt die Anzahl der Elemente in einem Set zurück
print(len(basket)) # Ausgabe der Anzahl der Elemente im Set (3)

print("Apfel" in basket) # Überprüft, ob ein Element im Set enthalten ist (True)
print("Banane" in basket) # Überprüft, ob ein Element im Set enthalten ist (False)

print(sorted(basket)) # Gibt die Elemente des Sets in sortierter Reihenfolge zurück (Apfel, Kirsche, Orange)

#print(basket.union({"Banane", "Kiwi"})) # Gibt die Vereinigung von zwei Sets zurück (Apfel, Kirsche, Orange, Banane, Kiwi)
#print(basket.intersection({"Banane", "Kiwi"})) # Gibt die Schnittmenge von zwei Sets zurück (leeres Set)
#print(basket.difference({"Banane", "Kiwi"})) # Gibt die Differenz von zwei Sets zurück (Apfel, Kirsche, Orange)

lst_numbers = [1, 2, 1, 3, 1, 4]
set_numbers = set(lst_numbers) # Wandelt die Liste in ein Set um, wodurch doppelte Werte entfernt werden
print(set_numbers) # Ausgabe der Elemente des Sets (1, 2, 3, 4)
unique_list = sorted(set_numbers) # Wandelt das Set wieder in eine sortierte Liste um
print(unique_list) # Ausgabe der Elemente der sortierten Liste (1, 2, 3, 4)

# %%9. Dictionaries und Schlüssel-Wert-Paare
print("\n9. Dictionaries und Schlüssel-Wert-Paare")
# Dictionaries sind muetable (veränderbare) Datenstrukturen, die mehrere Werte speichern können
# Dictionaries speichern Schlüssel-Wert-Paare, d.h. jedem Schlüssel wird ein Wert zugeordnet
# Dictionaries werden mit geschweiften Klammern {} definiert, wobei die Schlüssel-Wert-Paare durch Kommas getrennt werden und der Schlüssel und der Wert durch einen Doppelpunkt getrennt werden
person = {"Name": "Tobias", "Alter": 30, "Größe": 1.75}
print(person) # Ausgabe der Elemente des Dictionaries
print(person["Name"]) # Zugriff auf den Wert des Schlüssels "Name"
person["Alter"] = 31 # Ändert den Wert des Schlüssels "Alter"
print(person) # Ausgabe der Elemente des Dictionaries
print(person.get("Alter", "Nicht gefunden")) # Zugriff auf den Wert des Schlüssels "Alter" mit der Methode get()
print(person.get("Größe", "Nicht gefunden")) # Zugriff auf den Wert des Schlüssels "Größe" mit der Methode get()
# "Nicht gefunden" wird zurückgegeben, wenn der Schlüssel nicht im Dictionary enthalten ist

for key, value in person.items(): # Iteriert über die Schlüssel-Wert-Paare des Dictionaries
    print(f"{key}: {value}") # Ausgabe der Schlüssel-Wert-Paare des Dictionaries

### %%10. Schleifen range und List Comprehension
print("\n10. Schleifen range und List Comprehension")
y = [] # Leere Liste wird erstellt
#y = x² für x = 0, 1, 2, 3, 4
for x in range(5): # range(5) erzeugt eine Sequenz von Zahlen von 0 bis 4
    y.append(x**2) # Fügt das Quadrat von x zur Liste y hinzu
print(y) # Ausgabe der Liste y
# range:
# Konstruktor range (stop) erzeugt eine Sequenz von Zahlen von 0 bis stop-1
# Konstruktor range (start, stop) erzeugt eine Sequenz von Zahlen von start bis stop-1
# Konstruktor range (start, stop, step) erzeugt eine Sequenz von Zahlen von start bis stop-1 mit der Schrittweite step
# List Comprehension:
# List Comprehension ist eine kompakte Möglichkeit, eine Liste zu erstellen
y = [x**2 for x in range(5)] # List Comprehension erzeugt eine Liste von Quadraten von x für x = 0, 1, 2, 3, 4
print(y) # Ausgabe der Liste y  

# %%11. Wortsuche und Verzweigungen
print("\n11. Wortsuche und Verzweigungen")

words = ["Apfel", "Banane", "Kirsche", "Orange"]
longest_word = ""
for word in words:
    if len(word) > len(longest_word): # Überprüft, ob die Länge des aktuellen Wortes größer ist als die Länge des längsten Wortes
        longest_word = word # Setzt das aktuelle Wort als längstes Wort
print(f"Das längste Wort ist: {longest_word}") # Ausgabe des längsten Wortes

abstand = 0.25 # Meter

if abstand < 0.2: # Stopp
    print("Stopp! Abstand zu gering!")
elif abstand < 0.5: # Langsam fahren
    print("Langsam fahren! Abstand zu gering!")
else: # Alles gut
    print("Alles gut! Abstand ausreichend!")

# %%12. While-Schleife
print("\n12. While-Schleife")

zaehler = 3
while zaehler > 0: # Solange der Zähler größer als 0 ist
    print(f"Zähler: {zaehler}") # Ausgabe des Zählers
    zaehler -= 1 # Verringert den Zähler um 1

# %%13. Funktionen und Standardparameter
print("\n13. Funktionen und Standardparameter")

# Hinweis: Datentypen bei den Argumenten und beim Rückgabewert hinzufügen
# dadurch kann Ruff und Pylance den Code auf Richtigkeit überprüfen und gibt ggf. Warnungen aus
def summe_and_product(a:int, b:int) -> tuple[int, int]: # Definiert eine Funktion, die zwei Ganzzahlen a und b als Parameter hat und ein Tupel von zwei Ganzzahlen zurückgibt
    summe = a + b
    produkt = a * b
    return (summe, produkt) # Gibt die Summe und das Produkt von a und b zurück als Tupel

result_sum, result_product = summe_and_product(3, 5) # Ruft die Funktion summe_and_product mit den Parametern 3 und 5 auf
print(f"Summe: {result_sum}, Produkt: {result_product}") # Ausgabe der Ergebnisse

# Funktion mit optionalem Übergabeparameter

def grenzfrequenz(resistor: float, capacitor: float = 1e-6) -> float: # Definiert eine Funktion mit den Parametern resistor und capacitor (optional, Standardwert 1 µF) und gibt eine Gleitkommazahl zurück
    tau = resistor * capacitor
    cutoff_frequency = 1/(2*math.pi*tau)
    return cutoff_frequency # Gibt die Grenzfrequenz zurück

print(f"Grenzfrequenz: {grenzfrequenz(1_000): >10.2f} Hz")
print(f"Grenzfrequenz: {grenzfrequenz(1_000, 2e-6): >10.2f} Hz")

# %%14. Diagramme mit Matplotlib
import matplotlib.pyplot as plt

# Schleifen beim Test dürfen nicht kompakt sein (weißt auf KI hin)!!!
x = list(range(5)) # Erzeugt eine Liste von Zahlen von 0 bis 4
y = []
for wert in x:
    y.append(wert**2) # Fügt das Quadrat des Wertes zur Liste y hinzu

plt.plot(x, y, marker='o')
plt.xlabel("x") 
plt.ylabel("y(x) = x²")
plt.title("Quadratzahlen")
plt.grid(True)
plt.show() # Zeigt das Diagramm an  
plt.close() # Schließt das Diagramm, damit das nächste Diagramm angezeigt werden kann