# Funktion zur Umrechnung von Kilometern in Meilen
def kilometer_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles


# Funktion zur Umrechnung von Meilen in Kilometer
def miles_to_kilometer(miles):
    kilometers = miles / 0.621371
    return kilometers


# Hauptfunktion des Programms
def main():
    # Begrüßungsnachricht
    print("Willkommen zum Einheitsumrechner!")

    # Benutzer wählt die Art der Umrechnung
    choice = input("Möchten Sie Kilometer in Meilen umrechnen (1) oder Meilen in Kilometer (2)? ")

    # Verzweigung basierend auf der Benutzerauswahl
    if choice == "1":
        kilometers = float(input("Geben Sie die Anzahl der Kilometer ein: "))
        result = kilometer_to_miles(kilometers)
        print(f"{kilometers} Kilometer sind etwa {result:.2f} Meilen.")
    elif choice == "2":
        miles = float(input("Geben Sie die Anzahl der Meilen ein: "))
        result = miles_to_kilometer(miles)
        print(f"{miles} Meilen sind etwa {result:.2f} Kilometer.")
    else:
        print("Ungültige Eingabe. Bitte wählen Sie 1 oder 2.")


# Startet das Programm, wenn es direkt ausgeführt wird
if __name__ == "__main__":
    main()
