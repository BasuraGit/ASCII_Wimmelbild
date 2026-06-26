from util.Enums import ErfolgsEnum, ProgrammZustand
import os


class ZwischenMenue:
    """Zeigt die Rückmeldung nach einer Runde an und steuert den Folgezustand."""

    def starten(self, spiel):
        """Startet das passende Zwischenmenü für den letzten Erfolgszustand."""
        if spiel.letzter_erfolg == ErfolgsEnum.RIGHTINPUT:
            return self._erfolgreich(spiel)

        return self._timeout(spiel)

    def _anzeigen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def _timeout(self, spiel):
        while True:
            self._anzeigen()
            print("================================")
            print("        Zeit abgelaufen")
            print("================================")
            print(f"Dein Score: {spiel.score}")
            print()
            print("1. Spiel erneut starten")
            print("2. Zum Hauptmenü")
            print()

            auswahl = input("Auswahl: ")

            if auswahl == "1":
                spiel.neues_spiel()
                return ProgrammZustand.SPIEL
            if auswahl == "2":
                return ProgrammZustand.HAUPTMENUE

            input("Ungültige Eingabe. Enter zum Fortfahren...")

    def _erfolgreich(self, spiel):
        self._anzeigen()
        print("================================")
        print("         Nächste Runde")
        print("================================")
        print(f"Aktueller Score: {spiel.score}")
        print()
        input("Enter drücken für die nächste Spielrunde...")
        return ProgrammZustand.SPIEL