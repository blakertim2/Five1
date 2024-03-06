import random  # Importiere das Modul 'random', um Zufallsfunktionen zu nutzen


def zufallszahl_generator(untergrenze, obergrenze):
    """
    Generiert eine Zufallszahl zwischen der angegebenen Untergrenze und Obergrenze (inklusive).

    :param untergrenze: Die untere Grenze des Zufallsbereichs
    :param obergrenze: Die obere Grenze des Zufallsbereichs
    :return: Die generierte Zufallszahl
    """
    zufallszahl = random.randint(untergrenze, obergrenze)
    return zufallszahl


def main():
    print("Willkommen zum Zufallsgenerator!")

    # Benutzer gibt den Zufallsbereich an
    untergrenze = int(input("Geben Sie die untere Grenze des Zufallsbereichs ein: "))
    obergrenze = int(input("Geben Sie die obere Grenze des Zufallsbereichs ein: "))

    # Generiere und zeige die Zufallszahl
    ergebnis = zufallszahl_generator(untergrenze, obergrenze)
    print(f"Ihre Zufallszahl ist: {ergebnis}")


if __name__ == "__main__":
    main()
