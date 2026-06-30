from util.Enums import ProgrammZustand
import os

class HauptMenue:
    """Zeichnet das Hauptmenü und gibt Eingabe weiter."""
    def starten(self):
        """Startet das Hauptmenü."""
        self.anzeigen()
        return self.auswahl_verarbeiten()

    def anzeigen(self):
        """Leert das Terminal und gibt das Hauptmenü aus."""
        #print("\033[H\033[3J", end="")                            -> funktioniert komischerweise nicht
        os.system("cls" if os.name == "nt" else "clear")

        print("================================")
        print("       ASCW - Hauptmenü")
        print("================================")
        print("1: Spiel starten")
        print("2: Einstellungen")
        print("3: Spiel Beenden")
        print()

    def auswahl_verarbeiten(self):
        """Verarbeitet die Benutzerauswahl."""
        while True:
            auswahl = input("Auswahl: ")

            if auswahl == "1":
                return ProgrammZustand.SPIEL
            elif auswahl == "2":
                return ProgrammZustand.EINSTELLUNGEN
            elif auswahl == "3":
                return ProgrammZustand.BEENDEN

            input("Ungültige Eingabe. Enter zum Fortfahren...")
            self.anzeigen()

    def einstellungen_aufrufen(self):
        self.einstell