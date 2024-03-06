import random  # Importiere das Modul 'random', um Zufallsfunktionen zu nutzen


def spiel_schere_stein_papier(benutzerwahl):
    """
    Simuliert ein Schere-Stein-Papier-Spiel gegen den Computer.

    :param benutzerwahl: Die Auswahl des Benutzers (Schere, Stein oder Papier)
    :return: Das Ergebnis des Spiels (Gewonnen, Verloren oder Unentschieden)
    """
    mögliche_wahlen = ["Schere", "Stein", "Papier"]
    computerwahl = random.choice(mögliche_wahlen)

    print(f"Der Computer wählt: {computerwahl}")

    if benutzerwahl == computerwahl:
        return "Unentschieden"
    elif (
            (benutzerwahl == "Schere" and computerwahl == "Papier") or
            (benutzerwahl == "Stein" and computerwahl == "Schere") or
            (benutzerwahl == "Papier" and computerwahl == "Stein")
    ):
        return "Gewonnen"
    else:
        return "Verloren"


def main():
    print("Willkommen zum Schere-Stein-Papier-Spiel!")

    # Benutzer gibt die Wahl ein
    benutzerwahl = input("Wählen Sie Schere, Stein oder Papier: ")

    # Überprüfe die Gültigkeit der Benutzerwahl
    if benutzerwahl.lower() in ["schere", "stein", "papier"]:
        ergebnis = spiel_schere_stein_papier(benutzerwahl.capitalize())
        print(f"Ergebnis: {ergebnis}")
    else:
        print("Ungültige Eingabe. Bitte wählen Sie Schere, Stein oder Papier.")


if __name__ == "__main__":
    main()
